import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from rore_runtime.provider_jobs import (_run, analysis_page, decompilation_page, start_analysis,
                                        status, ProviderJobError)


class ProviderJobTests(unittest.TestCase):
    def test_analysis_start_checks_target_and_new_output_before_job_creation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "sample.bin"
            source.write_bytes(b"target")
            jobs = root / "jobs"
            with self.assertRaisesRegex(ProviderJobError, "new directory"):
                start_analysis(source, root, jobs_root=jobs)
            self.assertFalse(jobs.exists())
            with patch("rore_runtime.provider_jobs._start", return_value={"status": "started"}) as spawn:
                result = start_analysis(source, root / "new-run", root=root / "providers",
                                        jobs_root=jobs)
            self.assertEqual(result["status"], "started")
            request = spawn.call_args.args[0]
            self.assertEqual(request["source"], str(source))
            self.assertTrue(request["auto_install"])

    def test_runner_uses_existing_setup_and_retains_a_hash_checked_page(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            jobs = root / "jobs"
            job_id = "a" * 32
            job = jobs / job_id
            job.mkdir(parents=True)
            output = root / "analysis"
            source = root / "sample.bin"
            source.write_bytes(b"target")
            request = {"kind": "ghidra-analysis", "root": str(root / "providers"),
                       "source": str(source), "output": str(output), "address": "1000",
                       "timeout_seconds": 60, "archives": None, "auto_install": True}
            (job / "request.json").write_text(json.dumps(request), encoding="utf-8")

            def fake_analyze(_install, _jdk, _source, out, **_kwargs):
                out = Path(out)
                out.mkdir()
                analysis = {"schema_version": 1, "provider": "ghidra-headless",
                            "program": {"name": "sample.bin"},
                            "selected_function": {"references": {"total": 2, "emitted": 2,
                                                                 "complete": True,
                                                                 "items": [{"from": "1000", "to": "2000"},
                                                                           {"from": "1001", "to": "3000"}]}}}
                raw = json.dumps(analysis).encode()
                (out / "analysis.json").write_bytes(raw)
                pseudocode = b"void example(void) {}"
                (out / "decompile.c").write_bytes(pseudocode)
                run = {"status": "completed", "copy_integrity": {"unchanged": True},
                       "import_identity": {"verified": True}, "auto_analysis_timed_out": False,
                       "output_files": {"analysis.json": {"sha256": hashlib.sha256(raw).hexdigest()},
                                        "decompile.c": {"sha256": hashlib.sha256(pseudocode).hexdigest()}}}
                (out / "run.json").write_text(json.dumps(run), encoding="utf-8")
                return run

            with patch("rore_runtime.provider_jobs.probe", side_effect=ValueError("missing")), \
                 patch("rore_runtime.provider_jobs.install_ghidra") as setup, \
                 patch("rore_runtime.provider_jobs.analyze", side_effect=fake_analyze):
                _run(job)
            setup.assert_called_once()
            self.assertEqual(status(job_id, jobs_root=jobs)["status"], "completed")
            page = analysis_page(output, "references", offset=1, limit=1)
            self.assertEqual(page["items"], [{"from": "1001", "to": "3000"}])
            self.assertTrue(page["import_verified"])
            self.assertTrue(analysis_page(output, "run")["value"]["import_identity"]["verified"])
            self.assertEqual(decompilation_page(output, offset=5, characters=7)["text"], "example")
            (output / "decompile.c").write_bytes(b"tampered")
            with self.assertRaisesRegex(ProviderJobError, "hash differs"):
                decompilation_page(output)
            (output / "analysis.json").write_bytes(b"tampered")
            with self.assertRaisesRegex(ProviderJobError, "hash differs"):
                analysis_page(output, "references")

    def test_dead_worker_is_reported_as_interrupted_without_mutating_retained_state(self):
        with tempfile.TemporaryDirectory() as temp:
            job_id = "b" * 32
            job = Path(temp) / job_id
            job.mkdir()
            retained = {"job_id": job_id, "kind": "ghidra-install", "status": "queued"}
            (job / "state.json").write_text(json.dumps(retained), encoding="utf-8")
            (job / "pid.txt").write_text("12345", encoding="ascii")
            with patch("rore_runtime.provider_jobs._process_alive", return_value=False):
                observed = status(job_id, jobs_root=temp)
            self.assertEqual(observed["status"], "interrupted")
            self.assertEqual(observed["retained_status"], "queued")
            self.assertEqual(json.loads((job / "state.json").read_text(encoding="utf-8")), retained)


if __name__ == "__main__":
    unittest.main()
