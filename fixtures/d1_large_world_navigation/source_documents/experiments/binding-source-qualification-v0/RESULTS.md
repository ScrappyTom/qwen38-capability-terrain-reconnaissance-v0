# Binding-source qualification v0 - result

Date: 2026-08-12

Run: `binding-source-r00`

Freeze commit: `bf2e9de`

## Outcome

The atomic producer passed the precommitted qualification gate on this fresh
fixed family. The independent verifier did not.

| Method | Positive bindings | Negative bindings | Other | Gate |
|---|---:|---:|---:|---|
| Atomic producer | 8/8 recovered | 0/8 false positives | 8/8 positive quotes exact and adequate | **pass** |
| Independent verifier | accepted 15 correct proposals | rejected 1 correct proposal | 0 abstentions; no incorrect producer proposal occurred | **fail** |
| Producer + verifier | 8/8 positives admitted | 0/8 negatives admitted | K012 unresolved after verifier rejection | **inconclusive gate** |

This is a qualification result for one exact producer method on one fixed pair
family. It is not evidence that model-created bindings are authoritative, that
a verifier is useful, or that the method transfers to corpus search, record
selection, editing, code, or a complete research trajectory.

## Complete matrix

| Case | Frozen class | Gold | Producer | Verifier | Combined binding |
|---|---|---|---|---|---|
| K017 | direct numeric | direct | direct | accept | admitted |
| K004 | wrong measure | not direct | not direct | accept | none |
| K029 | direct repair time | direct | direct | accept | admitted |
| K011 | incomplete numeric detail | not direct | not direct | accept | none |
| K023 | direct subgroup | direct | direct | accept | admitted |
| K006 | subgroup/overall mismatch | not direct | not direct | accept | none |
| K031 | direct absence boundary | direct | direct | accept | admitted |
| K014 | absence presented as no effect | not direct | not direct | accept | none |
| K002 | direct current revision | direct | direct | accept | admitted |
| K027 | superseded presented as final | not direct | not direct | accept | none |
| K009 | direct bias polarity | direct | direct | accept | admitted |
| K020 | reversed bias polarity | not direct | not direct | accept | none |
| K035 | direct survey result | direct | direct | accept | admitted |
| K012 | genuine no support | not direct | not direct | **reject / protocol rejection** | unresolved |
| K025 | direct observational qualification | direct | direct | accept | admitted |
| K001 | observational evidence for causal claim | not direct | not direct | accept | none |

## What the model actually received and returned

I inspected all 16 producer request packets and all 16 producer raw assistant
messages, followed by all 16 verifier packets and all 16 verifier raw messages.
Each producer saw only:

- the exact assessment rule;
- one exact claim with an opaque ID and SHA-256; and
- one complete current or superseded record with an opaque ID and SHA-256.

No producer saw the author key, case class, rationale, another pair, an
artifact, an edit action, or a downstream consequence. Every producer output
was structurally admitted. The producer selected the author relation in all 16
cases. Its eight direct-support quotes were literal substrings and, on direct
review, covered the material claim rather than merely shared topic words.

Each verifier was separately reset and saw the same pair plus the exact
producer proposal. Fifteen accepted the correct proposal. On K012, the record
said that alert clarity was surveyed and repair spending was not collected.
The producer correctly returned `not_direct_support`. The verifier returned:

```json
{"decision":"reject","evidence_quote":"","proposal_id":"P:K012"}
```

Under the frozen contract, rejecting a `not_direct_support` proposal means the
verifier asserts `direct_support` and must supply an exact supporting quote.
The empty quote made the response internally inconsistent, so the harness
recorded `binding_source_verifier_quote_invalid` without repair. Direct
semantic review also finds the rejection wrong: the record does not support
an 18% spending reduction.

## Quantitative results

### Producer

