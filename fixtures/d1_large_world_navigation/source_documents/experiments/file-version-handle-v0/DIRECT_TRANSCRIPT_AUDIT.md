# File-version handle v0 direct transcript audit

Date: 2026-08-16

Scope: all eight `fvh-q38-r003` trajectories, including the saved request at
every read and patch turn, assistant action, tool result, candidate effect,
visible-check result, submission, terminal candidate, and external audit.
This audit does not infer model behavior from the aggregate manifest alone.

## Model-facing controls

Every cell used Qwen3.8-27B UD-IQ2_XXS, llama.cpp b10434, nonthinking mode,
4,096 maximum response tokens, temperature 0.7, top-p 0.8, top-k 20, min-p 0,
presence penalty 1.5, and seed 42 or 314159. Endpoint inspection reported no
profile mismatch.

Within each task/seed pair, the task bytes and initial candidate were the same.
All eight first assistant actions were exactly `tree` on `.`. The intended
model-facing contract difference was present:

- H0's system message said patch requires the current file hash returned by
  `read`, and its patch schema required `expected_file_sha256`;
- H1's system message said patch requires the current run-scoped file-version
  ID returned by `read`, and its patch schema required `basis_id`.

H1 reads still returned the literal SHA alongside the short ID. No card,
semantic status, coaching, retry, argument repair, or automatic action was
added.

## Trajectory-by-trajectory review

### Priority Catalog, seed 42, H0

Qwen read the package, models, and catalog. Its turn-5 models patch supplied:

```text
f967b0b65a0815c209e69cfee92a345140afa4bb948eab299df3368278cf3f33
```

The actual current SHA was:

```text
f967b0b65a0815c209e69cfee92a345140afa4bb948eab299df3368568278cf3
```

The host rejected the exact action as `file_version_mismatch`. Turn 6 repeated
the same file, old span, new span, and intended edit with the actual SHA; it
was accepted and mutated the candidate. This is the one prospective avoidable
raw-identity expression error.

Qwen then made four accepted catalog patches. The only visible check, on turn
11, crashed before evaluating the candidate because `packet_runtime` was
missing. Qwen continued editing and submitted on turn 16. Its external audit
was 40/53, but the broken feedback makes its post-check path unsuitable for a
treatment comparison.

Evidence:
[`turn-005 action`](runs/fvh-q38-r003/c/pc-42/H0_SHA256/trajectory/t/turns/turn-005/action.json),
[`turn-005 rejection`](runs/fvh-q38-r003/c/pc-42/H0_SHA256/trajectory/t/turns/turn-005/tool-result.json),
[`turn-006 action`](runs/fvh-q38-r003/c/pc-42/H0_SHA256/trajectory/t/turns/turn-006/action.json),
[`turn-006 effect`](runs/fvh-q38-r003/c/pc-42/H0_SHA256/trajectory/t/turns/turn-006/tool-result.json),
and [`turn-011 check`](runs/fvh-q38-r003/c/pc-42/H0_SHA256/trajectory/t/turns/turn-011/tool-result.json).

### Priority Catalog, seed 42, H1

Qwen read the same three files, used `FV0003` for the models patch and
`FV0002` for the catalog patch, and both were accepted. Its turn-8 check hit
the same missing-module failure and it submitted on turn 9. The external audit
was 37/53. The shorter path cannot be attributed to the handle because the
model received unusable task feedback and performed less work.

### Priority Catalog, seed 314159, H0

Qwen made three accepted patches with exact current SHAs. Both visible checks
crashed on the omitted runtime. Between them, Qwen attempted `tree` on `..`;
the stable path guard rejected it as `invalid_path`. Qwen submitted on turn 13
with 51/53 external predicates. This cell contains no SHA-expression failure.

Evidence:
[`turn-008 check`](runs/fvh-q38-r003/c/pc-314159/H0_SHA256/trajectory/t/turns/turn-008/tool-result.json),
[`turn-009 path rejection`](runs/fvh-q38-r003/c/pc-314159/H0_SHA256/trajectory/t/turns/turn-009/tool-result.json),
and [`turn-012 check`](runs/fvh-q38-r003/c/pc-314159/H0_SHA256/trajectory/t/turns/turn-012/tool-result.json).

### Priority Catalog, seed 314159, H1

Qwen made two accepted handle-bound patches, encountered the missing runtime
on its only visible check, and submitted on turn 9 with 44/53 external
predicates. There was no handle error. As in the other Priority cells, the
quality and closure path is invalid for comparison.

### Retry Queue, seed 42, both conditions

Both cells followed the same operation sequence:

```text
tree -> read __init__ -> read models -> read queue
     -> patch models -> read queue -> patch queue -> check -> submit
```

Every patch was accepted, both visible checks passed, and both submitted on
turn 9. Both external audits reached 10/12, but the missed predicates differed:
H0 missed lifetime uniqueness and isolated views; H1 missed model freezing and
isolated views. This is not evidence of a handle benefit or harm from one
sample per cell.

### Retry Queue, seed 314159, H0

Qwen made two accepted SHA-bound patches, passed the visible check, and
submitted on turn 9. The external audit reached 9/12, missing constructor
shape, lifetime uniqueness, and isolated views. No raw SHA was corrupted,
invented, or stale.

### Retry Queue, seed 314159, H1

Qwen made two accepted patches, then the visible check exposed a real
`NameError` for `_validate_job_id`. Its next action proposed the correct import
change but reused `FV0003`, which named the pre-patch version of `queue.py`.
The current file was `FV0004`. The host rejected the stale basis without
mutation and reported both the bound and current identities.

Qwen reread `queue.py`, received `FV0004`, applied the same import repair with
that handle, passed the check, and submitted on turn 13. The external audit was
8/12. This demonstrates exact stale-write protection and ordinary recovery; it
does not demonstrate that the handle improves basis tracking.

Evidence:
[`turn-008 failed check`](runs/fvh-q38-r003/c/rq-314159/H1_HANDLE/trajectory/t/turns/turn-008/tool-result.json),
[`turn-009 action`](runs/fvh-q38-r003/c/rq-314159/H1_HANDLE/trajectory/t/turns/turn-009/action.json),
[`turn-009 rejection`](runs/fvh-q38-r003/c/rq-314159/H1_HANDLE/trajectory/t/turns/turn-009/tool-result.json),
[`turn-010 reread`](runs/fvh-q38-r003/c/rq-314159/H1_HANDLE/trajectory/t/turns/turn-010/tool-result.json),
and [`turn-011 repair`](runs/fvh-q38-r003/c/rq-314159/H1_HANDLE/trajectory/t/turns/turn-011/action.json).

## Cross-trajectory interpretation

The exact action evidence supports four bounded findings:

1. A raw 64-character SHA can be transcribed incorrectly by Qwen3.8.
2. The tested short handle removed that error class without admitting stale or
   wrong-path writes.
3. In this screen the raw-hash error appeared in only one of four matched pairs
   and cost one recoverable turn.
4. A short handle did not prevent semantic stale-basis reuse: Qwen still used
   an older handle after mutating the file. Strict rejection and reread worked
   as intended.

The transcripts do not support the raw aggregate token comparison as a handle
effect. They also show why a fourth GPU run is unnecessary: the primary lead
gate fails on the action sequence itself, independently of the invalid
Priority quality data.
