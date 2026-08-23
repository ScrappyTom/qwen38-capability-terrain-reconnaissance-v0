# State-conditioned action-surface pilot v0 — results

Date: 2026-08-13

Status: **complete; predicted quality interaction stopped; no adaptive profile promoted**

## Outcome

The preregistered interaction did not occur in any of the three matched
domains.

- G11 never improved the local central-relation grade over G10.
- No response truncated, and all 24 first mutations used `replace_unit`; the
  large exact-object projection did not induce a whole-file action.
- The frozen construction grade produced G11 − G10 deltas of 0, −3, and +2.
  Direct contract audit found that every nonzero delta came from a frozen
  `TypeError` expectation that neither the authoritative source nor the blank
  construction scaffold specified.
- After preserving those frozen measurements but excluding them from
  task-grounded semantic comparison, G10 and G11 tied 8/8 in every
  construction domain.

The useful result is narrower and mechanical. Exact projected objects replaced
all acquisition reads in the small local state and cut G11 tokens by 46.20%
relative to G10. In the large construction state, Qwen reread the source,
whole target, and bounded units anyway; G11 used 96.61% more tokens than G10.
That is a state-conditioned efficiency result, not a quality profile.

The stable workbench remains unchanged. The experiment stays removable under
`experiments/`; no controller, classifier, default projection, or action policy
is promoted.

## Frozen comparison

The apparatus, fixtures, condition definitions, action union, response
allowance, and decision rule were committed at `63d3ab8` before measured
calls. Qualification and the replay-qualified disposable calibration were
committed at `c86916ee`.

Three new domains each supplied two states over the same authoritative rule:

- `local-comparison`: one existing bounded decision unit; complete oracle
  action 257–305 tokenizer tokens;
- `large-construction`: a 360-line frozen nonsemantic catalog plus five
  editable units; complete oracle action 6,253–6,615 tokens while every unit
  action was at most 185 tokens.

The 2 × 2 was:

| Condition | Task-author relation | Exact source and current target initially projected |
|---|---:|---:|
| G00 | no | no |
| G10 | yes | no |
| G01 | no | yes |
| G11 | yes | yes |

Every arm retained identical `read_file`, `read_unit`, `replace_file`,
`replace_unit`, `check`, and `submit` actions. Calls used strict schema actions,
Qwen3.6-27B IQ2 nonthinking, temperature 0, a 4,096-token completion ceiling,
and at most 18 turns. There was no retry or silent argument repair.

The preregistered primary comparison was G11 versus G10. A domain counted as
the predicted interaction only if G11 improved central relation cases without
losing local total cases and harmed construction through truncation/no
candidate or a lower total grade. At least two of three domains were required
to earn held-out replication.

## Execution and custody

All 24 cells completed once and submitted:

- 24/24 produced a candidate;
- 24/24 issued one visible check, and all 24 checks returned zero;
- 24/24 bound a submission to the current candidate and check;
- 24/24 first mutations were bounded-unit requests;
- 0/24 first mutations were whole-file requests;
- 0 incomplete responses, transport failures, or schema-interpretation
  failures;
- replay verification passed all 24 cells with zero errors.

Repository-wide local validation ran 517 tests: 503 passed and 14 archived
continuation tests were intentionally skipped. This is local validation, not
GitHub Actions verification.

The retained run is
[`runs/state-conditioned-action-surface-v0-run-001`](runs/state-conditioned-action-surface-v0-run-001).
Its preregistered derived result is
[`analysis.json`](runs/state-conditioned-action-surface-v0-run-001/analysis.json),
its post-run contract audit is
[`audit.json`](runs/state-conditioned-action-surface-v0-run-001/audit.json), and
its replay result is
[`verification.json`](runs/state-conditioned-action-surface-v0-run-001/verification.json).

## Frozen-grade results

### Aggregate

