# Failure Bench v0 results

Date: 2026-08-14

Run: `failure-bench-v0-run-001`

Status: **complete; one replicated semantic success with a modest compactness
miss, one strong exploratory action lead, and one retired repair-package
family; nothing promoted to the harness**

## Outcome

The broad failure-first approach was useful. It found three different movements
of the failure boundary rather than one universal information treatment:

- compact task-author coverage restored every reviewed qualifier on two tasks;
  the resulting artifacts were 22 and 19 words over an intentionally tight
  125-word limit;
- an aligned relation/current-target package produced the best Dispatch first
  mutation and satisfied all four directly tested governing invariants, versus
  zero for baseline; the frozen grader never exercised that mutation, so its
  planned aggregate is invalid while the direct result remains exploratory;
- repair packages stopped immediate submission on the discovery task, yet all
  three emitted exact no-op rewrites; on a sibling, the contrast package made a
  real partial repair but left the central visible defect.

The result does **not** earn a card, router, semantic host field, reviewer,
persistent memory object, or default package. It does earn a small Qwen
failure-interface playbook and one corrected relation-binding replication.

## Execution and custody

- 12 discovery calls and 6 frozen sibling calls;
- 18/18 HTTP responses succeeded and 18/18 model outputs passed their copied
  response schema;
- 135,379 prompt tokens, 16,762 completion tokens, 152,141 total tokens;
- 976,890 ms summed HTTP duration (16 minutes 16.9 seconds; not wall-clock
  throughput under concurrency);
- 18/18 request/response/candidate records verified against freeze
  `c9701c1697126b074cd1664b661322f21ee71e5c700118effe3fb8577951fe1f`;
- no retry, silent response repair, or second actor turn; and
- no change to `workbench/`.

Focused validation is green: 9/9 failure-bench tests passed, all 181 saved JSON
files parsed, the run verifier checked 18/18 calls, `git diff --check` passed,
and 157 local Markdown links across the changed governing documents resolved.

The repository-wide archived suite is not currently portable enough to serve
as a green branch check. In the working checkout, 627 tests ran with 36 errors
caused by `core.autocrlf=true` changing exact LF fixture bytes to CRLF. A clean
LF checkout removed those failures but ran only 612 tests and reported 37
errors plus 6 failures because historical tests depend on ignored/uncommitted
snapshots and candidate files absent from Git. No global-suite success is
claimed, and archive recovery is outside this experiment's scope.

The full per-cell machine record is
[`analysis.json`](runs/failure-bench-v0-run-001/analysis.json). Literal model
inputs, outputs, actions, effects, and candidates are under
[`runs/failure-bench-v0-run-001/calls/`](runs/failure-bench-v0-run-001/calls/).

## Discovery

### Qualifier loss

Condition-blind review used eight source-grounded criteria (`met=2`,
`partial=1`, `not_met=0`). All four artifacts preserved the correct central
interpretation and introduced no unsupported claims.

| Condition | Points | Words | 125-word contract | Total tokens | Result |
|---|---:|---:|---:|---:|---|
| Baseline | 10/16 | 107 | pass | 1,154 | Central direction right; six distinctions compressed |
| Compact coverage | 16/16 | 147 | fail | 1,398 | Complete reviewed semantic coverage |
| Aligned construction | 16/16 | 145 | fail | 1,513 | Complete reviewed semantic coverage |
| Contrastive construction | 15/16 | 128 | fail | 1,395 | Manager-selection detail omitted |

Compact and aligned improved the reviewed semantic endpoint by 6 points. The
compact package used 244 more tokens than baseline (+21.1%) and won the frozen
tie-break over aligned. Because the selection rule prioritized semantic points
before the word contract, compact advanced despite its 22-word overrun.

Decision: **complete semantic pass with a modest length-contract miss**. This
is a strong local result; the overrun is material only for uses that genuinely
require a 125-word artifact.

### Relation-to-action binding

The saved model-authored handoff correctly named the pending/release defects.
The fresh baseline nevertheless reproduced all four governing implementation
defects. The literal actions differed under treatment, but the frozen package
grader exited at an untouched public import and did not run the implementation
checks. Its recorded `11/12` for every cell is invalid as a passed-group count.

| Condition | Frozen recorded hidden | Effective mutation | Post-hoc governing invariants | Total tokens |
|---|---:|---:|---:|---:|
| Baseline | 11/12, import exit | yes | 0/4 | 5,665 |
| Compact relation | 11/12, import exit | yes | 3/4 | 5,789 |
| Aligned relation + target | 11/12, import exit | yes | 4/4 | 5,837 |
| Contrastive cases | 11/12, import exit | yes | 0/4 | 5,874 |

The 0/4 → 4/4 aligned difference is strong direct mechanical evidence from the
exact saved code, not a textual self-report. It is not negated by the broken
frozen grader. It remains exploratory rather than confirmatory because the
diagnostic was introduced after discovering the defect, covers four targeted
invariants rather than full package integration, and has one deterministic
trajectory per condition. Compact was carried forward only because the frozen
recorded tie-break selected it.

Decision: **frozen primary metric ineligible; aligned package is a strong
exploratory local success requiring one clean replication**.

### Feedback-to-repair and closure

