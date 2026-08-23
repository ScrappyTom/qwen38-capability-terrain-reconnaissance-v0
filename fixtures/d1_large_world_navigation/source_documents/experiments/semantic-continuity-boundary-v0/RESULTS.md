# Semantic Continuity Boundary v0 — results

## Outcome

The destructive-boundary study separated capture from post-reset use, and
both gates failed for different reasons.

- Qwen's two model-authored continuity notes captured 14/22 frozen semantic
  items: 7/11 in each world. They preserved the main polarity of five of six
  central relations, but dropped exact qualifiers, all three W02 source
  handles, and several negative contrasts. The W01 note also invented
  unsupported `primary` and `secondary` outcome labels.
- Retrieval-only graded 2 pass / 4 partial with 13/22 action items.
- Model-summary carryover graded 0 pass / 5 partial / 1 fail with 8/22 items.
- Correct oracle prose graded 2 pass / 3 partial / 1 fail with 11/22 items.

The oracle changed behavior and reduced exact reacquisition, but it did not
improve overall action quality. It cut evidence reads from six to two and
returned evidence bytes from 1,969 to 591, yet regressed U001 from a complete
retrieval-based revision to an unchanged unsupported claim. The frozen oracle
gate therefore failed despite a 66.67% read reduction.

All two capture calls and all eighteen Phase B trajectories were admitted and
submitted. Exact replay passed.

## Direct review of what the model actually saw and did

The investigator inspected both exact Phase A request packets and raw
responses, all eighteen initial Phase B requests, every continuation request
and raw action response, all thirteen literal evidence results, and all
eighteen final unit texts after exact replay.

### Phase A capture

The W01 note retained the estimate, confidence interval, p-value, ITT label,
coverage rates, low-score missingness, mean direction, measured retention, and
retention values. It omitted `prespecified`, the computer-generated assignment
method, causal support within the trial population, `can`, and `rather than
exaggerate`. It called P1 the primary outcome and P3 a secondary outcome even
though neither record assigned those roles.

The W02 note retained nonrandom adoption, baseline imbalance, adjusted status,
the full estimate, association/residual-confounding limits, coverage,
high-score missingness, mean direction, exaggeration direction, and the
unmeasured-outcome fields. It omitted regional-director selection, the symptom
score meaning, `can`, `rather than attenuate`, explicit absence of relapse
status/group percentages, and every `[P1]`–`[P3]` handle.

This is not merely a formatting miss. The capture artifact preserved useful
gist but was not an exact evidence-bound semantic state. It failed both 9/11
world thresholds, the handle gate, and the unsupported-assertion gate.

### Retrieval-only after reset

Retrieval-only read the one applicable exact record in every trajectory.

- U001 converted P1 into a complete randomization, prespecified ITT, exact
  estimate, and bounded causal statement: pass.
- U002 reread the complete missingness record and then resubmitted its short
  initial sentence unchanged: partial, 1/4.
- U003 reread P3 and expanded the accurate line. The result contained all
  three semantic items but violated the intended exact no-op: partial.
- U004 removed the unsupported `caused` wording but omitted clinic selection,
  explicit association status, and residual confounding: partial, 1/4.
- U005 corrected attenuation to exaggeration but lost the score subgroup,
  mean mechanism, `can`, and opposite-direction contrast: partial, 1/4.
- U006 removed the fabricated outcome and retained every measurement-limit
  fact: pass.

The baseline therefore recovered all central directions but not complete
relationships.

### Model-authored summary after reset

The model-summary arm read exact source on five of six units. Its only skipped
read was U001, where it immediately resubmitted the inaccurate initial
quantification even though its note contained randomization, ITT, and the
greater-reduction estimate.

On U002, U004, and U005, exact reopening plus the note still produced the same
gist compression seen in retrieval-only. U006 is particularly diagnostic: the
model reread the exact sentence saying that no relapse status or group
percentage was available, but its final text mirrored the lossy note and
omitted that sentence. The carried summary did not simply save reads; its
selection and compression remained salient after source reopening.

