# Reviewer frame factorial v1 — results

Date: 2026-08-12

Decision: **responsibility-scope action lead; automated assessor unqualified; no promotion**

## Result in plain language

This experiment produced two distinct results.

First, the model-authored exhaustive-binding assessor failed its one-shot gate.
It correctly labeled all four sections, and its target explanation explicitly
recognized missing H1 and H3 relationships, but its authoritative applicable-ID
field copied only the target's existing H4 citation and also omitted H2. The
four editor cells tied to that assessor were therefore not run.

Second, a separately frozen calibration supplied the already frozen fixture
ground truth as an explicitly fixture-authored assessment. With task, evidence,
candidate, assessment, actions, model, and settings held fixed:

- both whole-artifact editors read everything, checked, and finalized without
  editing; and
- both Policy-Implications-only editors read everything, reread the target,
  edited it, checked the new candidate, and finalized it.

The initial passed-check receipt did not determine whether an edit occurred.
Assigned responsibility scope did on this fixture. This differs from the first
factorial's S1-only pattern and makes the receipt interaction look unstable.

Neither bounded artifact is a clean exact-binding completion. S0 omitted H3.
S1 expressed H1 and H3 as `[H1, H3]`, a conventional human-readable combined
citation that is not one of the frozen exact handles recognized by the literal
custody parser. Both are therefore reported as improved but partial under the
pre-existing exact-handle policy.

## Stage 1: model-authored assessor gate

The assessor request was complete, schema-constrained, and successful at the
protocol level. Its relation labels were 4/4 correct and its applicable-ID sets
were 3/4 exact.

| Unit | Expected applicable records | Returned | Relation |
|---|---|---|---|
| U001 Summary | H1, H2, H3 | H1, H2, H3 | correct |
| U002 Findings | H2, H4 | H2, H4 | correct |
| U003 Caveats | H1, H3, H4 | H1, H3, H4 | correct |
| U004 Policy Implications | H1, H2, H3, H4 | H4 | correct `not_supported` |

Every returned applicable set exactly matched that unit's existing literal
citation set. For U004, the explanation nevertheless said H1 and H3 were
applicable and missing. It did not identify H2 as applicable to the adjusted
association. Thus useful comparison appeared in prose but was not transferred
to the new authoritative field.

The call used 2,231 prompt, 940 completion, and 3,171 total tokens and took
47.304 seconds. The verified stop and direct inspection are recorded in
`QUALIFICATION_RESULT.md`. No assessor retry or editor call followed that
failed gate.

## Stage 2: fixture-assessment calibration

The calibration used the same exact unused editor source state. No assessor was
called. The assessment was generated mechanically from the committed
`gold_assessment_template.json`, labeled `fixture_ground_truth`, and bound to
the existing review identity.

All 32 editor responses were complete schema actions and were admitted without
normalization or retry.

| Condition | Action path | Mutation | Terminal target binding surface |
|---|---|---:|---|
| W0 whole, no receipt | evidence; four sections; check; finalize | 0 | `[H4]` |
| W1 whole, pass receipt | evidence; four sections; check; finalize | 0 | `[H4]` |
| S0 bounded, no receipt | target; three other sections; evidence; target; replace; check; finalize | 1 | `[H2] [H1] [H4]`; H3 absent |
| S1 bounded, pass receipt | target; three other sections; evidence; target; replace; check; finalize | 1 | `[H2] [H1, H3] [H4]` |

W0 and W1 emitted byte-identical assistant action content on all seven turns.
S0 and S1 emitted byte-identical action content through the first six turns;
their only substantive divergence was the replacement body at turn seven.
Both then emitted the same `check` and `finalize` actions.

The receipt therefore had no observed effect on action selection, acquisition
order, mutation timing, checking, or finalization. It affected one citation
serialization inside the bounded replacement.

## Direct artifact adjudication

All four terminal artifacts preserve the locked Context, Methods, and
References bytes. No factual or inferential regression was found. Requirements
1 through 5 remain satisfied in every artifact.

