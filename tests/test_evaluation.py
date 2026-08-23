from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from discovery_runtime.evaluation import bounded_projection_value, run_against_disposable_workspace, stable_projection


class EvaluationTests(unittest.TestCase):
    def test_model_visible_diagnostic_is_bounded(self) -> None:
        value = bounded_projection_value({"actual": "x" * 5_000})
        self.assertLess(len(value["actual"]), 700)
        self.assertIn("exact raw externally custodied", value["actual"])

    def test_model_visible_diagnostic_normalizes_known_volatility(self) -> None:
        def raw(uuid, path, duration):
            return {
                "stdout": '{"passed":false,"failures":[{"case":"volatile","error":"id '
                + uuid
                + " at "
                + path.replace("\\", "\\\\")
                + " after "
                + duration
                + '"}]}',
                "exit_code": 1,
            }

        left = stable_projection(
            raw("123e4567-e89b-12d3-a456-426614174000", r"C:\\Temp\\one\\x.js", "12.4 ms"),
            check_id="test",
            candidate_id="a" * 64,
        )
        right = stable_projection(
            raw("223e4567-e89b-12d3-a456-426614174999", r"D:\\Tmp\\two\\x.js", "91.8 ms"),
            check_id="test",
            candidate_id="a" * 64,
        )
        self.assertEqual(left, right)

    def test_candidate_side_effect_is_confined_and_recorded(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp) / "live"
            workspace.mkdir()
            (workspace / "candidate.txt").write_text("before", encoding="utf-8")

            def mutating_operation(copied: Path):
                (copied / "candidate.txt").write_text("after", encoding="utf-8")
                return {
                    "command": ["synthetic"],
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "stdout_sha256": "",
                    "stderr_sha256": "",
                }

            raw = run_against_disposable_workspace(workspace, mutating_operation)
            self.assertEqual((workspace / "candidate.txt").read_text(encoding="utf-8"), "before")
            self.assertFalse(raw["integrity"]["passed"])
            self.assertEqual(raw["process_exit_code"], 0)
            self.assertEqual(raw["exit_code"], 1)


if __name__ == "__main__":
    unittest.main()
