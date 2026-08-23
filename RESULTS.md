# Capability-terrain reconnaissance v0 — results

Date: 2026-08-23

Freeze commit: `f3092c73065353d5fbdb4c3646632b6586c7e50b`

Run ID: `2026-08-23-capability-terrain-v0`

## Result in one sentence

Across a finite 39-call breadth tranche, Qwen3.8 showed that it can sometimes
carry exact evidence through construction, effect uptake, checking, and
closure, but the dominant cross-task failures were low-occupancy action
expression and incorrect readiness discrimination rather than context
capacity: 19 responses were rejected, two strong-partial artifacts were
submitted as complete, and no cell achieved independently correct completion.

## Why this tranche matters

The program had spent many experiments studying what happens near a full
context window. This tranche deliberately sampled other parts of the agent
pipeline. It found that context pressure was not active at all. The largest
measured prompt was 7,110 tokens against a 20,992-token prompt allowance, no
result body was demoted, and no exact reopen occurred.

The failures therefore cannot be attributed to a lack of prompt space. They
occurred at three different downstream boundaries:

```text
intended task action
        ↓
legal action expression/admission       often failed
        ↓
artifact construction and effect uptake sometimes succeeded
        ↓
verification coverage                   missed subtle requirements
        ↓
readiness / closure                      false closure in three cells
```

This is the intended value of breadth reconnaissance: it reveals which system
function is actually limiting before another context mechanism is designed.

## Mechanical disposition

The run is mechanically qualified.

- Exact authorized freeze and run ID matched.
- Launch preflight rehashed the 11.14 GB model, tokenizer projection, server,
  tokenizer, and evaluator runtimes successfully.
- 39 actor calls produced exactly 39 provider attempts and zero retries.
- All provider calls returned HTTP 200.
- All six postflight mutation/result checks passed.
- Every model server released; no process or listening port remained.
- No `TRANCHE_ABORTED.json` exists.
- The repository remained unchanged during measured execution.
- The raw run contains 458 sealed files, 10,620,769 bytes, under manifest
  `b6b40c3c444348efe1bcd6a26886806d67d215d04d78283b3d456dcd63cdfd3b`.
- `MECHANICAL_AUDIT.json` recomputes with zero failures.

The tranche used 96,407 prompt tokens and 5,250 completion tokens, or 101,657
serialized tokens total. Of prompt tokens, 73,830 were reported cached, for
76.58% aggregate cache reuse. Provider-call wall time was about 216.1 seconds;
asset hashing, six model loads, evaluation, and custody work are additional.

## Literal cell outcomes

| Cell | Calls | Valid / rejected | Literal path | Candidate | Evaluation / closure |
|---|---:|---:|---|---|---|
| D1 atlas discovery | 4 | 1 / 3 | invalid → root → invalid → invalid | unchanged | no memo; budget exhausted |
| D2 paper revision | 7 | 7 / 0 | tree → three reads → replace → check → submit | changed | visible pass; semantic 12/13; premature submission |
| D3 coverage calibration | 8 | 1 / 7 | seven invalid tree requests → tree | unchanged | starting failure remains; budget exhausted |
| D4 device-event repair | 9 | 3 / 6 | invalid → tree → invalid → target read → contract read → four invalid test reads | unchanged | starting failure remains; budget exhausted |
| D5 deployment-wave repair | 8 | 7 / 1 | tree → contract read → target read → invalid → test read → replace → check → submit | changed | visible pass; external 7/8; premature submission |
| D6 exact-current-state handoff | 3 | 1 / 2 | two invalid submits → submit | unchanged from D2 donor | same semantic 12/13; premature resubmission |

No cell triggered prompt pressure. No receipt substitution or reopen occurred.

## Action-expression terrain

Nineteen of 39 responses—48.7%—were rejected before an ordinary task action
could occur.

The rejections were not evidence that the model had no intended next action.
In almost every case the intended action was legible:

- 11 responses wrapped an otherwise plausible object in Markdown fences;
- seven appended extra braces, closing tags, or a duplicate object; and
- one returned a one-element array instead of the required object.

