# Balanced submission review v0 — result

Date: 2026-08-12

Decision: **qualification failed; no builder branch was run**

## Outcome

The balanced assessor returned one schema-valid response for all four fresh
qualification units. It classified both supported controls as `entailed` and
the direct sign inversion as `contradicted`. It classified the unsupported
bird-abundance claim as `contradicted` rather than the frozen
`undetermined` relation.

| Unit | Expected | Observed | Direct assessment |
|---|---|---|---|
| U001 wait estimate | entailed | entailed | Correct exact estimate and interval comparison |
| U002 wait direction | contradicted | contradicted | Correct sign and shorter/increased comparison |
| U003 coverage | entailed | entailed | Correct two-value and difference comparison |
| U004 bird abundance | undetermined | contradicted | Correctly recognized no support, then overclaimed contradiction |

The frozen gate required all four relation labels and explanations to be
correct. It therefore failed. The home-energy fixture was never sent to the
builder or assessor, and neither receipt-only nor assessment continuation
exists.

## What the exact output says

For U004 the assessor wrote that Q3 contains no abundance estimate and that
the doubling claim “cannot be supported.” That part is correct. It then said
the claim “conflicts with the absence of data” and emitted
`relation: contradicted`. Absence of an estimate does not establish the
opposite real-world outcome. Under the frozen definitions, no conflict was
identified and the claim is unresolved, so the proper label is
`undetermined`.

This is not a protocol or schema-admission failure. The response was complete,
bound to the exact review ID, covered every unit exactly once, used only each
unit's available evidence IDs, and needed no repair. It is a semantic
distinction failure between contradiction and lack of support.

The earlier asymmetric judge's supported-control inversion did not recur.
Positive evidence now had an explicit action and both positive controls were
labeled correctly. Balanced expressivity fixed that observed structural
failure but did not qualify the three-way epistemic taxonomy.

## Quantitative record

- model calls: 1;
- exact units: 4;
- structurally admitted responses: 1;
- correct relation labels: 3 of 4;
- entailed controls: 2 of 2 correct;
- direct contradictions: 1 of 1 correct;
- undetermined controls: 0 of 1 correct;
- prompt tokens: 1,260;
- completion tokens: 596;
- total tokens: 1,856;
- model call duration: 29,503 ms; and
- prospective builder calls: 0.

These four deliberately different controls qualify one fixed mechanism; they
are not a reliability or population estimate.

## Custody and direct review

The apparatus was committed at
`84488d391daa6b7f70fe9e3f60ae89cd9c45b284` before the call. The saved request
hash is `fdbcf7b26e3fa9cb1c01ea904cf3f2c030373f78891887aec27f6a6095110fd1`;
the raw response hash is
`4960c77668ddbe56793ff75c707b4d9cf8b4fcdf9e299b6c8799e5fa4d441723`.
The call used the pinned b10331 nonthinking endpoint and temperature-zero
request. Offline verification rebuilds the packet and request byte for byte,
reinterprets the raw response, checks both hashes, and checks the saved model
alias.

The investigator read the complete request, packet, raw response, admitted
assessment, artifact, and evidence—not just the summary counters.

## Decision and earned next question

Stop this three-relation v0. Do not change the U004 label, retry the call,
reword the same case, or run the prospective branches under the failed gate.

The output does support one narrower hypothesis. For a builder deciding
whether to inspect or revise, both contradiction and unresolved support mean
the same limited fact: the cited records do not support the unit as written.
A balanced per-unit relation of `supported` versus `not_supported` would avoid
claiming a stronger epistemic distinction than the assessor demonstrated. It
would still have no overall verdict, host semantic authority, gate, or
recommended action.

That binary relation is a new model-facing contract and must receive a new
qualification on fresh controls before any relay. It is not authorized by
relabeling this run after the fact.
