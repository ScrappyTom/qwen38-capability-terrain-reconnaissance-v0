# Reviewing-editor seat calibration v0 — results

Date: 2026-08-12

Decision: **calibration null; stop this review-seat escalation**

## Outcome

Changing action ownership from the original closing builder to a fresh
reviewing-editor seat did not repair the known claim-local citation gap.
Adding the qualified binary assessment to that fresh seat also did not help.

Both conditions:

- started from exact candidate C004 and passed check K000;
- read the complete paper and evidence update;
- read all four editable sections;
- ran one additional passing mechanical check against C004;
- made zero candidate mutations;
- finalized C004; and
- retained the same task-faithful 11-pass/1-partial artifact.

The sole valid gap remained: Recommendation makes H2-, H1-, and H3-dependent
claims while citing only H4.

This is post-hoc calibration on the task that selected the mechanism, not a
prospective performance comparison.

## Exact action sequences

Seat only:

```text
read evidence
read paper
read Executive Summary
read Results
read Limitations
read Recommendation
check C004 (passed)
finalize C004
```

Seat plus assessment:

```text
read evidence
read paper
check C004 (passed)
read Executive Summary
read Results
read Limitations
read Recommendation
finalize C004
```

Both runs used eight admitted native tool calls. Neither called
`replace_section`. The different order is behavioral divergence without a
candidate or grade difference.

## What the model actually said

The assessment-free seat produced almost no model-visible prose. Its actions
show complete acquisition followed by another check and finalization, but do
not reveal a substantive judgment that can be audited.

The assessment-equipped seat did expose its evaluation. Before rereading the
sections, it checked each numbered task requirement and declared each
satisfied. Its handling of the results requirement was task-faithful: it found
the raw means in Results rather than inventing an Executive-Summary placement
rule.

Its citation and assessment statements were wrong:

- it said “All sections cite the appropriate records”;
- after rereading Recommendation, it said H4 was cited appropriately even
  though the section's adjusted estimate, design, and missingness claims
  depend on H2, H1, and H3; and
- it concluded that “the assessment from the independent model indicated that
  the candidate passes all checks.”

The exact assessment visible in the initial user message instead contained:

```json
{"unit_id":"U004","relation":"not_supported", ...}
```

and explained the absent H1/H2/H3 support. The same user message separately
contained a passed mechanical check receipt. The reviewer therefore appears
to have conflated or overwritten the negative model assessment with the
positive machine check. This is an inference from its explicit public prose;
no private attention state is claimed.

## Grading correction

Direct review caught a defect in the parent task's frozen rubric. G01 required
the unadjusted 4.8 and 5.5 kW means specifically in Executive Summary, while
the actual task required the revised paper to report them without naming a
section. Results reports both means and the adjusted estimate. G01 passes at
the task level.

Thus the substantive grade is 11 pass / 1 partial, not the literal frozen
10 pass / 2 partial. The extra literal partial remains recorded as a grader
wording defect. Because both conditions produced identical bytes, this
correction changes neither comparison.

## Quantitative record

| Measure | Seat only | Seat + assessment |
|---|---:|---:|
| Model calls | 8 | 8 |
| File reads | 2 | 2 |
| Section reads | 4 | 4 |
| Checks | 1 pass | 1 pass |
| Candidate mutations | 0 | 0 |
| Prompt tokens | 26,582 | 35,819 |
| Completion tokens | 201 | 1,197 |
| Total tokens | 26,783 | 37,016 |
| Cached prompt tokens | 22,103 | 31,255 |
| Recorded model duration | 19.481 s | 66.064 s |
| Maximum request prompt | 4,651 | 6,180 |
| Task-faithful grade | 11 pass / 1 partial | 11 pass / 1 partial |

The assessment condition used 10,233 more tokens, a 38.21% increase. Its
maximum request occupied 12.32% of the 50,176-token context. Context pressure,
task absence, response truncation, protocol rejection, stale candidate
identity, or unavailable edit authority did not cause the null.

Latency is descriptive because the conditions ran sequentially and cache state
differed. The treatment's extra 46.583 seconds is not treated as a stable speed
estimate.

## Custody

The apparatus was committed at
`1c1faae92bb218e2bb9bcc39375a3b7799b63804` before either call. Offline
verification:

- checks the saved endpoint alias, model path, and b10331 build;
- binds the exact source candidate and K000 check;
- verifies the copied task, sources, packet, and assessment;
- rebuilds each condition's initial context;
- checks every request against accumulated messages and the pinned inference
  fields;
- reinterprets every native response against the same five tools;
- verifies all source candidate snapshots and their section-scoped history;
- establishes that neither seat created a new candidate version; and
- confirms both submissions and final files are exact C004 bytes.

Key hashes:

- experiment manifest: `0a0d2fdc…1bd4c`;
- seat-only first request: `e645af31…b34b86`;
- assessment-seat first request: `58808acf…76b92`; and
- both final artifacts: `6e51bdcf…4fef`.

## Decision

Stop the general reviewing-editor seat and the full assessment relay on this
task. The role change increased inspection, and the assessment changed public
evaluation prose and action order, but neither supplied correct closure.

This result sharpens the design target:

> The assessor can discriminate the local support gap. The failure occurs when
> that distinction must survive a larger task/check/artifact frame and become
> an edit decision.

Do not answer this with another reminder, a stronger verdict, or a mandatory
semantic gate. If work continues, the next defensible method is an atomic
unit-review operation on a genuinely new task: the same model call compares
one exact unit with its evidence and chooses `keep` or an exact replacement,
before any global finalize decision. That tests integration of discrimination
and action while keeping host logic mechanical. It should not be calibrated
again on this home-energy paper.
