from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from discovery_runtime.canonical import canonical_json_bytes, sha256_bytes, sha256_file, write_canonical_json
from discovery_runtime.postflight import verify_cell_postflight
from discovery_runtime.worlds import FileWorld


class PostflightTests(unittest.TestCase):
    def test_exact_mutation_replay_and_one_attempt(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source"
            source.mkdir()
            target = source / "candidate.txt"
            target.write_text("before", encoding="utf-8")
            expected = sha256_file(target)

            actual_world = FileWorld(
                source=source,
                runtime_root=root / "actual-world",
                mutable_paths={"candidate.txt"},
            )
            action = {
                "action": "replace_file",
                "path": "candidate.txt",
                "content": "after",
                "expected_file_sha256": expected,
            }
            result = actual_world.replace_file("candidate.txt", "after", expected)
            result_value = {
                **result,
                "schema_version": "exact-action-result-v0",
                "result_id": "RESULT-001",
            }

            run = root / "run"
            (run / "calls" / "call-001" / "provider-attempt-1").mkdir(parents=True)
            result_dir = run / "results" / "RESULT-001"
            result_dir.mkdir(parents=True)
            body = canonical_json_bytes(result_value)
            (result_dir / "result.json").write_bytes(body)
            write_canonical_json(
                result_dir / "receipt.json",
                {
                    "result_id": "RESULT-001",
                    "exact_body_bytes": len(body),
                    "exact_body_sha256": sha256_bytes(body),
                    "mechanical_identity": {"tool": "replace_file", "path": "candidate.txt"},
                    "exact_reopen": {"action": "reopen_exact", "result_id": "RESULT-001"},
                },
            )
            (run / "workspace").mkdir()
            (run / "workspace" / "candidate.txt").write_text("after", encoding="utf-8")
            write_canonical_json(
                run / "RESULT.json",
                {
                    "initial_candidate_id": actual_world.initial_manifest["manifest_sha256"],
                    "final_candidate_id": actual_world.candidate_id,
                    "calls": [{"call": 1, "action": action, "result_id": "RESULT-001"}],
                },
            )

            receipt = verify_cell_postflight(
                run_root=run,
                workspace_source=source,
                mutable_paths={"candidate.txt"},
            )
            self.assertTrue(receipt["passed"], receipt)


if __name__ == "__main__":
    unittest.main()
