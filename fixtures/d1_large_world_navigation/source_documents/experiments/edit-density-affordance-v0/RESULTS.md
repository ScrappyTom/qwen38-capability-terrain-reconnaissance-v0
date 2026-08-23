# Edit-Density Affordance v0 — Result

## Outcome

The adaptive-density lead failed. Qwen chose bounded-unit replacement first in
all three mixed-menu states, including the five-defect candidate. It did not
shift from unit to whole as defect density increased.

The result is mechanically clean:

- all nine cells reached a first check;
- all actions were schema-valid and admitted;
- no mutation was rejected;
- no response reached `finish_reason: length`;
- all nine trajectories submitted; and
- replay verification passed every request, response, candidate, diff, check,
  submission, and grade relation.

No action policy is promoted. The stable workbench remains unchanged.

## Primary pre-feedback result

The exact candidate bound to the first check was externally graded before
using the check response in analysis.

| Defective units | W first check | U first check | M first check | M first mutation | Terminal W / U / M |
|---:|---:|---:|---:|---|---|
| 1 | 12/16 | 12/16 | 12/16 | unit | 16/16 / 16/16 / 12/16 |
| 3 | 16/16 | 16/16 | 16/16 | unit | 16/16 / 16/16 / 16/16 |
| 5 | 16/16 | 16/16 | 16/16 | unit | 16/16 / 16/16 / 16/16 |

Forced W and U differed in first-check quality in 0/3 states. All three arms
also tied at the first check within every state. The mixed arm therefore
matched the better forced score in 3/3 states by equality, not by choosing a
superior action form.

The counterintuitive density pattern is fixture-bounded. The lone density-1
defect was the subtle reversed AP9 comparator. Adding the gate/cap defects in
density 3 made the complete defect set easier for these deterministic
trajectories to repair before checking. Density is prospectively controlled,
but the added defects necessarily change visible semantic content; the scores
do not imply that more defects generally improve Qwen.

## Frozen gate

| Requirement | Result |
|---|---|
| Every cell reaches first check | pass |
| No protocol or response-capacity failure | pass |
| No mutation admission rejection | pass |
| Mixed uses unit first at density 1 | pass |
| Mixed uses whole first at density 5 | **fail** |
| Mixed matches better forced first-check score in at least 2/3 | pass (3/3 ties) |

Because one preregistered requirement failed, `held_out_lead` is false. A
position-balanced density replication is not earned.

## Action and cost findings

| Arm | Terminal full pass | Turns | Mutation attempts | New candidate versions | Exact no-op mutations | Total tokens |
|---|---:|---:|---:|---:|---:|---:|
| W | 3/3 | 31 | 3 | 3 | 0 | 102,803 |
| U | 3/3 | 38 | 15 | 9 | 6 | 134,884 |
| M | 2/3 | 41 | 14 | 9 | 5 | 166,206 |

Whole-only used 23.78% fewer tokens than unit-only and 38.15% fewer than mixed
in this family. By state, W used fewer tokens than U by 34.22%, 7.91%, and
22.88% at densities 1, 3, and 5. W used fewer than M by 32.12%, 37.09%, and
44.84%. These are exact trajectory costs, not estimates of general tool
efficiency.

The most useful behavioral result is the density-1 path:

1. W checked the untouched candidate, received the literal mismatch, made one
   whole replacement, rechecked, and passed.
2. U read every unit, submitted five byte-identical unit bodies as admitted
   no-ops, received the same mismatch, reread and repaired `_result`, and
   passed.
3. M followed the five-no-op unit path, received the same mismatch, and then
   submitted the failed unchanged candidate.

This separates availability, action organization, effect, feedback, and
closure. The truth was present from the first request and made maximally local
by the check. The M trajectory still did not bind it to a repair.

At density 3, W and U ended with identical passing bytes; M added a redundant
validation branch but also passed. At density 5, all three arms ended with the
same exact passing bytes despite using one whole action versus five unit
actions. Action form changed the route and cost much more reliably than
artifact quality.

## Interpretation

This result refutes the narrow lead that Qwen would use defect density to
choose between these two exposed mutation forms. The mixed menu behaved as a
unit-preferring decision environment, not a measured adaptive selector.

It also strengthens three existing project findings:

- a tool menu changes work organization, not merely what actions are possible;
- an admitted action may be a no-op, so action count is not candidate progress;
- exact failed-check truth can be available and even repair-inducing in one
  surface while the same model submits it unchanged in another.

It does **not** establish that whole replacement is universally better. The
candidate was only 1,385 bytes, complete whole actions were 479 tokenizer
tokens in qualification, and every W action fit easily. Larger artifacts and
protected-scope tasks already have different evidence. Nor does it establish
that mixed menus generally harm Qwen; the preceding pilot's three mixed cells
all passed and one chose whole construction.

## Decision and next research boundary

Stop the matched edit-density selection line. Do not build a host density
classifier, adaptive menu, tool router, or default whole-only policy from this
pilot. Do not tune the density-1 fixture or rerun it to erase the failed mixed
closure.

If action affordance is revisited, the genuinely new variable is no longer
defect density. It is the representation of scope choice itself: two separate
mutation tools versus one neutral mutation operation with an explicit
whole/unit scope field, on a fresh held-out task. That could test whether the
observed serial-unit preference belongs to the semantic work state or to the
way the choice is presented. It should not be run automatically; the current
result is sufficient to stop and reconsider priorities.

## Evidence

- Frozen protocol: [`FREEZE.md`](FREEZE.md)
- Qualification: [`QUALIFICATION.md`](QUALIFICATION.md)
- Direct trajectory audit: [`AUDIT.md`](AUDIT.md)
- Analysis: [`runs/edit-density-affordance-v0-run-001/analysis.json`](runs/edit-density-affordance-v0-run-001/analysis.json)
- Replay verification: [`runs/edit-density-affordance-v0-run-001/verification.json`](runs/edit-density-affordance-v0-run-001/verification.json)
- Exact requests, raw responses, actions, results, candidates, diffs, receipts,
  and grades: [`runs/edit-density-affordance-v0-run-001`](runs/edit-density-affordance-v0-run-001/)

Total measured usage was 397,279 prompt tokens, 6,614 completion tokens, and
403,893 total tokens. Model duration summed to 451.395 seconds. These are nine
deterministic trajectories from one model/quant/profile and one matched task
family; they are not an exchangeable-sample success rate.