No unit improved over retrieval-only. U001 regressed to fail and U006 regressed
from pass to partial. The downstream arm finished with five fewer action items
and two fewer passing units while saving only one read.

### Task-author oracle after reset

The oracle contained all 22 Phase A items and every evidence handle. It was
behaviorally active:

- U003 preserved the supplied bytes without rereading;
- U004 converted the full observational relation into a complete action
  without rereading; and
- U001, U003, U004, and U005 skipped evidence reads.

But its behavior was not reliably better:

- U001 saw the complete randomization/ITT/greater-reduction relation and still
  submitted the inaccurate initial sentence unchanged;
- U002 reread the exact record and still returned only coverage plus `likely
  attenuated`; and
- U005 skipped the read and compressed the complete bias chain to coverage
  plus `likely exaggerated`.

Oracle passed U004 and U006, tied the retrieval baseline's two-pass total, and
finished two items below retrieval. It regressed U001, so the no-regression
condition failed before the efficiency alternative could qualify it.

## Frozen adjudication

| Unit | Retrieval only | Model summary | Oracle prose | Main observation |
|---|---:|---:|---:|---|
| U001 randomized | pass (4/4) | fail (0/4) | fail (0/4) | Both carried states induced unchanged submission; retrieval produced the complete action. |
| U002 low-score missingness | partial (1/4) | partial (1/4) | partial (1/4) | All three reread/acted paths collapsed to the same short claim. |
| U003 measured no-op | partial (3/3; rewrite) | partial (3/3; rewrite) | partial (2/3; exact) | Frozen no-op and A109 conflict; see measurement defect below. |
| U004 observational | partial (1/4) | partial (1/4) | pass (4/4) | Oracle alone converted the complete relation into action. |
| U005 high-score missingness | partial (1/4) | partial (1/4) | partial (1/4) | Every arm kept polarity but lost the mechanism and modality. |
| U006 unmeasured outcome | pass (3/3) | partial (2/3) | pass (3/3) | The lossy model note's omission survived an exact reread. |
| **Total** | **2 pass; 13/22** | **0 pass; 8/22** | **2 pass; 11/22** | **Neither continuity arm qualified.** |

All conditions recovered 6/6 central directions. Strict pair guards were 0/3
for retrieval-only, 0/3 for model summary, and 1/3 for oracle. Only oracle
preserved the intended no-op bytes.

## Measurement defect

Direct inspection found one frozen fixture inconsistency. Phase B says to
preserve an already complete measured claim byte-for-byte, and U003 was
designated as the exact no-op. However, action item A109 separately requires
the final line to state that retention was directly measured, wording absent
from the frozen U003 line.

No U003 output can literally satisfy both constraints. The oracle preserved
the exact bytes but missed A109; retrieval and model summary made A109 explicit
but rewrote the no-op. U003 remains useful behavioral evidence about source
reopening and preservation, but it cannot support a fully passing no-op claim.
This defect does not change either gate: oracle independently regressed U001
and lost two total items, while the model-summary capture and downstream arms
failed independently.

## Quantitative metrics

### Phase A

| Metric | Model capture |
|---|---:|
| attempted/admitted calls | 2 / 2 |
| captured items | 14/22 |
| worlds reaching 9/11 | 0/2 |
| prompt tokens | 1,627 |
| completion tokens | 332 |
| cached tokens | 98 |
| total tokens | 1,959 |
| summed HTTP duration | 29,284 ms |

### Phase B

| Metric | Retrieval only | Model summary | Oracle prose |
|---|---:|---:|---:|
| attempted/submitted trajectories | 6 / 6 | 6 / 6 | 6 / 6 |
| model turns | 12 | 11 | 8 |
| exact evidence reads | 6 | 5 | 2 |
| returned evidence bytes | 1,969 | 1,597 | 591 |
| prompt tokens | 16,085 | 16,272 | 11,845 |
| completion tokens | 992 | 898 | 877 |
| cached tokens | 9,076 | 8,617 | 4,621 |
| total tokens | 17,077 | 17,170 | 12,722 |
| summed HTTP duration | 63,722 ms | 59,950 ms | 57,299 ms |
| passing units | 2/6 | 0/6 | 2/6 |
| satisfied action items | 13/22 | 8/22 | 11/22 |

