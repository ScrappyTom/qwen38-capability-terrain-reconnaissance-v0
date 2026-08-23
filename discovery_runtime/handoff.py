from __future__ import annotations

from pathlib import Path
from typing import Any

from .canonical import sha256_file


def exact_candidate_packet(workspace: Path, mutable_paths: set[str]) -> list[dict[str, Any]]:
    files = []
    for relative in sorted(mutable_paths):
        path = workspace / Path(relative)
        if not path.is_file():
            raise RuntimeError(f"D6 current candidate file is missing: {relative}")
        data = path.read_bytes()
        try:
            content = data.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            content = None
        files.append(
            {
                "path": relative,
                "bytes": len(data),
                "sha256": sha256_file(path),
                "content_utf8": content,
            }
        )
    return files


def build_d6_message(
    *,
    donor_cell: str,
    task_text: str,
    workspace: Path,
    mutable_paths: set[str],
    visible_check_id: str,
    candidate_id: str,
    latest_check: dict[str, Any] | None,
    observation_receipts: list[dict[str, Any]],
) -> str:
    check_is_current = (
        latest_check is not None
        and latest_check.get("evaluated_candidate_id") == candidate_id
    )
    current_check: dict[str, Any]
    if check_is_current:
        current_check = {**latest_check, "currency": "current"}
    else:
        current_check = {
            "status": "not_run_for_current_candidate",
            "current_candidate_id": candidate_id,
            "latest_stale_check_handle": (
                {
                    "evaluated_candidate_id": latest_check.get("evaluated_candidate_id"),
                    "check_id": latest_check.get("check_id"),
                    "currency": "stale",
                }
                if latest_check is not None
                else None
            ),
        }
    surface = {
        "schema_version": "d6-exact-current-state-packet-v0",
        "donor_cell": donor_cell,
        "candidate_id": candidate_id,
        "work_surface": {
            "mutable_paths": sorted(mutable_paths),
            "visible_check_id": visible_check_id,
            "task_native_world_and_actions_remain_available": True,
        },
        "exact_current_candidate": exact_candidate_packet(workspace, mutable_paths),
        "current_check": current_check,
        "prior_observation_handles": observation_receipts,
        "external_history": "exactly_custodied_but_not_resident",
        "excluded": [
            "construction chronology",
            "prior final response",
            "old observation bodies",
            "external grader and readiness",
            "gold repair",
        ],
    }
    import json

    return (
        "AUTHORITATIVE TASK\n"
        + task_text
        + "\n\nFRESH EXACT CURRENT-STATE HANDOFF\n"
        + json.dumps(surface, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    )


def select_d6_donor(results: list[dict[str, Any]]) -> str | None:
    by_id = {row["cell_id"]: row for row in results}
    for cell_id in ("D2", "D3", "D4", "D5"):
        row = by_id[cell_id]
        if row["initial_candidate_id"] != row["final_candidate_id"]:
            return cell_id
    return None
