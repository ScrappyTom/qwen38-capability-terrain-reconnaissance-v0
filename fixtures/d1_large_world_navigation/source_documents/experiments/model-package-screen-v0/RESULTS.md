# Model Package Screen v0 Results

## Outcome

No comparator earned promotion over the existing Qwen3.6-27B package, and no
new harness mechanism is earned.

The most useful result is not a model leaderboard. It is a boundary map:

- the current Qwen3.6 package completed every trajectory, used the least
  tokens and time, and submitted only after a visible check passed;
- Qwen3.5 produced one semantically complete paper, but also submitted three
  artifacts after only failed visible checks and exhausted its 25,088-token
  context during construction;
- Gemma produced the only complete reservation repair, but also repeated the
  same one-character-wrong candidate hash for 20 consecutive rejected patch
  attempts and never submitted that incident brief;
- substantive obligation misses occurred in every package;
- the strict schema-action boundary admitted valid actions through the
  terminal state in 17 named trajectories. The remaining trajectory ended in
  a context-length response, not the earlier native-tool delimiter failure.

This supports retaining Qwen3.6 as the default package for this local
workbench. It does **not** show that Qwen3.6 weights, IQ2 quantization,
temperature zero, or 50k context independently caused the result. The frozen
unit is the complete inference package.

## Experimental boundary

The apparatus was frozen in commit
`02af21db80cc5a286365d48c8052511c519978dd` before the first model call. Six
fresh heterogeneous fixtures were run once under each of three locally
qualified packages. Initial candidates failed and goldens passed both frozen
machine boundaries. The project suite passed 248 tests with 14 expected skips
before inference.

For each fixture, the first requests had byte-equivalent `messages` and
`response_format` objects across packages. Only the package-owned model and
inference fields differed. All packages used llama.cpp b10331,
`schema-action-v1`, nonthinking mode, a 4,096-token action ceiling, the same
task bytes, and the same external harness.

The sampled packages retained their qualified recipes rather than forcing a
common sampler:

- Qwen3.6-27B IQ2: temperature 0, top-p 1, top-k 20, no explicit seed, 50,176
  context, q4 KV;
- Qwen3.5-9B Q6: temperature 0.7, top-p 0.8, top-k 20, seed 42, 25,088
  context, q8 KV;
- Gemma 4 12B Q5: temperature 1.0, top-p 0.95, top-k 64, seed 42, 25,088
  context, q8 KV.

Consequently this is a routing screen among deployable local packages, not a
weights-only, quant-only, sampler-only, or context-only comparison. One seeded
trajectory is one observation, not a failure-frequency estimate.

## Named trajectories

`P/F` means passed/failed visible checks. `patches` means accepted patches /
rejected actions. Token columns are saved prompt/completion/total usage. The
last column is the unmodified frozen hidden-grader observation, not the final
semantic adjudication.

| Package | Fixture | Terminal status | Turns | Visible P/F | Patches | Tokens P/C/T | Frozen hidden observation |
|---|---|---:|---:|---:|---:|---:|---|
| `qwen36-iq2-temp0` | quota-window | submitted | 11 | 1/1 | 2/0 | 30,320/970/31,290 | fail: `bad_policy_type` |
| `qwen36-iq2-temp0` | reservation-batch | submitted | 10 | 1/1 | 2/0 | 27,538/1,142/28,680 | fail: `wrong_pair_length`, `negative_available` |
| `qwen36-iq2-temp0` | event-digest | submitted | 12 | 1/0 | 4/1 | 45,796/1,821/47,617 | fail: `event_id_type`, `category_type`, `bool_time` |
| `qwen36-iq2-temp0` | cooling-centers-paper | submitted | 9 | 1/0 | 3/0 | 26,218/855/27,073 | pass |
| `qwen36-iq2-temp0` | cedar-incident-brief | submitted | 12 | 1/1 | 2/0 | 39,206/808/40,014 | fail: `causal_calibration`, `impact_window` |
| `qwen36-iq2-temp0` | freshness-runbook | submitted | 7 | 1/0 | 1/0 | 20,264/619/20,883 | fail: `closure_owner` |
| `qwen35-q6-s42` | quota-window | submitted | 15 | 0/2 | 3/0 | 63,836/1,692/65,528 | fail: `bad_policy_type` |
| `qwen35-q6-s42` | reservation-batch | submitted | 14 | 0/2 | 3/1 | 58,474/2,638/61,112 | fail: `wrong_pair_length` |
| `qwen35-q6-s42` | event-digest | protocol error | 15 | 0/1 | 2/5 | 148,817/15,380/164,197 | not graded |
| `qwen35-q6-s42` | cooling-centers-paper | submitted | 4 | 1/0 | 1/0 | 9,405/1,045/10,450 | fail: `subgroup_status`, `discussion_caution` |
| `qwen35-q6-s42` | cedar-incident-brief | submitted | 14 | 0/2 | 1/1 | 50,133/1,208/51,341 | fail: five named cases |
| `qwen35-q6-s42` | freshness-runbook | submitted | 10 | 1/0 | 4/0 | 39,760/872/40,632 | fail: `closure_owner` |
| `gemma4-12b-q5-s42` | quota-window | submitted | 8 | 1/0 | 2/0 | 22,848/1,170/24,018 | fail: `bad_policy_type` |
| `gemma4-12b-q5-s42` | reservation-batch | submitted | 12 | 1/1 | 4/1 | 48,665/2,075/50,740 | pass |
| `gemma4-12b-q5-s42` | event-digest | submitted | 8 | 1/0 | 2/1 | 29,074/1,780/30,854 | fail: `event_id_type`, `category_type` |
| `gemma4-12b-q5-s42` | cooling-centers-paper | submitted | 7 | 0/0 | 3/0 | 18,615/913/19,528 | fail: `subgroup_status` |
| `gemma4-12b-q5-s42` | cedar-incident-brief | turn limit | 24 | 0/1 | 1/20 | 162,469/5,334/167,803 | not graded |
| `gemma4-12b-q5-s42` | freshness-runbook | submitted | 6 | 0/0 | 1/0 | 16,844/563/17,407 | fail: five named cases |

