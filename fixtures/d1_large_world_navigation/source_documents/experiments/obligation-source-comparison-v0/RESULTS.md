# Obligation-source comparison v0 — result

Date: 2026-08-12

Run: `obligation-source-comparison-v0-run-001`

Freeze commit: `33ba8af`

## Outcome

No obligation source qualified, and the independent role added no value.

Both model roles selected the frozen task-author assignment on the five flawed
units and selected R4 rather than the frozen R1 preservation assignment on the
already-correct unit. Their six parsed selection objects were identical across
roles. All 19 calls were protocol-admitted.

The downstream result was a complete null by source: task-author, worker, and
independent-reviewer mappings produced the same six final unit texts. Every
central defect was corrected and the no-op was preserved, but all five edited
units omitted one qualification required by the frozen rubric. Every source
therefore graded 1 pass / 5 partial / 0 fail.

| Boundary | Result | Frozen decision |
|---|---|---|
| Worker preparation selector | 6/6 admitted; 5/6 exact frozen IDs; no abstention | fail |
| Independent reviewer selector | 6/6 admitted; 5/6 exact frozen IDs; no abstention | fail |
| Cross-role selection | same six selected IDs | no role effect |
| Task-author local action | 1 pass / 5 partial / 0 fail | incomplete control |
| Worker local action | 1 pass / 5 partial / 0 fail | no improvement |
| Independent local action | 1 pass / 5 partial / 0 fail | no improvement |
| Recomposition | not run | prerequisite not met |

The frozen exact-ID gate is preserved as failed. Direct review also found that
its U006 gold label was not exclusive: R1 was the intended preservation
assignment, but R4 literally applied as well because the unit already reported
the record's estimate, confidence interval, and p-value exactly. Both R1 and R4
actor calls returned the original line byte for byte. This is a fixture/gold
ambiguity, not evidence that the selectors misunderstood U006. It does not
rescue either condition under the precommitted rule.

## What the model actually received

I directly inspected all twelve selector requests and raw responses and all
seven actor requests and raw responses before grading.

For each unit, the worker and independent selector user messages were byte
identical. They contained:

- the same current candidate identity;
- one exact artifact unit and byte/hash identity;
- one exact evidence record and task-author binding;
- the same complete, unranked six-requirement catalog; and
- no gold obligation assignment, active obligation, prior response, action,
  grade, or recommended next step.

Only the selector system-role sentence differed. Each selector returned the
unit ID and one requirement ID or `ABSTAIN` through a strict JSON schema.

The actor received the full editorial task, the same unit, evidence record,
and provenance-free binding, plus a mechanically normalized exact requirement
object. Its request contained no task-author, worker, reviewer, selector, or
assignment-source label. Identical `(unit, requirement)` inputs were executed
once and mapped to every matching source.

## Selector result

| Unit | Frozen assignment | Worker | Independent | Direct finding |
|---|---:|---:|---:|---|
| U001 | R4 | R4 | R4 | exact |
| U002 | R6 | R6 | R6 | exact |
| U003 | R3 | R3 | R3 | exact |
| U004 | R5 | R5 | R5 | exact |
| U005 | R2 | R2 | R2 | exact |
| U006 | R1 | R4 | R4 | frozen mismatch; R4 also applicable |

Both roles were 5/6 against the frozen IDs (83.3333%) with zero abstentions.
The semantic selection objects matched 6/6 across roles. Their raw JSON bytes
did not match because the worker outputs used varying whitespace while the
independent outputs were compact; custody preserved that nonsemantic
difference.

This result supplies no evidence that an independent reviewer selects a better
obligation than the acting model. It also shows that a single-label obligation
gold can be ill-posed when several task requirements legitimately apply to one
unit. That is an experimental-design finding, not a reason to change this run.

## Local-action result

| Action | Unit / requirement | Grade | Direct finding |
|---|---|---|---|
| A001 | U001 / R4 | partial | corrected 12.6%, CI, and p-value; omitted `two-sided` |
| A002 | U002 / R6 | partial | made the claim observational; omitted nonrandom assignment |
| A003 | U003 / R3 | partial | supplied 64%/91% and exaggeration; omitted the rainy-evening part of the mechanism |
| A004 | U004 / R5 | partial | supplied post hoc, estimates, interaction, and no established modification; omitted explicit `not prespecified` |
| A005 | U005 / R2 | partial | removed the false GPA result and stated nonmeasurement; omitted the resulting inability to establish change |
| A006 | U006 / R1 | pass | exact byte-preserving no-op |
| A007 | U006 / R4 | pass | exact byte-preserving no-op under the alternate applicable requirement |

