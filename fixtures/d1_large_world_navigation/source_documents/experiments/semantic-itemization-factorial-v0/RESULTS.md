# Semantic itemization factorial v0 - result

Date: 2026-08-12

Run: `semantic-itemization-factorial-v0-run-001`

Freeze commit: `2b74019`

## Outcome

The frozen representation comparison is **ineligible**. All 24 calls were
mechanically admitted and replayed exactly, but the evidence-only control
represented the correct central direction on only 3 of 5 revision units. The
freeze required 5 of 5 so that the experiment would test retention of
secondary distinctions rather than basic recognition of a contradictory
target.

No representation is promoted. The run is preserved without a retry, prompt
change, fixture repair, or stable-workbench change.

| Condition | Pass | Partial | Fail | Action items | Revision directions | Pair guards | Exact U005 no-op |
|---|---:|---:|---:|---:|---:|---:|---|
| Evidence only | 1 | 3 | 2 | 4/22 | 3/5 | 0/3 | yes |
| Complete paragraph | 2 | 3 | 1 | 7/22 | 4/5 | 1/3 | yes |
| Same sentences on separate lines | 2 | 3 | 1 | 7/22 | 4/5 | 1/3 | yes |
| Same lines with opaque IDs | 2 | 4 | 0 | 7/22 | 5/5 | 1/3 | yes |

These are deterministic observations from six distinct units per condition,
not estimates of a task-distribution success rate.

## What the model actually received

I directly inspected every saved request, raw response, admitted result, final
unit, and transition before grading. Each fresh call received:

- the same local-editor system instruction;
- the complete editorial task;
- one exact current unit and content-addressed basis version;
- one complete bound evidence record and literal evidence handle;
- the exact unit/evidence binding;
- one of the four frozen `semantic_material` values; and
- the same strict result schema, temperature-zero nonthinking profile, and
  640-token completion ceiling.

The content-bearing arms used the same canonical sentences, punctuation,
capitalization, and order. Paragraph joined them with spaces; separate-lines
joined them with newline characters represented as JSON escapes in the user
message; opaque IDs added only `Jnnn | ` before those lines. No grade, gold
item, condition name, experiment purpose, or host semantic judgment was shown.

Every raw response finished normally with a schema-valid object. There were no
protocol rejections, retries, truncations, hidden repairs, or reasoning tokens.

## Frozen gate

| Requirement | Result |
|---|---|
| Six evidence-only calls admitted | pass |
| U005 preserved byte-for-byte | pass |
| Correct central direction on all five revision units | **fail: 3/5** |
| Fewer than 20/22 action items | pass: 4/22 |
| At least two revision units below pass | pass |

Evidence-only copied U001's observational claim despite an exact randomized
record and copied U006's numerical symptom claim despite an exact record saying
symptoms were not measured. Those are failures of the central correction, not
merely omissions of secondary qualifiers. The predeclared causal comparison
therefore cannot answer the intended item-retention question.

## Unit-level findings

Action-item groups were frozen as conjunctive. A line containing only one
fragment of a group did not receive credit for the group.

| Unit | Evidence only | Paragraph | Separate lines | Opaque IDs | Direct finding |
|---|---|---|---|---|---|
| U001 randomized | fail, 0/3 | fail, 0/3 | fail, 0/3 | partial, 0/3 | Evidence, paragraph, and lines copied `observational`; IDs produced `randomized trial` but omitted seeded assignment, prespecified ITT, and causal attribution. |
| U002 observational | partial, 0/4 | partial, 0/4 | partial, 0/4 | partial, 0/4 | Only paragraph added `nonrandom assignment`; every arm omitted the adoption bases, adjusted status, explicit noncausal boundary, and residual confounding. |
| U003 low-score nonresponse | partial, 0/4 | partial, 0/4 | partial, 0/4 | partial, 0/4 | All four emitted the identical gist: `can exaggerate`; all omitted coverage, scale, low-score mechanism, mean effect, and explicit `does not attenuate`. |
| U004 high-score nonresponse | partial, 0/4 | partial, 0/4 | partial, 0/4 | partial, 0/4 | All four copied the identical `likely attenuated` target, omitting the evidence chain and strengthening `can` to `likely`. |
| U005 measured no-op | pass, 4/4 | pass, 4/4 | pass, 4/4 | pass, 4/4 | Every condition preserved all 184 bytes exactly. |
| U006 unmeasured | fail, 0/3 | pass, 3/3 | pass, 3/3 | pass, 3/3 | Evidence-only copied unsupported symptom statistics; every content-bearing arm stated the recorded fields, measurement absence, and inference boundary. |

Only the measurement pair passed a strict pair guard, and only in the three
content-bearing conditions. No condition passed the design or missingness
pair guard.

## Pairwise observations

