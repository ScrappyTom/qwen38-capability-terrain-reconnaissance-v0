# Construction-boundary prospective comparison v0 — results

Date: 2026-08-12

Status: **complete prospective pair; no positive semantic replication**

Pre-call apparatus commit: `867f7c5`

Runs:

- `runs/whole_document_r00`
- `runs/declared_sections_r00`

## Bottom line

Declared-section construction produced the better artifact, eliminated a
whole-document byte failure, and used substantially fewer resources. It did
**not** produce a complete artifact. Both conditions independently omitted the
same required source binding in the Summary.

| Condition | Semantic result | Visible | Protected bytes | Total tokens | Wall time |
|---|---:|---:|---:|---:|---:|
| Whole document | 7 pass / 2 partial | failed | References changed | 61,690 | 179.643 s |
| Declared sections | **8 pass / 1 partial** | passed | exact | **34,669** | **74.605 s** |

The section artifact semantically dominates the whole-document artifact only
because it preserves the References bytes. Both are incomplete, so the frozen
decision rule says this is **not** a positive semantic replication and section
promotion stops. The module remains useful as a removable mechanical
construction option; it does not become the workbench default.

## Prospective integrity

The task, conditions, order, tools, oracle, graders, and decision rule were
committed before either call. The cool-roof title was absent from the parent
lineage at `2a5e767`. Task SHA-256 byte parity fixed the order as whole-document
first and declared-sections second. Each condition ran once, with no inspection
or change between calls.

After both calls, final papers were copied to SHA-named files. Both unique
artifacts were graded against the frozen rubric before the condition mapping,
manifests, messages, events, requests, or responses were opened. Raw byte and
machine checks were then recorded while the mapping remained closed. Only then
were conditions revealed and trajectories inspected.

The exact blind ledgers are in [`blind/grades`](blind/grades), and the mapping
is [`blind/condition-mapping.json`](blind/condition-mapping.json).

## Exact common input

Both conditions received the same 1,819-byte task and three starting files:

- stale paper: 2,010 bytes,
  `eab21249dc743298a88e940a6dbfe816a12b25e42bcb8e92b1df4dad539d2032`;
- analysis update: 1,267 bytes,
  `80c7fac7c20cd6b1f079d7812b1649a776bf056fedf88679616300e8ea7cd453`;
- editorial note: 962 bytes,
  `48ecfe4ea502ac0377dc6767f464b4096d3a9ab1f25ab0f67e43bd8deac73382`.

The substantive challenge joined four exact facts:

```text
72% sensor completeness in cool-roof buildings
94% in comparison buildings
missing cool-roof windows concentrated during hottest afternoon hours
complete-window analysis without weighting or imputation
→ possible downward bias in observed cool-roof temperature
→ possible overstatement of apparent cooling
```

Both models also had to preserve nonrandomized/association claim strength,
current temperature estimates, exploratory/not-prespecified subgroup status,
and H1/H2/H3 claim-source bindings.

Both calls used the same Qwen alias, temperature 0, nonthinking settings,
native OpenAI-style function calling, required serial tools, exact record
custody, visible checker, and submission semantics. The only model-facing
construction difference was:

- whole-document: `replace_document(expected_candidate_sha256, new_content)`;
- section: `read_section` plus conditional `replace_section` for Summary,
  Findings, and Interpretation.

## Blind artifact results

### Shared success

Both papers correctly:

- identify a matched controlled before-after, nonrandomized design;
- use association rather than causal language;
- report 27.4 °C, 29.1 °C, adjusted difference -1.3 °C, confidence interval
  -2.0 to -0.6, and p = 0.001 where required;
- report 72% versus 94% sensor completeness;
- preserve hottest-hour concentration, complete-window analysis, no weighting
  or imputation, possible downward bias, and overstatement of cooling;
- describe floor comparisons as exploratory and not prespecified in Findings
  and nonconfirmatory in Interpretation;
- remove the causal, directional subgroup, and citywide-mandate claims; and
- remain readable and internally consistent.

The fresh “sticky” polarity relation therefore did **not** distinguish the
conditions. Qwen integrated it correctly in both.

### Shared semantic defect

Both Summaries name differential sensor completeness or missingness as a
limitation but end that statement with only `[H1][H2]`. The task and editorial
note explicitly bind sensor-bias claims to `[H3]`. Findings and Interpretation
use H3 correctly, but the Summary claim is unbound to its declared source.

This is a partial citation-binding result in both artifacts. It is not an
acquisition failure: both models read the H3 source fact and the explicit
citation instruction before construction.

The section trajectory localizes the loss even earlier. Its model-authored
checklist says the Summary should note “nonrandomized design and sensor
missingness,” but unlike the nearby H1 and H2 bullets, it does not attach H3 to
that item. The omission therefore existed in model-owned preparation before the
Summary replacement was emitted. Section granularity did not repair it.

### Whole-document-only preservation defect

The whole-document paper adds one terminal LF to the protected References
section: 216 bytes rather than the frozen 215. Title, Background, and Methods
are exact, but the complete References section is not verbatim. Its final
artifact is therefore 7 pass / 2 partial after the required custody correction.