The frozen `json_object` generation assistance did not enforce the declared
bare-object transport. The strict parser correctly rejected these responses
without repair. Repetition varied sharply by situation:

- D3 repeated the same fenced `tree` request seven times before emitting one
  valid object;
- D4 repeatedly re-expressed the same test-file read with extra syntax and
  never recovered within its horizon;
- D5 recovered from one malformed test read on the next call; and
- D6 recovered from two fenced submissions on its third call.

This is not a global inability to express actions. The same profile produced
valid small actions throughout D2 and a valid 3,026-completion-token D5 file
replacement. Expression reliability is state-, task-, and trajectory-dependent.

It is nevertheless a system bottleneck. When calls are scarce, a syntactically
small but rejected action can consume the same decision slot as a substantive
construction or review step.

## D2: coherent integration with one lost qualification

D2 completed the cleanest full workflow in the tranche:

```text
inspect world
→ read paper
→ read evidence update
→ read editorial memo
→ replace paper
→ receive mutation effect
→ run current visible check
→ receive passing check
→ submit
```

The artifact was a strong partial. An independent candidate/task/evidence-bound
review found 12 of 13 frozen criteria met. The Abstract's statement that the
nonrandomized design “does not establish causation” is semantically sufficient
despite the hidden lexical grader missing it. The real remaining defect is in
Discussion: it says differential dropout could bias the association upward,
but does not retain the rubric-required complete-case/no-imputation basis in
that section.

Readiness is therefore `not_ready`, and D2's submission is premature. The
measured adjudication is frozen in `D2_SEMANTIC_ADJUDICATION.json`.

This cell is positive evidence for:

- exact multi-document acquisition;
- cross-source integration;
- a large coherent mutation;
- effect uptake into the following decision;
- current-check uptake; and
- task-native closure behavior.

It is negative evidence for complete qualification preservation and readiness
discrimination when the model-visible checker is narrower than the task.

## D5: large implementation with one governing rule omitted

D5 also traversed the complete action/effect/check/closure path. The actor read
the contract, target, and visible tests; generated a 10,375-byte replacement in
one action; saw the admitted effect; ran the current visible suite; and
submitted a correctly structured final response.

The visible suite passed, but the external evaluator passed only seven of eight
requirements. The implementation did not reject a disabled service when that
service was required by the requested dependency closure. The final response
claimed the implementation covered the contract and did not identify this
defect.

This is a different failure from D2's prose qualification loss, but it has the
same pipeline shape:

```text
broad task understanding
→ substantial construction
→ narrow visible check passes
→ one governing relation remains unmaterialized
→ actor closes anyway
```

The common failure is not lack of work. It is incomplete relation-to-action
binding combined with insufficient verification evidence and overconfident
closure.

## D6: exact reentry reconstituted closure, not correctness

D6 mechanically selected D2, the first changed D2–D5 candidate. Its fresh
packet contained the exact current paper, exact task, current visible-check
state, and identity/reopen receipts while excluding construction chronology,
hidden grading, readiness, and gold material.

The fresh actor immediately attempted to submit. Two attempts were rejected
only because they were fenced; the third was admitted. It did not read,
recheck, or mutate. The candidate remained byte-identical to D2.

This is descriptive evidence that an exact current-state packet can
reconstitute a high-level closure disposition without the construction
transcript. It is not evidence that reentry creates correct semantic
continuity: the inherited candidate was still 12/13 and not ready. D6 repeated
the donor's premature closure rather than discovering the missing
qualification.

D6 therefore separates two questions:

- Can a fresh actor recognize the current work state and choose an appropriate
  action category? Locally, yes: it recognized a closure-shaped state.
- Can that state support correct readiness discrimination? Locally, no.

Because D6 has no matched chronology control and shares D2's lineage, no causal
or transfer claim is made.

## D1, D3, and D4: useful failures rather than capability verdicts

