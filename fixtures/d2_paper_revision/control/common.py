from __future__ import annotations

import hashlib
import re
from pathlib import Path


EXPECTED_FILES = ["editorial_memo.md", "evidence_update.md", "paper.md"]
EXPECTED_TITLE = "# Adaptive Alerts and Overnight Retention: A Multisite Evaluation"
EXPECTED_SECTION_ORDER = [
    "Abstract",
    "Introduction",
    "Methods",
    "Results",
    "Discussion",
    "References",
]
EXPECTED_SOURCE_SHA256 = {
    "editorial_memo.md": "11eb5a7991372eaff8f72e3dc6a06606413350a992f639923d46b8031665885e",
    "evidence_update.md": "b329c4288fb9da0d51d52ba0480ea23494673d85147bdea7ad03f947d7b0f6d5",
}
EXPECTED_INTRODUCTION = """## Introduction

Loss of overnight sensor observations can delay recognition of clinical deterioration. Adaptive alerts may improve record retention by identifying interrupted streams before the observation window closes [D1].

We evaluated whether adaptive alerts were associated with retention of usable overnight sensor records across six inpatient wards.

"""
EXPECTED_METHODS = """## Methods

We conducted a prospective matched-cohort evaluation across six wards. Wards introduced adaptive alerts according to local operational schedules; patients were not randomly assigned. Each intervention observation was matched to a usual-monitoring observation by ward and baseline risk.

The primary endpoint was retention of a usable overnight sensor record through 06:00. The analysis used complete cases and did not impute missing sensor records. Ward-level subgroup comparisons were exploratory.

"""
EXPECTED_REFERENCES = """## References

[D1] Operations Consortium. Multisite rollout design record. 2026.

[D2] Analysis Group. Revised overnight-retention model. 2026.

[D3] Data Quality Team. Sensor-completeness audit. 2026.
"""
EXPECTED_REFERENCE_IDS = ["D1", "D2", "D3"]
OUTDATED_MARKERS = [
    "randomized trial",
    "caused a 12.0",
    "64.8%",
    "12.0 percentage",
    "3.2 to 20.8",
    "p = 0.01",
    "this preregistered subgroup",
    "negligible (<2%",
    "establishes that adaptive alerts caused",
    "supports immediate deployment",
    "confirmatory evidence that the intervention is most effective",
    "too rare to affect interpretation",
]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def candidate_files(candidate: Path) -> list[str]:
    return sorted(
        path.relative_to(candidate).as_posix()
        for path in candidate.rglob("*")
        if path.is_file()
    )


def read_candidate(candidate: Path) -> tuple[str, str, str]:
    return (
        (candidate / "paper.md").read_text(encoding="utf-8"),
        (candidate / "evidence_update.md").read_text(encoding="utf-8"),
        (candidate / "editorial_memo.md").read_text(encoding="utf-8"),
    )


def parse_document(text: str) -> tuple[str, list[str], dict[str, str]]:
    title = text.splitlines()[0] if text else ""
    matches = list(re.finditer(r"(?m)^## ([^\n]+)\n", text))
    order = [match.group(1) for match in matches]
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[match.group(1)] = text[match.start() : end]
    return title, order, blocks


def protected_material(blocks: dict[str, str]) -> dict[str, bool]:
    return {
        "introduction": blocks.get("Introduction") == EXPECTED_INTRODUCTION,
        "methods": blocks.get("Methods") == EXPECTED_METHODS,
        "references": blocks.get("References") == EXPECTED_REFERENCES,
    }


def source_hashes(evidence: str, memo: str) -> dict[str, str]:
    return {
        "editorial_memo.md": sha256_text(memo),
        "evidence_update.md": sha256_text(evidence),
    }


def citation_observation(paper: str, blocks: dict[str, str]) -> dict[str, object]:
    body = paper.split("## References\n", 1)[0]
    body_ids = sorted(set(re.findall(r"\[([A-Z]\d+)\]", body)))
    reference_ids = sorted(
        set(re.findall(r"(?m)^\[([A-Z]\d+)\]", blocks.get("References", "")))
    )
    return {
        "body_ids": body_ids,
        "missing_required": sorted(set(EXPECTED_REFERENCE_IDS) - set(body_ids)),
        "reference_ids": reference_ids,
        "undefined": sorted(set(body_ids) - set(reference_ids)),
    }


def obsolete_markers(paper: str) -> list[str]:
    lowered = paper.lower()
    return [marker for marker in OUTDATED_MARKERS if marker in lowered]


def normalized(text: str) -> str:
    return " ".join(text.lower().split())


def paragraph_containing(block: str, needle: str) -> str:
    for paragraph in block.split("\n\n")[1:]:
        if needle.lower() in paragraph.lower():
            return paragraph
    return ""


def contains_matched_cohort(text: str) -> bool:
    value = normalized(text)
    return "matched-cohort" in value or "matched cohort" in value


def contains_complete_case(text: str) -> bool:
    value = normalized(text)
    return "complete-case" in value or "complete case" in value


def contains_not_preregistered(text: str) -> bool:
    value = normalized(text)
    return "not preregistered" in value or "non-preregistered" in value
