from __future__ import annotations

import json
import re
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
    contains_complete_case,
    contains_matched_cohort,
    contains_not_preregistered,
    normalized,
    obsolete_markers,
    paragraph_containing,
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
    abstract = blocks.get("Abstract", "")
    results = blocks.get("Results", "")
    discussion = blocks.get("Discussion", "")

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

    def abstract_design() -> object:
        value = normalized(abstract)
        return {
            "association_language": "associated" in value,
            "matched_cohort": contains_matched_cohort(abstract),
            "nonrandomized": "nonrandomized" in value or "non-randomized" in value,
            "unsupported_causal_language": any(
                marker in value for marker in (" caused ", " demonstrate ", " establishes ")
            ),
        }

    run_case(
        "abstract_design",
        {
            "association_language": True,
            "matched_cohort": True,
            "nonrandomized": True,
            "unsupported_causal_language": False,
        },
        abstract_design,
    )

    def abstract_primary() -> object:
        value = normalized(abstract)
        return {
            "adjusted_difference": "18.4" in value,
            "adaptive_rate": "71.2%" in value,
            "citation_d2": "[d2]" in value,
            "confidence_interval": "6.1" in value and "30.7" in value,
            "usual_rate": "52.8%" in value,
        }

    run_case(
        "abstract_primary_result",
        {
            "adjusted_difference": True,
            "adaptive_rate": True,
            "citation_d2": True,
            "confidence_interval": True,
            "usual_rate": True,
        },
        abstract_primary,
    )

    def abstract_limitations() -> object:
        value = normalized(abstract)
        return {
            "causal_limit": "causal" in value and ("limit" in value or "cannot" in value),
            "citation_d1": "[d1]" in value,
            "citation_d3": "[d3]" in value,
            "dropout": "dropout" in value,
            "nonrandomized": "nonrandomized" in value or "non-randomized" in value,
        }

    run_case(
        "abstract_limitations",
        {
            "causal_limit": True,
            "citation_d1": True,
            "citation_d3": True,
            "dropout": True,
            "nonrandomized": True,
        },
        abstract_limitations,
    )

    def results_primary() -> object:
        paragraph = paragraph_containing(results, "18.4")
        value = normalized(paragraph)
        return {
            "adaptive_rate": "71.2%" in value,
            "adjusted_difference": "18.4" in value,
            "citation_d2": "[d2]" in value,
            "confidence_interval": "6.1" in value and "30.7" in value,
            "p_value": bool(re.search(r"p\s*=\s*0\.006", value)),
            "usual_rate": "52.8%" in value,
        }

    run_case(
        "results_primary_result",
        {
            "adaptive_rate": True,
            "adjusted_difference": True,
            "citation_d2": True,
            "confidence_interval": True,
            "p_value": True,
            "usual_rate": True,
        },
        results_primary,
    )

    def results_missingness() -> object:
        paragraph = paragraph_containing(results, "8.7%")
        value = normalized(paragraph)
        return {
            "adaptive_dropout": "8.7%" in value,
            "bias_upward": bool(re.search(r"bias.*upward", value)),
            "citation_d3": "[d3]" in value,
            "complete_case": contains_complete_case(paragraph),
            "no_imputation": "no imputation" in value or "without imputation" in value,
            "usual_dropout": "3.1%" in value,
        }

    run_case(
        "results_missingness",
        {
            "adaptive_dropout": True,
            "bias_upward": True,
            "citation_d3": True,
            "complete_case": True,
            "no_imputation": True,
            "usual_dropout": True,
        },
        results_missingness,
    )

    def results_subgroup() -> object:
        paragraph = paragraph_containing(results, "subgroup")
        value = normalized(paragraph)
        return {
            "citation_d3": "[d3]" in value,
            "exploratory": "exploratory" in value,
            "heterogeneity_not_established": (
                "heterogeneity" in value
                and ("do not establish" in value or "does not establish" in value)
            ),
            "not_preregistered": contains_not_preregistered(paragraph),
        }

    run_case(
        "results_subgroup_status",
        {
            "citation_d3": True,
            "exploratory": True,
            "heterogeneity_not_established": True,
            "not_preregistered": True,
        },
        results_subgroup,
    )

    def discussion_strength() -> object:
        value = normalized(discussion)
        return {
            "association_language": "associated" in value,
            "citation_d1": "[d1]" in value,
            "citation_d2": "[d2]" in value,
            "matched_cohort": contains_matched_cohort(discussion),
            "nonrandomized": "nonrandomized" in value or "non-randomized" in value,
            "unsupported_language": any(
                marker in value
                for marker in (
                    "adaptive alerts caused",
                    "establishes that",
                    "support immediate deployment",
                    "supports immediate deployment",
                )
            ),
        }

    run_case(
        "discussion_claim_strength",
        {
            "association_language": True,
            "citation_d1": True,
            "citation_d2": True,
            "matched_cohort": True,
            "nonrandomized": True,
            "unsupported_language": False,
        },
        discussion_strength,
    )

    def discussion_missingness() -> object:
        paragraph = paragraph_containing(discussion, "dropout")
        value = normalized(paragraph)
        return {
            "bias_upward": bool(re.search(r"bias.*upward", value)),
            "citation_d3": "[d3]" in value,
            "complete_case": contains_complete_case(paragraph),
            "no_imputation": "no imputation" in value or "without imputation" in value,
        }

    run_case(
        "discussion_missingness",
        {
            "bias_upward": True,
            "citation_d3": True,
            "complete_case": True,
            "no_imputation": True,
        },
        discussion_missingness,
    )

    def discussion_subgroup() -> object:
        paragraph = paragraph_containing(discussion, "subgroup")
        value = normalized(paragraph)
        return {
            "citation_d3": "[d3]" in value,
            "exploratory": "exploratory" in value,
            "heterogeneity": "heterogeneity" in value,
            "nonconfirmatory": (
                "nonconfirmatory" in value
                or bool(re.search(r"not\b.*\bconfirmatory", value))
            ),
            "not_preregistered": contains_not_preregistered(paragraph),
        }

    run_case(
        "discussion_subgroup_status",
        {
            "citation_d3": True,
            "exploratory": True,
            "heterogeneity": True,
            "nonconfirmatory": True,
            "not_preregistered": True,
        },
        discussion_subgroup,
    )

    def citation_binding() -> object:
        observation = citation_observation(paper, blocks)
        return {
            **observation,
            "abstract_design_d1": "[D1]" in abstract,
            "abstract_primary_d2": "[D2]" in abstract,
            "abstract_quality_d3": "[D3]" in abstract,
            "discussion_design_d1": "[D1]" in discussion,
            "discussion_primary_d2": "[D2]" in discussion,
            "discussion_quality_d3": "[D3]" in discussion,
            "results_primary_d2": "[D2]" in paragraph_containing(results, "18.4"),
            "results_quality_d3": "[D3]" in paragraph_containing(results, "8.7%"),
            "results_subgroup_d3": "[D3]" in paragraph_containing(results, "subgroup"),
        }

    run_case(
        "citation_binding",
        {
            "abstract_design_d1": True,
            "abstract_primary_d2": True,
            "abstract_quality_d3": True,
            "body_ids": EXPECTED_REFERENCE_IDS,
            "discussion_design_d1": True,
            "discussion_primary_d2": True,
            "discussion_quality_d3": True,
            "missing_required": [],
            "reference_ids": EXPECTED_REFERENCE_IDS,
            "results_primary_d2": True,
            "results_quality_d3": True,
            "results_subgroup_d3": True,
            "undefined": [],
        },
        citation_binding,
    )

    def unsupported_claims() -> object:
        editable = normalized("\n".join((abstract, results, discussion)))
        patterns = {
            "affirmative_causation": r"\b(caused|causes|proves|demonstrates|establishes)\b",
            "deployment_recommendation": (
                r"\b(supports?|recommends?)\b.{0,30}\bdeployment\b"
                r"|\bshould be deployed\b"
            ),
            "dismissed_missingness": r"\b(negligible|cannot explain|too rare)\b",
            "directional_subgroup": r"\b(largest|most effective|modifies the alert effect)\b",
        }
        return [name for name, pattern in patterns.items() if re.search(pattern, editable)]

    run_case("unsupported_claims_absent", [], unsupported_claims)
    run_case("obsolete_literal_markers", [], lambda: obsolete_markers(paper))

    print(
        json.dumps(
            {
                "case_count": 16,
                "failures": failures,
                "grader": "paper-revision-hidden-v1",
                "passed": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