The baseline submitted the unchanged red Config Stack candidate. Each treatment
instead emitted a patch, but every patch had the current 4,049-byte file as
both `old` and `new` and was rejected as an exact no-op.

| Condition | Next action | Effect | Visible | Hidden | Total tokens |
|---|---|---|---:|---:|---:|
| Baseline | submit | no mutation | 2/4 | 4/12 | 15,404 |
| Typed discrepancy | patch | rejected exact no-op | 2/4 | 4/12 | 17,744 |
| Unresolved invariants | patch | rejected exact no-op | 2/4 | 4/12 | 17,784 |
| Counterfactual repair | patch | rejected exact no-op | 2/4 | 4/12 | 17,737 |

The packages changed action selection but not action content or world effect.
They added 15.1%–15.4% total tokens. Contrast was carried to transfer only as
the lowest-token ineffective intervention under the frozen tie-break.

Decision: **retire these discovery packages**.

## Sibling transfer

### Qualifier: Appointment reminder

| Cell | Points | Words | Contract | Total tokens |
|---|---:|---:|---:|---:|
| Baseline | 13/16 | 120 | pass | 1,135 |
| Compact coverage | 16/16 | 144 | fail | 1,393 |

Compact improved assigned-clinic analysis, missing-data-method coverage, and
the exact low-attendance qualifier. It added 258 tokens (+22.7%) and exceeded
the word limit by 19 words.

Decision: **replicated semantic success with a modest length-contract miss**.
For ordinary long-context work this is a successful coverage intervention. A
separate compression step is relevant only when the output must actually stay
within 125 words.

### Relation: Segment Assembler

Baseline made an effective code mutation and recorded 10/12 hidden groups. The
compact package instead returned a detailed model-owned `record_item`. That
operation was present in the copied response schema but absent from the reduced
bench executor, which rejected it as unsupported. The candidate did not change,
and its nominal 11/12 was another early public-import reduction rather than an
executed comparison.

Decision: **transfer apparatus-invalid; no sibling claim**.

### Feedback: Dependency Planner

| Cell | Next action | Mutation | Visible | Hidden | Total tokens |
|---|---|---:|---:|---:|---:|
| Baseline | submit | no | 3/4 | 10/12 | 19,676 |
| Contrast | replace file | yes | 3/4 | 11/12 | 21,516 |

Contrast broke immediate red submission and fixed the hidden
`sequence_forward_refs_and_reads` group. It still failed visible
`ordinary_plan` and hidden identifier validation, because it did not establish
one public `PlanTask` identity and returned `None` for invalid reads. It cost
1,840 additional tokens (+9.4%).

Decision: **descriptive situation-specific improvement, not a transferable
repair policy**. The discovery family remains retired.

## What was learned

### 1. Information packages can move a failure rather than solve it

Qualifier coverage solved the measured semantic omission and moved the only
remaining miss to compactness. Repair packages moved premature submission into
exact no-op serialization. These effects are interpretable only because
semantic quality, format compliance, action effects, and costs remain
separately visible.

### 2. Semantic possession, action choice, expression, and effect are distinct

Config Stack is the cleanest sequence:

```text
exact failed-check truth present
        ↓
treatment makes repair the chosen operation
        ↓
model serializes unchanged old/new bytes
        ↓
machine rejects no-op
        ↓
world remains red
```

“The model reacted to feedback” and “the model repaired the candidate” are not
interchangeable claims.

### 3. The literal grading boundary matters as much as the prompt

The Dispatch aggregate suggested a four-way tie. Direct code inspection showed
large differences. The problem was not semantic disagreement; the grader never
reached the code and the reducer overstated tests as passed. This is precisely
why the repository rule requires inspecting model input, output, candidate, and
custody logs before diagnosing performance.

### 4. Coarse packages are useful for discovery, not promotion

Compact coverage, aligned comparison, and counterfactual repair changed
different boundaries. None is a universal view. The result supports a local
playbook, not an adaptive classifier.

## Final decision

| Family | Decision |
|---|---|
| Qualifier loss | Retain compact task-author coverage as a **replicated semantic success** for these qualified dense-synthesis omissions. Record the 15.2%–17.6% length overruns separately; require compression only where that limit is operationally real. |
| Relation-to-action | Mark the frozen primary metric **ineligible**, not the literal action result. Preserve aligned relation + target as a **strong exploratory 0/4→4/4 local success** for one corrected replication. |
| Feedback-to-repair | **Retire** the three tested discovery packages. Preserve the sibling's partial action divergence as descriptive evidence only. |
| Stable workbench | **Retain unchanged.** |

The next highest-return experiment is four calls: two fresh authentic
relation-known/action-violated boundaries, each tested with baseline versus the
frozen aligned package class, using a grader that directly exercises the
mutated object and a response schema containing only executable operations.
No additional package search, reviewer, routing, or repair loop is warranted
before that check.

## Evidence links

- [Freeze](FREEZE.md)
- [Direct trajectory audit](DIRECT_TRAJECTORY_AUDIT.md)
- [Custody qualifications](CUSTODY_CORRECTIONS.md)
- [Qwen playbook](PLAYBOOK.md)
- [Selection record](runs/failure-bench-v0-run-001/selection.json)
- [Verification](runs/failure-bench-v0-run-001/verification.json)
- [Machine-readable analysis](runs/failure-bench-v0-run-001/analysis.json)