| State | Condition | Full passes | Passed cases | Total tokens | Model duration |
|---|---|---:|---:|---:|---:|
| local | G00 | 2/3 | 29/30 | 51,854 | 140.505 s |
| local | G10 | 2/3 | 29/30 | 51,738 | 146.115 s |
| local | G01 | 2/3 | 29/30 | 27,153 | 98.013 s |
| local | G11 | 2/3 | 29/30 | 27,837 | 97.928 s |
| construction | G00 | 2/3 | 29/33 | 341,310 | 246.555 s |
| construction | G10 | 2/3 | 31/33 | 312,456 | 207.230 s |
| construction | G01 | 2/3 | 29/33 | 606,030 | 278.305 s |
| construction | G11 | 2/3 | 30/33 | 614,328 | 276.797 s |

### Preregistered primary pairs

| Domain | Local G10 | Local G11 | Construction G10 | Construction G11 | Predicted interaction |
|---|---:|---:|---:|---:|---:|
| cold-chain | 10/10 | 10/10 | 11/11 | 11/11 | no |
| access-window | 10/10 | 10/10 | 11/11 | 8/11 | no |
| retention-release | 9/10 | 9/10 | 9/11 | 11/11 | no |

No local benefit occurred, so the preregistered interaction count was 0/3
regardless of the construction outcomes. The frozen decision is
`narrow_conditional_or_null_stop`.

## Post-run grader-contract audit

The frozen grade is preserved. It is not silently repaired or regraded.
However, direct review found a task/grader mismatch in every construction
fixture:

1. The authoritative source says which input types are valid.
2. It never says that invalid inputs must raise `TypeError`, `ValueError`, or
   any exception.
3. The construction `_validate` unit is a blank `return None` scaffold, so
   there is no inherited exception convention.
4. The frozen grader nevertheless requires `TypeError` in three validation
   cases per domain.

This matters because all five nonzero primary-case differences were exactly
that hidden convention:

- access G10 raised `TypeError`; G11 raised `ValueError`, creating the formal
  −3;
- retention G10 raised `ValueError` in two cases; G11 raised `TypeError`,
  creating the formal +2.

Neither difference establishes better use of the authoritative task. Excluding
only the underdetermined construction validation group gives:

| Domain | G10 specified behavior | G11 specified behavior | Difference |
|---|---:|---:|---:|
| cold-chain | 8/8 | 8/8 | 0 |
| access-window | 8/8 | 8/8 | 0 |
| retention-release | 8/8 | 8/8 | 0 |

This is an investigator audit, not a new experimental score. Its purpose is to
prevent the hidden grader convention from being misreported as a semantic
treatment effect.

## Direct request, response, and artifact review

Aggregate scores alone hide the most useful behavior.

### Cold-chain

All four conditions in both states implemented the governing calibration,
temperature-ceiling, and manual-duration relationship correctly. The large
conditions followed the same broad trajectory: reread the source and target,
read each unit, make bounded replacements, check, and submit. The projected
large objects changed cost, not the action sequence or grade.

### Access-window

In construction, G00 and G01 both omitted the explicit rule that an emergency
code extending the MFA window to 60 minutes does not grant access after minute
60. G10 and G11 both preserved that relation and passed all four central
cases. Thus the compact task-author relation had a useful descriptive effect
here; adding exact objects to that relation did not improve specified
behavior.

The formal G10/G11 difference came entirely from error class. G10's validator
raised `TypeError`. G11 returned false from `_validate` and then raised
`ValueError("Invalid input types")` in `decide`. Both enforced the stated type
domain; only the unannounced exception convention differed.

### Retention-release

The local input made the decisive relation unusually explicit: duplicate
status lowers the age threshold but never waives legal hold or export
verification. That relation was present in both G10 and G11, and G11 also
contained the literal source and current target. Nevertheless, all four local
conditions placed duplicate deletion before export verification and failed
the `duplicate_pending` case. All then passed the limited visible check and
submitted.

This is another direct instance of the external boundary already seen in the
project: relation availability or restatement does not guarantee that the
emitted action obeys it.

