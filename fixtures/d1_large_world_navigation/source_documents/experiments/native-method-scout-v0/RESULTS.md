# Native method scout v0

Date: 2026-08-11/12

Status: **exploratory course correction; evidence preserved, no harness
promotion**

## Decision in one paragraph

The recent project held one agent ecology fixed and varied model-facing facts
inside it. Direct review of Framebridge's June-to-early-July history and the
active context experiments shows that this was too narrow. Those projects
changed the work method when the model resisted: navigation topology, action
representation, executable feedback, editing affordances, workflow seats, and
sampling all mattered. A small native Pi scout now supplies the same warning
locally. Qwen3.6-27B used ordinary `read`/`bash`/`edit`/`write` tools to escape
failure paths that persisted in the schema-action loop, including the exact
bounded-cache sequence defect. It did not become a complete semantic auditor:
it still omitted explicit requirements, and both a fresh reviewer and a
model-authored 16-check contract suite certified a known-incomplete artifact.

Keep the custody workbench as a stable observer, fixture runner, snapshotter,
and grader. Stop assuming its bounded action loop is the only agent method to
study. The next project line is whole-method scouting followed by direct
trajectory inspection, not another sequence of factual cards or closure
messages.

## What was personally inspected

This review did not rely on the cross-repository summaries. The investigator
read the historical designs, source, saved prompts, raw assistant/tool
transcripts, check outputs, and final artifacts directly.

### Framebridge, June 22 through early July

The relevant history is a sequence of materially different methods, not one
architecture converging monotonically:

