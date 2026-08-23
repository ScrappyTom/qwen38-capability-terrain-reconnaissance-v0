# Semantic-clause geometry v0 - held-out result

Date: 2026-08-13

Status: **complete but formally ineligible; no contrast passed or failed and no
model-facing view is promoted**.

## Question

The dependency-topology study showed that a task-author coverage
specification could improve high-fan-in synthesis, but that treatment added a
semantic decomposition, separate clauses, evidence bindings, and an output
obligation role at once. This study held the clause strings, clause IDs,
bindings, exact sources, current target, task, action contract, model profile,
and response allowance fixed while separating:

1. semantic decomposition: `integrated_account` versus `exact_source`;
2. clause individuation: `independent_items` versus `integrated_account`; and
3. obligation role: `output_obligations` versus `independent_items`.

The independent and obligation projections differed only in one `kind` value.
There was no retrieval, tool use, retry, feedback, prior history, or automated
semantic grader.

## Formal decision

The preregistered experiment required at least three of four held-out worlds
to instantiate the untreated phenotype:

- the exact-source artifact fully preserves the central missingness mechanism
  and direction;
- at least two of seven secondary distinctions are less than fully preserved;
  and
- the artifact meets the 165-word contract.

Only `H-WATER` qualified. All three contrasts are therefore **ineligible**.
The single eligible world's win/loss values are retained in `analysis.json`,
but they cannot pass or fail a prospective hypothesis.

| World | Exact-source central | Secondary items incomplete | Word limit | Eligible |
|---|---:|---:|---:|---:|
| Library returns | met | 1 | fail (178 words) | no |
| Leak repair | met | 5 | pass (155 words) | yes |
| Court reminders | partial | 6 | pass (74 words) | no |
| Irrigation advisories | partial | 6 | pass (65 words) | no |

This is not a null result. It is an invalidated confirmatory comparison: the
held-out controls did not provide enough instances of the state the treatment
was designed to address.

## Descriptive outcomes only

Human semantic points use the frozen meaning rubric (`met = 2`, `partial = 1`,
`not_met = 0`) and exclude the separate provenance criterion. The totals below
span eligible and ineligible worlds and therefore do not replace the formal
gate.

| Condition | Semantic points | Provenance fully met | Word limit met | Total tokens | Token delta vs exact |
|---|---:|---:|---:|---:|---:|
| Exact source | 40/64 | 2/4 | 3/4 | 4,827 | - |
| Integrated account | 58/64 | 3/4 | 4/4 | 6,390 | +32.38% |
| Independent items | 55/64 | 2/4 | 4/4 | 6,740 | +39.63% |
| Output obligations | 56/64 | 3/4 | 4/4 | 6,764 | +40.13% |

The content-equivalent pairwise pattern across all four worlds was:

- integrated account versus exact source: 3 higher, 1 tie;
- independent items versus integrated account: 1 higher, 1 tie, 2 lower; and
- output obligations versus independent items: 1 higher, 1 tie, 2 lower.

These counts are descriptive because three worlds failed qualification. They
do not support a claim that an integrated account dominates, but they do
weaken the expectation that separate item containers or an obligation label
are generally sufficient causes of the earlier semantic-frame gain.

## What the exact outputs show

The investigator inspected every complete saved request, raw response, and
artifact after the independent blind review was sealed.

### Untreated behavior was not stable enough for the intended comparison

The library artifact copied nearly the full evidentiary account, scored 15/16,
and exceeded the word limit. It was too complete and too long to instantiate
central-gist compression.

The water artifact instantiated the intended failure: it preserved the broad
attenuation direction while omitting design, timing, arm-level numerical
detail, and no-imputation status. It also cited the rainfall distractor and
converted a possible bias into a likely reduction of a supposed "true effect
size."

The court and farm artifacts compressed much more severely. Both omitted the
assigned-population estimand, coverage and adjustment details, much numerical
context, the intermediate mean/rate-shift mechanism, and uncertainty. Their
central rubric was only partial, so they were semantic-content rescue cases,
not qualified tests of secondary-detail retention after a correct central
interpretation.

### Correct decomposition helped descriptively, but representation did not order reliably

All three semantic conditions received the same eight task-author clause
strings and bindings. They restored much of the missing design, numerical,
coverage, subgroup, and mechanism content in the court and farm worlds. The
integrated account produced the highest descriptive total and was equal to or
better than independent items in three of four worlds.

The obligation role did not reliably add coverage. It beat neutral items only
on water, tied on court, and scored lower on library and farm. In court, the
neutral-item and obligation artifacts were substantively almost the same. A
one-field role declaration did not generally cause the clauses to bind more
strongly to the output.

Semantic material also did not eliminate transformation errors. Several
artifacts strengthened `can attenuate` or `can exaggerate` into a categorical
claim even though the exact clause preserved possibility and unknown
magnitude. The integrated library artifact cited an irrelevant precipitation
record; the independent water artifact cited rainfall. Exact bindings did not
guarantee discriminating provenance.

## Interpretation

This experiment successfully isolated the treatment-side variables but failed
to qualify enough task-side controls. Its strongest defensible update is:

> A correct external semantic decomposition can make materially more source
> distinctions survive a bounded synthesis, but this run does not establish
> that separate item objects or an obligation role cause the improvement.

That update is consistent with the earlier oracle-positive controls and with
the later negative line/ID and role/binding factorials. It does not establish
a deployable semantic-state object, because the task author supplied the
correct clauses. It also does not show that a model or reviewer can create a
faithful clause set.

## Decision and next boundary

- Promote no card, compiler, obligation surface, or default semantic view.
- Do not tune these four held-out worlds or reinterpret the one eligible cell
  as a passed experiment.
- Stop treating surface itemization or role labeling as the leading causal
  explanation of the old 20/22 and 21/22 results.
- Preserve integrated semantic decomposition as an oracle positive control,
  not as host-owned truth.
- If this contrast is revisited, qualify a bank using untreated baseline calls
  and blind review **before any treatment calls are made**. Freeze only worlds
  with central meaning intact, at least two secondary losses, and a valid
  output contract; then expose the unseen treatments. Such a study estimates
  treatment effects conditional on a known baseline failure phenotype, not
  the prevalence of that phenotype.

The apparatus remains outside `workbench/`; deleting this experiment removes
it without changing the stable harness.

## Evidence

- Frozen design: [`FREEZE.md`](FREEZE.md)
- Predictions: [`PREDICTION_REGISTER.md`](PREDICTION_REGISTER.md)
- Review contract: [`REVIEW_PROTOCOL.md`](REVIEW_PROTOCOL.md)
- Direct custody/process audit: [`AUDIT.md`](AUDIT.md)
- Deterministic reduction:
  [`runs/semantic-clause-geometry-v0-run-001/analysis.json`](runs/semantic-clause-geometry-v0-run-001/analysis.json)
- Sealed blind review:
  [`runs/semantic-clause-geometry-v0-run-001/blind/semantic-reviews.sealed.json`](runs/semantic-clause-geometry-v0-run-001/blind/semantic-reviews.sealed.json)
- Exact run summary:
  [`runs/semantic-clause-geometry-v0-run-001/summary.json`](runs/semantic-clause-geometry-v0-run-001/summary.json)
