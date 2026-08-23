# Atomic claim edit focus v0 — results

Date: 2026-08-12

Decision: **known-fixture calibration passed; prospective transfer required**

## Result

All four stateless focused calls completed normally. The model added the three
missing individual handles and preserved the already correct fourth claim:

| Claim | Bound record | v0 output | Focused output |
|---|---|---|---|
| C001 adjusted association | H2 | added CI and p-value, no citation | appended `[H2]` |
| C002 nonrandom selection | H1 | unchanged, no citation | appended `[H1]` |
| C003 geocoding completeness | H3 | added rates, no citation | appended `[H3]` |
| C004 housing-density caveat | H4 | retained `[H4]` | retained `[H4]` |

The combined candidate has exactly one expected individual handle inside each
frozen claim span, no other H1–H4 handle inside those spans, and no changes
outside the spans. Its visible mechanical check passed against the exact new
candidate.

The focused calls used 3,874 prompt tokens, 172 completion tokens, and 4,046
total tokens. Summed HTTP duration was 16.392 seconds. No reasoning, retry,
repair, normalization, voting, fallback, or cross-call history occurred.

Relative to v0, the added obligation cost 160 prompt tokens across four calls
(4.3%) while completion tokens fell by 41. Total tokens rose by 119 (3.0%).
These are paired descriptions of one deterministic known fixture, not latency
or efficiency estimates.

## Direct input/output finding

The model-facing difference was only the additional
`active_local_obligation` field containing the task's existing requirement 6.
The system prompt, full task, candidate, claims, evidence, relations, declared
handles, response schema, model, and inference settings were unchanged.

All three previously deficient outputs changed from content-oriented behavior
to binding-oriented behavior:

- C001 stopped expanding the confidence interval and p-value and returned the
  original claim plus `[H2]`.
- C002 changed from an exact no-op to the original claim plus `[H1]`.
- C003 stopped expanding the group rates and returned the original claim plus
  `[H3]`.
- C004 remained an exact no-op because `[H4]` was already present.

This is not merely increased evidence salience: the evidence, relation, and
declared handle were already present in v0. The added field changed which
existing task obligation governed the local action.

## Human artifact adjudication

The final Policy Implications paragraph is factually unchanged except for the
three citations. Each handle follows the exact claim it supports. The sentence
with H1 and H3 remains grammatical and now keeps the records separate rather
than serializing an undeclared combined token. The recommendation remains
proportionate, and no causal or effect-modification overstatement was added.

The full paper continues to satisfy the substantive requirements through its
existing Summary, Findings, and Caveats. The focused output avoids the v0
candidate's redundant repetition of CI, p-value, and geocoding rates.

## Interpretation boundary

On this known fixture, the result supports a three-part local work item:

```text
exact claim + exact supporting evidence + active obligation → exact local text
```

The first two components were sufficient for relationship discrimination but
not for selecting the intended edit. Adding the active obligation redirected
all three deficient outputs.

This does not show that the host can or should choose the obligation. The
experimenter selected requirement 6 after inspecting v0's failure. A practical
system would need the obligation to come from a task author, model-owned work
artifact, or another explicitly tested source. Custody alone cannot infer it.

No section card, aggregate assessment, semantic grader, or global reviewer was
needed for this calibration. No stable-harness change is earned.

## Next gate

Freeze a genuinely new task before calls. Define its claim spans, evidence
records, and active obligations independently of model output. Then run the
same stateless focused operation without prompt changes. A successful transfer
would make the local work-item representation a lead; failure would identify
which part of the representation does not generalize.

