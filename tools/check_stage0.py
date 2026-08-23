from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery_runtime.canonical import sha256_file
from discovery_runtime.manifest import recursive_manifest
from tools.validate_d2_adjudication import DEFAULT_RECORD, validate as validate_d2_adjudication


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-external-hashes",
        action="store_true",
        help="Skip large host-asset hashing in unit tests; the canonical pre-freeze check omits this flag.",
    )
    args = parser.parse_args()
    failures: list[str] = []
    source_lock = json.loads((ROOT / "SOURCE_LOCK.json").read_bytes())
    for row in source_lock["files"]:
        path = ROOT / row["path"]
        if not path.is_file():
            failures.append(f"source_lock_missing:{row['path']}")
            continue
        if path.stat().st_size != row["bytes"] or sha256_file(path) != row["sha256"]:
            failures.append(f"source_lock_mismatch:{row['path']}")

    for name, relative in (
        ("fixture", "fixtures"),
        ("gold", "qualification/gold"),
        ("evaluator", "qualification/evaluators"),
        ("adjudication", "qualification/adjudications"),
    ):
        expected = json.loads((ROOT / f"{name.upper()}_MANIFEST.json").read_bytes())
        actual = recursive_manifest(ROOT / relative)
        if actual != expected:
            failures.append(f"{name}_manifest_mismatch")

    provenance = json.loads((ROOT / "MATERIALIZATION_PROVENANCE.json").read_bytes())
    provenance_rows = provenance.get("rows", [])
    destinations = [row.get("destination") for row in provenance_rows]
    if provenance.get("row_count") != 154 or len(provenance_rows) != 154:
        failures.append("materialization_provenance_row_count")
    if len(set(destinations)) != len(destinations):
        failures.append("materialization_provenance_duplicate_destination")
    direct_rows = [row for row in provenance_rows if row.get("derivation") == "exact_git_blob_bytes"]
    if len(direct_rows) != 149 or provenance.get("all_direct_rows_byte_equal") is not True:
        failures.append("materialization_provenance_direct_rows")
    for row in provenance_rows:
        destination = row.get("destination")
        if not isinstance(destination, str):
            failures.append("materialization_provenance_invalid_destination")
            continue
        path = ROOT / destination
        if not path.is_file():
            failures.append(f"materialization_provenance_missing:{destination}")
            continue
        if path.stat().st_size != row.get("materialized_bytes") or sha256_file(path) != row.get("materialized_sha256"):
            failures.append(f"materialization_provenance_mismatch:{destination}")
        if row.get("derivation") == "exact_git_blob_bytes":
            if row.get("byte_equal") is not True or not all(
                isinstance(row.get(key), str) and row.get(key)
                for key in ("repository", "commit", "source_path", "git_blob_oid", "source_sha256")
            ):
                failures.append(f"materialization_provenance_incomplete_direct:{destination}")

    profile = json.loads((ROOT / "MODEL_PROFILE_LOCK.json").read_bytes())
    if not args.skip_external_hashes:
        for label, path_key, hash_key in (
            ("model", "model_path", "model_sha256"),
            ("tokenizer_projection", "tokenizer_projection_path", "tokenizer_projection_sha256"),
            ("server", "server_path", "server_sha256"),
            ("tokenizer", "tokenizer_path", "tokenizer_sha256"),
        ):
            path = Path(profile[path_key])
            if not path.is_file() or sha256_file(path) != profile[hash_key]:
                failures.append(f"{label}_lock_mismatch")

    contract = json.loads((ROOT / "TRANCHE_CONTRACT.json").read_bytes())
    calls = sum(contract["cells"][cell]["call_ceiling"] for cell in ("D1", "D2", "D3", "D4", "D5", "D6"))
    if calls != contract["max_total_actor_calls"] or calls != 42:
        failures.append("call_ceiling_arithmetic")
    token_ceiling = calls * (contract["prompt_ceiling_tokens"] + contract["completion_allowance_tokens"])
    if token_ceiling != contract["max_total_serialized_tokens"]:
        failures.append("token_ceiling_arithmetic")
    if contract["run_order"] != ["D1", "D2", "D3", "D4", "D5", "D6"]:
        failures.append("run_order")

    qualification = json.loads((ROOT / "STAGE0_QUALIFICATION.json").read_bytes())
    if qualification.get("passed") is not True or qualification.get("failures") != []:
        failures.append("stage0_not_qualified")
    if qualification.get("no_model_calls") is not True:
        failures.append("stage0_model_calls")
    if [row["cell_id"] for row in qualification["full_task_cells"]] != ["D2", "D3", "D4", "D5"]:
        failures.append("qualified_cell_order")
    if [row["donor_cell"] for row in qualification["D6"]["branches"]] != ["D2", "D3", "D4", "D5"]:
        failures.append("d6_branch_order")
    if not all(
        row.get("actual_packet_live_capacity_gate") is True
        and row.get("stress_packet_fits") is True
        and row.get("stress_current_check_prompt_tokens", contract["prompt_ceiling_tokens"] + 1)
        <= contract["prompt_ceiling_tokens"]
        for row in qualification["D6"]["branches"]
    ):
        failures.append("d6_capacity_qualification")
    if qualification["D6"]["null"] != {"backup": None, "model_calls": 0, "qualified": True, "slot_consumed": True}:
        failures.append("d6_null")
    if qualification["D6"].get("capacity_ineligible") != {
        "backup": None,
        "model_calls": 0,
        "qualified": True,
        "slot_consumed": True,
        "trigger": "the exact actual donor packet exceeds the live prompt ceiling",
    }:
        failures.append("d6_capacity_ineligible_qualification")
    if contract["cells"]["D6"].get("capacity_ineligible_calls") != 0:
        failures.append("d6_capacity_ineligible_rule")
    actions = json.loads((ROOT / "ACTION_CONTRACTS.json").read_bytes())
    if not any(row.get("action") == "submit" for row in actions.get("file_world", [])):
        failures.append("submit_action_missing")
    if not all(any(row.get("action") == action for row in actions.get("atlas_world", [])) for action in ("atlas_root", "atlas_expand", "atlas_search", "atlas_read")):
        failures.append("atlas_actions_missing")
    rubric = json.loads((ROOT / "qualification/D2_REQUIREMENT_RUBRIC.json").read_bytes())
    if len(rubric.get("criteria", [])) != 13 or rubric.get("closure_ready_rule") != "all criteria met and no blocking unsupported claim":
        failures.append("d2_requirement_rubric")
    adjudication = json.loads((ROOT / "ADJUDICATION_PROTOCOL.json").read_bytes())
    d2_adjudication = adjudication.get("applies_to", {}).get("D2", {})
    if (
        d2_adjudication.get("runtime_default") != "not_adjudicated"
        or d2_adjudication.get("rubric") != "qualification/D2_REQUIREMENT_RUBRIC.json"
        or "thirteen" not in d2_adjudication.get("closure_rule", "")
    ):
        failures.append("d2_adjudication_protocol")
    d2_gold_adjudication = validate_d2_adjudication(DEFAULT_RECORD)
    if (
        d2_gold_adjudication.get("passed") is not True
        or d2_gold_adjudication.get("derived_closure_readiness") != "ready"
        or set(d2_gold_adjudication.get("criterion_statuses", {}).values()) != {"met"}
    ):
        failures.append("d2_gold_adjudication")
    borrowing = json.loads((ROOT / "BORROWING_LEDGER.json").read_bytes())
    for row in borrowing.get("sources", []):
        if re.fullmatch(r"[0-9a-f]{40}", str(row.get("commit", ""))) is None:
            failures.append(f"borrowing_commit:{row.get('repository')}")

    if (ROOT / "runs").exists() and any((ROOT / "runs").iterdir()):
        failures.append("unexpected_measured_runs")
    receipt = {"schema_version": "capability-terrain-stage0-check-v0", "passed": not failures, "failures": failures, "external_hashes_checked": not args.skip_external_hashes, "source_files_checked": len(source_lock["files"]), "provenance_rows_checked": len(provenance_rows), "fixture_manifest_sha256": qualification["fixture_manifest"]["manifest_sha256"], "gold_manifest_sha256": qualification["gold_manifest"]["manifest_sha256"], "evaluator_manifest_sha256": qualification["evaluator_manifest"]["manifest_sha256"], "adjudication_manifest_sha256": qualification["adjudication_manifest"]["manifest_sha256"], "d2_gold_adjudication_sha256": d2_gold_adjudication.get("record_sha256"), "calls": calls, "serialized_token_ceiling": token_ceiling}
    print(json.dumps(receipt, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