The model again made every central correction while losing a secondary clause
from each multi-clause requirement/evidence pair. This happened with the exact
task-author obligation, so choosing a different obligation source cannot
explain or fix it. The active obligation is an exact pointer, not an execution
guarantee.

The wrong-against-gold R4 selection did not damage U006 because the actor also
received the complete task and evidence and obeyed the general instruction to
preserve an already-satisfactory unit. This is useful robustness, but it does
not qualify the selector under the frozen rule.

## Quantitative findings

### Worker-preparation selector

- calls: 6;
- protocol admitted: 6/6;
- exact frozen assignments: 5/6;
- abstentions: 0;
- prompt tokens: 7,814;
- completion tokens: 167;
- total tokens: 7,981;
- cached prompt tokens: 620;
- reasoning tokens: 0;
- summed HTTP time: 33.417 seconds.

### Independent-reviewer selector

- calls: 6;
- protocol admitted: 6/6;
- exact frozen assignments: 5/6;
- abstentions: 0;
- prompt tokens: 7,850;
- completion tokens: 114;
- total tokens: 7,964;
- cached prompt tokens: 650;
- reasoning tokens: 0;
- summed HTTP time: 21.336 seconds.

The roles ran sequentially, so their latency difference is descriptive, not a
role-performance comparison.

### Combined selector work

- calls: 12;
- exact frozen assignments: 10/12;
- prompt tokens: 15,664;
- completion tokens: 281;
- total tokens: 15,945;
- cached prompt tokens: 1,270;
- reasoning tokens: 0;
- summed HTTP time: 54.753 seconds;
- share of recorded run tokens: 67.3751%.

### Deduplicated actor work

- unique calls: 7;
- protocol admitted: 7/7;
- condition-mapped unit actions: 18;
- redundant deterministic executions avoided: 11;
- central defects corrected: 5/5;
- strict passes among flawed units: 0/5;
- no-op variants preserved: 2/2;
- prompt tokens: 7,149;
- completion tokens: 572;
- total tokens: 7,721;
- cached prompt tokens: 1,074;
- reasoning tokens: 0;
- summed HTTP time: 40.190 seconds;
- share of recorded run tokens: 32.6249%.

### Whole evidence run

- calls: 19;
- protocol admitted: 19/19;
- prompt tokens: 22,813;
- completion tokens: 853;
- total tokens: 23,666;
- cached prompt tokens: 2,344;
- reasoning tokens: 0;
- summed HTTP time: 94.943 seconds.

## Interpretation

This experiment separates two results that would otherwise be easy to blur.

First, both model roles could identify the operation needed for every actually
flawed unit. The independent role changed neither selection nor action. The
single remaining exact-ID mismatch arose on a no-op for which the catalog had
two applicable requirements, exposing a flaw in single-label gold rather than
a clean selector miss.

Second, perfect source control did not produce exhaustive local action. The
task-author arm supplied the exact intended requirement, yet the actor retained
only the central correction and dropped one required qualification in every
edited unit. This repeats the productive-but-incomplete local behavior on a
new fixture more strongly than it distinguishes obligation sources.

The evidence therefore does not support adding an independent planner,
promoting a worker-authored obligation map, or treating a task-author label as
sufficient semantic control. It also does not support a conclusion that model
roles cannot select useful obligations; the flawed-unit selections were all
correct and the no-op comparison was ambiguous.

## Decision

- Do not promote task-author, worker-owned, or independent-reviewer obligation
  assignment as a runtime mechanism from this result.
- Do not tune the same fixture, add retries, broaden the selector output, or
  silently substitute the frozen gold.
- Preserve the finding that task requirements can overlap; a future
  obligation experiment would need a prospectively defensible multi-label or
  mutually exclusive contract, not a regrade of U006.
- Do not run Stage 4 recomposition on these outputs. Five of six local units
  are already incomplete, so any final artifact would confound local semantic
  loss with composition behavior.
- Keep the stable workbench, custody substrate, and model server unchanged.

## Validation

- freeze committed and pushed before calls at `33ba8af`;
- endpoint identity: llama.cpp `b10331-7ba604f1c`, alias
  `qwen36-27b-iq2-coding`, 50,176 context;
- request settings: temperature 0, reasoning disabled, JSON-schema outputs,
  no tools, no retries;
- saved-run replay verification: passed;
- direct review: 12 selector requests/responses and 7 actor
  requests/responses;
- semantic grading and the U006 ambiguity finding were added only after the
  run;
- complete local suite: 418 tests passed with 14 expected archived skips;
- targeted Ruff, JSON, Markdown-link, and Git whitespace checks: passed;
- the stable `workbench/` and model-server profile were unchanged.

This is local validation, not GitHub Actions verification.
