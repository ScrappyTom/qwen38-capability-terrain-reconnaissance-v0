# Binary submission review v0 — results

Date: 2026-08-12

Decision: **qualified assessor; prospective terminal-quality null; no promotion**

## Outcome

The narrowed binary assessor passed its independent four-unit qualification.
On the fresh home-energy task, one common builder then produced candidate C004,
passed the mechanical check, and called `submit_for_review`. The exact same
pending call and candidate were branched.

The independent assessor classified three sections `supported` and
Recommendation `not_supported`. Receipt-only and assessment-relay builders
then each made the same operational decision on their first continuation call:

```text
finalize C004
```

Neither branch read, edited, or checked after review. Both submitted the same
3,111 bytes with SHA-256
`6e51bdcfc0d2f3ff0804d316b68fe29a066cffcd1defb2036b3aaf5975e44fef`.
Task-faithful artifact grading was 11 pass / 1 partial / 0 fail in both
conditions. The literal frozen rubric initially produced 10 pass / 2 partial,
but one supposed partial came from an unsupported section-placement criterion,
as corrected below.

This is a clean terminal-quality null. The treatment added a semantically
relevant model judgment but caused no observable action or artifact change.

## Qualification

The fresh reservoir note contained two supported controls, one direct count
conflict, and one leak-rate claim whose cited record had no leak-rate
measurement. The assessor returned all four frozen binary labels correctly:

| Unit | Expected | Observed | Exact comparison |
|---|---|---|---|
| U001 | supported | supported | 12 of 20 gates matched B1 |
| U002 | not_supported | not_supported | B1 reported 12 pass, 5 fail, 3 uninspected—not all 20 pass |
| U003 | supported | supported | 4.2, 3.9, and 0.3 mg/L matched B2 |
| U004 | not_supported | not_supported | B3 contained no before/after leak-rate measure |

U004's prose still used “contradicts” loosely, but its actual binary assertion
was only `not_supported`, and it correctly identified the missing measurement.
The contract deliberately collapses direct conflict and unresolved support.
No response was repaired or retried.

The pre-call apparatus commit was
`97dfeed2855f4b4816d3a332f50dd59c02f45d9f`. Qualification used one call,
1,795 total tokens, and 27.783 seconds.

## Common builder trajectory

The common prefix was straightforward and fully admitted:

```text
read paper
read evidence
read four editable sections
replace Executive Summary
replace Results
replace Limitations
replace Recommendation
check (passed)
submit_for_review
```

All 12 native tool responses were structurally admitted. There were four
candidate mutations, each changing exactly one declared editable section.
`Background`, `Methods`, and `References` remained raw-byte exact. The check
ran against C004 and passed.

The last common request used 6,089 prompt tokens, 12.14% of the 50,176-token
context. Neither task absence, context pressure, response truncation, protocol
rejection, nor stale candidate/check binding explains either remaining
artifact gap.

## Artifact judgment

There was one unique artifact. Direct task-to-artifact grading found eleven
requirements passed and one partial:

1. **G10 — claim-local citations.** Recommendation cites H4 for the subgroup
   claims but does not cite H2 for the adjusted estimate, H1 for
   nonrandomization/residual confounding, or H3 for differential missingness
   where those claims reappear.

The frozen G01 text required both unadjusted means specifically in Executive
Summary. The actual editorial task required the revised paper to report those
means but did not assign them to a section. Results reports both 4.8 and 5.5 kW
and the adjusted estimate. G01 therefore passes under the task. The literal
10-pass/2-partial rubric output remains recorded as a grader-wording defect;
it is not used as the substantive grade.

The paper correctly handled the adjusted interval and p-value, causal
limitation, raw-versus-adjusted distinction, exact telemetry coverage, bias
direction, exploratory subgroup status, interaction p-value, restrained
recommendation, protected bytes, and removal of obsolete assertions.

The complete itemized judgment is in `artifact_grade.json`.

## What the assessor got right—and could not see

The prospective assessor's three positive judgments accurately matched H1-H4
values and relations in Executive Summary, Results, and Limitations.

Its negative Recommendation judgment was also materially correct within its
declared evidence boundary. Literal citations attached only H4 to that unit,
while the unit also made H2-dependent estimate claims, H1-dependent design
claims, and H3-dependent missingness claims. This corresponds directly to the
independent G10 partial grade.

