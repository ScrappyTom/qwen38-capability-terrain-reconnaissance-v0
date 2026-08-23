from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from discovery_runtime.handoff import build_d6_message, select_d6_donor


class HandoffTests(unittest.TestCase):
    def test_first_changed_donor_and_null(self) -> None:
        rows = [{"cell_id": cell, "initial_candidate_id": "a", "final_candidate_id": "a"} for cell in ("D2", "D3", "D4", "D5")]
        self.assertIsNone(select_d6_donor(rows))
        rows[2]["final_candidate_id"] = "b"
        self.assertEqual(select_d6_donor(rows), "D4")

    def test_handoff_contains_exact_candidate_but_no_readiness(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "candidate.txt").write_text("exact current bytes", encoding="utf-8")
            (root / "unread.txt").write_text("must not be injected", encoding="utf-8")
            message = build_d6_message(donor_cell="D3", task_text="task", workspace=root, mutable_paths={"candidate.txt"}, visible_check_id="npm_test", candidate_id="a" * 64, latest_check=None, observation_receipts=[])
            self.assertIn("exact current bytes", message)
            self.assertNotIn("must not be injected", message)
            self.assertIn("not_run_for_current_candidate", message)
            self.assertIn("npm_test", message)
            self.assertNotIn("closure_ready", message)


if __name__ == "__main__":
    unittest.main()