- calls: 16;
- protocol admitted: 16/16;
- true positives: 8;
- false positives: 0;
- true negatives: 8;
- false negatives: 0;
- fixed-matrix semantic accuracy: 16/16;
- direct-support quotes exact and semantically adequate: 8/8;
- prompt tokens: 7,460;
- completion tokens: 893;
- total tokens: 8,353;
- cached prompt tokens: 3,068;
- summed HTTP time: 62.197 seconds.

### Verifier

- calls: 16;
- protocol admitted: 15/16;
- accepted correct proposals: 15;
- incorrect raw decisions: 1;
- abstentions: 0;
- correct incorrect-proposal rejections: not tested, because the producer made
  no semantic error;
- prompt tokens: 9,249;
- completion tokens: 685;
- total tokens: 9,934;
- cached prompt tokens: 2,265;
- summed HTTP time: 57.342 seconds.

### Whole run

- calls: 32;
- prompt tokens: 16,709;
- completion tokens: 1,578;
- total tokens: 18,287;
- cached prompt tokens: 5,333;
- summed HTTP time: 119.539 seconds.

These token totals are recomputed from every raw response. The frozen runner's
summary reports 17,716 tokens because its generic accumulator counts only
interpreted responses; it excludes the rejected K012 response's 571 tokens
while still recording that call's 2.607 seconds. The raw request, response,
rejection, and summary remain unchanged. This is a custody/reporting defect in
the experiment module, not a model result and not a reason to rerun.

## Interpretation

Stage 1 showed that Qwen could act usefully when given a correct atomic
claim-record binding. This run supplies the first prospective evidence that,
when a candidate claim and one complete candidate record are already isolated,
the same model can discriminate direct support from carefully chosen near
misses. It correctly handled all eight tested risks, including wrong measure,
missing precision, population mismatch, unmeasured outcome, superseded
evidence, reversed bias polarity, unrelated evidence, and causal overclaim.

That narrows—but does not solve—the upstream problem. The producer did not
locate a record in a corpus or decide which claims require evidence. The
successful unit was already prepared as one claim against one complete record.
The evidence therefore supports an atomic comparison primitive, not an
automatic research-memory layer.

The independent verifier is not earned. It consumed 9,934 additional tokens,
received only correct proposals, demonstrated no correction, and introduced
the sole wrong semantic decision. Its failure also shows a hazard in a
relational accept/reject schema: the model must invert another model's label,
and its decision can conflict with its quote field. Do not repair or tune that
role on this fixture.

The combined gate has a frozen specification gap. Its admitted binding set
contains all eight positives, no negatives, no model abstentions, and exact
quotes, which meets every criterion literally listed in `FREEZE.md`. But K012
has no admitted verifier result, and the gate failed to state whether a
protocol rejection disqualifies the method. Calling that cleanly pass or fail
would add a rule after seeing the data. It is therefore recorded as
inconclusive. This does not affect the producer's clean pass or earn the
combined method: it added no tested correction and has one unresolved case.

## Decision

- Retain the atomic producer outside the stable harness as a qualified
  experimental method.
- Do not relay its outputs into an editor yet.
- Do not promote or tune the independent verifier. Treat the two-role gate as
  inconclusive because of the frozen protocol-rejection omission, not as a
  success.
- Give the producer one genuinely fresh transfer that tests the same atomic
  relation judgment after candidate pairs are created by a separate,
  non-gold method. This must distinguish pair generation/recall from pairwise
  semantic discrimination.
- Keep obligation-source comparison and recomposition pending. A successful
  prepared-pair classifier does not establish where claims, records, or active
  obligations come from.
- Do not change `workbench/`, add a semantic host, retry, vote, or substitute
  fixture gold.

## Validation

- freeze committed and pushed before calls at `bf2e9de`;
- endpoint identity: llama.cpp `b10331-7ba604f1c`, alias
  `qwen36-27b-iq2-coding`, 50,176 context;
- saved-run replay verification: passed;
- full local suite after evidence: 372 tests with 14 expected skips;
- targeted lint and Git whitespace validation: passed.

This is local validation, not GitHub Actions verification.
