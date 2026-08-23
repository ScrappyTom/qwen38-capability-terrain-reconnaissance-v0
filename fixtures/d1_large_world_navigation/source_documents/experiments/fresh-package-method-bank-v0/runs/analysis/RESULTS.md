# Fresh Qwen3.6/Qwen3.8 package bank results

Date: 2026-08-14

## Decision

Use the qualified Qwen3.8 package as the primary local experimental model for
this workbench, while retaining Qwen3.6 as a deterministic comparison package.
Do not interpret that decision as general model superiority or code-task
readiness.

Qwen3.8 showed a repeated package-level advantage in action organization,
completion, and evidence-grounded writing. It did **not** eliminate the
broader code-quality pattern: several independent written obligations still
disappeared during construction. A later task-text re-audit also found that
the raw hidden graders overstated this pattern by enforcing exception classes
that Telemetry, Shipment, and most Stock clauses did not specify.

The stable harness stays frozen. No card, semantic state, retry, action repair,
reviewer, router, or automatic coaching mechanism is promoted.

## What ran

Six genuinely fresh tasks were each run once under the unchanged
`ordinary-v0` action-result loop with two complete deployable packages:

- two multi-obligation code repairs;
- two evidence-grounded document revisions; and
- two substantial code constructions.

The model-facing task messages and strict action schema were identical within
each pair. Qwen3.6 used its temperature-zero package on llama.cpp b10331.
Qwen3.8 used the recommended nonthinking sampler with seed 42 on llama.cpp
b10434. This is a package comparison, not a weights-only or sampler-only
comparison.

All twelve trajectories replay-verified. All model servers were operated
serially and externally. After the last cell, the Qwen3.8 process and port
were gone, free physical RAM was 52.95 GB, and dedicated VRAM usage returned
to 594 MiB.

## Named outcomes

| Task | Qwen3.6 | Qwen3.8 | Direct interpretation |
|---|---|---|---|
| R1 telemetry repair | submitted; 7/11 raw, 9/11 task-aligned | submitted; 7/11 raw, 10/11 task-aligned | Both missed the explicit frozen-model requirement. 3.6 additionally admitted bool/non-finite sample values. The other raw differences were exception-class policies absent from the task. |
| R2 shipment repair | submitted; 7/10 raw, 10/10 task-aligned | submitted; 7/10 raw, 10/10 task-aligned | Both rejected every task-forbidden input and met the written tuple contracts. The three raw failures came from unannounced exception classes and an unstated outer-tuple requirement. |
| E1 shuttle brief | submitted; machine audit green | submitted; machine audit green | Both substantively strong. 3.6 had a localized uncited Summary and read only the already-informative brief; 3.8 reopened all locked records and produced tighter bindings. |
| E2 cold-storage memo | submitted; machine audit green | submitted; machine audit green | 3.6 retained an unsupported adopt-everywhere recommendation. 3.8 removed it and preserved uncertainty. Clear 3.8 quality advantage. |
| C1 reservation construction | loop-censored; terminal 7/11 | submitted; raw 8/11 | 3.8 encoded lifetime identity and escaped the import failure. Direct audit found that its successful reschedule never updated stored state, which the hidden grader missed. Strong workflow advantage, not a clean one-group quality win. |
| C2 stock construction | token-censored; terminal 5/12 raw | submitted; 5/12 raw | Equal raw total, but 3.8 produced a materially better reverse operation and passed the visible check. Direct task review isolates two explicit 3.8 failures: apply never enforces lifetime ID uniqueness, so successful apply and reverse IDs can be reused through apply. Most other raw failures were unannounced exception-class policies. |

These are six named paired case studies, not six exchangeable samples. No
pooled pass percentage or confidence interval is reported.

## Workflow and cost

| Package | Submitted | Censored | Actions | Rejected actions | Failed visible checks | Cumulative reported tokens | Summed model time |
|---|---:|---:|---:|---:|---:|---:|---:|
| Qwen3.6 package | 4 | 2 | 71 | 8 | 9 | 439,119 | 1,193.73 s |
| Qwen3.8 package | 6 | 0 | 51 | 0 | 1 | 172,560 | 517.03 s |

