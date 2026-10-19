import hashlib
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from rore_runtime.provider_setup import (Archive, SetupError, _download_verified,
                                         _extract_verified, doctor, install_ghidra, plan)


class ProviderSetupTests(unittest.TestCase):
    def test_plan_and_doctor_do_not_create_provider_root(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "providers"
            offered = plan(root)
            self.assertFalse(root.exists())
            self.assertEqual(len(offered["artifacts"]), 2)
            self.assertTrue(all(x["archive_status"]["status"] == "missing" for x in offered["artifacts"]))
            self.assertEqual(doctor(root)["ghidra"]["status"], "not-installed-in-selected-root")
            self.assertFalse(root.exists())

    def test_download_must_match_pinned_size_and_hash_before_promotion(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "download" / "tool.zip"
            payload = b"verified archive bytes"
            item = Archive("tool.zip", "https://example.invalid/tool.zip",
                           hashlib.sha256(payload).hexdigest(), len(payload), "tool")

            class Response(io.BytesIO):
                def __init__(self, content):
                    super().__init__(content)
                    self.headers = {"Content-Length": str(len(content))}

            with patch("rore_runtime.provider_setup.urllib.request.urlopen", return_value=Response(payload)):
                self.assertEqual(_download_verified(item, destination), destination)
            self.assertEqual(destination.read_bytes(), payload)
            with patch("rore_runtime.provider_setup.urllib.request.urlopen") as remote:
                self.assertEqual(_download_verified(item, destination), destination)
                remote.assert_not_called()

            bad = Archive("bad.zip", item.url, item.sha256, item.size, "bad")
            with patch("rore_runtime.provider_setup.urllib.request.urlopen", return_value=Response(b"wrong")):
                with self.assertRaisesRegex(SetupError, "pinned size|mismatch"):
                    _download_verified(bad, destination.parent / bad.name)
            self.assertFalse((destination.parent / bad.name).exists())

    def test_extraction_rejects_traversal_and_symlink_without_escape(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            item = Archive("test.zip", "https://example.invalid/test.zip", "0" * 64, 0, "mini-jdk")
            archive_path = root / item.name
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("mini-jdk/bin/java.exe", b"java")
                archive.writestr("mini-jdk/../../escape.txt", b"bad")
            with self.assertRaisesRegex(SetupError, "unsafe archive member"):
                _extract_verified(archive_path, item, root)
            self.assertFalse((root / "escape.txt").exists())

            symlink_path = root / "symlink.zip"
            with zipfile.ZipFile(symlink_path, "w") as archive:
                link = zipfile.ZipInfo("mini-jdk/link")
                link.create_system = 3
                link.external_attr = 0o120777 << 16
                archive.writestr(link, "../escape.txt")
            with self.assertRaisesRegex(SetupError, "non-regular archive member"):
                _extract_verified(symlink_path, item, root)

    def test_contained_extraction_and_existing_provider_never_overwrites(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            item = Archive("test.zip", "https://example.invalid/test.zip", "0" * 64, 0, "mini-jdk")
            archive_path = root / item.name
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("mini-jdk/bin/java.exe", b"java")
            installed = _extract_verified(archive_path, item, root)
            self.assertEqual((installed / "bin" / "java.exe").read_bytes(), b"java")
            with self.assertRaisesRegex(SetupError, "refusing to overwrite"):
                _extract_verified(archive_path, item, root)
            self.assertEqual((installed / "bin" / "java.exe").read_bytes(), b"java")

    def test_existing_versioned_directories_are_probed_not_rewritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "ghidra_12.1.4_PUBLIC").mkdir()
            (root / "jdk-25.0.4.1+1").mkdir()
            with patch("rore_runtime.provider_setup.windows_x64", return_value=True), \
                 patch("rore_runtime.provider_setup.probe", return_value={"status": "components-qualified-not-target-tested"}):
                result = install_ghidra(root)
            self.assertEqual(result["status"], "components-qualified-not-target-tested")
            self.assertTrue(all(x["status"] == "existing_directory_not_archive_attested" for x in result["actions"]))
