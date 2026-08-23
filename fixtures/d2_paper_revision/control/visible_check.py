from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable

from common import (
    EXPECTED_FILES,
    EXPECTED_REFERENCE_IDS,
    EXPECTED_SECTION_ORDER,
    EXPECTED_SOURCE_SHA256,
    EXPECTED_TITLE,
    candidate_files,
    citation_observation,
    obsolete_markers,
    parse_document,
    protected_material,
    read_candidate,
    source_hashes,
)


def main() -> int:
    candidate = Path(sys.argv[1]).resolve()
    failures: list[dict[str, Any]] = []

    def run_case(name: str, expected: object, observe: Callable[[], object]) -> None:
        try:
            actual = observe()
        except Exception as exc:
            actual = {"exception": f"{type(exc).__name__}: {exc}"}
        if actual != expected:
            failures.append({"case": name, "expected": expected, "actual": actual})

    run_case("candidate_file_set", EXPECTED_FILES, lambda: candidate_files(candidate))

    paper, evidence, memo = read_candidate(candidate)
    title, order, blocks = parse_document(paper)

    run_case(
        "locked_source_identity",
        EXPECTED_SOURCE_SHA256,
        lambda: source_hashes(evidence, memo),
    )
    run_case(
        "document_structure",
        {"sections": EXPECTED_SECTION_ORDER, "title": EXPECTED_TITLE},
        lambda: {"sections": order, "title": title},
    )
    run_case(
        "protected_material",
        {"introduction": True, "methods": True, "references": True},
        lambda: protected_material(blocks),
    )
    run_case("obsolete_literal_markers", [], lambda: obsolete_markers(paper))
    run_case(
        "citation_syntax",
        {
            "body_ids": EXPECTED_REFERENCE_IDS,
            "missing_required": [],
            "reference_ids": EXPECTED_REFERENCE_IDS,
            "undefined": [],
        },
        lambda: citation_observation(paper, blocks),
    )

    print(
        json.dumps(
            {
                "case_count": 6,
                "check_id": "visible",
                "failures": failures,
                "passed": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
