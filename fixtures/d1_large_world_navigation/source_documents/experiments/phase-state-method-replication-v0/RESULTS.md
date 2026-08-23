# Phase-state method replication v0 results

Status: **complete; process package not promoted**

Date: 2026-08-16

## Verdict

The simpler architectural result replicated: a complete accumulated
transcript was not necessary to produce correct current artifacts after an
authority-changing phase boundary. Fresh-world reentry produced the only
12/12 code candidate and a clean 11/11 research memo. It did not complete code
closure within the frozen 16-call opportunity, so this is evidence for
artifact continuity rather than a claim that fresh reentry always completes
more efficiently.

The complete process-checkpoint package did not pass its promotion gate. It
again organized the next phase earlier, but that advantage did not become a
reliable end-to-end win:

- its code actor implemented all 11 current product groups in two calls, then
  exhausted the 4,096-token response channel while attempting a whole-file
  test rewrite and left two stale Phase-A test assertions;
- its research actor submitted in ten actor calls, correctly replaced the old
  policy, and preserved the full factual core, but one final sentence
  over-strengthened when some follow-up evidence had to exist; and
- checkpoint production plus eager selected bytes made research P more costly
  and slower than on-demand fresh-world W.

No checkpoint, reset policy, plan, phase router, card, or semantic
invalidation mechanism is promoted. The stable `workbench/` is unchanged.

## Measured outcomes

### Code

| Condition | Status | Actor / method calls | Method tokens | Max actor prompt | Product groups | Package tests | Closure |
|---|---|---:|---:|---:|---:|---:|---:|
| Transcript T | protocol error | 6 / 6 | 106,694 | 21,282 | 11/11 | fail | no |
| Fresh world W | turn limit | 16 / 16 | 176,594 | 24,166 | 11/11 | pass | no |
| Process P | protocol error | 4 / 5 | 53,975 | 10,609 | 11/11 | fail | no |

T and P each emitted an incomplete JSON patch while trying to replace the
entire 7,309-byte package-test file. T used exactly the full combined context
window: 21,282 prompt + 3,806 completion = 25,088. P had input headroom but
hit the independent 4,096-token completion ceiling. W chose bounded patches,
used a failed check to remove one newly invented contradictory test, and
passed the full 12/12 audit on its last permitted call.

### Research

| Condition | Status | Actor / method calls | Method tokens | Read bytes | Semantic review | Model time |
|---|---|---:|---:|---:|---:|---:|
| Transcript T | submitted | 11 / 11 | 163,500 | 2,377 | 11/11 | 187.2 s |
| Fresh world W | submitted | 13 / 13 | 88,115 | 13,281 | 11/11 | 174.0 s |
| Process P | submitted | 10 / 11 | 120,607 | 11,544 | 10 met + 1 partial | 258.6 s |

All three passed the 14/14 supporting lexical audit and used only current
records. T and W met every frozen semantic criterion. P correctly revised the
Phase-A wait rule, so the prior stale-rule failure did not replicate. Its
partial criterion is a new, narrower overstatement: a final sentence
grammatically makes safety/generalization evidence a precondition before the
limited extension even though R9 requires that evidence only for future
citywide deployment.

## What replicated

### Exact current world can carry the work

Across the earlier scout and this replication, fresh-world actors have now
reconstructed useful work in four distinct code/research transitions without
prior transcript, summary, plan, or checkpoint. In this replication W reached
the best code artifact and tied the cleanest research semantics. This is
meaningful evidence that transcript history need not be the durable world
state.

### A checkpoint changes organization

P reached the first mutation earlier in both tasks. In code it mutated on
actor call 2 versus T call 4 and W call 8. In research it mutated on actor call
5 versus T call 7 and W call 8. The checkpoint was accurate, explicitly
non-authoritative, and used downstream.

The package therefore has an organizational effect. What failed to replicate
was a complete quality-and-cost advantage.

## What did not replicate

### Process was not consistently cheaper

P used 53,975 method tokens on code, about half of T and 69% below W. On
research it used 120,607: 26% below transcript but 37% above fresh world. Its
producer and larger repeated base prompt also made it slower than both
research comparators. Fewer actor actions do not automatically mean lower
local-GPU cost.

### The prior stale semantic rule did not recur

The new research checkpoint and actor both recognized that R9 superseded R6
and that a limited monitored extension may proceed. The remaining P issue was
an over-strengthened timing sentence, not preservation of the old wait rule.
Semantic derivative staleness remains a real prior observation, but this run
does not establish it as the checkpoint package's recurring failure.

## The newly sharp boundary

The code result identifies a concrete action-channel problem rather than a
generic need for more reasoning or context. Exact replacement of a large file
requires serializing both the old and new complete texts. T and P knew the
right test revision but chose an action whose representation could not fit.
W selected smaller patches and crossed the boundary.

This repeats a pattern seen in earlier saved work: input working-set capacity,
semantic correctness, action organization, and output serialization capacity
are separate. A model can know what to do and still choose an infeasible
expression of it.

## Frozen decision

P does not match the best comparator's complete code artifact and does not
show a repeated cost advantage across both workflows. It therefore does not
earn component isolation or default use.

Retain:

- exact external custody and replay;
- ordinary transcript as a comparison condition;
- fresh current-world reentry as a removable recovery/phase tool;
- explicit authority separation between task records and model-authored
  derivatives; and
- direct evaluation of product, self-authored verification, action effect,
  and closure as separate outcomes.

Do not promote:

- automatic checkpoint generation;
- a persistent process card or plan;
- semantic cache invalidation by the host;
- a phase router; or
- a claim that transcript is useless or fresh world is always cheaper.

## Recommended next work

Do not run another checkpoint-format or semantic-state factorial. Two things
are now earned at different levels:

1. **Mechanical action-surface qualification, without changing the stable
   harness.** Specify an experiment-local hash-bound whole-file replacement
   action that sends the new bytes once rather than duplicating old and new
   complete files. Validate its custody and replay semantics and test it on a
   fresh large-edit workflow. This is earned by repeated literal
   serialization failures, not by a desire to rescue P.
2. **Then test bounded phase reentry over several phases.** Compare transcript
   accumulation with fresh current-world reconstruction across a longer
   authentic code or research workflow, using the same qualified action
   surface in both arms. The question is whether externally custodied world
   state can keep each phase bounded without losing semantic quality as
   history grows.

Automatic checkpoints remain parked unless a later broad trajectory provides
a new whole-method reason to revisit them.

## Evidence

- [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md)
- [`RESEARCH_QUALITATIVE_REVIEW.md`](RESEARCH_QUALITATIVE_REVIEW.md)
- [`METRICS.json`](METRICS.json)
- [`ACTION_LEDGER.json`](ACTION_LEDGER.json)
- [`EXTERNAL_EVALUATION.json`](EXTERNAL_EVALUATION.json)
- [`POSTRUN_VERIFICATION.json`](POSTRUN_VERIFICATION.json)
- [`AUDIT_CORRECTION.md`](AUDIT_CORRECTION.md)
- exact r3 custody under [`runs/r3/`](runs/r3/)
- preserved apparatus corrections in [`EXECUTION_CORRECTION.md`](EXECUTION_CORRECTION.md)