## Package-level factual metrics

### Terminal and action state

| Package | Terminal states | Turns | tree/read/search/patch/check/submit | Accepted patches | Rejected actions | Checks P/F | Submitted with no check | Submitted after only failed checks | Exact response recurrences | Context ceiling |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Qwen3.6 | 6 submitted | 61 | 6/24/1/15/9/6 | 14 | 1 | 6/3 | 0 | 0 | 4 | 0 |
| Qwen3.5 | 5 submitted; 1 protocol error | 72 | 4/30/2/21/9/5 | 14 | 7 | 2/7 | 0 | 3 | 17 | 1 |
| Gemma | 5 submitted; 1 turn limit | 65 | 5/15/0/35/5/5 | 13 | 22 | 3/2 | 2 | 0 | 20 | 0 |
| **All** | 16 submitted; 1 protocol error; 1 turn limit | **198** | **15/69/3/71/23/16** | **41** | **30** | **11/12** | **2** | **3** | **41** | **1** |

The rejection codes were exact machine observations:

- Qwen3.6: one `patch_not_applicable`;
- Qwen3.5: six `no_op_patch` and one `patch_not_applicable`;
- Gemma: 21 `file_version_mismatch` and one
  `patch_not_applicable`;
- overall: 21 `file_version_mismatch`, six `no_op_patch`, and three
  `patch_not_applicable`.

The 20 Gemma incident recurrences are not inferred from similar intent. The
assistant response bytes and rejected action were identical. The expected
file hash contained `...37264d3c...`; the exact current hash returned on every
rejection contained `...37264d8c...`.

### Usage and elapsed time

| Package | Cached prompt | Prompt | Completion | Total | Model time | Recorded wall time |
|---|---:|---:|---:|---:|---:|---:|
| Qwen3.6 | 157,995 | 189,342 | 6,215 | 195,557 | 360.150 s | 367.625 s |
| Qwen3.5 | 316,257 | 370,425 | 22,835 | 393,260 | 706.644 s | 713.403 s |
| Gemma | 260,210 | 298,515 | 11,835 | 310,350 | 432.692 s | 438.960 s |
| **All** | **734,462** | **858,282** | **40,885** | **899,167** | **1,499.486 s** | **1,519.988 s** |

These are server-reported usage fields summed as recorded. They should not be
recomputed from one another: llama.cpp's per-turn `total_tokens` field is not
always the arithmetic sum of its prompt and completion fields in the saved
responses.

### Evidence volume

| Package | Request bytes | Response bytes | Preserved run files | Preserved run bytes |
|---|---:|---:|---:|---:|
| Qwen3.6 | 769,942 | 1,181,557 | 1,272 | 6,872,999 |
| Qwen3.5 | 1,493,874 | 2,108,701 | 1,367 | 10,575,284 |
| Gemma | 1,017,259 | 1,474,161 | 1,256 | 8,129,359 |
| **All** | **3,281,075** | **4,764,419** | **3,895** | **25,577,642** |

The complete per-run extraction also records action sequence, every rejection
message, every check result and candidate binding, reads and rereads, searches,
candidate-version count, last mutation, post-mutation reads, maximum per-turn
usage, finish reasons, provider-observed seed, final/submitted candidate IDs,
record count, and exact-response hashes. Those facts are in
[`metrics.json`](metrics.json); [`analyze.py`](analyze.py) deterministically
rebuilds the file from the raw runs.

## Semantic artifact findings

The frozen hidden boundary reported two machine passes: the Qwen3.6 paper and
the Gemma reservation repair. It reported 14 failures and did not grade two
unsubmitted trajectories. That is a factual description of the instrument,
not a quality score.

Direct task-and-artifact review identified four fully complete submitted
artifacts by name:

- Qwen3.6 paper;
- Qwen3.6 runbook;
- Qwen3.5 paper;
- Gemma reservation repair.

