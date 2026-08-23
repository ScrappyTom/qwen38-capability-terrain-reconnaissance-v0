# Versioned Clause Action v0 — results

Date: 2026-08-12

Status: **complete; sequential micro construction stopped; recomposition not authorized**

## Outcome

The complete task-author clause packet worked better as one local construction
frame than as nineteen sequential one-clause actions.

| Measure | Compound | Versioned micro |
|---|---:|---:|
| Protocol-admitted calls | 6/6 | 19/19 |
| Final unit grades | 5 pass / 1 partial / 0 fail | 4 pass / 1 partial / 1 fail |
| Frozen clauses satisfied | 18/19 | 17/19 |
| Clause regressions after first satisfaction | n/a | 0 |
| Exact no-op preserved | 1/1 | 1/1 |
| Total tokens | 7,620 | 19,097 |
| Summed HTTP duration | 66.482 s | 166.272 s |

The micro condition improved zero paired units, tied the compound grade on five,
and made U004 worse. It used 2.5062 times the total tokens and 2.5010 times the
summed HTTP duration. It fails every positive branch of the frozen decision
rule. No recomposition was run.

These are six paired diagnostic units, not exchangeable benchmark samples. The
counts describe this fixture; they are not success-rate estimates.

## What each condition produced

### Compound

- U001 passed: it stated prespecified adjusted analysis, the correct estimate,
  interval, two-sided p-value, comparator, and handle.
- U002 passed: it removed causation, reported the exact association, disclosed
  nonrandom assignment and residual confounding, and retained `[M2]`.
- U003 was partial: it included the rates, low-rating nonresponse mechanism,
  raised observed mean, and correct direction, but changed the record's `can
  exaggerate` modality to the stronger `exaggerates`.
- U004 passed all four subgroup clauses and removed the original confirmed-
  effect claim.
- U005 passed all three measurement-limit clauses.
- U006 was preserved byte-for-byte.

### Versioned micro

- U001 passed after its first action copied the complete relevant record into
  the unit; its next two clause actions were exact no-ops.
- U002 passed. Its first action satisfied three of four clauses, its third added
  residual confounding, and two actions were exact no-ops.
- U003 remained partial. The first two actions correctly repaired direction and
  mechanism. The last two copied the imperative clause text into the artifact:
  `Report usable follow-up coverage...` and `State that mobile-clinic
  nonresponse...`. Those are editing instructions, not factual claims.
- U004 failed. Every listed clause appears, but the unit retained the original
  unsupported assertion that the subgroup `confirmed a larger completion
  effect` and then appended the contradictory statement that the estimates do
  not establish effect modification.
- U005 passed after three mutations.
- U006 was preserved byte-for-byte.

No satisfied clause was later removed. The failure was not memory loss in the
strict sense. It was failure to transform an active instruction into artifact
prose, plus preservation of a locally incompatible source assertion.

## Direct custody review

Every one of the 25 saved requests and raw responses was inspected, including
all nineteen intermediate unit versions. All responses had
`finish_reason: stop`, llama.cpp reported `truncated: false`, no response
contained a reasoning field, and every schema-bound basis version matched the
exact current unit.

Replay verified:

- 6/6 compound admissions;
- 19/19 micro admissions;
- zero rejections or skipped clauses;
- exact request reconstruction;
- exact result and transition hashes; and
- 26,717 total tokens across both conditions.

The run used the frozen nonthinking Qwen3.6-27B profile at temperature 0. There
were no tools, retries, host semantic decisions, adaptive clause changes, or
stable-workbench modifications.

## Interpretation

The tested sequential method is not a solution to compound semantic use. More
action boundaries did not make the same facts safer or more complete. They
made the artifact longer, created opportunities to copy meta-instructions into
the claim, and allowed an original contradiction to survive while a disclaimer
was appended.

The more useful observation is in the control: a complete, explicit local
clause packet plus the exact unit and exact bound record produced five complete
units and one narrow modality miss in one call each. This is materially closer
to the proposed tool-artifact direction than the prior single selected
obligation. But this experiment did **not** compare the complete packet with a
no-packet condition on the same fixture. Fixture differences prevent treating
the prior 1/6 or 3/6 results as that causal control.

The next defensible experiment is therefore not another sequential editor. It
is a fresh paired qualification of the upstream artifact itself:

1. exact unit + exact record + binding + full task; versus
2. the same packet plus the complete task-author local clause set;
3. one stateless construction call per unit in both conditions; and
4. no reviewer, selector, micro loop, semantic host, or recomposition.

That comparison asks whether the complete local contract adds value, rather
than whether repeated actions can rescue it. Clause wording or representation
should not be tuned until that value is isolated.

## Decision

- Stop `versioned_micro` v0; do not replicate or tune it.
- Retain exact version succession as custody evidence, not as a default model
  workflow.
- Do not mechanically recompose these outputs because neither condition met
  the frozen 6/6 threshold.
- Treat the one-call complete-clause packet as a prospective lead only.
- Keep `workbench/` and the model-server profile unchanged.

The full machine-readable adjudication is in `ADJUDICATION.json`; the immutable
requests, raw responses, results, transitions, manifests, endpoint inspection,
fixture copy, and model-profile copy are under
`runs/versioned-clause-action-v0-run-001/`.
