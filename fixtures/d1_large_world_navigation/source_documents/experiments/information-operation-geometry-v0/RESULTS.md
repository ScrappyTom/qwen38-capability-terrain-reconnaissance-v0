# Information-operation geometry v0 — results

Date: 2026-08-13

Status: **complete; no state-conditioned projection profile; fixture family stopped**

## Outcome

The experiment executed cleanly but did not instantiate the substantive
information-operation problem it was designed to discriminate.

- 36/36 requests completed and were admitted.
- 36/36 responses ended with `finish_reason: stop`.
- There were zero retries, response-capacity failures, schema failures,
  transport failures, or host repairs.
- Exact replay verified all 36 requests, responses, results, artifacts,
  projections, identities, and usage totals.
- The complete run used 50,905 tokens and 519.771 seconds of summed model HTTP
  duration.

Under direct task-grounded audit, every condition preserved all 18 substantive
items for transfer, all 18 for comparison, and all 18 for construction. All 72
comparison verdicts were correct. Two transfer outputs omitted required source
handles, and one construction output added a stray closing brace.

The frozen lexical grader produced large apparent semantic-arm deficits, but
direct review showed those were treatment-correlated paraphrase and
segmentation errors. The frozen numbers remain saved; they are not valid as a
semantic comparison of the four views.

The preregistered full interaction screen is non-discriminating. Source-led
comparison and construction were at ceiling, leaving only transfer formally
eligible; transfer's variation was handle binding rather than substantive
fact preservation. No projection profile is promoted.

## What was tested

Three fresh six-record worlds—parcel quarantine, scholarship allocation, and
cold-chain dispatch—were each used for:

- exact transfer;
- source-target comparison; and
- construction of a corrected artifact.

Every cell received the same six exact sources and six exact targets. Four
views varied only the projection ecology:

1. exact source objects followed by targets;
2. one integrated canonical relation account plus exact objects;
3. each canonical relation adjacent to its exact source and target; or
4. the same relations independently scoped as output obligations plus exact
   objects.

Conditions 2–4 carried the same canonical semantic clause strings exactly
once. All conditions used one fresh nonthinking Qwen call, temperature 0, a
1,280-token allowance, the same strict JSON-schema submission, no tools, no
feedback, and no retries.

The apparatus and decision rules were committed and pushed at `30261500`
before the first measured call.

## Frozen machine scores

These values are retained as the preregistered instrument output:

| Operation | Condition | Full passes | Passed items | Satisfied atoms | Tokens |
|---|---|---:|---:|---:|---:|
| Transfer | source-led | 2/3 | 12/18 | 66/91 | 3,370 |
| Transfer | integrated | 2/3 | 12/18 | 66/91 | 3,987 |
| Transfer | aligned | 3/3 | 18/18 | 91/91 | 4,510 |
| Transfer | obligations | 3/3 | 18/18 | 91/91 | 4,563 |
| Compare | source-led | 3/3 | 18/18 | 97/97 | 3,741 |
| Compare | integrated | 0/3 | 6/18 | 78/97 | 4,330 |
| Compare | aligned | 0/3 | 7/18 | 80/97 | 4,880 |
| Compare | obligations | 0/3 | 6/18 | 76/97 | 4,891 |
| Construct | source-led | 3/3 | 18/18 | 91/91 | 3,429 |
| Construct | integrated | 2/3 | 17/18 | 90/91 | 4,065 |
| Construct | aligned | 2/3 | 17/18 | 90/91 | 4,545 |
| Construct | obligations | 2/3 | 16/18 | 89/91 | 4,594 |

The direct audit in [`AUDIT.md`](AUDIT.md) explains why the compare and most
construction deficits are false negatives. The scorer's accepted phrases were
closer to source wording, while semantic views induced faithful relation-text
paraphrases. Missing handles also prevented segmentation and caused complete
content to receive zero item atoms.

## Audited result

### Semantic content

| Operation | Source-led | Integrated | Aligned | Obligations |
|---|---:|---:|---:|---:|
| Transfer | 18/18 | 18/18 | 18/18 | 18/18 |
| Compare | 18/18 | 18/18 | 18/18 | 18/18 |
| Construct | 18/18 | 18/18 | 18/18 | 18/18 |

