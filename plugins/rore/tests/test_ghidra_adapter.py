import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from rore_runtime.ghidra_adapter import analyze


class GhidraAdapterTests(unittest.TestCase):
    def test_import_identity_and_analysis_limits_control_status(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "sample.bin"
            source.write_bytes(b"exact target bytes")
            expected_md5 = hashlib.md5(source.read_bytes()).hexdigest()
            qualified = {"headless": str(root / "provider"), "jdk": str(root),
                         "provider": "ghidra-headless", "status": "components-qualified-not-target-tested"}

            def run_case(label, imported_md5, timed_out=False, selection=None,
                         decompile_file=False, malformed=False, omit_selection=False,
                         refs_complete=True, omit_refs=False):
                class FinishedProvider:
                    def __init__(self, command, **_kwargs):
                        output = Path(command[command.index("-postScript") + 2])
                        analysis = {"schema_version": 1, "provider": "ghidra-headless",
                                    "auto_analysis_timed_out": timed_out,
                                    "program": {"executable_md5": imported_md5}}
                        for key in ("functions", "strings", "external_symbols", "external_entry_points"):
                            analysis[key] = {"total": 0, "emitted": 0, "complete": True}
                        if selection is not None:
                            analysis["selected_function"] = {"requested_address": "1000", "status": selection}
                            if selection == "decompiled":
                                analysis["selected_function"]["function_entry"] = "1000"
                                analysis["selected_function"]["output_file"] = "decompile.c"
                                analysis["selected_function"]["instructions"] = {
                                    "total": 1, "emitted": 1, "complete": True,
                                    "items": [{"address": "1000", "bytes_hex": "90", "listing": "NOP"}]}
                                if not omit_refs:
                                    analysis["selected_function"]["references"] = {
                                        "total": 2 if not refs_complete else 1, "emitted": 1,
                                        "complete": refs_complete,
                                        "items": [{"from": "1000", "from_space": "ram", "to": "2000",
                                                   "to_space": "ram", "type": "DATA",
                                                   "source": "ANALYSIS", "operand_index": 0,
                                                   "external": False, "memory": True, "stack": False,
                                                   "register": False, "flow": False, "read": True,
                                                   "write": False, "indirect": False}]}
                                if decompile_file:
                                    (output.parent / "decompile.c").write_text("void f() {}", encoding="utf-8")
                        if omit_selection:
                            analysis.pop("selected_function", None)
                        output.write_text("[]" if malformed else json.dumps(analysis), encoding="utf-8")

                    def wait(self, **_kwargs):
                        return 0

                with patch("rore_runtime.ghidra_adapter.probe", return_value=qualified), \
                     patch("rore_runtime.ghidra_adapter.subprocess.Popen", FinishedProvider):
                    return analyze(root, root, source, root / label,
                                   address="1000" if selection is not None else None)

            completed = run_case("completed", expected_md5)
            self.assertEqual(completed["status"], "completed")
            self.assertTrue(completed["import_identity"]["verified"])
            self.assertEqual((root / "completed" / "input" / source.name).read_bytes(), source.read_bytes())
            self.assertEqual(run_case("analysis-timeout", expected_md5, timed_out=True)["status"], "partial")
            self.assertEqual(run_case("no-function", expected_md5, selection="no_function_at_address")["status"], "partial")
            missing_decompile = run_case("missing-decompile", expected_md5, selection="decompiled")
            self.assertEqual(missing_decompile["status"], "failed")
            selected = run_case("with-decompile", expected_md5,
                                selection="decompiled", decompile_file=True)
            self.assertEqual(selected["status"], "completed")
            self.assertEqual(selected["selected_function"]["references"]["items"][0]["to"], "2000")
            self.assertEqual(run_case("capped-references", expected_md5, selection="decompiled",
                                      decompile_file=True, refs_complete=False)["status"], "partial")
            self.assertEqual(run_case("missing-references", expected_md5, selection="decompiled",
                                      decompile_file=True, omit_refs=True)["status"], "failed")
            omitted = run_case("selection-omitted", expected_md5,
                               selection="decompiled", decompile_file=True, omit_selection=True)
            self.assertEqual(omitted["status"], "failed")
            self.assertIn("omitted", omitted["error"])
            mismatch = run_case("wrong-import", "0" * 32)
            self.assertEqual(mismatch["status"], "failed")
            self.assertIn("do not match", mismatch["error"])
            self.assertEqual(json.loads((root / "wrong-import" / "run.json").read_text())["status"], "failed")
            malformed_export = run_case("malformed-export", expected_md5, malformed=True)
            self.assertEqual(malformed_export["status"], "failed")
            self.assertIn("schema/provider identity mismatch", malformed_export["error"])

    def test_existing_run_directory_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "sample.bin"
            source.write_bytes(b"source")
            output = root / "existing"
            output.mkdir()
            marker = output / "keep"
            marker.write_bytes(b"original")
            with patch("rore_runtime.ghidra_adapter.probe", return_value={"headless": "unused", "jdk": str(root)}):
                with self.assertRaises(FileExistsError):
                    analyze(root, root, source, output)
            self.assertEqual(marker.read_bytes(), b"original")

    def test_selection_sentinel_cannot_be_requested(self):
        with self.assertRaisesRegex(ValueError, "address must"):
            analyze("unused", "unused", "unused", "unused", address="none")
