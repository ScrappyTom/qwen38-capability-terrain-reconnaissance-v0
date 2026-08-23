from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery_runtime.actions import action_catalog, parse_action, system_prompt
from discovery_runtime.atlas import SourceAtlas
from discovery_runtime.canonical import canonical_json_bytes, sha256_bytes, sha256_file, write_canonical_json
from discovery_runtime.evaluation import parsed_json_result, run_external, run_final_response_external, run_visible
from discovery_runtime.handoff import build_d6_message
from discovery_runtime.manifest import recursive_manifest
from discovery_runtime.worlds import FileWorld


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = json.loads((ROOT / "TRANCHE_CONTRACT.json").read_bytes())
PROFILE = json.loads((ROOT / "MODEL_PROFILE_LOCK.json").read_bytes())
WORK = ROOT / "qualification" / "work"

TARGETS = {
    "D2": ("paper.md", ROOT / "qualification/gold/d2_paper_revision/paper.md"),
    "D3": ("src/coalesce-coverage.mjs", ROOT / "qualification/gold/d3_coverage_coalescing/src/coalesce-coverage.mjs"),
    "D4": ("src/fold-device-events.mjs", ROOT / "qualification/gold/d4_device_event_folding/src/fold-device-events.mjs"),
    "D5": ("src/deployment-waves.mjs", ROOT / "qualification/gold/d5_deployment_wave_planning/src/deployment-waves.mjs"),
}


