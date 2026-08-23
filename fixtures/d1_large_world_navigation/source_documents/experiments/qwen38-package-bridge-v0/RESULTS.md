# Qwen3.8 Package Bridge v0 Results

## Outcome

The bridge found a meaningful Qwen3.8 package lead on five of the six named
tasks, plus one severe construction-boundary regression.

Direct artifact review found complete submissions for:

- quota-window repair;
- reservation-batch repair;
- cooling-centers paper revision;
- cedar incident evidence synthesis; and
- freshness runbook integration.

The event-digest construction submitted a syntax-broken package after a
repeated exact-patch mismatch loop. This is not a six-task pass rate: each
fixture is a different named challenge and each has one seeded trajectory.

The frozen hidden graders reported only two passes. Direct review established
that the paper, incident brief, and runbook failures were lexical false
negatives. The machine outputs remain preserved; they are not used as semantic
ground truth.

The practical decision is therefore nuanced:

- Qwen3.8 is now a serious candidate for bounded repair, evidence synthesis,
  and document revision in this workbench;
- it has not earned global default status because its blank-package
  construction trajectory was both worse and vastly more expensive; and
- the next comparison should use fresh work and separate package quality from
  action-expression reliability rather than rerun or tune these six tasks.

## Experimental boundary

The apparatus was committed and pushed at
`cd85e7ac` before the first bridge task call. Qwen3.8 received the exact six
fixtures, tool/action surface, response schema, 4,096-token action allowance,
24-turn limit, checks, and graders previously used in
`model-package-screen-v0`.

The measured package was:

- Qwen3.8-27B `UD-IQ2_XXS`, loaded-file SHA-256
  `8d1b37297d6cf98303cd396896f35e01089ddcc904053a9c6997f7a1c35b8524`;
- llama.cpp `b10434-7e4c0a968`;
- 50,176 context, q4 K/V cache, 65/65 CUDA layers;
- nonthinking;
- temperature 0.7, top-p 0.8, top-k 20, min-p 0, presence penalty 1.5,
  repeat penalty 1.0;
- request seed 42; and
- strict `schema-action-v1` through `response_format: json_schema`.

The corresponding Qwen3.6 screen used its qualified temperature-zero package
on llama.cpp b10331. Therefore the named comparison is between complete
deployable packages, not model weights alone. Every Qwen3.8 first request had
the same `messages` and `response_format` as its Qwen3.6 counterpart; only
package-owned inference fields differed.

## Six named trajectories

`P/F` records visible checks. `patches` records accepted/rejected patch
actions. Frozen machine output and direct artifact judgment are intentionally
separate.

| Fixture | Status | Turns | Visible P/F | Patches | Total tokens | Model time | Frozen machine observation | Direct judgment |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Quota window | submitted | 9 | 1/0 | 2/0 | 24,450 | 63.127 s | pass, 12/12 | **complete** |
| Reservation batch | submitted | 11 | 1/0 | 3/0 | 38,527 | 85.245 s | pass, 13/13 | **complete** |
| Event digest | submitted | 23 | 0/2 | 5/4 | 299,779 | 1,061.631 s | fail, syntax error | **operational failure** |
| Cooling-centers paper | submitted | 6 | 1/0 | 1/0 | 15,794 | 61.769 s | fail, 11/13 | **complete**; lexical false negatives |
| Cedar incident brief | submitted | 9 | 1/0 | 1/0 | 24,201 | 53.282 s | fail, 10/13 | **complete**; lexical/section false negatives |
| Freshness runbook | submitted | 7 | 1/0 | 1/0 | 20,921 | 43.304 s | fail, 13/14 | **complete**; hyphenation false negative |

## Factual package metrics

| Measure | Qwen3.8 bridge |
|---|---:|
| Named trajectories | 6 |
| Terminal states | 6 submitted |
| Turns | 65 |
| `tree/read/patch/check/submit` | 6 / 29 / 17 / 7 / 6 |
| Accepted patches | 13 |
| Rejected actions | 4, all `patch_not_applicable` |
| Checks passed/failed | 5 / 2 |
| Submissions after only failed checks | 1 |
| Exact assistant-response recurrences | 12 |
| Context ceilings | 0 |
| Cached/prompt/completion/total tokens | 344,321 / 401,629 / 22,043 / 423,672 |
| Model time | 1,368.358 s |
| Recorded wall time | 1,374.968 s |
| Preserved evidence | 1,294 files; 6,886,090 bytes |

Eleven of the 12 exact-response recurrences and all four rejections occurred
in the event-digest trajectory. The other five runs were operationally clean.

## Named comparison with Qwen3.6

The earlier Qwen3.6 trajectory is the incumbent named comparator, not a
population estimate.

| Fixture | Qwen3.6 direct judgment | Qwen3.8 direct judgment | Q36 turns/tokens | Q38 turns/tokens |
|---|---|---|---:|---:|
| Quota | not complete (`Q3`) | **complete** | 11 / 31,290 | 9 / 24,450 |
| Reservation | not complete (`R2`, `R4`) | **complete** | 10 / 28,680 | 11 / 38,527 |
| Event digest | not complete but importable | **operational failure** | 12 / 47,617 | 23 / 299,779 |
| Paper | **complete** | **complete** | 9 / 27,073 | 6 / 15,794 |
| Incident | not complete (`I3`) | **complete** | 12 / 40,014 | 9 / 24,201 |
| Runbook | **complete** | **complete** | 7 / 20,883 | 7 / 20,921 |

