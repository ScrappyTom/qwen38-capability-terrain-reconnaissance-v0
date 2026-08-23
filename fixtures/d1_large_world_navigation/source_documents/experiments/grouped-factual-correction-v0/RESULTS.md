# Grouped factual correction v0 — results

Date completed: 2026-08-15

Decision: **stop this review-plus-correction package; retain the ordinary loop
as the incumbent comparator**

## Result in one sentence

The grouped reviewer saw the complete task, exact candidate, and every literal
executable packet, but found only 1 of 12 executed defects; the added correction
episodes repaired 0 packets, regressed 0, and left aggregate quality unchanged
at 44/56 while adding 264,174 tokens.

This is a fresh whole-method negative, not a microformat comparison.

## Qualification and custody

Five of the six ordinary first candidates contained at least one executed
packet defect, exceeding the frozen informativeness gate of three. The sixth
cell was a genuine 9/9 ceiling and is reported but contributes no repair
opportunity.

- model: Qwen3.8-27B UD-IQ2_XXS;
- server: llama.cpp b10434, alias `qwen38-27b-iq2-coding`;
- seeds: 42 and 314159;
- all six grouped responses admitted under the frozen schema;
- all twelve ordinary/correction trajectories replay-verified;
- all first and terminal packet catalogs re-executed exactly;
- verification errors: 0; and
- `workbench/` was unchanged.

The measured evidence is in
[`runs/gfc-q38-r001`](runs/gfc-q38-r001). The frozen apparatus copied into the
run remains the authoritative pre-call implementation.

## Per-cell result

| Seed | Task | First packets | Actual first defects | Reviewer defects reported | Review correct | Terminal packets | Net packet delta |
|---:|---|---:|---|---|---:|---:|---:|
| 42 | Session Vault | 7/10 | S01, S05, S09 | none | 7/10 | 7/10 | 0 |
| 42 | Priority Catalog | 7/9 | P07, P08 | none | 7/9 | 7/9 | 0 |
| 42 | Config Overlay | 6/9 | C01, C07, C08 | none | 6/9 | 6/9 | 0 |
| 314159 | Session Vault | 8/10 | S01, S05 | none | 8/10 | 8/10 | 0 |
| 314159 | Priority Catalog | 9/9 | none | none | 9/9 | 9/9 | 0 |
| 314159 | Config Overlay | 7/9 | C01, C08 | C01 | 8/9 | 7/9 | 0 |

The first candidates therefore totaled 44/56 and the terminal candidates also
totaled 44/56. There were zero complete packet repairs and zero regressions.
Five terminal candidate IDs were identical to their first candidate IDs. The
sixth changed source but did not improve an executed packet.

## The reviewer metric that matters

Raw label accuracy was 45/56 (80.36%), but that number is misleading because
44 packets already passed and the reviewer almost always returned `present`.

| Review outcome | Count |
|---|---:|
| Actual passing packets | 44 |
| Actual failing packets | 12 |
| `present` findings | 55 |
| `absent` findings | 1 |
| `cannot_determine` findings | 0 |
| Correct `present` findings | 44/44 |
| Correct `absent` findings | 1/12 |
| Defect recall | **8.33%** |
| Absent-finding precision | 100% (1/1) |
| Balanced accuracy | 54.17% |

An always-`present` response would have scored 44/56. The grouped reviewer
improved that trivial baseline by one label. This is confirmation behavior,
not useful factual verification.

## Correction outcome

The only correctly reported defect, Config C01 at seed 314159, did cause a
related edit. The reviewer had identified that assigning to `Layer.name` did
not raise `FrozenInstanceError`. The correction actor added an `__setattr__`
that raised generic `AttributeError`. The exact executable program catches
`FrozenInstanceError`, so the patched packet terminated with uncaught
`AttributeError`. It also retained the wrong empty-key exception class.

Thus the single captured defect provides one instance of related action but
zero exact repair. It is not enough evidence to make a broad claim that
correct factual findings cannot be used. The dominant failure occurred one
boundary earlier: eleven of twelve real defects were never reported.

## Cost

| Stage | Prompt tokens | Completion tokens | Total tokens | Model HTTP time |
|---|---:|---:|---:|---:|
| Ordinary first candidates | 438,472 | 21,927 | 460,399 | 22.22 min |
| Grouped reviews | 36,585 | 7,809 | 44,394 | 8.23 min |
| Correction episodes | 216,767 | 3,013 | 219,780 | 4.81 min |
| Complete package | 691,824 | 32,749 | 724,573 | 35.25 min |

Review plus correction added 264,174 tokens, or 57.38% over the ordinary
first-candidate cost, and 13.03 minutes of recorded model HTTP time. It
produced no packet-quality gain.

## Interpretation boundary

This result does **not** show that grouped packets are intrinsically worse than
isolated packets. The prior canonical-packet calibration showed grouped and
isolated at the same 51/52 on known development candidates, with isolated
calls costing 4.39 times as many tokens.

It does show that the 51/52 result did not transfer into a reliable reviewer
of fresh Qwen-authored candidates. The literal audit rules out the recurring
insufficient-input explanation: each review contained the complete original
task, every current source file, every packet program, every exact expected
result, and the execution convention. Several responses traced the decisive
branch or ordering correctly and then asserted that the contradictory expected
result would be produced.

The task-author packet catalog remains useful as executable verification. The
model's prediction of those executions is not a substitute for running them.

## Decision and next earned boundary

- Do not promote the grouped reviewer.
- Do not promote the correction handoff.
- Do not add either to `workbench/`.
- Do not tune wording, split packets into separate calls, or add more review
  roles around this negative.
- Retain the ordinary exact action-result loop as the incumbent comparator,
  not as a universal optimum.

The next high-value test, if continued, is mechanically different: execute
the frozen packet programs and give a fresh correction actor the literal
failed receipts—packet ID, exact expected JSON, exact observed JSON or process
error, and current candidate identity—without host advice. That would test
whether exact verification truth can cross into repair, rather than asking a
second Qwen call to predict truth the host can directly establish.

See [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md) for the literal
input/output audit and
[`POSTRUN_VERIFICATION_CORRECTION.md`](POSTRUN_VERIFICATION_CORRECTION.md) for
the bounded post-run reporting correction.