### Complete artifact contract

| Operation | Source-led | Integrated | Aligned | Obligations |
|---|---:|---:|---:|---:|
| Transfer | 2/3 | 2/3 | 3/3 | 3/3 |
| Compare | 3/3 | 3/3 | 3/3 | 3/3 |
| Construct | 3/3 | 3/3 | 3/3 | 2/3 |

The complete-artifact exceptions were C014 and C015, which omitted all six
source handles despite preserving every source rule, and C023, which appended
a literal `}` after an otherwise complete artifact.

## Cost

| Condition | Prompt | Completion | Total | Summed duration |
|---|---:|---:|---:|---:|
| source-led | 8,166 | 2,374 | 10,540 | 125.431 s |
| integrated | 10,017 | 2,365 | 12,382 | 127.936 s |
| aligned | 11,479 | 2,456 | 13,935 | 134.335 s |
| obligations | 11,656 | 2,392 | 14,048 | 132.069 s |

Relative to source-led, integrated used 17.48% more total tokens, aligned
32.21% more, and obligations 33.28% more. Completion volume was nearly flat;
the cost was overwhelmingly added prompt context. These are descriptive totals
from one deterministic call per cell, not production latency estimates.

## Direct behavioral findings

The views frequently produced byte-identical artifacts despite visibly
different projection structures. All four conditions were identical on W-A
transfer and construction and W-C transfer. Three semantic conditions were
identical on W-A comparison; three conditions were identical on W-C
construction. The model often simply used the exact source strings.

The one condition-sensitive result was formal addressability. On W-B
transfer, source-led and integrated outputs were byte-identical and omitted all
handles. Aligned and obligation views retained every handle. Because all four
preserved every substantive rule, this is a provenance/output-binding lead,
not evidence that semantic truth survived only in the richer views.

The obligation condition also produced C023's stray brace. More explicit
objects are therefore not monotonically cleaner even in this bounded setup.

## Why the substantive screen failed

The experiment changed the requested operation, but not the dependency graph
enough. Its “multi-constraint construction” still assigned one source record
to one output sentence six times. Comparison also decomposed into six explicit
one-pair judgments. These tasks did not require several distant observations
to be integrated into one claim, decision, or mutation—the failure shape that
motivated Track A.

Consequently, exact source-led input was already sufficient for perfect
substantive comparison and construction. The result cannot support either a
universal view or a state-conditioned view selector; it says that on small,
explicit, one-to-one units, added semantic framing was unnecessary and costly.

## Decision

1. Stop this fixture family without tuning or rerunning it.
2. Promote no semantic view, card, obligation set, operation classifier, or
   context compiler.
3. Retain exact source-led input as the cheapest adequate view for these easy
   comparison/construction cells—not as a general default.
4. Retain one narrow addressability lead from W-B transfer; do not replicate it
   as the project's main question.
5. The next Track A design, if pursued, must vary actual information
   dependencies: one-to-one transfer, pairwise discrimination, and genuinely
   many-to-one synthesis. The source-led synthesis baseline must be qualified
   away from ceiling before measured conditions run.

That is the big-picture correction: an operation label is not enough. The
projection may matter when it changes how several facts must be jointly used,
but this family mostly let Qwen copy or judge each record independently.

## Evidence and validation

The immutable evidence is in
[`runs/information-operation-geometry-v0-run-001`](runs/information-operation-geometry-v0-run-001).
It contains the copied fixture/profile, endpoint snapshot, projection catalog,
schedule, all 36 requests and raw responses, HTTP receipts, exact artifacts,
results, manifests, usage, frozen lexical grades, and verification receipt.

- exact replay: 36/36 verified;
- experiment-specific tests: 8/8 passed before measurement;
- complete local suite before measurement: 542 tests run, 528 passed and 14
  archived-continuation tests intentionally skipped;
- complete local suite after adding saved-run replay coverage: 543 tests run,
  529 passed and 14 archived-continuation tests intentionally skipped;
- `git diff --check`: passed before measurement.

This is local validation, not GitHub Actions verification.