def tokenizer_count(data: bytes) -> int:
    with tempfile.NamedTemporaryFile(dir=WORK, delete=False, suffix=".txt") as handle:
        handle.write(data)
        path = Path(handle.name)
    try:
        completed = subprocess.run(
            [PROFILE["tokenizer_path"], "-m", PROFILE["tokenizer_projection_path"], "-f", str(path), "--show-count", "--no-bos"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        match = re.search(r"Total number of tokens:\s*(\d+)", completed.stdout)
        if match is None:
            raise RuntimeError("could not parse llama-tokenize output")
        return int(match.group(1))
    finally:
        path.unlink(missing_ok=True)


def verify_listed_manifest(task_dir: Path, expected_id: str) -> dict[str, Any]:
    manifest = json.loads((task_dir / "starting-world-manifest.json").read_bytes())
    failures = []
    listed = []
    for row in manifest["files"]:
        path = task_dir / "fixture" / row["path"]
        actual = {"path": row["path"], "bytes": path.stat().st_size, "sha256": sha256_file(path)}
        listed.append(actual)
        if actual["bytes"] != row["bytes"] or actual["sha256"] != row["sha256"]:
            failures.append(row["path"])
    actual_paths = sorted(path.relative_to(task_dir / "fixture").as_posix() for path in (task_dir / "fixture").rglob("*") if path.is_file())
    expected_paths = sorted(row["path"] for row in manifest["files"])
    return {"declared_manifest_sha256": manifest["manifest_sha256"], "expected_manifest_sha256": expected_id, "file_failures": failures, "path_set_matches": actual_paths == expected_paths, "passed": manifest["manifest_sha256"] == expected_id and not failures and actual_paths == expected_paths}


def sample_final_response(cell_id: str) -> str:
    return (
        "Root cause: The initial implementation did not implement the complete documented contract and omitted required validation and ordering behavior.\n"
        f"Files changed: The declared implementation target for {cell_id} was replaced; protected task files were not changed.\n"
        "Verification: The visible test suite and frozen external artifact grader both pass for the exact candidate.\n"
        "Remaining limitations: This reference only proves that a legal complete action exists within the experimental envelope."
    )


def grade_final_response(cell_id: str, task_dir: Path) -> dict[str, Any]:
    text = sample_final_response(cell_id)
    with tempfile.NamedTemporaryFile(dir=WORK, delete=False, suffix=".txt") as handle:
        handle.write(text.encode("utf-8"))
        path = Path(handle.name)
    try:
        raw = run_final_response_external(cell_id, repo_root=ROOT, final_response_path=path)
        return {"raw": raw, "parsed": parsed_json_result(raw)}
    finally:
        path.unlink(missing_ok=True)


def qualify_cell(cell_id: str) -> dict[str, Any]:
    cell = CONTRACT["cells"][cell_id]
    fixture = ROOT / cell["fixture"]
    source = fixture / cell["workspace"]
    with tempfile.TemporaryDirectory(dir=WORK, prefix=f"{cell_id.lower()}-") as temporary:
        base = Path(temporary)
        initial = base / "initial"
        gold = base / "gold"
        shutil.copytree(source, initial)
        world = FileWorld(
            source=source,
            runtime_root=gold,
            mutable_paths=set(cell["mutable_paths"]),
        )
        target_relative, gold_source = TARGETS[cell_id]
        target = gold / target_relative
        starting_hash = sha256_file(target)
        action = {
            "action": "replace_file",
            "path": target_relative,
            "content": gold_source.read_text(encoding="utf-8"),
            "expected_file_sha256": starting_hash,
        }
        action_bytes = canonical_json_bytes(action)
        parse_action(action_bytes, atlas=False)
        mutation_result = world.replace_file(
            target_relative,
            action["content"],
            action["expected_file_sha256"],
        )
        initial_id = recursive_manifest(initial)["manifest_sha256"]
        gold_id = world.candidate_id
        initial_visible_raw, initial_visible = run_visible(cell_id, repo_root=ROOT, workspace=initial, candidate_id=initial_id)
        gold_visible_raw, gold_visible = run_visible(cell_id, repo_root=ROOT, workspace=gold, candidate_id=gold_id)
        initial_external_raw = run_external(cell_id, repo_root=ROOT, workspace=initial)
        gold_external_raw = run_external(cell_id, repo_root=ROOT, workspace=gold)
        final_grade = grade_final_response(cell_id, fixture) if cell_id in {"D3", "D4", "D5"} else None
        return {
            "cell_id": cell_id,
            "initial_candidate_id": initial_id,
            "gold_candidate_id": gold_id,
            "target": target_relative,
            "starting_target_sha256": starting_hash,
            "gold_target_sha256": sha256_file(gold_source),
            "gold_target_bytes": gold_source.stat().st_size,
            "known_good_action_bytes": len(action_bytes),
            "known_good_action_tokens": tokenizer_count(action_bytes),
            "known_good_executor_path": {
                "accepted": mutation_result["accepted"],
                "candidate_before": mutation_result["candidate_before"],
                "candidate_after": mutation_result["candidate_after"],
                "candidate_after_matches_gold": mutation_result["candidate_after"] == gold_id,
                "visible_check_bound_to_gold": gold_visible["evaluated_candidate_id"] == gold_id and gold_visible["currency"] == "current",
            },
            "completion_allowance_tokens": PROFILE["completion_allowance_tokens"],
            "initial_visible": initial_visible,
            "gold_visible": gold_visible,
            "initial_external": {"exit_code": initial_external_raw["exit_code"], "parsed": parsed_json_result(initial_external_raw)},
            "gold_external": {"exit_code": gold_external_raw["exit_code"], "parsed": parsed_json_result(gold_external_raw)},
            "final_answer": final_grade,
            "minimum_calls": cell["minimum_calls"],
            "malformed_action_slack": cell["malformed_action_slack"],
            "call_ceiling": cell["call_ceiling"],
        }


def qualify_d1() -> dict[str, Any]:
    fixture = ROOT / CONTRACT["cells"]["D1"]["fixture"]
    atlas = SourceAtlas(fixture / "host/FROZEN_ATLAS.json", fixture / "source_documents")
    read_failures = []
    total = 0
    for document in atlas.documents.values():
        try:
            data = atlas._document_bytes(document)
            total += len(data)
        except Exception as exc:
            read_failures.append(f"{document['path']}: {exc}")
    workspace = fixture / "workspace"
    candidate_id = recursive_manifest(workspace)["manifest_sha256"]
    visible_raw, visible = run_visible("D1", repo_root=ROOT, workspace=workspace, candidate_id=candidate_id)
    return {
        "document_count": len(atlas.documents),
        "section_count": len(atlas.sections),
        "total_exact_bytes": total,
        "atlas_sha256": atlas.atlas_sha256,
        "source_commit": atlas.source_commit,
        "read_failures": read_failures,
        "initial_visible": visible,
        "selection_call_ceiling": CONTRACT["cells"]["D1"]["call_ceiling"],
        "claim_limit": CONTRACT["cells"]["D1"]["claim_limit"],
    }


def qualify_d6(cell_rows: list[dict[str, Any]]) -> dict[str, Any]:
    branches = []
    for row in cell_rows:
        cell_id = row["cell_id"]
        cell = CONTRACT["cells"][cell_id]
        fixture = ROOT / cell["fixture"]
        source = fixture / cell["workspace"]
        with tempfile.TemporaryDirectory(dir=WORK, prefix=f"d6-{cell_id.lower()}-") as temporary:
            workspace = Path(temporary) / "workspace"
            shutil.copytree(source, workspace)
            target_relative, gold_source = TARGETS[cell_id]
            (workspace / target_relative).write_bytes(gold_source.read_bytes())
            candidate_id = recursive_manifest(workspace)["manifest_sha256"]
            task_text = (fixture / cell["task"]).read_text(encoding="utf-8")
            current_check = {"check_id": cell["visible_check"], "evaluated_candidate_id": candidate_id, "current_candidate_id": candidate_id, "currency": "current", "passed": True, "tests": []}
            receipts = [
                {
                    "result_id": f"RESULT-{index:03d}",
                    "exact_body_sha256": f"{index:064x}",
                    "exact_body_bytes": 32_768,
                    "mechanical_identity": {
                        "tool": "read",
                        "path": target_relative,
                    },
                    "exact_reopen": {
                        "action": "reopen_exact",
                        "result_id": f"RESULT-{index:03d}",
                    },
                }
                for index in range(1, cell["call_ceiling"] + 1)
            ]
            message = build_d6_message(donor_cell=cell_id, task_text=task_text, workspace=workspace, mutable_paths=set(cell["mutable_paths"]), visible_check_id=cell["visible_check"], candidate_id=candidate_id, latest_check=current_check, observation_receipts=receipts)
            messages = [
                {"role": "system", "content": system_prompt(atlas=False, max_calls=5)},
                {"role": "user", "content": message},
            ]
            # Offline count uses the exact frozen manual non-thinking template.
            rendered = "".join(f"<|im_start|>{item['role']}\n{item['content'].strip()}<|im_end|>\n" for item in messages) + "<|im_start|>assistant\n<think>\n\n</think>\n\n"
            branches.append({"donor_cell": cell_id, "candidate_id": candidate_id, "packet_bytes": len(message.encode("utf-8")), "offline_prompt_tokens": tokenizer_count(rendered.encode("utf-8")), "call_ceiling": 5, "exact_mutable_candidate_resident": True, "unread_workspace_files_resident": False, "inherited_receipt_count": len(receipts), "current_check_variant": "current"})
            stale = build_d6_message(donor_cell=cell_id, task_text=task_text, workspace=workspace, mutable_paths=set(cell["mutable_paths"]), visible_check_id=cell["visible_check"], candidate_id=candidate_id, latest_check={**current_check, "evaluated_candidate_id": "f" * 64}, observation_receipts=receipts)
            branches[-1]["stale_check_packet_bytes"] = len(stale.encode("utf-8"))

            maximum_workspace = Path(temporary) / "maximum-workspace"
            shutil.copytree(source, maximum_workspace)
            (maximum_workspace / target_relative).write_bytes(b'\\"' * 16_384)
            maximum_candidate_id = recursive_manifest(maximum_workspace)["manifest_sha256"]
            _, maximum_current_check = run_visible(
                cell_id,
                repo_root=ROOT,
                workspace=maximum_workspace,
                candidate_id=maximum_candidate_id,
            )
            maximum_message = build_d6_message(
                donor_cell=cell_id,
                task_text=task_text,
                workspace=maximum_workspace,
                mutable_paths=set(cell["mutable_paths"]),
                visible_check_id=cell["visible_check"],
                candidate_id=maximum_candidate_id,
                latest_check=maximum_current_check,
                observation_receipts=receipts,
            )
            maximum_messages = [
                {"role": "system", "content": system_prompt(atlas=False, max_calls=5)},
                {"role": "user", "content": maximum_message},
            ]
            maximum_rendered = "".join(f"<|im_start|>{item['role']}\n{item['content'].strip()}<|im_end|>\n" for item in maximum_messages) + "<|im_start|>assistant\n<think>\n\n</think>\n\n"
            stress_tokens = tokenizer_count(maximum_rendered.encode("utf-8"))
            branches[-1]["stress_admitted_target_bytes"] = 32_768
            branches[-1]["stress_current_check_prompt_tokens"] = stress_tokens
            branches[-1]["stress_packet_fits"] = stress_tokens <= PROFILE["prompt_ceiling_tokens"]
            branches[-1]["actual_packet_live_capacity_gate"] = True
    return {
        "selection_order": ["D2", "D3", "D4", "D5"],
        "branches": branches,
        "null": {"qualified": True, "model_calls": 0, "slot_consumed": True, "backup": None},
        "capacity_ineligible": {
            "qualified": True,
            "model_calls": 0,
            "slot_consumed": True,
            "backup": None,
            "trigger": "the exact actual donor packet exceeds the live prompt ceiling",
        },
        "claim_limit": CONTRACT["cells"]["D6"]["claim_limit"],
    }


def executable_lock() -> dict[str, Any]:
    commands = {}
    for name, command in {"python": [sys.executable, "--version"], "node": [shutil.which("node") or "node", "--version"], "npm": [shutil.which("npm") or "npm", "--version"]}.items():
        completed = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8")
        executable = shutil.which(command[0]) or command[0]
        path = Path(executable).resolve()
        commands[name] = {"path": str(path), "sha256": sha256_file(path), "version": completed.stdout.strip()}
    return commands


def main() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    expected_manifests = {
        "D3": "ca9706114cd088369fb1039fc7d673a531b58581cb560f51b84749f3172cc1ee",
        "D4": "4fca1e601ae73330a9cd92f07e958702fe8adf59e625360cc07289561ee7fac2",
        "D5": "1ac302c38aa00ed18a441460a7590739319fb0b258319b868b6383eae1d6df7c",
    }
    listed = {
        cell_id: verify_listed_manifest(ROOT / CONTRACT["cells"][cell_id]["fixture"], expected)
        for cell_id, expected in expected_manifests.items()
    }
    cells = [qualify_cell(cell_id) for cell_id in ("D2", "D3", "D4", "D5")]
    d1 = qualify_d1()
    d6 = qualify_d6(cells)
    gold_manifest = recursive_manifest(ROOT / "qualification" / "gold")
    write_canonical_json(ROOT / "GOLD_MANIFEST.json", gold_manifest)
    evaluator_manifest = recursive_manifest(ROOT / "qualification" / "evaluators")
    write_canonical_json(ROOT / "EVALUATOR_MANIFEST.json", evaluator_manifest)
    adjudication_manifest = recursive_manifest(ROOT / "qualification" / "adjudications")
    write_canonical_json(ROOT / "ADJUDICATION_MANIFEST.json", adjudication_manifest)
    action_contracts = {
        "schema_version": "capability-terrain-action-contracts-v0",
        "response_transport": "one bare JSON object with llama.cpp json_object generation assistance; authoritative host parser; no repair or retry",
        "file_world": action_catalog(atlas=False),
        "atlas_world": action_catalog(atlas=True),
        "system_prompts": {
            str(calls): {
                "sha256": sha256_bytes(system_prompt(atlas=False, max_calls=calls).encode("utf-8")),
                "bytes": len(system_prompt(atlas=False, max_calls=calls).encode("utf-8")),
            }
            for calls in (5, 8, 9)
        },
        "atlas_system_prompt": {
            "calls": 4,
            "sha256": sha256_bytes(system_prompt(atlas=True, max_calls=4).encode("utf-8")),
            "bytes": len(system_prompt(atlas=True, max_calls=4).encode("utf-8")),
        },
        "submit_final_response": {
            "D2": "non-empty bounded final_response",
            "D3_D4_D5": "four exact ordered labels retained from the task; independently graded",
            "D6": "inherits donor closure contract",
        },
    }
    write_canonical_json(ROOT / "ACTION_CONTRACTS.json", action_contracts)
    evaluator_lock = executable_lock()
    write_canonical_json(ROOT / "EVALUATOR_RUNTIME_LOCK.json", evaluator_lock)

    failures = []
    for cell in cells:
        if cell["initial_external"]["exit_code"] == 0:
            failures.append(f"{cell['cell_id']}: initial candidate unexpectedly passes external evaluator")
        if cell["gold_external"]["exit_code"] != 0 or not cell["gold_visible"]["passed"]:
            failures.append(f"{cell['cell_id']}: known-good candidate does not pass")
        if cell["known_good_action_tokens"] > PROFILE["completion_allowance_tokens"]:
            failures.append(f"{cell['cell_id']}: known-good action exceeds completion allowance")
        if cell["minimum_calls"] + cell["malformed_action_slack"] > cell["call_ceiling"]:
            failures.append(f"{cell['cell_id']}: minimum path plus slack exceeds call ceiling")
        if cell["final_answer"] is not None and not cell["final_answer"]["parsed"].get("passed"):
            failures.append(f"{cell['cell_id']}: final response contract not expressible")
    for cell_id, row in listed.items():
        if not row["passed"]:
            failures.append(f"{cell_id}: starting manifest mismatch")
    if d1["document_count"] != 103 or d1["section_count"] != 971 or d1["total_exact_bytes"] != 766_502 or d1["read_failures"]:
        failures.append("D1: atlas custody mismatch")
    for branch in d6["branches"]:
        if branch["offline_prompt_tokens"] > PROFILE["prompt_ceiling_tokens"]:
            failures.append(f"D6 {branch['donor_cell']}: initial packet exceeds prompt ceiling")

    qualification = {
        "schema_version": "capability-terrain-stage0-qualification-v0",
        "passed": not failures,
        "failures": failures,
        "no_model_calls": True,
        "source_lock_sha256": sha256_file(ROOT / "SOURCE_LOCK.json"),
        "fixture_manifest": json.loads((ROOT / "FIXTURE_MANIFEST.json").read_bytes()),
        "gold_manifest": gold_manifest,
        "evaluator_manifest": evaluator_manifest,
        "adjudication_manifest": adjudication_manifest,
        "starting_manifest_checks": listed,
        "D1": d1,
        "full_task_cells": cells,
        "D6": d6,
        "tranche_call_ceiling": CONTRACT["max_total_actor_calls"],
        "tranche_serialized_token_ceiling": CONTRACT["max_total_serialized_tokens"],
        "offline_token_count_caveat": "llama-tokenize over the frozen manual non-thinking template is a conservative Stage-0 feasibility check; live /apply-template plus /tokenize governs measured admission",
    }
    write_canonical_json(ROOT / "STAGE0_QUALIFICATION.json", qualification)
    if failures:
        raise SystemExit("\n".join(failures))


if __name__ == "__main__":
    main()