The two other runbooks contained all operational rules but had citation-form
defects: Qwen3.5 left literal `Cite ...` instructions in the artifact, and
Gemma invented composite forms such as `[M02, C1]` instead of the exact source
handles. The remaining submitted artifacts each missed at least one explicit
obligation. The two unsubmitted terminal candidates were not treated as
submissions.

The difference between the frozen grade and the artifact review matters:

- Qwen3.6's runbook is a machine false negative caused by
  `service-owner` versus `service owner`;
- Qwen3.5's paper states that the subgroup was exploratory, not preregistered,
  and not evidence that effects differed, and it uses association language;
  its grade expected narrower vocabulary;
- Qwen3.6's incident really does have a source-binding omission for the impact
  window even though its causal wording is adequate;
- Gemma's paper really does omit “not preregistered” and makes the unsupported
  recommendation to expand to every neighborhood.

The full obligation map and all 18 judgments are in
[`ADJUDICATION.md`](ADJUDICATION.md). Frozen grader output remains unchanged in
the raw run directories.

## What the trajectories say

### 1. Relationship-use failure is not Qwen3.6-specific

Gemma received the literal current file hash on 20 consecutive
`file_version_mismatch` results and repeated the same old expected hash every
time. Qwen3.5 received literal failed visible-check cases, repeated failed
checks in three tasks, and submitted anyway. Those are direct examples of
available machine facts failing to control the next transition in two other
packages.

This weakens any model-specific explanation of the prior Qwen3.6 failures. It
does not prove one universal cause: the failure surfaces differ, and every
package was observed only once per named task.

### 2. The Qwen3.6 package fits this harness better than the comparators

Qwen3.6 was the only package to submit every task and to condition every
submission on a passed visible check. It also used fewer turns, prompt tokens,
completion tokens, model time, and rejected actions than either comparator.
Its failures on these tasks were mostly narrow contract completeness,
type/value error classification, or source binding rather than action-boundary
collapse.

That is enough to retain it as the workbench default. It is not enough to say
temperature zero is generally superior. Temperature, model, quant, context,
KV, and sampler moved together as qualified packages.

### 3. Visible checks influenced packages differently and did not certify the task

All six Qwen3.6 submissions followed a passed visible check. Qwen3.5 submitted
quota, reservation, and incident after only failed checks. Gemma submitted two
writing tasks without running a check. Meanwhile, several visible passes still
left explicit hidden or investigator-observed obligations unmet.

The appropriate lesson is not “add more semantic gates.” It is that visible
checks are bounded instruments and that package behavior around them is an
important routing property. The host should continue recording exactly which
candidate a check covered without pretending the check proves semantic
sufficiency.

### 4. Schema-constrained actions continue to solve the serialization boundary

The strict action union produced admitted actions across Qwen, Qwen3.5, and
Gemma without client-side XML, argument repair, or a second tool protocol. The
only non-admitted terminal response occurred after Qwen3.5 filled its 25,088
context on the construction task; `finish_reason` was `length` and the final
turn used exactly 25,088 tokens.

This preserves the earlier conclusion: schema-constrained JSON is a removable
model-server interface that eliminates the recurring native-delimiter class
for this local ecology. It does not make the model choose or use actions well.

### 5. Grader brittleness is now an experimental-process issue

The direct review found both false negatives and real misses hidden behind
false-negative case names. A semantic grader inside the live harness would
recreate the host-authority problem. The defensible process is instead:

1. freeze task-derived mechanical instruments prospectively;
2. preserve their exact output even when imperfect;
3. inspect the actual prompts, responses, actions, results, and final bytes;
4. publish a clearly labeled investigator adjudication alongside, not over,
   the machine result.

Future fixtures should make literal checks robust to harmless hyphenation and
task-equivalent wording where that can be specified mechanically. The frozen
fixtures and results here should not be retroactively changed.

## Decision

- Keep the workbench and schema-action interface frozen.
- Keep Qwen3.6-27B IQ2 temperature zero as the default local package.
- Do not promote Qwen3.5 or Gemma from this screen. Gemma's reservation result
  is a task-specific lead, not a recurring advantage.
- Do not add cards, plans, semantic status, retries, argument repair, automatic
  rereads, submission coaching, or a stronger gate.
- Stop this screen rather than tune around any of the six tasks.
- Treat package choice, context allocation, action ecology, and verification
  behavior as coupled routing variables in future work.

The next useful work is not another factual projection. Use the stable lab for
real fresh tasks, preserve trajectories, and screen a new package only when an
independently justified candidate or a concrete routing question appears.

## Reproduction and evidence

- Apparatus: [`PROTOCOL.md`](PROTOCOL.md), [`QUALIFICATION.md`](QUALIFICATION.md),
  and [`matrix.json`](matrix.json)
- Exact raw trajectories: [`../../runs/model-package-screen-v0`](../../runs/model-package-screen-v0)
- Factual extraction: [`analyze.py`](analyze.py) and [`metrics.json`](metrics.json)
- Investigator artifact review: [`ADJUDICATION.md`](ADJUDICATION.md)

All 18 raw run directories replay-verified after completion. This is local
validation, not GitHub Actions verification.