Across all six tasks, Qwen3.8 used 423,672 tokens versus Qwen3.6's 195,557
and 1,368.358 model-seconds versus 360.150. Those aggregate ratios—2.17x
tokens and 3.80x time—are dominated by one pathological construction run.

Excluding event digest, Qwen3.8 used 123,893 tokens versus 147,940 for Qwen3.6
(16.3% fewer), and 42 turns versus 49. Its model time was still 306.727
seconds versus 261.159 (17.4% slower), consistent with the changed model and
runtime package rather than excess interaction alone.

Per task, Qwen3.8's token ratio relative to Qwen3.6 was:

- quota: 0.78;
- reservation: 1.34;
- event digest: 6.30;
- paper: 0.58;
- incident: 0.60; and
- runbook: 1.00.

This is heterogeneous work-shape behavior, not one overall efficiency number.

## What the trajectories imply

### 1. The model-package change matters

Qwen3.8 repaired three named obligation sets that Qwen3.6 had missed: quota
validation, reservation validation, and incident source binding. It matched
Qwen3.6's already-complete paper and runbook while using fewer turns on paper
and incident. That is too coherent to dismiss as a grader artifact, because it
comes from direct code/document inspection.

It remains one seeded trajectory per named task, and the sampler/runtime also
changed. The earned claim is a deployable-package lead on these bounded work
shapes, not a general Qwen3.8 capability ranking.

### 2. Construction/action expression is a separate risk axis

The event-digest run was not primarily an information-acquisition failure.
The model read the task and current file, found substantive defects, and
generated a cleaner intended implementation. It then lost one quote in an
accepted whole-file action and repeatedly failed to bind its next exact patch
to the literal malformed source it had reread.

This cleanly separates semantic intent from admitted world effect. A model can
understand the needed artifact and still fail at exact action expression and
closure. That axis should be measured separately in the next model study.

### 3. The graders are bounded instruments, not semantic judges

Only two frozen hidden checks passed, while direct review found five complete
artifacts. Three of those five complete artifacts received false-negative
overall machine grades, comprising six failed lexical or section-scoped grader
groups across paper (two), incident (three), and runbook (one). The false
negatives came from task-equivalent wording, hyphenation, and section-specific
matching—not close scientific interpretation. Future studies should retain
mechanical graders for executable behavior and exact contracts, but
substantive conclusions require direct, preferably blinded, artifact review
against the task and evidence.

This does not authorize post-hoc generosity. The event-digest syntax error and
invalid example remain genuine failures. The distinction is whether the
instrument directly establishes the task property it claims to measure.

### 4. The stable harness remains informative

The unchanged custody loop exposed successful bounded work, lexical grader
defects, a one-character mutation error, four exact admission rejections,
repeated rereads, repeated identical responses, failed verification, and
premature submission without normalizing them into one score. No new cards,
semantic status, retries, or coaching are earned.

## Decision and next step

- Keep the workbench and strict schema-action interface frozen.
- Preserve Qwen3.6 as the incumbent comparator rather than calling it the
  universally best package.
- Treat Qwen3.8 as the leading candidate package for bounded repair and
  evidence/document transformations, pending fresh-task replication.
- Do not use Qwen3.8's event-digest failure to add automatic patch repair or
  retries. First test whether the literal-action failure recurs on fresh
  construction work.
- Do not run the previously drafted 32-cell diagnostic matrix yet. The package
  bridge shows that model package and action-expression shape can create more
  variance than the proposed information treatment.

The highest-value next experiment is a fresh, compact two-package replication
bank with three preserved work shapes:

1. bounded multi-obligation code repair;
2. evidence-grounded document/research transformation; and
3. blank or large construction with exact mutation pressure.

Run Qwen3.6 and Qwen3.8 on the same fresh tasks and grade literal artifacts and
world effects directly. If a material package difference recurs, open a small
matched-sampler attribution branch. Independently, if a repeated non-apparatus
failure leaves treatment headroom, cross one qualified information treatment
with model. Neither branch is a mandatory gate in front of the other.

## Reproduction and evidence

- Apparatus: [`PROTOCOL.md`](PROTOCOL.md), [`QUALIFICATION.md`](QUALIFICATION.md),
  [`PREFLIGHT.md`](PREFLIGHT.md), and [`matrix.json`](matrix.json)
- Exact raw trajectories: [`runs/`](runs/)
- Factual extraction: [`metrics.json`](metrics.json)
- Direct review: [`ADJUDICATION.md`](ADJUDICATION.md)

All six run directories replay-verified after completion. The focused local
preflight passed 57/57 tests; the post-run focused suite, including replay,
request-equivalence, and metrics checks, passed 60/60. This is local
validation, not CI verification. Replay verification reconstructs the saved
custody state; it is not a repeated-inference determinism test.
