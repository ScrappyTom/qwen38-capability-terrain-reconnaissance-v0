# Candidate-pair recall transfer v0 — result

Date: 2026-08-12

Run: `candidate-pair-recall-r00`

Freeze commit: `810d34a`

## Outcome

The model-owned selector passed. The unchanged producer classified all 48
relations correctly but failed its stricter quote-adequacy gate on one positive
case. The selected candidate pipeline passed its literal relation-admission
gate, but the frozen overall decision does not authorize a larger experiment
because the producer did not pass every clause.

| Boundary | Result | Frozen gate |
|---|---|---|
| Full-corpus candidate selector | all 5 gold pairs selected; 5 total candidates; unsupported claim selected none | **pass** |
| Unchanged atomic producer | 5 TP, 0 FP, 43 TN, 0 FN; 5/5 quotes exact; 4/5 quotes adequate | **fail** |
| Selector + producer pipeline | 5 gold bindings, 0 negative bindings, 0 selected-pair protocol rejections | **pass** |
| Overall advancement | producer quote clause failed | **stop** |

This is not a failed relation-discrimination result. It is a perfect relation
matrix plus one incomplete supporting-span choice. The distinction matters
because the candidate, binding, and source-span objects should not be treated
as one capability.

## What the model actually received

I inspected all six saved selector requests and raw outputs, then all 48 saved
producer requests and raw outputs against the exact claims, complete records,
and author key.

Each selector call contained:

- one exact claim with artifact ID `A:claims`, whole-artifact SHA-256 version,
  source path, section, byte range, exact text, and text hash;
- the same complete unranked eight-record catalog;
- for every record, artifact ID `A:source-corpus`, whole-artifact SHA-256
  version, source path, section, literal current/superseded status, byte range,
  complete text, and text hash; and
- no gist, rank, relevance label, gold binding, rationale, prior selection, or
  downstream action.

Correct record positions were deliberately nonmonotonic: 6, 4, 8, 2, and 7
for the five supported claims. Every selector call was stateless. All six
responses were protocol-admitted.

The producer then received all 48 claim-major, record-major pairs independently
through the byte-pinned Stage-2 prompt, rule, schema, and settings. It never
saw selector output, artifact-catalog metadata, author gold, another pair, or
an editor.

## Selector result

| Claim | Proposed records | Gold direct record | Correct record position |
|---|---|---|---:|
| C:R8 | S:D3 | S:D3 | 6 |
| C:L2 | S:A7 | S:A7 | 4 |
| C:Q5 | S:H4 | S:H4 | 8 |
| C:B1 | S:M6 | S:M6 | 2 |
| C:N9 | S:V2 | S:V2 | 7 |
| C:F4 | none | none | — |

The selector therefore had 5/5 gold-pair recall, selected 5 of 48 possible
pairs, selected nothing for the unsupported claim, and reduced pairwise
assessment work by 43/48, or 89.5833%.

## Complete producer matrix

`D` means `direct_support`; `N` means `not_direct_support`. Every cell matches
the frozen author matrix.

| Claim \ Record | S:J9 | S:M6 | S:P1 | S:A7 | S:K8 | S:D3 | S:V2 | S:H4 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C:R8 | N | N | N | N | N | D | N | N |
| C:L2 | N | N | N | D | N | N | N | N |
| C:Q5 | N | N | N | N | N | N | N | D |
| C:B1 | N | D | N | N | N | N | N | N |
| C:N9 | N | N | N | N | N | N | D | N |
| C:F4 | N | N | N | N | N | N | N | N |

This includes correct rejection of the 18.4-second notification-latency record
for the 18.4-minute arrival claim, the superseded 21.7-minute preliminary
record, all cross-claim topical neighbors, and the explicit no-energy-data
record for the unsupported 11% bill claim.

## Supporting quotes

All five positive quotes were exact substrings. Four covered every material
claim element.

| Pair | Exact | Adequate | Finding |
|---|---:|---:|---|
| C:R8 × S:D3 | yes | **no** | Quote contained request-to-arrival, 18.4 minutes, and the CI, but omitted `Final audited dispatch analysis: on declared heat-alert days`. |
| C:L2 × S:A7 | yes | yes | Covered subgroup, follow-up, percentage, repeat use, and heat-alert days. |
| C:Q5 × S:H4 | yes | yes | Covered high-demand longer-wait missingness and downward wait-time bias. |
| C:B1 × S:M6 | yes | yes | Covered voluntary enrollment, 14%, comparison, and noncausal limit. |
| C:N9 × S:V2 | yes | yes | Covered exact absence of indoor-temperature measurement. |