In the large retention state, G10 and G11 both passed every explicitly
specified ordinary, central, and frozen-structure case. Their formal +2
difference again came only from `ValueError` versus the grader's unannounced
`TypeError` convention.

## State-conditioned efficiency

| State and contrast | Reads, control → treatment | Token change | Model-duration change |
|---|---:|---:|---:|
| local G10 → G11 | 8 → 0 | −46.20% | −32.98% |
| local G00 → G01 | 9 → 0 | −47.64% | −30.24% |
| construction G10 → G11 | 21 → 21 | +96.61% | +33.57% |
| construction G00 → G01 | 16 → 21 | +77.56% | +12.88% |

The small projected target was operationally usable immediately. Each exact-
object local cell first supplied the whole-target SHA-256 to `replace_unit`;
the host rejected all six attempts as `unit_version_mismatch`, exposed the
literal current unit identity, and Qwen repaired the action without a read.
Even with that factual rejection, the projected-object arms required fewer
calls and tokens than their controls.

The large target behaved differently. Every G01 and G11 construction cell
reread the source, reread the whole target, and read its five bounded units
despite already receiving the source and target bytes in the initial
projection. Because the complete initial user message remains in every later
request, injecting a roughly 20–23 KB target multiplied cumulative prompt
cost without substituting for acquisition.

This does not establish a universal size threshold. It shows that an automatic
large projection was redundant in these six trajectories while the small
projection substituted for reads in the matched local states.

## Relation to the decision-environment hypothesis

The pilot supports the vocabulary but not the proposed adaptive policy.

A projection did define more than an information subset:

- the small exact-object frame changed the first operation from acquisition
  to attempted mutation;
- the large exact-object frame did not create the same transition and instead
  coexisted with complete reacquisition;
- the fixed bounded-unit action menu kept all large trajectories within the
  response channel, despite every oracle whole-file action exceeding 4,096
  tokens.

That last result is important relative to the adjacent deployment failure.
Rich exact objects did **not** inherently cause a monolithic truncated action
when bounded mutation units were explicit and available. This experiment does
not isolate why Qwen selected them, because every arm had the same menu. It
does show that the prior `relation + operands → oversized mutation` path is
not a general consequence of richer context.

What did not survive is the stronger prediction that the two mechanically
defined states would produce opposite quality effects from adding exact
objects. The state labels predicted cost, not semantic quality, and even the
cost effect was mediated by what Qwen chose to reread.

## Decision

1. Stop the predicted G11-versus-G10 quality interaction at v0.
2. Promote no state classifier, context compiler, card, default exact-object
   projection, or automatic profile selector.
3. Preserve the exact-object efficiency interaction as descriptive evidence:
   small current objects can replace acquisition; automatic large objects can
   duplicate it at high cumulative cost.
4. Preserve the bounded action-surface observation: all 24 trajectories chose
   bounded first mutations and none hit the 4,096-token expression boundary.
   This is not a causal qualification of `replace_unit` because there was no
   action-menu control.
5. Treat the construction validation mismatch as a fixture-design defect.
   Future task graders must specify the exact invalid-input effect in the
   authoritative task or avoid scoring its exception class.
6. Do not tune or rerun these fixtures. Any later action-affordance experiment
   must use new tasks and isolate the menu/action representation rather than
   another semantic wrapper.

## Limits

- one deterministic trajectory per cell, not a reliability estimate;
- three synthetic Python domains with matched scaffolds;
- a deliberately large nonsemantic catalog, not naturally long code;
- cumulative token counts include the treatment projection in every retained
  user message;
- the relation is task-author supplied, not model-authored;
- the frozen visible checks exercised only two ordinary cases and did not
  expose the retention binding failure;
- the construction grader defect blocks semantic interpretation of its
  exception-class deltas;
- no treatment varied the bounded-unit action menu itself.

The result therefore answers one narrow question: in this fixed six-action
ecology, automatically projecting exact source and target objects did not
improve quality beyond an already-present task-author relation. It changed
acquisition and cost in opposite directions across the two state shapes.