D1's four decisions contained a coherent navigation intent—root followed by
root expansion—but three responses failed admission. Only the root request
executed. This is evidence about action binding/expression under an atlas
interface, not evidence that the model could not choose a useful evidence
branch.

D3 was deliberately included as an ordinary-success calibration world based
on prior sister-program evidence. Here it never got beyond listing the tree:
seven fenced copies of the same action consumed seven calls. The cell is
dominated by interface expression and cannot adjudicate code-repair ability.

D4 made more discovery progress: it listed the world and read the target and
contract. It then spent four calls attempting to read the visible test file
with malformed extra syntax. It never reached construction. Again, the failure
boundary is action admission, not rule formation or implementation quality.

These cells should remain failures in literal task accounting. They should not
be regraded as successful because their intended actions were understandable.
But their claim limit matters: downstream abilities were unobserved rather
than disproved.

## Capability-terrain update

| System function | Evidence from this tranche |
|---|---|
| Exact custody and replay | Strong mechanical positive across all cells |
| Context capacity safety | Inactive; no prompt approached pressure |
| Discovery intent | Visible in D1/D3/D4, but frequently blocked at expression |
| Action admission | Dominant negative: 19/39 rejected responses |
| Multi-source relationship formation | Strong local positive in D2, incomplete qualification retention |
| Relation-to-action binding | Mixed: substantial D2/D5 work, one material requirement omitted in each |
| Large mutation expression | Positive in D2 and especially D5 |
| Effect uptake | Positive in D2/D5: both mutation effects crossed a later model boundary |
| Feedback uptake | Positive for visible checks; negative for coverage sufficiency |
| Repair | Not reached after a model-visible failure in any changed cell |
| Closure | Behaviorally available, but unsafe: three submissions of not-ready artifacts |
| Exact reentry | Reconstituted closure behavior, not independent readiness judgment |

The run supports a broader systems conclusion: the model-facing action and
verification interfaces can dominate behavior long before the context window
does. Improving residency would not have fixed D3's fenced actions, D4's extra
syntax, or the missing D2/D5 requirements.

## Information economics

The tranche used prompt capacity inefficiently in a different way from the
earlier pressure studies. There was ample context, but many prompt-heavy calls
produced tiny rejected expressions:

- D3 spent 11,402 prompt tokens to obtain one admitted `tree` action;
- D4 spent 19,985 prompt tokens to obtain three admitted discovery actions;
- D1 spent 8,201 prompt tokens for one admitted atlas action.

By contrast, D2 spent 19,219 prompt tokens and produced a near-complete paper,
while D5 spent 27,968 prompt tokens and produced a large near-complete code
artifact. Token count alone does not explain utility. The economically relevant
chain is:

```text
information available
× action expressible
× action admitted
× requirements materialized
× verification discriminating
× closure correct
```

A failure in any factor can make the preceding prompt expenditure yield little
or negative task value.

## Supported conclusions

The run supports these local claims:

1. At low context occupancy, action serialization/admission can be a larger
   bottleneck than context capacity for this Qwen3.8 profile.
2. The profile can perform coherent evidence integration and large exact
   artifact construction under the same action surface when expression binds.
3. Visible effect and check uptake do not guarantee complete relation-to-action
   binding or correct readiness.
4. A fresh exact-current-state handoff can preserve a closure disposition
   without preserving or creating a correct completeness judgment.
5. Broad capability mapping exposed qualitatively different failures that a
   longer receipt-only pressure trajectory would not have found.

## Nonclaims

The run does not establish:

- natural-task prevalence of any failure;
- a causal effect of task domain or prompt wording;
- inability on D1, D3, or D4 beyond the observed expression horizon;
- that a different syntax transport would improve artifact quality;
- that visible-check insufficiency alone caused D2 or D5 false closure;
- that exact reentry is better or worse than chronology; or
- a generally preferred context architecture.

No second seed, repaired action protocol, additional call, or successor is
authorized by this result. The correct next program action is to update the
capability terrain and choose any subsequent broad probe by information gain,
not to tune this same interface automatically.
