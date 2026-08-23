# Action-Affordance Selection v0 — Results

## Decision

The pilot produced a clean terminal-quality tie and therefore did **not**
instantiate the frozen selection opportunity:

- 9/9 cells submitted and passed every full case;
- forced whole and forced unit quality differed in 0/3 fixtures;
- mixed used both mutation forms, but there was no better forced quality arm
  for it to select; and
- the held-out-lead gate failed. No mutation policy is promoted.

The useful narrower observation is behavioral. With both forms available,
Qwen used bounded-unit replacement for the localized and coupled repair, then
whole-file replacement for the construction. The menu changed action
organization and cost without changing terminal quality. That is evidence
that an action menu is part of the decision environment; it is not evidence
that Qwen selected the globally best operation.

## Frozen comparison

Every arm received the same exact task, authoritative contract, initial
candidate, model profile, nonthinking sampler, 4,096-token response allowance,
reads, visible check, and submission. The only model-facing difference was the
declared mutation menu and the strict schema needed to express it:

- `W`: `replace_file` only;
- `U`: `replace_unit` only; and
- `M`: both operations.

Both mutation forms bound to the full current candidate version. Static
qualification established that an oracle whole action and the sequence of
oracle unit actions reconstructed identical passing bytes and that every legal
oracle action fit well within the response allocation.

## Per-cell results

| Fixture / shape | Arm | Full grade | First mutation | Reads | Mutation attempts / admitted | Checks | Turns | Prompt | Completion | Total tokens | Model time |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| incident-routing / localized repair | W | 12/12 | file | 2 | 1 / 1 | 1 | 5 | 10,964 | 439 | 11,403 | 28.145 s |
|  | U | 12/12 | unit | 2 | 1 / 1 | 1 | 5 | 10,401 | 280 | 10,681 | 20.528 s |
|  | M | 12/12 | unit | 0 | 1 / 1 | 1 | 3 | 5,553 | 239 | 5,792 | 17.116 s |
| quota-reservation / coupled repair | W | 12/12 | file | 2 | 1 / 1 | 1 | 5 | 11,213 | 529 | 11,742 | 32.344 s |
|  | U | 12/12 | unit | 7 | 6 / 4 | 1 | 15 | 55,820 | 1,237 | 57,057 | 77.101 s |
|  | M | 12/12 | unit | 7 | 4 / 4 | 1 | 13 | 46,450 | 820 | 47,270 | 54.613 s |
| batch-window / construction | W | 13/13 | file | 2 | 1 / 1 | 1 | 5 | 11,342 | 639 | 11,981 | 37.387 s |
|  | U | 13/13 | unit | 7 | 6 / 6 | 2 | 16 | 66,726 | 1,311 | 68,037 | 82.307 s |
|  | M | 13/13 | file | 2 | 1 / 1 | 1 | 5 | 11,940 | 658 | 12,598 | 38.873 s |

Across all nine cells there were 72 actions, 31 reads, 22 mutation attempts,
20 admitted mutations, 10 checks, and nine submissions. Usage was 230,409
prompt tokens, 6,152 completion tokens, 236,561 total tokens, 189,801 cached
tokens, zero reasoning tokens, and 388.414 seconds of model time. No response
ended with `finish_reason: length`; no schema response or transport call failed.

Aggregated by arm:

| Arm | Turns | Total tokens | Model time |
|---|---:|---:|---:|
| W | 15 | 35,126 | 97.876 s |
| U | 36 | 135,775 | 179.936 s |
| M | 21 | 65,660 | 110.602 s |

Relative to `W`, `U` used 286.54% more tokens and 140% more turns; `M` used
86.93% more tokens and 40% more turns. Relative to `U`, `M` used 51.64% fewer
tokens and 41.67% fewer turns. These are descriptions of three different
fixtures, not estimates over a task population.

## What the exact trajectories show

### Localized repair

Forced whole and forced unit both reread the contract and a target view before
one correct mutation. Mixed used the already projected exact objects and
immediately replaced only `route`, then checked and submitted. Its three-call,
5,792-token path was the smallest in the matrix.

