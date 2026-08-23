# Staged Construction Replication v0 Results

Status: **complete; the frozen staged package did not replicate and is closed**

The only positive whole-method lead from `agent-method-scout-v0` did not
survive this prospective replication. On three fresh blank-package
construction tasks, staged hybrid was higher than ordinary on one task, tied
the executable-group count on one, and was lower on one. The frozen rule
required staged to be higher on at least two tasks and lower on none.

No component isolation is earned. The stable workbench remains unchanged, and
ordinary remains the reference comparator rather than a demonstrated
generally best method.

## What ran

The experiment compared two complete methods using the same local
Qwen3.6-27B server profile:

- model alias: `qwen36-27b-iq2-coding`;
- quantized model profile: Qwen3.6-27B UD-IQ2_XXS;
- temperature `0`, thinking disabled, and 4,096 generated tokens per response;
- `ordinary`: one actor with the exact action surface;
- `staged_hybrid`: the scout's frozen preparer, non-authoritative workspace,
  fresh actor, and one same-model review after first submission.

The three fixtures were written and mechanically qualified before model calls.
They were not selected from observed Qwen failures. Reference candidates
passed every visible and hidden executable group, while blank candidates
failed. All six measured cells followed the preregistered schedule without a
rerun.

## Paired result

| Task | Ordinary | Staged hybrid | Paired observation |
|---|---:|---:|---|
| Segment Assembler | 4/12; visible check green | 4/12; visible check red | Raw tie, but not equivalent: ordinary omitted the constructor default; staged omitted new-message buffer initialization and ordinary `add` calls raised `KeyError`. |
| Config Stack | 4/12; visible check red | 7/12; visible check red | Staged improved three executable groups but retained validation, supported-value, recursive provenance, replacement, and deletion defects. |
| Dependency Planner | 10/12; visible check red | 5/12; visible check red | Staged regressed five groups. It mixed string dependency IDs with `PlanTask` objects in completion state, breaking readiness, completion, and batching. |

These are task-specific executable case groups, not exchangeable benchmark
items. The 18/36 ordinary and 16/36 staged sums below are descriptive only.
One defect can cascade through several groups, as the Segment constructor
default demonstrates.

## Frozen replication decision

| Criterion | Required | Observed | Result |
|---|---|---|---|
| Ordinary non-ceiling tasks | at least 2 | 3 | pass |
| Tasks where staged is strictly higher | at least 2 | Config only | fail |
| Tasks where staged is lower | none | Dependency | fail |
| Staged cells reaching first submission | all 3 | all 3 | pass |

The package-level lead therefore **does not survive**. This closes the exact
preparer/workspace/fresh-actor/submit-review bundle. The result does not prove
that every possible staged method is harmful; it says this already-observed
package has failed its fresh replication and should not be decomposed or tuned
as if its Dispatch result were stable.

## Cost and custody metrics

| Method | Model calls | Prompt tokens | Completion tokens | Total tokens | Server duration (ms) | Environment/workspace actions | Rejected actions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ordinary | 53 | 382,355 | 19,772 | 402,127 | 1,075,587 | 53 | 9 |
| Staged hybrid | 96 | 776,518 | 21,925 | 798,443 | 1,285,713 | 93 | 2 |

Across this exact schedule, staged used:

- 98.6% more total tokens;
- 103.1% more prompt tokens;
- 81.1% more model calls;
- 75.5% more model-issued actions; and
- 19.5% more recorded server time.

The lower staged rejection count did not correspond to better construction.
This is another reminder that clean protocol admission is not task quality.
Config staged ended at 399,831 of the common 400,000-token ceiling.

First-submission and terminal candidate IDs were identical in all six cells.
The staged reviewers therefore caused zero artifact changes.

## Preparation did not reliably become construction

All three staged preparers read the complete task-facing blank package.
Together they produced four model-authored items, four revisions, and zero
exact captures.

- Segment's single item was unusually complete. It explicitly retained the
  default constructor, sequence, idempotency, conflicts, total consistency,
  completion, closure, capacity, ordering, discard, and isolation. The fresh
  actor still omitted `self._segments[message_id] = []`, received the exact
  resulting `KeyError` twice, and submitted unchanged.
- Config's first item retained many important validation, merge, deletion,
  lifetime, and copying requirements. The preparer then revised it four times
  into an increasingly generic implementation plan. The final item had lost
  most of the discriminating rules.
- Dependency's two items named package structure and generic topological
  behavior but did not externalize the representation invariant that
  dependencies are string IDs while task records are objects. The actor mixed
  those two domains in its implementation.

The package therefore failed at several different boundaries: useful
preparation could be ignored during construction, useful detail could be
discarded by the preparer itself, and a generic preparation could omit the
governing invariant. Presence of a stage or item is not evidence of useful
semantic continuity.

## Same-model submit review again produced false closure

The three staged candidates entered review after visible checks were still
red. The fresh reviewers emitted:

- 41 `supported` findings;
- zero `not_supported` findings; and
- zero `uncertain` findings.

The reviewed candidates then failed 20 external executable groups in
aggregate. Each actor immediately resubmitted the same candidate after review.
Concrete false certifications included the missing Segment buffer,
Config's invalid recursive/provenance behavior, and Dependency's broken
ready/blocked/complete/batches relations.

This replicates the scout's strongest negative result: the tested generic,
same-model, submit-time reviewer is not a semantic backstop. In this decision
environment it supplied confidence at closure without discriminating the
known-visible defects.

## What the model knew

The literal saved requests confirm that every actor received the complete task
contract. The model name, temperature, nonthinking policy, schema-action
contract, and action menu were preserved in each request. Staged preparers and
actors inspected the blank files; the external graders were never included in
model context.

The central failures were therefore not missing task transfer. They occurred
during semantic decomposition, representation choice, construction, use of
literal check feedback, and closure. That conclusion comes from the saved
prompts, outputs, actions, files, and receipts, not from group totals alone.

## Decision

Do not:

- promote or tune this staged package;
- isolate its preparer, fresh-context reset, workspace, or reviewer as though
  the compound benefit had replicated;
- add its workspace or reviewer to the stable harness;
- interpret fewer rejected actions as better work; or
- call ordinary generally superior from three deterministic pairs.

Retain:

- ordinary as the incumbent comparator;
- the stable custody/replay substrate;
- complete-method experiments as a useful broad exploratory unit;
- first-submission snapshots and terminal grading; and
- direct review of prompts, artifacts, action sequences, checks, and reviews.

The most defensible next move is not another staged-package microfactorial.
This lead has had its fresh replication and failed. Future broad exploration
should begin with a genuinely different complete decision ecology and a
specific work challenge, while leaving custody fixed.

See `DIRECT_TRAJECTORY_AUDIT.md` for the literal path audit and
`runs/staged-construction-replication-v0-run-001/analysis.json` for the
deterministic reduction.
