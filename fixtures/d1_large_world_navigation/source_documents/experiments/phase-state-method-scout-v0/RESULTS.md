# Phase-state method scout v0 results

Status: **complete development scout; no method promoted**

Date: 2026-08-16

## Verdict

The scout supports a narrower and more useful claim than “the transcript
should not be state”:

> On one code revision and one research revision, Qwen3.8 completed the next
> phase from a fresh current world, with or without a model-authored process
> checkpoint. A bounded checkpoint reduced actor reacquisition and calls, but
> did not make model-authored semantic derivatives reliable.

All six continuations submitted. All three code artifacts passed a complete
16-group executable audit. All three research artifacts passed the 12-group
literal audit and retained the full required factual core under direct review.
The transcript research memo was semantically cleanest; world and process each
contained a different unsupported or stale decision claim.

No reset policy, plan system, checkpoint schema, phase router, semantic card,
or two-model workflow is promoted.

## Results

| Task | Condition | Terminal quality | Actor / method calls | Method tokens | Max prompt | Direct qualitative result |
|---|---|---:|---:|---:|---:|---|
| Allocation ledger | Transcript | 16/16 | 5 / 5 | 36,957 | 9,099 | Complete |
| Allocation ledger | Fresh world | 16/16 | 7 / 7 | 19,700 | 4,666 | Complete; cheapest code method |
| Allocation ledger | Process checkpoint | 16/16 | 4 / 5 | 26,695 | 5,838 | Complete; fewer actor calls, checkpoint cost erased token advantage over world |
| Telehealth memo | Transcript | 12/12 literal; complete factual core | 10 / 10 | 127,467 | 17,119 | Cleanest semantic artifact; one literal-check repair |
| Telehealth memo | Fresh world | 12/12 literal; complete factual core | 14 / 14 | 96,813 | Two literal-check repairs; unsupported extra-cost caveat |
| Telehealth memo | Process checkpoint | 12/12 literal; complete factual core | 6 / 7 | 58,534 | First-check pass; stale Phase-A decision rule survived |

Across both tasks, process used 12 method calls and 85,229 tokens versus
transcript at 15 calls/164,424 tokens and world at 21 calls/116,513 tokens.
This did not translate into a general time win: recorded model time was about
263 seconds for process, 285 seconds for transcript, and 224 seconds for
world. Those are six case trajectories, not performance estimates.

## What the scout establishes

### Exact current world can carry operational continuity

Neither fresh condition lost the task or failed to recover necessary files.
The code world actor reacquired tree, change, SPEC, and implementation; the
research world actor reacquired the current review, index, memo, and final
effect/cost records. Both completed.

The transcript therefore is not demonstrated to be necessary state for these
phase transitions. It did remain useful: it avoided some reacquisition and
produced the best research artifact.

### The process package changed action organization

Both process actors used the checkpoint and exact selected files. Code went
from world's seven actor calls to four; research went from fourteen to six.
The research actor passed its literal audit after one construction rather than
after two repairs.

This is a package effect combining:

- a separate producer inference;
- a fresh actor context;
- a model-authored checkpoint;
- a mechanical manifest;
- selected exact current files; and
- different first-action readiness.

The study does not identify which component caused the effect.

### Authority labels are necessary but insufficient

The checkpoint explicitly labeled its objective, completion claims,
relevance choices, hypotheses, and plan as model-authored and
non-authoritative. Its statements were accurate. Yet the research actor
retained an old decision criterion embedded in the editable Phase-A memo:
obtain a later finalized positive estimate before expansion. The current [R7]
record was already final and the current task permitted a limited monitored
extension under uncertainty.

The important boundary is not merely transcript versus state. It is:

```text
task-authored authority
        +
mechanically current world
        +
model-authored derivatives inside that world
        ↓
fresh decision and action
```

Mechanical currentness cannot certify the meaning of a model-authored
artifact.

## Apparatus correction

The first research transcript reached a passing check and emitted `submit`,
then Windows rejected a 261-character experiment-owned submission snapshot
path. The raw r1 run remains an `integrity_failure`. A correction declared and
committed before rerun shortened only the experimental run IDs/output path.
All ten rerun transcript requests, actions, and pre-submit results were
byte-identical to r1, and the terminal candidate ID was identical. The
corrected run then received passing submission and grade receipts.

The split verifier passed all completed and preserved-failure trajectories,
source identities, candidate equality, correction equivalence, runtime
profile, 66/66 offload, memory, and clean shutdown.

## Limitations

- This is one common trunk and one continuation per condition in each domain.
- Both fixtures are development tasks designed for this scout.
- Conditions are complete methods with unequal producer and acquisition work;
  no component-causal conclusion is permitted.
- The research machine audit is lexical and literal. Direct semantic review
  is required and was not blinded.
- The shared stable system message inaccurately called the research
  environment a “code-repair workbench.” It was held across conditions but
  must be made task-neutral before cross-domain replication.
- Fixed seed and sampler make exact replay useful but do not estimate method
  reliability.
- Prompt caching makes cumulative token totals a poor proxy for wall time.

## Decision and next step

Retain the ordinary loop and stable custody substrate. Preserve this process
checkpoint only as a removable experimental method.

The next earned study is a **fresh whole-method replication**, not component
isolation:

1. correct the factually inaccurate cross-domain system label without adding
   semantic guidance;
2. create two or three new multi-phase workflows in which task-authoritative
   state changes and an existing model-authored artifact, test, or plan may
   contain stale implications;
3. compare the same frozen transcript, fresh-world, and process packages under
   a common model/time/action ceiling;
4. separately grade executable behavior, exact authority transfer,
   model-authored derivative revision, semantic quality, action organization,
   and cost; and
5. promote nothing unless process matches transcript quality while retaining
   a useful operational/cost advantage across fresh code and research work.

If that package replicates, then isolate checkpoint production, selected exact
files, fresh context, and explicit artifact-authority labels. If it does not,
close automatic process-state generation and keep fresh current-world reentry
as an on-demand capacity/recovery tool rather than normal continuity.

## Evidence

- [`FREEZE.md`](FREEZE.md)
- [`EXECUTION_CORRECTION.md`](EXECUTION_CORRECTION.md)
- [`POSTRUN_VERIFICATION.json`](POSTRUN_VERIFICATION.json)
- [`METRICS.json`](METRICS.json)
- [`ACTION_LEDGER.json`](ACTION_LEDGER.json)
- [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md)
- [`RESEARCH_QUALITATIVE_REVIEW.md`](RESEARCH_QUALITATIVE_REVIEW.md)
- literal run stores under `runs/r1` and `runs/r2`

