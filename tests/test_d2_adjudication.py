from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_d2_adjudication import (
    DEFAULT_RECORD,
    canonical_json_bytes,
    validate,
)


class D2AdjudicationTest(unittest.TestCase):
    def test_gold_record_is_candidate_bound_and_ready(self) -> None:
        result = validate(DEFAULT_RECORD)
        self.assertTrue(result["passed"], result["failures"])
        self.assertEqual("ready", result["derived_closure_readiness"])
        self.assertEqual(13, len(result["criterion_statuses"]))
        self.assertEqual({"met"}, set(result["criterion_statuses"].values()))

    def test_frozen_closure_rule_rejects_non_met_ready_record(self) -> None:
        record = json.loads(DEFAULT_RECORD.read_text(encoding="utf-8"))
        record["criterion_dispositions"][0]["disposition"] = "partial"
        with tempfile.TemporaryDirectory(prefix="d2-adjudication-test-") as temporary:
            path = Path(temporary) / "record.json"
            path.write_bytes(canonical_json_bytes(record))
            result = validate(path)
        self.assertFalse(result["passed"])
        self.assertEqual("not_ready", result["derived_closure_readiness"])
        self.assertTrue(
            any("closure_readiness" in failure for failure in result["failures"])
        )


if __name__ == "__main__":
    unittest.main()
