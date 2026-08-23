# Direct transcript audit

Run: `2026-08-23-capability-terrain-v0`

Freeze: `f3092c73065353d5fbdb4c3646632b6586c7e50b`

This document records literal actor behavior. It does not repair malformed
responses or infer hidden reasoning.

## D1 — large-world atlas discovery

| Call | Literal intended expression | Admission | Effect |
|---:|---|---|---|
| 1 | `[{"action":"atlas_root"}]` | rejected: response was an array | none |
| 2 | `atlas_root` | accepted | root catalog delivered next call |
| 3 | `atlas_expand(ROOT, 0)` plus closing tags | rejected: extra JSON data | none |
| 4 | same expansion plus closing tags | rejected: extra JSON data | none |

The candidate remained the 545-byte draft memo. The external memo evaluator
failed for unchanged target, 54 body words, and no evidence links.

## D2 — evidence-bound paper revision

| Call | Action | Admission/effect |
|---:|---|---|
| 1 | `tree(.)` | accepted |
| 2 | read `paper.md` | accepted; exact paper delivered call 3 |
| 3 | read `evidence_update.md` | accepted; delivered call 4 |
| 4 | read `editorial_memo.md` | accepted; delivered call 5 |
| 5 | replace complete `paper.md` | accepted; candidate changed to `6e637d…`; effect delivered call 6 |
| 6 | run visible check | accepted; current pass delivered call 7 |
| 7 | submit | accepted; terminal |

The hidden machine grader passed 14 of 16 cases. Independent semantic review
overrode one lexical false negative but retained one real partial criterion:
Discussion omitted the complete-case/no-imputation basis of the upward-bias
qualification. Final disposition: 12 met, one partial, `not_ready`.

## D3 — coverage-window calibration

Calls 1–7 each emitted a fenced `tree(.)` object and were rejected as invalid
JSON. Call 8 emitted the same object bare and was accepted. No file was read,
no mutation occurred, and the starting external failure remained.

## D4 — device-event folding

| Call | Literal intended expression | Admission |
|---:|---|---|
| 1 | fenced `tree(.)` | rejected |
| 2 | `tree(.)` | accepted |
| 3 | fenced target read | rejected |
| 4 | read `src/fold-device-events.mjs` | accepted |
| 5 | read `docs/device-events.md` | accepted |
| 6 | test read plus extra brace | rejected |
| 7 | same | rejected |
| 8 | same plus closing tags and duplicate object | rejected |
| 9 | same plus extra brace | rejected |

The target remained unchanged and failed both the inherited evaluator and the
plain-object supplement.

## D5 — deployment-wave planning

| Call | Action | Admission/effect |
|---:|---|---|
| 1 | `tree(.)` | accepted |
| 2 | read contract | accepted |
| 3 | read target | accepted |
| 4 | duplicated/tagged test read | rejected |
| 5 | read visible test | accepted |
| 6 | replace complete target | accepted; candidate changed to `d6debc…`; effect delivered call 7 |
| 7 | run `npm_test` | accepted; three visible tests passed and result delivered call 8 |
| 8 | submit four-section final response | accepted; response contract passed |

The external artifact evaluator passed seven of eight checks. It found that a
disabled service required by dependency closure was not rejected. Final
disposition: changed strong-partial artifact and premature submission.

## D6 — exact current-state reentry

D2 was selected mechanically because it was the first changed D2–D5 candidate.
The D6 candidate ID exactly equaled D2's final candidate ID.

| Call | Literal intended expression | Admission |
|---:|---|---|
| 1 | fenced submit of current paper | rejected |
| 2 | fenced submit of current paper | rejected |
| 3 | same submit, bare JSON | accepted |

No read, check, or mutation occurred. D6 submitted the exact unchanged 12/13
D2 paper. This is a premature resubmission under the frozen semantic rubric.

## Aggregate expression failures

| Failure shape | Count |
|---|---:|
| Markdown-fenced otherwise plausible object | 11 |
| Extra brace, closing tag, or duplicated object | 7 |
| Array instead of object | 1 |
| Total rejected responses | 19 |

The host made no repair and issued no retry. All rejected calls remain part of
the measured behavior and resource accounting.

## Exact delivery and effect facts

- Every result marked delivered appeared in a later model request.
- D2's mutation effect crossed into call 6; its current visible-check result
  crossed into call 7.
- D5's mutation effect crossed into call 7; its current visible-check result
  crossed into call 8.
- Terminal submit results, by definition, did not cross another model boundary.
- No result body was demoted, no reopen occurred, and no prompt exceeded the
  20,992-token ceiling.
- All 39 completed calls have exactly one `provider-attempt-1` directory and
  no later attempt.
