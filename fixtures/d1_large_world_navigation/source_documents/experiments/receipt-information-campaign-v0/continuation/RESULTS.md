# Priority Catalog turn-limit continuation — results

Source run: `ric-q38-r002`, cell `tc-pc42-category-order`

Continuation runs:

- `ric-q38-r003-continuation`: exact calls 11–20 for all three arms;
- `ric-q38-r004-trace-followon`: exact calls 21–30 for the one branch still
  censored at call 20.

Status: **complete; all three branches reached natural submission**

## Verdict

The original ten-call cutoff censored useful work in the final-receipt branch,
but more turns were not a general repair mechanism.

- `T0_NONE` submitted the unchanged call-10 candidate immediately on call 11
  and failed the grader.
- `T1_FINAL` continued a coherent implementation, repaired the temporal target,
  passed the visible check, and submitted on call 17. It gained five net saved
  contract predicates, but also regressed replacement-category behavior and
  failed the hidden grade.
- `T2_TRACE` retained its already-passing temporal target, made two stable
  validation fixes by call 20, then spent six more calls changing the same
  replacement logic, failed the same visible check twice, and submitted on
  call 26 despite `passed:false`. Calls 21–26 produced zero contract-predicate
  transitions.

Thus a ten-call terminal comparison understated the value of `T1_FINAL` and
created the trace arm's apparent 2/3 versus 1/3 target advantage. At natural
submission, final and trace each repaired 2/3 temporal targets across the
original three-cell scout. The trace has no remaining target advantage.

## Exact outcomes

| Arm | Natural stop | Focus at call 10 | Focus at stop | Clear contract effect after call 10 | Grade |
|---|---:|---:|---:|---|---:|
| `T0_NONE` | submit, call 11 | failed | failed | none | failed |
| `T1_FINAL` | submit, call 17 | failed | passed | five clear fixes plus one process-sensitive ordering fix; one regression | failed |
| `T2_TRACE` | submit, call 26 | passed | passed | two validation fixes; no further transition after call 20 | failed |

The saved complete-audit counts were:

- `T0_NONE`: 45/53 at call 10 and 45/53 at submission;
- `T1_FINAL`: 41/53 at call 10 and 46/53 at submission; and
- `T2_TRACE`: 42/53 at call 10, 44/53 at call 20, and 44/53 at submission.

One identity-based same-priority predicate can vary across fresh Python
processes for candidates that still sort by object identity. The named target,
collateral predicates, exact visible-check results, and saved run-time audits
are primary; aggregate counts and that predicate are secondary.

## What additional turns bought

| Arm | Total calls | Total reported tokens | Model-call time | Marginal result after call 10 |
|---|---:|---:|---:|---|
| `T0_NONE` | 11 | 79,873 | 171.4 s | unchanged submit |
| `T1_FINAL` | 17 | 152,011 | 181.0 s | target repair and net contract gain |
| `T2_TRACE` | 26 | 367,587 | 409.8 s | two validation fixes, then no net gain and failed-check submission |

For `T2_TRACE`, calls 11–20 consumed 156,891 reported tokens and calls 21–26
consumed another 144,500. The latter six calls changed no audited predicate.
The largest prompt was 26,196 tokens, well below the pinned 50,176-token
context; the largest completion was 708 tokens against the 4,096-token response
allowance.
This was action-turn organization and closure behavior, not context or response
capacity exhaustion.

## Method decision

For complex multi-step repair studies, a ten-call cutoff is too small to treat
as a natural terminal outcome. A turn-limit ending is administrative censoring.
If the literal transcript shows active work, preserve the checkpoint and
continue it under a separately frozen, disclosed budget before judging value.

That does not imply that 20 or 30 calls improves correctness by itself:

- one branch falsely closed as soon as a narrow visible check passed;
- another closed correctly on that check but remained hidden-contract
  incomplete; and
- the longest branch submitted after two explicit failures of the same check.

The stable harness remains unchanged. Turn allowance is already fixture
configuration. The earned change is to experimental interpretation and budget
selection, not a new card, retry, semantic gate, or host coaching rule.

## Meta-process correction

The first campaign report compared the temporal arms at the frozen ten-call
cutoff and treated their terminal-status rows as if they represented completed
model behavior. That was too quick. Literal inspection showed that the
Priority final-only and trace branches were still engaged in construction or
repair when the apparatus stopped them. The cutoff was an administrative
event, not a model decision.

This is an investigator-side version of the same compression problem the
project observes in models: an exact trajectory was reduced to a convenient
summary label, and the label began governing the conclusion. The user noticed
the unresolved work before the formal analysis did.

The custody substrate made the error recoverable. The exact request history,
candidate, profile, actions, and results could be resumed while changing only
the disclosed total allowance. No approximate rerun or reconstructed model
state was needed. The resulting evidence changed the comparison: the trace's
apparent target advantage disappeared at natural submission.

The governing correction is therefore broader than “increase the turn
limit”:

- derived statuses and aggregate tables are navigation aids, not substitutes
  for the literal trajectory;
- a result is not ready for a move-on decision until its endpoint is audited;
- productive unfinished work, repetitive ineffective work, and voluntary
  closure are different states even when a runner labels them all terminal;
- fixed-call comparisons can observe different methods at different points on
  their work curves; and
- natural submission records closure, not correctness.

The original cutoff evidence remains preserved. This forward correction
changes its interpretation rather than rewriting it.

## Evidence

- [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md)
- [`FREEZE.md`](FREEZE.md)
- [`TRACE_FOLLOWON_FREEZE.md`](TRACE_FOLLOWON_FREEZE.md)
- exact first continuation: `../runs/ric-q38-r003-continuation/`
- exact residual-censoring follow-on: `../runs/ric-q38-r004-trace-followon/`
