from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from discovery_runtime.canonical import canonical_json_bytes, sha256_bytes, write_canonical_json
from discovery_runtime.runner import CellRunner


class RunnerTests(unittest.TestCase):
    def test_d6_inherited_result_reopens_and_new_identity_does_not_alias(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fixture = root / "fixture"
            workspace = fixture / "workspace"
            workspace.mkdir(parents=True)
            (workspace / "candidate.txt").write_text("candidate", encoding="utf-8")
            (fixture / "task.md").write_text("task", encoding="utf-8")

            parent = root / "parent"
            result_dir = parent / "results" / "RESULT-001"
            result_dir.mkdir(parents=True)
            original = {
                "schema_version": "exact-action-result-v0",
                "result_id": "RESULT-001",
                "tool": "read",
                "content": "old exact evidence",
                "candidate_id": "0" * 64,
            }
            body = canonical_json_bytes(original)
            (result_dir / "result.json").write_bytes(body)
            write_canonical_json(
                result_dir / "receipt.json",
                {
                    "result_id": "RESULT-001",
                    "exact_body_bytes": len(body),
                    "exact_body_sha256": sha256_bytes(body),
                    "exact_reopen": {"action": "reopen_exact", "result_id": "RESULT-001"},
                },
            )

            runner = CellRunner(
                repo_root=root,
                cell_id="D6",
                cell={
                    "fixture": "fixture",
                    "workspace": "workspace",
                    "task": "task.md",
                    "mutable_paths": ["candidate.txt"],
                    "call_ceiling": 1,
                    "donor_cell": "D3",
                },
                profile={},
                run_root=root / "run",
                inherited_result_root=parent,
            )
            reopened, terminal = runner.execute(
                {"action": "reopen_exact", "result_id": "RESULT-001"}, root / "call"
            )
            self.assertFalse(terminal)
            self.assertEqual(reopened["source_result_id"], "RESULT-001")
            self.assertEqual(reopened["reopened_exact_result"]["content"], "old exact evidence")
            self.assertEqual(reopened["reopened_exact_result"]["candidate_id"], "0" * 64)
            self.assertEqual(reopened["reopened_exact_body_sha256"], sha256_bytes(body))

            stored = runner._save_result(reopened, message_index=2)
            self.assertEqual(stored.result_id, "RESULT-002")
            self.assertEqual(json.loads(stored.body)["result_id"], "RESULT-002")
            self.assertIn("RESULT-001", runner.reopen_store)
            self.assertIn("RESULT-002", runner.reopen_store)
            reopened_again, _ = runner.execute(
                {"action": "reopen_exact", "result_id": "RESULT-001"}, root / "call-2"
            )
            self.assertEqual(reopened_again["reopened_exact_result"]["content"], "old exact evidence")
            self.assertEqual(reopened_again["source_result_id"], "RESULT-001")

    def test_pressure_relief_skips_a_non_saving_receipt(self) -> None:
        class CharacterTokenizer:
            @staticmethod
            def count_messages(messages):
                rendered = "".join(row["content"] for row in messages)
                return len(rendered), rendered

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fixture = root / "fixture"
            workspace = fixture / "workspace"
            workspace.mkdir(parents=True)
            (workspace / "candidate.txt").write_text("candidate", encoding="utf-8")
            (fixture / "task.md").write_text("task", encoding="utf-8")
            runner = CellRunner(
                repo_root=root,
                cell_id="D3",
                cell={
                    "fixture": "fixture",
                    "workspace": "workspace",
                    "task": "task.md",
                    "mutable_paths": ["candidate.txt"],
                    "call_ceiling": 1,
                },
                profile={"prompt_ceiling_tokens": 0},
                run_root=root / "run",
            )
            runner.tokenizer = CharacterTokenizer()
            runner.messages = [{"role": "user", "content": "x"}]
            stored = runner._save_result({"tool": "submit", "accepted": True}, message_index=0)
            stored.delivered_at_call = 1
            (runner.run_root / "calls" / "call-001").mkdir(parents=True)
            receipt = runner._relieve_if_needed(1)
            self.assertFalse(receipt["fit"])
            self.assertFalse(stored.demoted)
            self.assertEqual([row["result_id"] for row in receipt["skipped_nonpositive"]], ["RESULT-001"])

    def test_mutation_marks_prior_check_stale(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fixture = root / "fixture"
            workspace = fixture / "workspace"
            workspace.mkdir(parents=True)
            target = workspace / "candidate.txt"
            target.write_text("before", encoding="utf-8")
            (fixture / "task.md").write_text("task", encoding="utf-8")
            runner = CellRunner(
                repo_root=root,
                cell_id="D3",
                cell={
                    "fixture": "fixture",
                    "workspace": "workspace",
                    "task": "task.md",
                    "mutable_paths": ["candidate.txt"],
                    "call_ceiling": 1,
                },
                profile={},
                run_root=root / "run",
            )
            runner.latest_check = {
                "evaluated_candidate_id": runner.world.candidate_id,
                "current_candidate_id": runner.world.candidate_id,
                "currency": "current",
            }
            expected = runner.world.read("candidate.txt")["file_sha256"]
            runner.execute(
                {
                    "action": "replace_file",
                    "path": "candidate.txt",
                    "content": "after",
                    "expected_file_sha256": expected,
                },
                root / "call",
            )
            self.assertEqual(runner.latest_check["currency"], "stale")
            self.assertEqual(runner.latest_check["current_candidate_id"], runner.world.candidate_id)


if __name__ == "__main__":
    unittest.main()
