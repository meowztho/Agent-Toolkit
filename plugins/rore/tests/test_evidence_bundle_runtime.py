import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from rore_runtime.bundle import (BundleError, capture_evidence, compare, export_bundle,
                                 import_bundle, init_bundle, inspect, validate)
from rore_runtime.rea_bridge import import_rea, inspect_rea_original, preview_rea


def make_bundle(root: Path) -> bytes:
    root.mkdir()
    (root / "raw").mkdir()
    raw = b"\x00\xffreference bytes\n"
    (root / "raw" / "sample.bin").write_bytes(raw)
    (root / "full-notes.md").write_text("Complete reference-native notes\n", encoding="utf-8")
    (root / "rore-evidence.json").write_text(json.dumps({
        "format": "rore-evidence-bundle", "version": 1,
        "target": {"identity": "sha256:reference", "environment": "test"},
        "evidence": [{"id": "E-001", "source": {"kind": "artifact", "locator": "sample.bin"},
                      "method": "original byte read", "raw": [{"path": "raw/sample.bin", "sha256": hashlib.sha256(raw).hexdigest()}],
                      "unabridged_detail": "preserved"}],
        "findings": [{"id": "FIND-001", "evidence_ids": ["E-001"], "statement": "hypothesis"}],
        "paths": [{"id": "PATH-001", "evidence_ids": ["E-001"], "finding_ids": ["FIND-001"]}],
        "models": [], "unknowns": [], "additional_material": {"kept": True},
    }, ensure_ascii=False), encoding="utf-8")
    return raw


