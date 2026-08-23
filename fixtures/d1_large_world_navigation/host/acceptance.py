from __future__ import annotations

import json
import re
from pathlib import Path


TARGET = "Q3XL_LARGE_WORLD_RUNTIME_MEMO.md"
STARTING_SHA256 = "REPLACED_BY_FREEZE"
HEADINGS = (
    "# Q3 XL large-world runtime evidence memo",
    "## Executive decision",
    "## Supported capabilities",
    "## Observed boundaries and recurring errors",
    "## Runtime implications",
    "## Optional or parked mechanisms",
    "## Limits and counterexamples",
    "## Recommended next authentic test",
    "## Evidence index",
)
LINK_RE = re.compile(r"\[[^\]]+\]\((experiments/[^)]+)\)")


def main() -> int:
    root = Path.cwd()
    files = sorted(path for path in root.rglob("*") if path.is_file())
    errors: list[str] = []
    if [path.relative_to(root).as_posix() for path in files] != [TARGET]:
        errors.append("candidate must contain exactly the target memo")
    target = root / TARGET
    text = target.read_text(encoding="utf-8") if target.is_file() else ""
    import hashlib

    observed_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if observed_sha == STARTING_SHA256:
        errors.append("target is unchanged from the frozen draft")
    positions = [text.find(heading) for heading in HEADINGS]
    if any(position < 0 for position in positions):
        errors.append("one or more required headings are missing")
    elif positions != sorted(positions):
        errors.append("required headings are out of order")
    body = text.split("## Evidence index", 1)[0]
    word_count = len(re.findall(r"\b[\w'-]+\b", body))
    if not 1400 <= word_count <= 2400:
        errors.append(f"memo body word count {word_count} is outside 1400..2400")
    links = LINK_RE.findall(text)
    if len(set(links)) < 12:
        errors.append("fewer than 12 unique experiment evidence links")
    studies = {path.split("/", 2)[1] for path in links if path.count("/") >= 2}
    if len(studies) < 8:
        errors.append("evidence links span fewer than 8 experiment directories")
    result = {
        "passed": not errors,
        "errors": errors,
        "target": TARGET,
        "target_sha256": observed_sha,
        "body_word_count": word_count,
        "unique_evidence_links": len(set(links)),
        "linked_experiment_directories": len(studies),
    }
    print(json.dumps(result, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
