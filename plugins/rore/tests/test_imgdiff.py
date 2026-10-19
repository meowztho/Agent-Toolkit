import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import rore_imgdiff as diff


def capture(x, height=32):
    rows = [[(255, 255, 255) for _ in range(48)] for _ in range(height)]
    for y in range(8, 16):
        for col in range(x, x + 8):
            rows[y][col] = (0, 0, 0)
    return 48, height, rows


class ReferenceImageDiffTests(unittest.TestCase):
    def test_visual_indicator_is_not_an_equivalence_verdict(self):
        first, second = capture(6), capture(24)
        layout, _ = diff.compare(first, second, cols=1)
        pixel, _ = diff.compare(first, second, mode="pixel")
        self.assertEqual(layout["similarity_indicator"], 100.0)
        self.assertLess(pixel["similarity_indicator"], 100.0)
        self.assertNotIn("verdict", layout)
        self.assertTrue(pixel["regions"])

    def test_cli_binds_output_to_input_bytes_and_reports_crop(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "v1.png"
            second = Path(directory) / "v2.png"
            output = Path(directory) / "changes.png"
            diff.write_png(first, *capture(6))
            diff.write_png(second, *capture(24, height=40))
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                self.assertEqual(diff.main([str(first), str(second), "--mode", "pixel",
                                            "--out", str(output), "--json"]), 0)
            report = json.loads(stdout.getvalue())
            self.assertEqual(report["sha256"]["first"], hashlib.sha256(first.read_bytes()).hexdigest())
            self.assertEqual(report["sha256"]["second"], hashlib.sha256(second.read_bytes()).hexdigest())
            self.assertEqual(report["compared_at"]["height"], 32)
            self.assertGreater(report["height_delta_pct"], 0)
            self.assertTrue(output.is_file())
            self.assertNotIn("verdict", report)

    def test_corrupt_png_crc_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "bad.png"
            diff.write_png(source, *capture(6))
            damaged = bytearray(source.read_bytes())
            damaged[29] ^= 1
            source.write_bytes(damaged)
            with self.assertRaisesRegex(diff.PngError, "CRC"):
                diff.read_png(source)

    def test_cli_never_overwrites_a_reference_or_existing_diff(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.png"
            second = Path(directory) / "second.png"
            output = Path(directory) / "existing.png"
            diff.write_png(first, *capture(6))
            diff.write_png(second, *capture(24))
            output.write_bytes(b"keep me")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(diff.main([str(first), str(second), "--out", str(output)]), 2)
            self.assertEqual(output.read_bytes(), b"keep me")
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    diff.main([str(first), str(second), "--out", str(first)])
            self.assertEqual(diff.read_png(first)[0:2], (48, 32))


if __name__ == "__main__":
    unittest.main()