The section paper cannot mutate the protected region through its tool surface.
Its title, Background, Methods, References, and both locked sources are
raw-byte exact. It is 8 pass / 1 partial.

## Exact trajectories

### Whole document

The whole-document action sequence was:

```text
read paper
read analysis update
read editorial note
replace document — rejected: missing final newline
replace document — rejected: missing final newline
replace document — accepted with two terminal LFs
check — failed: References changed
read current paper
replace document — rejected: missing final newline
replace document — accepted no-op with two terminal LFs
check — same failure
read current paper
submit failed candidate
```

Across five complete-document payloads, the model emitted only two distinct
byte strings. Three ended with zero LF characters and were rejected. Two ended
with two LF characters; the first created `C001`, and the second was an exact
no-op. It never emitted the required single terminal LF.

After the first failed check, `read_file(paper.md)` returned the current
candidate, not the original. The model later said it needed to inspect the
original References section, but called the same current-paper read again. The
original remained earlier in the transcript, yet the model did not recover the
one-byte distinction. It then explicitly submitted after two identical failed
check receipts.

This is a mechanical construction/transition failure, not missing semantic
evidence.

### Declared sections

The section sequence was:

```text
malformed read_file argument — rejected
read Summary
read Findings
read Interpretation
read analysis update
read editorial note
replace Summary
replace Findings
replace Interpretation
check — passed
submit
```

The first native response tried to place several XML-like tool-call fragments
inside one `read_file.path` string. llama.cpp returned one standardized native
tool call; strict schema validation rejected it as `path_not_allowed`. The
harness did not split, normalize, or repair it. Qwen recovered on the next
turn, and all ten later actions were accepted.

After exact section and source reads, the model authored a three-part change
list, then changed exactly one declared section per candidate transition:

```text
C000 --Summary--------> C001
C001 --Findings-------> C002
C002 --Interpretation-> C003
```

The one visible check passed on `C003`, and that candidate was submitted. The
model did not reread the final paper.

## Quantitative findings

| Measure | Whole document | Declared sections |
|---|---:|---:|
| Assistant/tool calls | 13 | 11 |
| Accepted changed actions | 1 | 3 |
| Accepted no-op actions | 1 | 0 |
| Rejected actions | 3 | 1 |
| Candidate versions incl. initial | 2 | 4 |
| Checks | 2 failed | 1 passed |
| Cumulative prompt tokens | 58,115 | 33,307 |
| Cached prompt tokens | 53,376 | 29,059 |
| Uncached input tokens | 4,739 | 4,248 |
| Completion tokens | 3,575 | 1,362 |
| Reasoning tokens | 0 | 0 |
| Cumulative total tokens | 61,690 | 34,669 |
| Model elapsed | 179.421 s | 74.473 s |
| Run wall time | 179.643 s | 74.605 s |

Declared sections used 56.20% of the whole-document total tokens, 41.51% of
the model time, and 41.53% of wall time. These differences are descriptive for
one fixed pair. The tool surfaces and resulting histories differ by design.

## Supporting-audit qualification

The supporting lexical audit reports failure for both papers because it
requires the exact strings “without missing-data weighting or imputation” and
“nonconfirmatory.” Both papers instead say “used no missing-data weighting or
imputation” and “do not provide confirmatory evidence.” Those are semantically
equivalent under the frozen primary rubric. The audit is retained as a useful
example of a machine instrument overstating a phrase mismatch; it does not
change either semantic grade.

## Interpretation

This pair separates two effects that the School calibration had combined.

1. **Mechanical construction improved.** Section-scoped authority made
   protected-byte corruption impossible, eliminated whole-file newline
   serialization, avoided the failed-check loop, and cut measured cost.
2. **Semantic binding did not complete.** Both frames lost the same H3 binding
   in the same Summary claim, even though the fact and instruction were in
   context. More exact artifact boundaries did not supply claim-source
   discrimination.

The result therefore does not say “action framing does not matter.” It says the
frame mattered strongly for exact construction and workflow cost, but did not
solve the remaining semantic relation. This is narrower and more useful than
either promoting the interface or dismissing it.

## Decision

Apply the frozen rule: both artifacts are incomplete, so there is no positive
semantic replication. Do not tune the cool-roof task, rerun either condition,
add a citation gate, or make section replacement a default workbench surface.

Retain the section module as an optional experimental operation because its
mechanical effect replicated prospectively. The next project question, if
pursued, must be distinct from section granularity: how to make model-chosen
claim/source binding part of construction without recreating the already weak
model-maintained citation ledger or letting the host decide relevance. This
result alone does not earn that mechanism.

## Verification

`analysis-summary.json` verifies the frozen apparatus, condition order, exact
initial messages, every native request/response, message history, tool/result
link, malformed first-turn custody, candidates, transitions, snapshots, raw
protected and locked-source bytes, check/submission bindings, blind mapping,
blind semantic ledgers, machine receipts, token sums, timing sums, and both
terminal submissions. All verification predicates are true.

Local validation after both runs:

- focused Ruff and Python compilation pass;
- `python -m unittest discover -s tests -q`: 248 passed, 14 intentionally
  skipped;
- `python -m pytest -q`: 270 passed, 14 intentionally skipped; and
- no GitHub Actions verification is claimed.