Relative to retrieval-only, model-summary Phase B used one fewer read
(-16.67%), 372 fewer evidence bytes (-18.89%), one fewer turn (-8.33%), and 93
more tokens (+0.54%). Including the two reusable Phase A capture calls, its
end-to-end total was 19,129 tokens, 2,052 above retrieval-only (+12.02%).

Oracle used four fewer reads (-66.67%), 1,378 fewer evidence bytes (-69.98%),
four fewer turns (-33.33%), and 4,355 fewer Phase B tokens (-25.50%). Its
task-author construction cost is not measured. Efficiency did not rescue its
quality regression under the frozen rule.

The complete run used 48,928 tokens: 45,829 prompt, 3,099 completion, 22,412
reported cached, and zero reasoning tokens. Summed HTTP duration was 210,255
ms.

## Interpretation

The clean result is not that semantic continuity was inert. The oracle clearly
altered reopening and action behavior. The result is:

> Broad carried semantic truth can reduce reacquisition and sometimes support
> a correct later action, but it can also make Qwen declare the current claim
> sufficient before the required relation has been expressed.

The earlier local semantic-frame experiments placed the exact branch-specific
relationship beside the exact record and action, reaching 20/22 and 21/22
items. This experiment carried a broader three-record note across a reset and
revealed the future unit only afterward. Even the correct oracle then reached
11/22. The evidence therefore distinguishes local preparation from general
semantic persistence: a state artifact does not automatically recreate the
focused action frame that produced the earlier benefit.

The model-authored result adds a second limitation. Capture itself was lossy,
and reopening exact source did not reliably dislodge the summary's omissions.
This is a plausible anchoring/salience effect, not proof of an internal mental
mechanism; the saved behavioral divergence is the evidence.

## Decision

- Do not promote task-author oracle continuity or model-authored continuity.
- Do not add typed semantic state, a default memory surface, or a staleness
  experiment.
- Do not tune the same fixture, patch the U003 rubric retroactively, or require
  the host to judge semantic completeness.
- Retain exact retrieval as the stronger baseline.
- Preserve the prior branch-local semantic-frame result as a separate positive
  finding: locality and action placement, not persistence alone, appear to be
  doing important work.

The next useful design discussion is therefore about how a model or tool can
select and materialize one exact branch-local working artifact at the moment
of action without asking the host to author semantic truth. This run does not
itself earn an implementation of that mechanism.

## Limitations

- Two synthetic dossiers, two deterministic capture calls, and one Phase B
  trajectory per cell do not estimate run-to-run or population variance.
- The task-author oracle is an experimental ceiling, not a deployable source of
  semantic truth.
- The three-record state is intentionally broader than the earlier local
  frames, so the experiment tests broad continuity rather than serialization
  alone.
- Evidence reopening was optional; read choice is part of the observed
  treatment effect.
- U003 has the frozen no-op/item inconsistency described above.
- No world mutation or staleness was tested because clean-boundary utility did
  not qualify.

## Evidence and validation

The immutable evidence is under
`runs/semantic-continuity-boundary-v0-run-001/`: copied fixture and profile,
endpoint snapshots, frozen identities, both Phase A requests and raw responses,
all Phase B request/response/action/result/message/transition records, condition
manifests, and summaries.

Exact replay verified every request, response interpretation, action, literal
read result, continuation message, submission, transition, final unit,
manifest, usage total, fixture, profile, prompt, schema, and frozen hash. All
14 experiment tests passed with replay enabled.
The complete local suite ran 466 tests: 452 passed and 14 archived-
continuation tests were intentionally skipped. Git whitespace validation
passed. This is local validation, not GitHub Actions verification.
