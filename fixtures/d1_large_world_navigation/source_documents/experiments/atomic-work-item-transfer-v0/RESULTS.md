# Atomic work-item transfer v0 — results

Date: 2026-08-12

Decision: **relation gate failed 15/16; editor conditions correctly not run**

## Result

All 16 prospective atomic relation calls completed normally and satisfied the
strict scalar response schema. Fifteen relations matched the frozen matrix.
One false positive caused the gate to fail:

```text
claim C103:
Attendance-scan completeness differed between pilot and comparison schools.

record H2:
tardy-arrival rates, adjusted association, confidence interval, and p-value

expected: does_not_support
returned: supports
```

The runner preserved the complete model-authored binding artifact, wrote the
failed qualification, and made zero editor calls. Neither U0 nor F1 has a model
response or candidate artifact for this fixture.

The 16 calls used 9,357 prompt tokens, 2,152 completion tokens, and 11,509
total tokens. The summed HTTP duration was 114.321 seconds. Reasoning was
disabled and no retry, repair, normalization, voting, fallback, or prompt
variation occurred.

Descriptively, all 4 frozen positive pairs were found and 11 of 12 frozen
negative pairs were rejected. These are cells in one designed matrix, not
independent samples or estimates of sensitivity and specificity.

## Direct input/output finding

The C103/H2 request contained exactly one claim and the complete H2 record. H2
contains no statement about scan coverage or completeness. The model's
explanation nevertheless said:

> Tardy-arrival rates are a direct measure of attendance scan completeness
> (specifically regarding late arrivals).

It then treated the 12.6% versus 15.4% tardiness rates as proof that scan
completeness differed. That bridge is false: outcome rates among recorded
students and the proportion of enrolled students with usable scans are
different quantities.

In the adjacent C103/H3 call, the model correctly identified the actual 74%
versus 94% completeness rates as direct support. The resulting artifact
therefore bound both H2 and H3 to C103.

Every other explanation was consistent with the supplied pair. In particular,
the model correctly kept the overall 1.9-point result separate from H4's 2.7
and 0.8 subgroup estimates, separated nonrandom selection from scan missingness,
and rejected H1–H3 as support for the complete H4 subgroup claim.

## Interpretation

The known heat-response fixture established that removing section and list
aggregation can expose a capability Qwen failed to express in an exhaustive
section array. This prospective task adds an important boundary: one claim and
one record per call does not guarantee correct relationship discrimination.

The failure occurred at the smallest tested semantic unit. It was not caused
by an exhaustive output list, lost cross-claim state, citation serialization,
context pressure, tool protocol, or edit planning. The model made a local
category error between two related but distinct measures.

That means an atomic binding artifact can be exact in custody while still be
semantically wrong. If downstream code treats every model-authored `supports`
result as authoritative, the false H2 binding would be carried forward cleanly
rather than corrected.

## What remains unanswered

The prospective U0-versus-F1 edit comparison did not run. This experiment says
nothing new about whether an active obligation improves local editing on a
fresh task. The adaptive heat-response result remains a promising known-case
calibration, not a transferred effect.

It would be invalid to override the frozen gate, discard H2 after inspecting
the output, rewrite C103, or run the editors against the expected diagonal.
Those actions would turn a prospective failure into a tuned demonstration.

## Design implication

Three replaceable concerns should remain separate:

1. **Binding acquisition:** who or what says this claim is governed by this
   evidence record?
2. **Local obligation:** which task requirement is active for that bound pair?
3. **Local action:** what exact text should replace the claim span?

This run failed concern 1 before concerns 2 and 3 were exercised. The result
does not argue for section aggregation; it argues against treating a single
model-authored binary match as semantic authority merely because it is atomic.

A next experiment, if pursued, should test the local-action representation
with correct bindings supplied prospectively by an explicit source such as a
task author or frozen fixture. A separate experiment can study model-owned
binding acquisition. Combining them behind one mandatory perfect gate obscures
which capability is being tested.

No stable-harness change, automatic matcher, obligation selector, editor, or
submission mechanism is earned.