The aggregate Qwen3.8 path used 60.7% fewer cumulative reported tokens and
56.7% less summed model time. That difference is dominated by the two Qwen3.6
construction tails; it is not a general efficiency estimate.

Per task, Qwen3.8 token use changed by:

- R1: +4.9%;
- R2: -1.6%;
- E1: +127.4%, because it reopened three locked records that 3.6 skipped;
- E2: +3.4%;
- C1: -75.6%; and
- C2: -90.6%.

“Cumulative reported tokens” sums each request's usage and therefore counts
the growing transcript again on later turns. It is the frozen resource-censor
quantity, not unique context bytes.

## Strongest recurring failure

The clearest cross-task pattern is not missing truth. It is loss of
independent written distinctions during construction. The surviving examples
are heterogeneous: frozen dataclasses in Telemetry, lifetime identifier
enforcement in Stock, successful stored-state mutation in Reservation, and
the exact type/value distinction where Reservation explicitly specified it.

The initial report overstated the exception-class portion. Telemetry,
Shipment, and most Stock clauses require invalid inputs to be rejected but do
not prescribe `TypeError` versus `ValueError`. Their hidden graders did. Those
raw failures remain useful diagnostics of evaluator policy, but they are not
task failures. Shipment is the clearest correction: both candidates satisfy
the literal task even though both retain raw 7/10 grader results.

Where the task did state independent behaviors, the facts were already in the
prompt and the model read the target files. Qwen3.8 often implemented the
central mechanism while omitting one independently stated invariant or world
effect.

The second recurring failure is false closure from incomplete verification.
Qwen3.8 submitted all four code artifacts immediately after a visible pass.
Three retained explicit task defects; Shipment did not, despite its raw grader
failure. The receipts were factual for the cases they executed, but they were
too narrow to establish completeness on the other three tasks.

## What the harness should do for Qwen3.8

Retain these parts as the baseline:

1. external single-instance model-server lifecycle;
2. strict schema-constrained actions with no client repair;
3. exact reads, patches, candidate versions, results, checks, and submissions;
4. a 4,096-token action allowance;
5. factual non-progress and cumulative-resource censors; and
6. direct semantic review for document/research work.

The next high-return intervention is not another static view. It is a
removable **verification-complete method** on fresh code tasks: expose exact
executable results only for contract groups stated in the task rather than a
small happy-path check or grader-authored additions. This remains machine
logic and factual feedback; it does not tell the model how to repair anything.

Only if exact, requirement-complete verification still leaves the same
independent-constraint omissions should the project add the already-frozen
`evidence-v0` task-author coverage artifact. That ordering separates:

```text
truth was never tested / exposed at verification
from
truth was exposed exactly but still did not govern repair
```

A compact next study should use two new validation-dense code tasks and the
Qwen3.8 package first:

1. ordinary loop with the existing bounded check style;
2. ordinary loop with a complete factual contract check; and
3. only if condition 2 retains real headroom, complete check plus the frozen
   task-author coverage artifact.

Qwen3.6 should be added only when a treatment effect is worth testing for
model interaction. A matched-sampler subset is independently justified if the
project needs to attribute the package difference; it is not a prerequisite
to improving Qwen3.8's workbench method.

## Evaluation corrections carried forward

- Machine checks are authoritative only for the behavior they execute.
- Task text outranks an accidental extra grader convention.
- A direct source audit can reveal missing world effects that a green group
  failed to test.
- Document supporting audits do not establish semantic support or absence of
  unsupported recommendations.
- Rubric-only additions not stated in the task remain diagnostic; they do not
  become post-run hard requirements.
- Replay verification establishes custody reconstruction, not inference
  repeatability.

See `DIRECT_TRAJECTORY_AUDIT.md` for the literal prompt/action/artifact review
and `metrics.json` for exact per-run usage and action counts.
