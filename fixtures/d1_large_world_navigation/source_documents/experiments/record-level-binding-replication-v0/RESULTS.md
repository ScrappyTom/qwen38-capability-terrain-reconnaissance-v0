# Record-level binding replication v0 - result

Date: 2026-08-12

Run: `record-level-binding-r00`

Freeze commit: `d3c8671`

## Outcome

All three frozen gates passed on the fresh estuary-aeration family.

| Boundary | Result | Frozen gate |
|---|---|---|
| Full-catalog selector | 6/6 gold records recalled; 7 candidates total; 8/8 protocol-admitted | **pass** |
| Record-relation producer | 6 TP, 10 TN, 0 FP, 0 FN; 16/16 protocol-admitted | **pass** |
| Selector + producer | six gold bindings admitted; one extra candidate rejected; no missed or negative binding | **pass** |
| Overall decision | all three gates passed | **advance to obligation-source comparison** |

This qualifies one record-level binding pipeline at an 8-claim by 12-record
scale. It does not show that a full catalog scales, that supporting quotations
are never useful, or that removing a quote caused the successful relations.

## What the model actually received

I directly inspected all eight saved selector requests and raw responses, the
shared complete record catalog, and all sixteen producer requests and raw
responses before grading.

Each selector call contained one exact claim and the same twelve complete
structural records. Claims and records carried artifact ID, whole-artifact
version, source path, section identity, byte range, exact text, and SHA-256;
records also carried literal current or superseded status. The catalog was
unranked and had no gist, relevance label, author binding, qualification pair,
expected relation, prior response, or downstream action.

Each producer call contained one exact claim, one complete record, and the
same assessment rule. Its response schema had only case ID, claim ID, record
ID, and relation. It had no quote, span, explanation, confidence, verifier,
edit, obligation, or submission field.

## Selector result

| Claim | Proposed records | Gold direct record | Finding |
|---|---|---|---|
| C:T4 | R:D8 | R:D8 | exact |
| C:W2 | R:S5 | R:S5 | exact |
| C:M7 | R:C2 | R:C2 | exact |
| C:H1 | R:G9 | R:G9 | exact |
| C:J6 | R:N4 | R:N4 | exact |
| C:P3 | R:M1 | R:M1 | exact |
| C:E8 | R:E3 | none | extra candidate; record explicitly says cost was not measured |
| C:B5 | none | none | exact empty set |

The selector recalled all six gold pairs and proposed seven of 96 possible
pairs. Candidate precision against direct gold was 6/7. The one extra is not a
false support finding: the selector contract defined candidates as records
worth exact assessment. The producer then rejected it as not direct support.

Pairwise assessment work for the operational candidate path was reduced by
89/96, or 92.7083%. This is a pair-count result only; no unrun exhaustive
latency or token total is inferred.

## Producer result

All sixteen fixed qualification pairs were protocol-admitted and correct:

- six direct pairs returned `direct_support`;
- ten high-risk negative pairs returned `not_direct_support`;
- no false positive or false negative occurred.

The negatives included:

- a 0.8 value and matching interval in seconds rather than dissolved oxygen;
- a superseded, uncalibrated oxygen estimate;
- a record that explicitly lacked cost data for the unsupported 13% claim;
- adult-fish and visual-survey records that could not support blue-crab
  abundance;
- a design/causality record paired with the unrelated salinity obligation;
- an operations ledger paired with a clogging-frequency claim; and
- a final oxygen estimate paired with the completeness/missingness claim.

The selector's seven proposed pairs were all among the frozen qualification
set. The producer admitted the six gold relations and rejected C:E8/R:E3, so
the pipeline output exactly matched the author binding set.

## Quantitative findings

### Selector

- calls: 8;
- protocol admitted: 8/8;
- gold-pair recall: 6/6;
- selected pairs: 7/96;
- candidate precision against direct gold: 6/7;
- unsupported-claim candidate pairs: 1;
- pair-assessment reduction: 92.7083%;
- prompt tokens: 25,942;
- completion tokens: 154;
- total tokens: 26,096;
- cached prompt tokens: 819;
- summed HTTP time: 58.051 seconds.

### Fixed producer qualification

- calls: 16;
- protocol admitted: 16/16;
- true positives: 6;
- false positives: 0;
- true negatives: 10;
- false negatives: 0;
- relation accuracy: 16/16;
- prompt tokens: 7,194;
- completion tokens: 646;
- total tokens: 7,840;
- cached prompt tokens: 2,144;
- summed HTTP time: 47.209 seconds.

### Recorded candidate-pipeline workload

This is the eight selector calls plus the seven already-recorded producer calls
for selector-proposed pairs. No response was rerun.

- calls: 15;
- prompt tokens: 29,100;
- completion tokens: 404;
- total tokens: 29,504;
- cached prompt tokens: 1,690;
- summed HTTP time: 77.515 seconds.

### Whole evidence run

- calls: 24;
- prompt tokens: 33,136;
- completion tokens: 800;
- total tokens: 33,936;
- cached prompt tokens: 2,963;
- summed HTTP time: 105.260 seconds.

## Interpretation

The record-only contract replicated the useful part of the preceding transfer
on a new domain and a somewhat larger catalog. Qwen located every direct
record, tolerated nonmonotonic positions, and distinguished all frozen direct
and adversarial negative pairs. The extra explicit-absence candidate behaved
as the architecture intended: candidate generation stayed recall-oriented and
the separate relation operation rejected it.

This is stronger evidence for the decomposition:

```text
exact claim + complete record catalog
-> candidate records
-> exact claim-record relation
```

It does not establish that the full catalog is an economical model-facing
view. The selector consumed 26,096 of the run's 33,936 tokens because all
twelve exact records were repeated for eight stateless claims. Gists,
retrieval tools, or automatic slicing were not tested and are not earned by a
failure here; there was no recall failure at this size.

Removing the quote field avoided asking the model to create a second, narrower
source representation. Because this was a fresh qualification rather than a
matched quote/no-quote contrast, the result does not prove that quote removal
caused better performance. It qualifies the simpler record-level interface
for the next source-isolated stage.

## Decision

- Retain exact structural records as the citation objects for this research
  line.
- Retain candidate selection and relation judgment as separate model roles or
  operations; neither output becomes host semantic truth.
- Advance to the prospectively separate obligation-source comparison.
- Do not add a supporting-quote requirement, verifier, gist, retrieval tool,
  host relevance, edit relay, recomposition, or stable-workbench dependency
  from this result.
- Continue to preserve task-author gold only as experimental control and
  offline grading evidence.

## Validation

- freeze committed and pushed before calls at `d3c8671`;
- endpoint identity: llama.cpp `b10331-7ba604f1c`, alias
  `qwen36-27b-iq2-coding`, 50,176 context;
- saved-run replay verification: passed;
- direct review: 8 selector requests/responses and 16 producer
  requests/responses;
- semantic grading was added only after the model run;
- full local suite: 401 tests passed with 14 expected skips;
- targeted Ruff, JSON, Markdown-link, and Git whitespace validation: passed.

During result documentation, appending the outcome to the contract file caused
replay to reject its changed SHA-256. The post-run addition was removed and the
frozen contract remains byte-identical; outcome prose lives in this result and
the mutable governing status documents.

This is local validation, not GitHub Actions verification.