The following differences are preserved as descriptive behavior. Because the
frozen interpretability gate failed, none is eligible for the predeclared lead
decision.

| Comparison | Grade changes | Item delta | Byte-identical final texts | Total-token delta | Finding |
|---|---|---:|---:|---:|---|
| Paragraph vs evidence | U006 fail -> pass; no regression | +3 | 4/6 | +466 (+7.8451%) | One measurement-boundary improvement; below the content-lead threshold even before the gate. |
| Separate lines vs paragraph | no grade change | 0 | 4/6 | +3 (+0.0468%) | No item or grade evidence for newline segmentation. |
| Opaque IDs vs separate lines | U001 fail -> partial; no regression | 0 | 4/6 | +142 (+2.2156%) | One central-direction change, but no conjunctive item gain; formally ineligible because the control gate failed. |

The paragraph and line arms differed textually on U002 and U006 but had
identical grades and item totals. The ID arm changed U001 and U006 relative to
the line arm; only U001 changed grade. U003, U004, and U005 were byte-identical
across all four conditions.

## Quantitative findings

### Evidence only

- calls: 6;
- admitted: 6/6;
- prompt tokens: 5,108;
- completion tokens: 832;
- cached prompt tokens: 2,900;
- reasoning tokens: 0;
- total tokens: 5,940;
- summed HTTP time: 55.438 seconds.

### Complete paragraph

- calls: 6;
- admitted: 6/6;
- prompt tokens: 5,587;
- completion tokens: 819;
- cached prompt tokens: 3,026;
- reasoning tokens: 0;
- total tokens: 6,406;
- summed HTTP time: 44.802 seconds.

### Separate lines

- calls: 6;
- admitted: 6/6;
- prompt tokens: 5,595;
- completion tokens: 814;
- cached prompt tokens: 3,495;
- reasoning tokens: 0;
- total tokens: 6,409;
- summed HTTP time: 43.669 seconds.

### Opaque IDs

- calls: 6;
- admitted: 6/6;
- prompt tokens: 5,713;
- completion tokens: 838;
- cached prompt tokens: 3,566;
- reasoning tokens: 0;
- total tokens: 6,551;
- summed HTTP time: 44.649 seconds.

### Whole run

- calls: 24;
- admitted: 24/24;
- prompt tokens: 22,003;
- completion tokens: 3,303;
- cached prompt tokens: 12,987;
- reasoning tokens: 0;
- total tokens: 25,306;
- summed HTTP time: 188.558 seconds.

Summed HTTP time is not an independent latency experiment; prompt-cache state
and the frozen nonblocked call order differed across cells.

## Interpretation

The experiment does not establish that itemization works or fails. Its control
did not instantiate the preregistered failure shape. The model sometimes did
not make the basic evidence-required correction, so secondary-item retention
cannot be cleanly separated from target-copying and central recognition in
this fixture.

Within that limitation, two behavioral facts are clear:

1. Merely changing spaces to newline delimiters produced no grade or item
   change.
2. Opaque IDs changed one central decision, but did not cause any additional
   complete action-item group to survive into output.

The content-bearing arms' shared U006 repair shows that repeated task-author
content can affect an action. It does not show that paragraph, line, or ID
representation is a generally useful method. The repeated U003/U004 gist
outputs also show that complete visible content did not by itself ensure that
the output retained the content's distinct coverage, mechanism, direction,
modality, and negative-contrast parts.

No claim about attention slots, memory objects, internal compression, or model
psychology follows from these six bounded units.

## Decision

- Stop this factorial at its frozen v0 result.
- Do not rerun or tune the fixture to make the evidence-only gate pass.
- Do not promote newline segmentation, opaque IDs, semantic items, a compiler,
  model-authored state, cards, or a submission tool.
- Preserve the earlier 20/22 and 21/22 itemized-frame runs as bounded positive
  observations. Their cause remains unresolved: this planned control neither
  qualified nor refuted the representation comparison.
- Keep the stable workbench and server profile unchanged.
- Before another semantic representation experiment, isolate the local action
  decision itself on already-qualified operands; do not assume that a complete
  visible relation will be applied or that a copied target means its evidence
  was absent.

## Validation

- freeze committed and pushed before model calls at `2b74019`;
- endpoint identity: llama.cpp `b10331-7ba604f1c`, alias
  `qwen36-27b-iq2-coding`, 50,176 context;
- exact saved-run replay: passed;
- direct review: 24 requests, 24 raw responses, 24 results, 24 final units,
  and 24 transitions;
- semantic grading added only after the model run;
- full local suite: 491 tests run with 14 expected skips;
- focused suite: 12/12 passed; targeted Ruff, JSON, local Markdown-link, and
  Git whitespace checks passed;
- stable `workbench/`: unchanged.

This is local validation, not GitHub Actions verification.
