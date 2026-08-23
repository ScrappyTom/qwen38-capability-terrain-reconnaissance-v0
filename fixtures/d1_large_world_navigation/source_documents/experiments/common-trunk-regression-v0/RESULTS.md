# Common-trunk regression re-verification v0 results

## Verdict

The common-trunk screen completed, but the C0/C1 receipt comparison had no
eligible input.

All eight Qwen3.8 first-pass actors repaired their disclosed target, retained
the passing sibling, introduced no contract-audit regression, passed the
complete executable audit, and submitted naturally. Under the frozen rule,
no continuation branch was allowed.

This is a valid zero-input stop, not evidence that a fresh pass and a
contrastive regression receipt are equivalent. Their comparison was never
run.

## Exact outcome

| Observation | Result |
|---|---:|
| Fresh tasks | 4 |
| Fixed seeds per task | 2 |
| Common trunks | 8 |
| Natural submissions | 8/8 |
| Original targets repaired | 8/8 |
| Passing siblings retained | 8/8 |
| Complete-audit predicates, source | 82/90 |
| Complete-audit predicates, terminal | 90/90 |
| Newly regressed predicates | 0 |
| Branch-eligible trunks | 0/8 |
| C0/C1 branch calls | 0 |
| Model calls | 32 |
| Accepted actions | 32/32 |
| Rejected actions | 0 |
| Total reported tokens | 79,736 |
| Prompt tokens | 77,967 |
| Completion tokens | 1,769 |
| Summed model duration | 149,778 ms |

Every trajectory used the same four-action organization:

```text
read exact implementation
→ one accepted patch
→ visible two-predicate check passed
→ submit
```

There were no no-op mutations, failed visible checks, rejected actions,
turn-limit endings, or continuations.

## What the tasks established

The two local validation tasks produced the expected split between type and
value/range branches at both seeds. The two history/order tasks also repaired
their target while preserving deletion/reintroduction or new-category
behavior.

Three of four task pairs produced byte-identical terminal candidates across
seeds. Category Stream produced two different but contract-audit-complete
implementations. Seed 42 removed the obsolete category-history deletion
branch cleanly. Seed 314159 replaced the deletion with an empty `pass` branch.
The latter is executable-contract correct but less clean. This is a concrete
reason to preserve direct code review alongside predicate totals.

Only three of eight terminal candidates were byte-identical to their
task-author golden. All eight nevertheless passed every frozen executable
predicate. The audit establishes task-contract behavior, not unique or ideal
implementation form.

## What was not tested

The intended causal question required a first pass that both:

1. fixed the disclosed target; and
2. broke a predicate that had passed on the source.

No first pass did that. Therefore the study supplies no behavioral evidence
for any of these comparisons:

- fresh opportunity versus no fresh opportunity;
- empty re-verification versus regression receipts;
- receipt-assisted containment versus target undoing; or
- C0/C1 cost differences.

Do not report the absent branch as a null treatment effect.

## Why the state did not arise

The opportunity control was corrected, but the fresh fixtures were deliberately
clean one-defect states. Exact target/control receipts, exact candidate bytes,
and a local implementation made the repair highly discriminating. That was a
reasonable pre-call construction rule, but it removed the messy partial-work
ecology in which the earlier regressions occurred.

This refines the experimental method:

> A causal branch design can be sound while its common trunk fails to
> instantiate the phenomenon. Qualify the transition state itself before
> spending treatment calls.

If regression containment is revisited, use naturally produced first-pass
candidates from fresh, broader repair/construction work and branch only after
an independently executed audit discovers a real source-passing-to-terminal-
failing transition. Do not make these four fixtures harder after seeing this
result.

## Research decision

- Keep the stable harness unchanged.
- Retain failed-plus-passing local receipts as a bounded prior lead; this study
  neither promotes nor refutes them as a general policy.
- Stop this run at the frozen zero-input gate.
- Keep generic action-organization interventions parked.
- Preserve complete-audit false closure as the next separate avenue because it
  targets a distinct, already observed transition rather than manufacturing a
  regression here.

See [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md) for the literal
input/action/output review and [`APPARATUS_CORRECTION.md`](APPARATUS_CORRECTION.md)
for the reporting-only verifier correction.

## Validation boundary

- 8/8 experiment apparatus tests pass.
- 8/8 saved trajectories replay-verify with zero reported errors.
- The run snapshot's 57-file source lock verifies.
- Every golden and every terminal complete audit passes.
- The model server was stopped after the batch; process and port counts both
  returned to zero.

The broader repository discovery suite is currently not green: 634 tests ran,
with 584 passes, 14 skips, and 36 errors in archived-experiment artifact/
fixture integrity checks outside this new experiment (including older reviewer,
semantic-frame, dependency-topology, and information-state archives). This
study did not modify those archived sources. The result is therefore locally
verified, not a claim of repository-wide CI health.