W0 and W1 preserve the original target defect: Policy Implications makes H1,
H2, and H3-dependent claims while binding only H4.

S0 accurately adds the confidence interval and p-value with H2 and preserves
the selection and subgroup interpretations. It puts H1 after a sentence that
also invokes differential geocoding, so the H3-dependent claim remains
unbound. Exact target coverage improves from one of four records to three of
four.

S1 accurately adds H2 and writes `[H1, H3]` after the selection/geocoding
sentence. Its intended record mapping is semantically transparent and all
facts are faithful. However, the frozen citation extractor recognizes only
individual handles matching `[H1]`, `[H2]`, `[H3]`, or `[H4]`; it does not
interpret `[H1, H3]` as two bindings. Under that exact policy, the target has
only H2 and H4 plus one undeclared combined token and remains partial.

The experiment did not specify whether combined bracket lists were permitted.
This ambiguity is reported rather than resolved after seeing the output. No
parser expansion, normalization, or special grader case was added.

Across the calibration:

- 4/4 conditions finalized;
- 2/4 mutated Policy Implications;
- 2/4 improved the target artifact;
- 0/4 are unambiguous exact-binding completions; and
- 4/4 ran a fresh check before finalization.

These are condition descriptions from one non-exchangeable fixture, not
success-rate estimates.

## Quantitative observations

| Measure | W0 | W1 | S0 | S1 | Total |
|---|---:|---:|---:|---:|---:|
| Calls / admitted actions | 7 | 7 | 9 | 9 | 32 |
| Candidate mutations | 0 | 0 | 1 | 1 | 2 |
| Protocol rejections | 0 | 0 | 0 | 0 | 0 |
| Execution rejections | 0 | 0 | 0 | 0 | 0 |
| Prompt tokens | 21,023 | 22,445 | 29,464 | 31,282 | 104,214 |
| Completion tokens | 79 | 79 | 309 | 312 | 779 |
| Total tokens | 21,102 | 22,524 | 29,773 | 31,594 | 104,993 |
| Cached prompt tokens | 16,917 | 18,707 | 24,976 | 26,599 | 87,199 |
| Summed HTTP duration | 13.999 s | 13.418 s | 26.312 s | 26.559 s | 80.288 s |

## What this changes

The clean within-fixture result is not merely that a shorter view helped. The
bounded editors acquired all four editable sections and the complete evidence
file, just as the whole-artifact editors did. The difference was their assigned
responsibility and resulting action sequence:

```text
whole responsibility:
evidence → all sections → passed check → finalize unchanged

bounded responsibility:
target → other sections → evidence → target again → edit → passed check → finalize
```

The same correct information was inert under whole-artifact responsibility and
actionable under target responsibility. That is evidence that the task/action
frame can govern whether recognized evidence crosses into mutation, even when
information acquisition is not narrower.

Across the two factorial fixtures, bounded S1 edited both times. Receipt
visibility did not replicate as a necessary factor: with a complete assessment
here, S0 edited too. The strongest current lead is therefore bounded assigned
responsibility, not a visible passed-check receipt.

The failed assessor also narrows the upstream problem. Asking for one exhaustive
section-level relation list did not solve binding synthesis; the model copied
the existing literal list even while explaining missing relationships. If an
automated assessment artifact is pursued, the next earned question is whether
one exact claim per assessment unit can preserve claim-to-record bindings
without a section-level aggregation step. That would be another removable
experiment, not a harness feature.

## Decision

Do not add a permanent bounded-work surface, hide or emphasize passed checks,
promote a reviewer stage, accept combined citations by normalization, or put
fixture-authored semantics into the harness.

Retain three findings:

1. exact scope assignment changed action on this new fixture;
2. initial receipt visibility did not robustly control action; and
3. section-level exhaustive binding output remains unqualified as an automated
   upstream artifact.

The stable custody and schema-action substrate requires no change.