The assessor did not need to identify G01: direct review established that G01's
section-placement constraint was not in the editorial task. More generally,
the assessor still receives exact claims already present in configured
artifact sections and their literal citations, but no editorial task; it
cannot establish task completeness or omitted obligations. That remains an
intentional scope limit.

## Builder response to review

The two first post-review requests had the same 25-message prefix and differed
only in the successful `submit_for_review` tool result:

- receipt-only: `assessment: null`;
- treatment: the candidate-bound, model-authored, non-authoritative four-unit
  assessment.

Both response messages contained empty content and exactly one zero-argument
`finalize` call. Tool-call IDs and raw response bytes differed, but the action
and arguments were identical. There was no post-review candidate version.

Operationally, Qwen did not use a correct and relevant `not_supported`
classification when deciding whether to continue work. This run cannot reveal
private reasons. It establishes only the observable transition:

```text
assessment identifies one claim/evidence binding gap
-> builder immediately finalizes the assessed candidate unchanged
```

## Quantitative comparison

| Measure | Receipt-only | Binary assessment |
|---|---:|---:|
| Shared pre-review calls | 12 | 12 |
| Post-review calls | 1 | 1 |
| Post-review actions | finalize | finalize |
| Post-review reads / edits / checks | 0 / 0 / 0 | 0 / 0 / 0 |
| Task-faithful grade | 11 pass / 1 partial | 11 pass / 1 partial |
| Literal frozen rubric | 10 pass / 2 partial | 10 pass / 2 partial |
| Final SHA-256 | `6e51bd…4fef` | `6e51bd…4fef` |
| Builder tokens, shared prefix plus branch | 50,398 | 51,284 |
| Assessor tokens | 0 | 3,040 |
| Total condition-accounted tokens | 50,398 | 54,324 |

The treatment cost 3,926 additional tokens, 7.79% over receipt-only when the
assessor call is included. The post-review treatment request itself was 886
prompt tokens larger. Completion was 14 tokens in both branches.

Recorded latency is descriptive, not a fair speed comparison. Receipt-only
ran first and its one continuation took 12.900 seconds with no cached prompt
tokens; treatment ran second and took 3.093 seconds with 6,023 cached prompt
tokens. The assessor took 47.372 seconds. The common prefix used 44,101 tokens
and 67.009 seconds.

The actual prospective execution made 15 model calls and used 60,621 tokens:
12 shared builder calls, one assessor call, and one continuation per branch.
Qualification was a separate one-call, 1,795-token run.

## Custody and process qualification

Offline verification:

- rebuilds both qualification and prospective packets and requests byte for
  byte;
- reinterprets both schema-constrained assessor responses;
- verifies the saved endpoint alias, model path, and b10331 build;
- checks every common native request against the exact accumulated message
  history and every response through the declared tool schema;
- verifies candidate IDs, hashes, bytes, snapshots, succession, and exact
  one-section mutation scope;
- checks both branches begin at the same pending call and candidate;
- verifies both first actions are `finalize`; and
- verifies both final artifacts equal the boundary candidate byte for byte.

Important hashes:

- qualification request: `e7d3b614…c2d8d1`;
- qualification raw response: `278cfd61…e4584`;
- review packet: `9ae5d3ef…ebd69`;
- prospective assessor request: `2318df6e…c8083`;
- prospective assessor raw response: `6ffbd77b…2451`; and
- final artifact: `6e51bdcf…4fef`.

One process defect did occur: the prospective CLI printed the condition-labeled
summary before artifact grading. Because it also exposed that both conditions
submitted one byte-identical artifact, this cannot favor either condition, but
the grade is not described as blind. The runner now prints only the run ID and
summary path for future prospective executions. This post-run correction does
not alter any saved request, response, candidate, assessment, or result.

## Decision

Do not promote or tune the binary assessment relay. It qualified as a local
claim-support discriminator and correctly found a real citation-binding gap,
but relaying it to the original builder at closure produced no behavioral or
terminal-quality difference.

The more precise lesson is not “reviewers do not work.” It is:

> Correct model-authored review information can still be inert when returned
> as optional advice to the builder that has already selected closure.

This earns one different method class, not another wording change: give a
fresh reviewing editor direct custody-safe read/edit/check/finalize operations
rather than asking the original builder to consume an advisory judgment. A
same-task run would be calibration only because this result selected the
mechanism; any performance claim would require a new task. Prior generic
reviewers falsely certified omissions, so the next seat must preserve the
qualified exact unit/evidence comparison rather than revert to an unconstrained
“review everything” prompt.