For C:R8, the complete record directly supports the complete claim and the
relation label is correct. The selected substring is nevertheless incomplete
under the frozen rule. The host did not widen it to the whole record or attach
the omitted prefix.

## Quantitative findings

### Selector

- calls: 6;
- protocol admitted: 6/6;
- selected pairs: 5/48;
- gold-pair recall: 5/5;
- candidate pair precision against direct gold: 5/5;
- unsupported-claim candidates: 0;
- pair-assessment reduction: 89.5833%;
- prompt tokens: 13,455;
- completion tokens: 163;
- total tokens: 13,618;
- cached prompt tokens: 585;
- summed HTTP time: 44.357 seconds.

### Exhaustive producer

- calls: 48;
- protocol admitted: 48/48;
- relation accuracy: 48/48;
- true positives: 5;
- false positives: 0;
- true negatives: 43;
- false negatives: 0;
- exact positive quotes: 5/5;
- semantically adequate positive quotes: 4/5;
- prompt tokens: 22,548;
- completion tokens: 2,094;
- total tokens: 24,642;
- cached prompt tokens: 9,475;
- summed HTTP time: 161.365 seconds.

### Candidate pipeline workload

The counterfactual pipeline cost is the six recorded selector calls plus the
five already-recorded producer calls for selected pairs. No call was rerun.

- calls: 11;
- prompt tokens: 15,805;
- completion tokens: 532;
- total tokens: 16,337;
- cached prompt tokens: 1,580;
- summed HTTP time: 68.021 seconds;
- versus exhaustive producer: 77.0833% fewer calls, 33.7026% fewer tokens,
  and 57.8465% less summed HTTP time.

### Whole evidence run

- calls: 54;
- prompt tokens: 36,003;
- completion tokens: 2,257;
- total tokens: 38,260;
- cached prompt tokens: 10,060;
- summed HTTP time: 205.722 seconds.

## Interpretation

At this small corpus size, upstream availability and candidate formation were
not the limiting problem. Qwen used a complete exact artifact inventory to
select the five correct records with no distractors, despite permuted positions
and strong lexical traps. The unchanged atomic producer then separated every
direct and negative pair correctly. This is stronger evidence than the earlier
hand-selected pair family that the relation operation can transfer.

It does not show that full-corpus prompting scales. The selector repeated all
eight complete records six times and consumed 13,618 tokens before any pair
judgment. Although the resulting 11-call pipeline was cheaper than 48
exhaustive producer calls, a larger corpus would make repeated full views
increasingly expensive. No gist or retrieval tool is earned from a capacity
failure here; those remain possible operands for a deliberately larger scale
test, not defaults.

The only strict failure was source-span sufficiency. The evidence record was
already an exact paragraph with document, version, section, range, and hash.
The model correctly bound that whole record, then chose a narrower literal
quote that dropped two qualifiers. This suggests three distinct objects:

```text
candidate pair
→ claim-to-record relation
→ supporting subspan, only when the record unit is too broad
```

Requiring a model-authored quote on every already-atomic record may be
redundant; removing it would change the contract and cannot be done
retroactively. Conversely, if subspan citation is required, its completeness
must be qualified separately. Exact record custody does not make a narrow
quote exhaustive.

## Decision

- Retain the exact artifact inventory and model-owned selector as positive
  bounded evidence, not a default harness view.
- Retain the 48/48 relation matrix as positive transfer evidence.
- Record the unchanged producer as failing its full precommitted gate because
  quote adequacy was 4/5.
- Record the candidate pipeline as passing its literal relation-admission gate,
  but do not advance to a larger-corpus/tool experiment under this freeze.
- Do not add gists, retrieval tools, host relevance, retries, quote widening,
  another verifier, downstream editing, obligation selection, or
  recomposition from this result.
- Before another behavioral call, decide offline whether an exact atomic
  evidence record is itself the citation unit or whether a separately
  qualified supporting-subspan object is required. Any changed contract must
  use a fresh task.

## Validation

- freeze committed and pushed before calls at `810d34a`;
- endpoint identity: llama.cpp `b10331-7ba604f1c`, alias
  `qwen36-27b-iq2-coding`, 50,176 context;
- saved-run replay verification: passed;
- full local suite after evidence: 386 tests with 14 expected skips;
- targeted Ruff, JSON, exact-span, prompt-hash, no-gold-leak, and no-relay
  validation: passed;
- `git diff --check` reports source-preserved blank lines at EOF in the six
  exact fixture copies inside the saved run. Those bytes are replay-bound and
  were not rewritten after evidence collection; no other whitespace warning
  remains.

This is local validation, not GitHub Actions verification.