class EvidenceBundleTests(unittest.TestCase):
    def test_public_cli_initializes_and_captures_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            source, bundle = base / "trace.log", base / "bundle"
            source.write_bytes(b"one complete trace\n")
            cli = Path(__file__).resolve().parents[1] / "scripts" / "rore.py"
            for arguments in (("bundle-init", str(bundle), "sha256:target", "--environment", "test"),
                              ("evidence-add", str(bundle), "E-001", "runtime:test", "observed trace", str(source)),
                              ("validate", str(bundle))):
                result = subprocess.run([sys.executable, str(cli), *arguments],
                                        capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(json.loads(result.stdout)["ok"])
            self.assertEqual(inspect(bundle, "E-001")["record"]["method"], "observed trace")

    def test_init_and_capture_preserve_full_raw_files_and_existing_records(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            bundle = base / "bundle"
            first, second = base / "trace.json", base / "asset.bin"
            first.write_bytes(b'{"request":1}\n')
            second.write_bytes(b"\x00\xffasset bytes")
            init_bundle(bundle, "sha256:target", "test host")
            result = capture_evidence(bundle, "E-001", "artifact:sample", "capture exact files", [first, second])
            self.assertEqual(result["counts"]["evidence"], 1)
            record = inspect(bundle, "E-001")["record"]
            self.assertEqual([(bundle / item["path"]).read_bytes() for item in record["raw"]],
                             [first.read_bytes(), second.read_bytes()])
            document = json.loads((bundle / "rore-evidence.json").read_text(encoding="utf-8"))
            document["findings"].append({"id": "FIND-001", "evidence_ids": ["E-001"], "statement": "bounded"})
            (bundle / "rore-evidence.json").write_text(json.dumps(document), encoding="utf-8")
            before = (bundle / "rore-evidence.json").read_bytes()
            with self.assertRaisesRegex(BundleError, "duplicate record id"):
                capture_evidence(bundle, "E-001", "artifact:other", "repeat", [first])
            self.assertEqual((bundle / "rore-evidence.json").read_bytes(), before)
            capture_evidence(bundle, "E-002", "artifact:asset", "capture existing retained file", [bundle / record["raw"][1]["path"]])
            self.assertEqual(inspect(bundle, "FIND-001")["record"]["statement"], "bounded")
            self.assertEqual(validate(bundle)["counts"]["evidence"], 2)
            archive = base / "bundle.zip"
            export_bundle(bundle, archive)
            restored = base / "restored"
            import_bundle(archive, restored)
            self.assertEqual(compare(bundle, restored)["changed_files"], [])

    def test_capture_rejects_existing_or_invalid_bundle_without_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            bundle, source = base / "bundle", base / "raw.bin"
            source.write_bytes(b"raw")
            init_bundle(bundle, "target")
            with self.assertRaisesRegex(BundleError, "already exists"):
                init_bundle(bundle, "other")
            (bundle / "rore-evidence.json").write_text("not JSON", encoding="utf-8")
            with self.assertRaisesRegex(BundleError, "invalid rore-evidence.json"):
                capture_evidence(bundle, "E-001", "source", "method", [source])
            self.assertEqual(list((bundle / "raw").iterdir()), [])

    def test_rea_6_2_0_writer_export_import(self):
        source = Path(__file__).parent / "fixtures" / "rea_6_2_0_export.json"
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),
                         "8b2a9957142c17f1545db1f748078234a9166c8ef00fa3c8c17f8cd7a63ea198")
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "imported"
            info = import_rea(source, destination)
            self.assertEqual(info["counts"]["evidence"], 2)
            self.assertEqual((destination / "raw/rea-evidence-bundle.json").read_bytes(), source.read_bytes())
            record = inspect_rea_original(
                destination, "ev_99c602b583a82295c08923db5439e21c09117fb91af8869612e9225d752698ad")
            self.assertEqual(record["record"]["normalized_result"], {"magic": "MZ"})

    def test_rea_6_2_0_unknown_revision_export(self):
        source = Path(__file__).parent / "fixtures" / "rea_6_2_0_unknown_revisions.json"
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),
                         "69af0b84504379ff0a8cb11e6f888c02e30dbcfdc2ec6ecbbb3ecc97d7af5ad4")
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "imported"
            import_rea(source, destination)
            self.assertEqual((destination / "raw/rea-evidence-bundle.json").read_bytes(), source.read_bytes())
            self.assertEqual(validate(destination)["counts"]["unknowns"], 2)
            original = json.loads(source.read_text(encoding="utf-8"))
            for revision in original["unknowns"]:
                record_id = f"{revision['unknown_id']}:r{revision['revision']}"
                self.assertEqual(inspect_rea_original(destination, record_id)["record"], revision)


    def test_rea_export_import_keeps_original_and_revision_identities(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            source, destination = base / "rea.json", base / "rore"
            original = {
                "artifacts": [], "providers": [], "environments": [], "scenarios": [], "captures": [],
                "records": [{"evidence_id": "ev_123", "operation": "inspect bytes", "predicate_type": "rea.test",
                             "subject": {"digest": {"sha256": "a" * 64}}, "provider": {"id": "test"},
                             "raw_result": {"opaque": [1, 2]}, "normalized_result": {"value": True}},
                            {"evidence_id": "ev_456", "operation": "inspect other", "subject": {"digest": {"sha256": "b" * 64}}}],
                "unknowns": [{"unknown_id": "unk_123", "revision": 1, "question": "Why?",
                              "status": "open", "supporting_evidence_ids": ["ev_123"]},
                             {"unknown_id": "unk_123", "revision": 2, "question": "Why still?",
                              "status": "investigating", "contradicting_evidence_ids": ["ev_123"]}],
            }
            raw = json.dumps(original, ensure_ascii=False, indent=3).encode("utf-8")
            source.write_bytes(raw)
            self.assertEqual(preview_rea(source)["subject_sha256"], ["a" * 64, "b" * 64])
            cli = Path(__file__).resolve().parents[1] / "scripts" / "rore.py"
            for arguments in [("rea-preview", str(source)), ("rea-import", str(source), str(destination)),
                              ("validate", str(destination)), ("inspect", str(destination), "ev_123")]:
                result = subprocess.run([sys.executable, str(cli), *arguments], capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(json.loads(result.stdout)["ok"])
            self.assertEqual((destination / "raw/rea-evidence-bundle.json").read_bytes(), raw)
            self.assertEqual(validate(destination)["target"]["identity_scope"], "source-bundle")
            self.assertEqual(validate(destination)["counts"]["unknowns"], 2)
            self.assertEqual(inspect(destination, "unk_123:r2")["record"]["evidence_ids"], ["ev_123"])
            self.assertEqual(inspect_rea_original(destination, "ev_123")["record"], original["records"][0])
            self.assertEqual(inspect_rea_original(destination, "unk_123:r2")["record"], original["unknowns"][1])
            (destination / "raw/rea-evidence-bundle.json").write_bytes(b"changed")
            with self.assertRaisesRegex(BundleError, "hash mismatch"):
                inspect_rea_original(destination, "ev_123")
            with self.assertRaisesRegex(BundleError, "already exists|new directory"):
                import_rea(source, destination)

    def test_rea_shape_and_duplicate_ids_rejected_without_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            source, destination = base / "rea.json", base / "rore"
            source.write_text('{"records": []}', encoding="utf-8")
            with self.assertRaisesRegex(BundleError, "needs artifacts"):
                import_rea(source, destination)
            self.assertFalse(destination.exists())
            source.write_text(json.dumps({**{key: [] for key in ("artifacts", "providers", "environments", "scenarios", "captures", "unknowns")},
                                          "records": [{"evidence_id": "ev_x", "operation": "read"},
                                                      {"evidence_id": "ev_x", "operation": "read"}]}), encoding="utf-8")
            with self.assertRaisesRegex(BundleError, "duplicate REA evidence_id"):
                import_rea(source, destination)
            self.assertFalse(destination.exists())

    def test_public_cli_validate_and_export_import(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            source, restored, archive = base / "source", base / "restored", base / "handoff.zip"
            make_bundle(source)
            cli = Path(__file__).resolve().parents[1] / "scripts" / "rore.py"
            for arguments in [("validate", str(source)), ("export", str(source), str(archive)),
                              ("import", str(archive), str(restored)), ("inspect", str(restored), "E-001")]:
                result = subprocess.run([sys.executable, str(cli), *arguments], capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(json.loads(result.stdout)["ok"])
            self.assertEqual((source / "full-notes.md").read_bytes(), (restored / "full-notes.md").read_bytes())

    def test_complete_round_trip_and_compare(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            original, restored = base / "original", base / "restored"
            raw = make_bundle(original)
            self.assertEqual(validate(original)["counts"]["evidence"], 1)
            self.assertEqual(inspect(original, "E-001")["record"]["unabridged_detail"], "preserved")
            archive = base / "handoff.zip"
            export_bundle(original, archive)
            before = archive.read_bytes()
            with self.assertRaisesRegex(BundleError, "new file"):
                export_bundle(original, archive)
            self.assertEqual(archive.read_bytes(), before)
            self.assertEqual(zipfile.ZipFile(archive).getinfo("raw/sample.bin").compress_type, zipfile.ZIP_STORED)
            import_bundle(archive, restored)
            self.assertEqual((restored / "raw/sample.bin").read_bytes(), raw)
            self.assertEqual((restored / "full-notes.md").read_bytes(), (original / "full-notes.md").read_bytes())
            self.assertEqual(compare(original, restored)["changed_files"], [])
            self.assertFalse(compare(original, restored)["only_left_ids"])

    def test_tamper_and_broken_link_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "bundle"
            make_bundle(root)
            (root / "raw/sample.bin").write_bytes(b"changed")
            with self.assertRaisesRegex(BundleError, "hash mismatch"):
                validate(root)
            make_bundle(Path(temp) / "another")
            another = Path(temp) / "another"
            document = json.loads((another / "rore-evidence.json").read_text(encoding="utf-8"))
            document["findings"][0]["evidence_ids"] = ["E-404"]
            (another / "rore-evidence.json").write_text(json.dumps(document), encoding="utf-8")
            with self.assertRaisesRegex(BundleError, "invalid evidence_ids"):
                validate(another)

    def test_archive_path_traversal_is_rejected_without_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            archive, destination = base / "unsafe.zip", base / "destination"
            with zipfile.ZipFile(archive, "w") as output:
                output.writestr("../escape.txt", "bad")
            with self.assertRaisesRegex(BundleError, "unsafe relative path"):
                import_bundle(archive, destination)
            self.assertFalse(destination.exists())
            self.assertFalse((base / "escape.txt").exists())
            with zipfile.ZipFile(archive, "w") as output:
                output.writestr("CON.txt", "bad")
            with self.assertRaisesRegex(BundleError, "unsafe relative path"):
                import_bundle(archive, destination)


if __name__ == "__main__":
    unittest.main()