The mixed choice was locally coherent: one marked unit contained the entire
defect. It also shows that initial exact objects can substitute for reacquisition
when the next mutation is sufficiently local. This is one deterministic cell,
not a stable policy estimate.

### Coupled multi-unit repair

Whole replacement completed in one mutation and five turns. Forced unit and
mixed both reread the contract, whole candidate, and all five units, then
replaced `validate`, `available`, `allowance`, and `classify`; `decide` did not
need a change once the helpers were repaired.

Mixed therefore chose unit work despite whole work being far cheaper on the
matched forced paths: 47,270 tokens for mixed versus 11,742 for whole-only. The
choice looks more like a repair-versus-construction heuristic than global cost
optimization. It is the main counterexample to claiming that exposing both
forms makes operation choice efficient.

### Moderate construction

Whole-only and mixed both reread the contract and candidate, emitted one
whole-file implementation, passed their first visible check, and submitted.
Unit-only read all five units and constructed them sequentially. Its first
complete candidate graded 10/13 externally: the model used `ValueError` where
the exact contract required `TypeError` for three validation cases. The visible
check exposed one of those cases as expected `TypeError` versus observed
`ValueError`; Qwen replaced `validate`, fixed all three full-grade cases, passed
the second check, and submitted 13/13.

This is the most relevant path-quality observation. The unit construction did
not lose the contract or candidate; it lost one exact validation distinction
during construction and recovered when a discriminating result made it local.
The two whole-construction paths represented that distinction in their first
candidate. Terminal scoring alone would hide the action-boundary difference.

## Direct-audit qualification

The aggregate `U` cost is not a clean affordance cost estimate. In
`quota-reservation/U`, the first two `validate` mutations ended with a newline.
The world rejected both as `new_body_outer_whitespace`; the third byte-equivalent
body without the final newline was admitted. The action catalog and schema did
not declare that trailing newline constraint, even though the system called
them authoritative. This is a real mechanical contract defect, not model
semantics. The factual rejection was not silently repaired, and the model
recovered, but the two extra calls must not be attributed to unit granularity.

Subtracting those two calls would not erase the broad coupled-path difference:
the unit path still required all acquisition plus four mutation turns rather
than one whole mutation. It does prevent treating the exact 15-turn/57,057-token
cell as a clean causal cost measurement.

No grader-only semantic requirement was found. Every case maps to a literal
contract ID, invalid-input exception classes are explicit, and the submitted
alternate implementations were directly reviewed against the source. They are
not byte-identical to the fixture oracle but satisfy the stated contracts.

See [`AUDIT.md`](AUDIT.md) for the input/output/artifact inspection and
`runs/action-affordance-selection-v0-run-001/verification.json` for custody
replay.

## Interpretation

This result supports four bounded statements:

1. Both whole and unit mutation interfaces can carry correct work when both
   payloads fit.
2. The available mutation menu can change acquisition, construction sequence,
   and first-check quality even with identical world facts.
3. Qwen can choose different mutation forms across visibly different work
   shapes, but did not choose the lower-cost forced form on the coupled repair.
4. A discriminating mechanical check can repair a construction-time semantic
   detail that exact task availability did not preserve into the first unit
   candidate.

It does **not** show a terminal-quality advantage for either mutation form, an
adaptive quality policy, or a universal best operation. The stable workbench
and default renderer remain unchanged.

## Next high-ROI question

If this line continues, the next experiment should isolate **edit density**
rather than add another context wrapper. Use a fresh matched family with the
same contract size, candidate size, unit menu, and response allowance, but one,
three, or five units prospectively requiring change. Cross `W`, `U`, and `M`.
Make the primary quality measure the externally graded first complete candidate
*before* any visible-check feedback, while retaining terminal recovery as a
separate outcome.

That would answer two questions this pilot could not:

- whether mixed operation choice has a repeatable locality/density crossover;
  and
- whether sequential unit construction changes constraint survival before
  verification, rather than merely adding calls.

The unit-body newline contract must be corrected and fully declared before
freezing such a study. No classifier or adaptive host is earned; the model can
continue choosing from the mixed menu.