- The June 24 read-loop work retracted a claimed model floor after changing
  the action from free quote generation to exact host-adopted span selection.
  Binary self-verification and vague obligations were weak; contrastive exact
  selection was much stronger. See the pinned
  [branch learnings](https://github.com/ScrappyTom/framebridge/blob/d46b81ffa666ace5ab614da12e41d06aa6c1cfb6/experiments/BRANCH_LEARNINGS.md).
- The June 24-25 navigation branch found that a flat action menu produced
  circling, while one-obligation-at-a-time steering, exact numbered-line
  selection, and model-planned structural navigation changed the result. A
  need-specific configuration-resolution transform helped the look-alike case;
  this was not evidence for one universal view. See the pinned
  [navigation findings](https://github.com/ScrappyTom/framebridge/blob/d46b81ffa666ace5ab614da12e41d06aa6c1cfb6/experiments/NAV_FINDINGS.md).
- The June 26 agent comparison found that Hermes and MiMo adaptively read
  neighborhoods that the fixed Framebridge mechanism under-read. A leaner
  grounded read loop later reached the same score band with fewer factual
  errors. Adding cross-file or same-file periphery then made the 4B result
  worse. See the pinned
  [agent benchmark findings](https://github.com/ScrappyTom/framebridge/blob/d46b81ffa666ace5ab614da12e41d06aa6c1cfb6/AGENT_BENCHMARK_FINDINGS.md).
- On June 27, the same small model drove a bare native-tool edit ladder through
  read, propose, verify, and commit without reducer-controlled action schemas.
  The implementation is preserved in
  [`grounded_edit_readloop.py`](https://github.com/ScrappyTom/framebridge/blob/d46b81ffa666ace5ab614da12e41d06aa6c1cfb6/grounded_edit_readloop.py).
- On a real SPAR failure, greedy decoding produced a stable wrong-reasoning
  attractor. The measured Qwen sampler changed the same loop from 0/6 to 2/3
  verified passes. That is evidence that apparent workflow resistance can be
  decoding ecology, not missing state. See the pinned
  [reality arc](https://github.com/ScrappyTom/framebridge/blob/d46b81ffa666ace5ab614da12e41d06aa6c1cfb6/REALITY_ARC.md).
- Later contract and autonomy work changed the topology again: model-drafted
  tests, a separate review phase, executable contracts, independent builders,
  and mechanical selection. Those runs were expensive and imperfect, but they
  are not variants of a current-state card. See the pinned
  [contract loop](https://github.com/ScrappyTom/framebridge/blob/d46b81ffa666ace5ab614da12e41d06aa6c1cfb6/CONTRACT_LOOP.md)
  and [autonomy arc](https://github.com/ScrappyTom/framebridge/blob/d46b81ffa666ace5ab614da12e41d06aa6c1cfb6/AUTONOMY_ARC.md).

The durable Framebridge lesson is therefore not merely "avoid host
semantics." It is: **when a faithful loop produces a stable failure, reconsider
the entire interaction method before adding another message to that loop.**

### Active context experiments

The active repository independently supports the same correction:

- Its
  [continuous-loop protocol](https://github.com/ScrappyTom/Context_Management_Test_07.18.2026/blob/9c401ceeabacc7f120dfed2adfeda414dad202c6/CONTINUOUS_LOOP_PROTOCOL.md)
  deliberately uses full ordinary history, mechanical tools, and no semantic
  human intervention, compaction, ranking, plan, or checklist.
- Direct review of the committed Qwen3.6 MoE Jinja trajectory found a complete
  read/edit/test/submit path in that nearly bare loop. Direct review of the 9B
  trajectory found that the model often knew the right code region but fought
  the exact-patch and command affordances: corrupt patches, shell redirection
  passed as arguments, and disallowed alternatives. The raw Qwen3.6
  [transcript](https://github.com/ScrappyTom/Context_Management_Test_07.18.2026/blob/9c401ceeabacc7f120dfed2adfeda414dad202c6/continuous_loop_runs/coding01-qwen36-moe-20260719-204616/transcript.json)
  and 9B
  [transcript](https://github.com/ScrappyTom/Context_Management_Test_07.18.2026/blob/9c401ceeabacc7f120dfed2adfeda414dad202c6/continuous_loop_runs/coding01-20260719-173606/transcript.json)
  preserve what each model actually saw and emitted.
- In the active evidence-selection case, a generic self-audit saw the exact
  material and still blessed the central selection. A targeted decision
  question that separated pre-payment insurer failures from post-payment
  diversion changed the model's analysis. An equal-priority set-cover question
  then recovered the omitted source. This was not more information; it was a
  different decision problem. See the committed
  [adjudication](https://github.com/ScrappyTom/Context_Management_Test_07.18.2026/blob/9c401ceeabacc7f120dfed2adfeda414dad202c6/evaluation_notes/active_qa_adjudication.md).

These observations involve other Qwen sizes and packages. They are method
evidence, not a performance estimate for the current 27B quant.

## Local scout setup

The scout used:

- Pi release `v0.84.1`, commit
  `53fa77ccd8a279eb87e92294ef3687b03ff80112`;
- Node `v24.19.0` from the official Windows distribution;
- llama.cpp `b10331-7ba604f1c` at `http://127.0.0.1:8080/v1`;
- model alias `qwen36-27b-iq2-coding`, 50,176 context, nonthinking;
- temperature 0, top-p 1, top-k 20, min-p 0, maximum completion 4,096;
- native OpenAI-style function calls, streaming, no forced tool choice, and
  `parallel_tool_calls: false`; and
- Pi's unmodified default coding prompt and its four ordinary tools: `read`,
  `bash`, `edit`, and `write`.

A read-only Pi provider hook recorded every final serialized request without
changing it. The session JSONL records every user, assistant, tool-call, and
tool-result object. Provider logs include the exact system prompt, tool
schemas, sampling fields, and replayed history.

The model could read the visible-check source. That is part of this native
coding ecology and a material difference from the workbench's candidate-only
world. The scout therefore compares bundles, not editors in isolation.

The first dispatch run accidentally placed observer files in the working
directory. They appeared in the initial `ls` result but were never opened.
All later logs and checks were outside the candidate workspace.

## Exact observed runs

Pi usage below is the sum of its recorded uncached input, cache-read, and
output tokens. It is not directly interchangeable with the workbench's prompt
token accounting. A tool error includes an intentionally failing check as well
as malformed tool arguments.

| Run | Assistant calls | Tool results / errors | Recorded tokens | Machine result | Direct artifact judgment |
|---|---:|---:|---:|---|---|
| Dispatch builder | 25 | 24 / 6 | 132,562 | visible 4/4; hidden 11/12 | Missed lifetime item-ID uniqueness. |
| Bounded-cache builder | 15 | 14 / 1 | 70,268 | visible 4/4 after one failure; hidden 12/12 | No explicit core-contract miss found in direct spot review. |
| Reservation builder | 14 | 13 / 2 | 51,829 | visible 5/5; hidden 13/13 | Still returns `ValueError` for a non-string line SKU and non-integer/bool availability, where the task requires `TypeError`. |
| Fresh dispatch reviewer | 18 | 17 / 1 | 96,224 | visible 4/4; hidden 11/12 | Made no edit and declared the incomplete artifact correct. |
| Executable-contract reviewer | 21 | 20 / 3 | 144,112 | self-authored checks 16/16; visible 4/4; hidden 11/12 | Its 13.7 KB suite omitted lifetime uniqueness, then certified the omission. |

Across the five runs, 93 assistant responses and 88 native tool calls completed
without the earlier first-turn delimiter collapse. That does not establish a
native-tool reliability rate. Pi's prompt, streaming behavior, `tool_choice`
policy, and tool set all differed from the earlier Contact request. Qwen also
placed literal quote characters inside three dispatch path arguments; Pi
rejected them, and the model escaped through `bash` or `edit` rather than
requiring client repair.

### Dispatch construction

The model read the fixture and visible check, wrote a monolithic implementation
and README, repaired a package-relative import, passed the visible check, and
stopped. Its initial implementation already satisfied more of the task than
the two prior schema-action artifacts:

- original 4K schema creation: 8/12 hidden cases in 23 calls;
- exact-diagnostic schema run: 9/12 hidden cases in 15 calls; and
- native Pi scout: 11/12 hidden cases in 25 calls.

The remaining defect was not a transition error. The implementation never
recorded item IDs after completion, despite the exact task sentence being in
the first and every subsequent provider request.

### Bounded-cache construction

The first native implementation reproduced the exact sequence bug from the
ordinary schema-action run: updating an existing key consumed a new sequence.
The visible check returned the expected and observed sequence values. Qwen's
next action was a targeted `edit` of `put`; the next check passed, and the
frozen hidden grade was 12/12.

For the same task, the prior ordinary schema run used 22 calls, repeated the
same literal failed check, emitted six exact no-op whole-file patches, and
submitted 11/12. The direct-thinking run used 7 calls and reached 12/12. The
native result shows that the thinking result was not unique evidence for a
reasoning toggle: a different ordinary action ecology also made the failure
usable, although less efficiently than that thinking trajectory.

### Reservation repair

The native run fixed duplicate aggregation, original ordering, missing SKU,
atomicity, pair shape, bool quantity, and negative availability. It passed all
frozen machine cases. Direct task-to-code review nevertheless found three
wrong-type classifications outside that grader's coverage. This is a concrete
example of why machine grade and investigator semantic review must remain
separate even when the machine score is perfect.

### Review topology

The generic fresh reviewer had the full task, artifact, visible check, shell,
and edit authority. It wrote several ad hoc probes, reran the passing check,
and declared all requirements satisfied without testing reuse of an ID after
completion.

The stronger contract reviewer was told to encode every explicit requirement
as black-box checks before judging the artifact. It produced 16 named checks,
fixed a bug in its own check suite, obtained 16/16, reread the implementation,
and again declared it complete. Its suite tested sequence numbers and separate
instances but never tested lifetime uniqueness. No candidate byte changed.

This reproduces an old Framebridge boundary in a cleaner form: model-authored
formal state or tests can externalize work, but they are not authoritative
coverage merely because they execute.

## What this changes

The project had frozen both the laboratory and the method. Only the laboratory
should have been frozen.

The stable laboratory remains:

```text
fixture/world -> exact records -> snapshots/versions -> external checks
              -> transcript inspection -> investigator adjudication
```

The agent method becomes an experimental operand:

```text
schema action loop | native Pi | another native agent | staged seats
adaptive navigation | executable oracle | sampled/thinking mode
```

This does **not** earn a Pi integration into the workbench, removal of the
schema-action seam, a mandatory reviewer, automatic test generation, or a new
card. It earns a change in experimental strategy.

## Resistance policy

Use the observed resistance to choose a different method class instead of
rendering another reminder:

| Observed resistance | Next method worth scouting |
|---|---|
| Repeated malformed or no-op edits despite a correct local diagnosis | A different native editing/tool ecology. |
| A check names a failure but exposes no discriminating operands | A better executable observation or direct test inspection. |
| The same belief/action repeats under identical deterministic history | A measured sampler/thinking package or fresh session, not another state restatement. |
| Navigation repeatedly reopens the wrong neighborhood | Model-planned structural navigation or a need-specific transform. |
| A visible check passes while explicit obligations remain unused | Do not add a generic reviewer; seek independent executable coverage or a genuinely different decision decomposition. Keep investigator grading. |
| Evidence is present but the model answers the wrong comparison | Reframe the decision question or obligation partition; do not merely append more evidence. |

## Next work

1. Run one genuinely new, real repository task under native Pi with the
   observer outside the loop. Use ordinary project tests rather than a
   synthetic visible/hidden split where possible.
2. Inspect the exact request, all tool transitions, final diff, tests, and task
   obligations. Treat the whole Pi ecology as the condition.
3. If it encounters a stable failure, change method class once: use Hermes or
   a targeted executable/decision topology selected from the failure shape.
   Do not tune Pi's prompt around the observed task.
4. Only after a method changes behavior on a fresh task should the project ask
   which smallest removable element caused the gain.

The goal is exploration with custody, not a tournament and not a universal
agent architecture.

## Preserved evidence

The [`raw`](raw/) directory contains exact Pi session histories and exact
serialized provider-request logs for all five runs. The
[`final-artifacts`](final-artifacts/) directory contains the three builder
artifacts used in direct review. The complete model-authored contract check
and its later self-repair are preserved as literal `write` and `edit` calls in
`dispatch-contract-review.session.jsonl`; the generated file contained
intentional trailing whitespace and is not normalized into a second source
artifact.

Raw evidence SHA-256 values:

```text
798203ebbd1d31e00bc3d72ad27b30630a7c5cb1298ad0793fd1014972c718c6  bounded-cache-builder.provider-requests.ndjson
90e13e5acda3ee7b86e73fabf39e8c0e3c7fddcf0b06886611f59e2bccc1ddfb  bounded-cache-builder.session.jsonl
024505c4455ce4fcbdf7c83c1f739d15d2cd6af44289ebb46c6ce61fd2e0ee27  dispatch-builder.provider-requests.ndjson
4e73b634c104e85f8325fe7fa867be6f093984e35d4defba5b8ac6ceadeae4be  dispatch-builder.session.jsonl
b520305c5e4d2dfc3064af9af7c180d04446e71c953a4da2774d4bb9ee6c32df  dispatch-contract-review.provider-requests.ndjson
037d94014986a521ba4a18c1bdf98a7a40f4381a63d3b90576269fce535a36b1  dispatch-contract-review.session.jsonl
1df0cda38d296e71130284a88462a3fbd08daae294e9a8ada8e3fe3a16bf0014  dispatch-generic-review.provider-requests.ndjson
1f4f304114d57182a4441917e82558fb0846807a4f5edf4152d65de2303f3317  dispatch-generic-review.session.jsonl
3bf944dcce19bedb560835a05500f170a1ac42795ecc58ae97074650e394bf84  reservation-builder.provider-requests.ndjson
0a48f9b4cb0c47b439860ff46785cb779759de8ee871fabcfe710338cacf258a  reservation-builder.session.jsonl
```

This is local exploratory evidence, not CI verification or a prospective
benchmark.
