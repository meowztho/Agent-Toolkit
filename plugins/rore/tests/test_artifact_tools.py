import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path

from rore_runtime.artifact_tools import (ArtifactError, capabilities, inspect_file,
                                         inventory_directory, inventory_zip, read_file_bytes, read_zip_member)
from rore_runtime.binary_layout import inspect_binary_layout, map_file_offset


class ArtifactToolsTests(unittest.TestCase):
    def test_pe_signature_and_file_offsets_are_bounded_to_original_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "sample.exe"
            data = bytearray(256)
            data[:2] = b"MZ"
            data[0x3c:0x40] = (0x80).to_bytes(4, "little")
            data[0x80:0x84] = b"PE\0\0"
            source.write_bytes(data)
            inspection = inspect_file(source)
            self.assertEqual(inspection["source"]["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual(inspection["format"]["candidate"], "pe")
            window = read_file_bytes(source, 0x80, 4)
            self.assertEqual(window["coordinate_space"], "file-offset")
            self.assertEqual(window["bytes"]["hex"], "50450000")
            self.assertIn("no section", window["mapping_limit"])
            with self.assertRaisesRegex(ArtifactError, "no partial bytes"):
                read_file_bytes(source, 254, 4)

    def test_rewritten_stable_file_can_be_inspected_on_windows(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "rewritten.bin"
            source.write_bytes(b"old")
            source.write_bytes(b"new")
            self.assertEqual(inspect_file(source)["source"]["sha256"], hashlib.sha256(b"new").hexdigest())

    def test_zip_inventory_preserves_duplicate_member_identity_and_unsafe_names(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / "sample.zip"
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
                    output.writestr("asset.dat", b"first")
                    output.writestr("asset.dat", b"second")
                    output.writestr("../outside.dat", b"unsafe-name")
            page = inventory_zip(archive, offset=1, limit=2)
            self.assertEqual(page["total_members"], 3)
            self.assertEqual([item["index"] for item in page["members"]], [1, 2])
            self.assertFalse(page["members"][1]["safe_relative_path"])
            self.assertIsNone(page["next_offset"])
            self.assertEqual(read_zip_member(archive, 0, 0, 5)["bytes"]["ascii"], "first")
            self.assertEqual(read_zip_member(archive, 1, 0, 6)["bytes"]["ascii"], "second")
            self.assertFalse((Path(temp) / "outside.dat").exists())

    def test_corrupt_deflate_member_reports_artifact_error(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / "corrupt.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
                output.writestr("data.bin", b"abc" * 200)
            data = bytearray(archive.read_bytes())
            name_size = int.from_bytes(data[26:28], "little")
            extra_size = int.from_bytes(data[28:30], "little")
            data[30 + name_size + extra_size] = 0xff
            archive.write_bytes(data)
            with self.assertRaisesRegex(ArtifactError, "member decoding failed"):
                read_zip_member(archive, 0, 0, 1)

    def test_cli_uses_same_read_only_artifact_core(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "data.bin"
            source.write_bytes(b"\x00RORE\xff")
            cli = Path(__file__).resolve().parents[1] / "scripts" / "rore.py"
            for args in [("capabilities",), ("file-inspect", str(source)),
                         ("file-bytes", str(source), "1", "4")]:
                result = subprocess.run([sys.executable, str(cli), *args], capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(json.loads(result.stdout)["ok"])
            result = subprocess.run([sys.executable, str(cli), "file-bytes", str(source), "4", "4"],
                                    capture_output=True, text=True, encoding="utf-8")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("no partial bytes", result.stderr)
            self.assertEqual(len(capabilities()["operations"]), 7)

    def test_directory_inventory_pages_metadata_without_following_link(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "app"
            root.mkdir()
            (root / "asset.png").write_bytes(b"png-candidate")
            (root / "code").mkdir()
            (root / "code" / "main.js").write_text("// example", encoding="utf-8")
            first = inventory_directory(root, limit=2)
            second = inventory_directory(root, offset=first["next_offset"], limit=2)
            names = [entry["path"] for entry in first["entries"] + second["entries"]]
            self.assertEqual(set(names), {"asset.png", "code", "code/main.js"})
            self.assertEqual(first["total_entries"], 3)
            self.assertEqual(first["coverage"], "enumerated-once")
            self.assertIn("not atomic", first["limit"])

    def test_pe_layout_distinguishes_file_offset_rva_and_preferred_va(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "layout.exe"
            data = bytearray(0x400)
            data[:2] = b"MZ"
            data[0x3c:0x40] = (0x80).to_bytes(4, "little")
            data[0x80:0x84] = b"PE\0\0"
            data[0x84:0x86] = (0x8664).to_bytes(2, "little")
            data[0x86:0x88] = (1).to_bytes(2, "little")
            data[0x94:0x96] = (0xF0).to_bytes(2, "little")
            data[0x98:0x9a] = (0x20B).to_bytes(2, "little")
            data[0x98 + 24:0x98 + 32] = (0x140000000).to_bytes(8, "little")
            data[0x98 + 60:0x98 + 64] = (0x200).to_bytes(4, "little")
            section = 0x80 + 24 + 0xF0
            data[section:section + 8] = b".text\0\0\0"
            for at, value in ((8, 0x180), (12, 0x1000), (16, 0x200), (20, 0x200)):
                data[section + at:section + at + 4] = value.to_bytes(4, "little")
            source.write_bytes(data)
            layout = inspect_binary_layout(source)
            self.assertEqual(layout["format"], "pe")
            mapped = map_file_offset(source, 0x210)
            self.assertEqual(mapped["status"], "mapped")
            self.assertEqual(mapped["candidates"][0]["rva"], 0x1010)
            self.assertEqual(mapped["candidates"][0]["preferred_va"], 0x140001010)
            self.assertFalse(map_file_offset(source, 0x390)["candidates"][0]["within_declared_virtual_size"])

    def test_elf_layout_reports_link_time_address_without_runtime_base(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "layout.elf"
            data = bytearray(0x120)
            data[:6] = b"\x7fELF\x02\x01"
            data[16:18] = (3).to_bytes(2, "little")
            data[18:20] = (0x3e).to_bytes(2, "little")
            data[32:40] = (64).to_bytes(8, "little")
            data[54:56] = (56).to_bytes(2, "little")
            data[56:58] = (1).to_bytes(2, "little")
            data[64:68] = (1).to_bytes(4, "little")
            for at, value in ((72, 0x100), (80, 0x2000), (96, 0x20), (104, 0x30)):
                data[at:at + 8] = value.to_bytes(8, "little")
            source.write_bytes(data)
            layout = inspect_binary_layout(source)
            self.assertEqual(layout["format"], "elf")
            self.assertEqual(layout["load_segments"][0]["file_size"], 0x20)
            mapped = map_file_offset(source, 0x110)
            self.assertEqual(mapped["candidates"][0]["link_time_vaddr"], 0x2010)
            self.assertEqual(mapped["status"], "mapped")
            self.assertEqual(map_file_offset(source, 0x80)["status"], "unmapped")

    def test_pe_layout_reports_overlap_without_choosing_loader_mapping(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "overlap.exe"
            data = bytearray(0x500)
            data[:2] = b"MZ"
            data[0x3c:0x40] = (0x80).to_bytes(4, "little")
            data[0x80:0x84] = b"PE\0\0"
            data[0x86:0x88] = (3).to_bytes(2, "little")
            data[0x94:0x96] = (0xF0).to_bytes(2, "little")
            data[0x98:0x9a] = (0x10B).to_bytes(2, "little")
            section_at = 0x80 + 24 + 0xF0
            for index, (name, raw_offset, raw_size, virtual_size) in enumerate((
                (b".rsrc", 0x200, 0x100, 0x100),
                (b".reloc", 0x280, 0x80, 0x80),
                (b".bss", 0, 0, 0x200),
            )):
                at = section_at + index * 40
                data[at:at + len(name)] = name
                for offset, value in ((8, virtual_size), (12, 0x1000 + index * 0x1000),
                                      (16, raw_size), (20, raw_offset)):
                    data[at + offset:at + offset + 4] = value.to_bytes(4, "little")
            source.write_bytes(data)
            diagnostics = inspect_binary_layout(source)["raw_layout_diagnostics"]
            self.assertEqual(diagnostics["overlapping_raw_ranges"], [{
                "section_indices": [0, 1], "file_offset_start": 0x280,
                "file_offset_end_exclusive": 0x300,
            }])
            self.assertEqual(diagnostics["zero_raw_sections"], [2])
            self.assertEqual(map_file_offset(source, 0x290)["status"], "ambiguous")


if __name__ == "__main__":
    unittest.main()
