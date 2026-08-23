# Qwen3.8 Factual Zoom Ladder v0 Results

Run: `qwen38-factual-zoom-ladder-v0-run-001`

Date: 2026-08-14

## Result in one sentence

A clause-only factual frame recovered three of four defects that the prior
one-requirement compliance review missed while preserving all four satisfied
controls; removing two unrelated package files recovered the fourth defect,
so no smaller decision slice was triggered.

## What changed from the prior atomic review

The prior atomic review still showed the complete task and asked for a
`fully_satisfied` judgment on a compound requirement. This diagnostic changed
the whole decision frame:

- one self-contained factual predicate;
- no original task or other requirements;
- `present`, `absent`, or `cannot_determine`, rather than compliance status;
- one fresh inference;
- exact code only; and
- no tools, repairs, checks, or overall verdict.

Therefore the first-level result identifies a useful **clause-only factual
method package**. It does not isolate whether the active ingredient was clause
decomposition, removing the background task, or replacing the compliance
label.

## Adaptive progression

| Pair | Prior atomic review | Clause + full package | Clause + target file | First pair success |
|---|---:|---:|---:|---|
| R10 resource validation | false support | defect missed; control correct | defect and control correct | target file |
| R11 resource validation | false support | defect and control correct | not run | full package |
| S08 apply-ID reuse | false support | defect and control correct | not run | full package |
| S12 reversal-ID reuse | false support | defect and control correct | not run | full package |

At the broadest new level:

- 8/8 calls were admitted;
- 7/8 findings were correct;
- 3/4 genuine defects were detected;
- 4/4 satisfied controls were confirmed;
- there were no false defect findings; and
- there were no `cannot_determine` findings.

Only R10 advanced. At the full-target-file level, both the defect and control
were correct. The frozen rule therefore stopped the ladder before the exact
decision-slice level.

## The R10 transition

The question was byte-identical across the two calls. The complete
`calendar.py` bytes were also identical. The second view removed only
`reservation_calendar/__init__.py` and `models.py`:

| Measure | Full package | Target file | Change |
|---|---:|---:|---:|
| Code files | 3 | 1 | -2 |
| Code bytes | 3,852 | 3,617 | -235 (-6.1%) |
| Prompt tokens | 1,418 | 1,210 | -208 (-14.7%) |
| Total tokens | 1,665 | 1,423 | -242 (-14.5%) |
| HTTP/model time | 16.10 s | 13.41 s | -16.7% |

With the full package, Qwen asserted that `_validate_string` raises `TypeError`
for a non-string even though the exact helper contains one `ValueError` branch
for both non-string and empty values. Its purported literal evidence was a
nonliteral stitched block.

With only the target file, Qwen quoted the exact helper and correctly answered
`absent`:

> The helper `_validate_string` raises `ValueError` if the value is not a
> nonempty string. Therefore, it does not raise `TypeError` for non-string
> types.

This is a real within-run information-view divergence. One trajectory cannot
establish that the extra 235 bytes caused the error reliably; it can establish
that the complete candidate was not necessary and that the narrower exact
file supported the correct discrimination without harming its paired control.

## Why the other three changed

R11 asked the same helper distinction as one direct factual question. Qwen
correctly identified that `_validate_string` raises `ValueError` for both
cases.

S08 asked whether `apply` checks `batch_id` against `_used_ids` before
mutation. Qwen answered `absent` and correctly distinguished recording an ID
from enforcing uniqueness. In the prior atomic review it had explicitly said
that `apply` lacked this check and nevertheless emitted `fully_satisfied`.

S12 asked the cross-operation question directly: after `reverse` records a
reversal ID, does a later `apply` reject it? Qwen correctly answered `absent`.
The prior compound review focused on what `reverse` itself did and failed to
carry the lifetime invariant into the later `apply` operation.

## Evidence fidelity

Semantic findings were correct in 9/10 adaptive calls, but literal-evidence
fidelity was only 8/10:

- the incorrect R10 full-package call fabricated a stitched excerpt and
  misreported the helper behavior; and
- the correct S12 control appended stray JSON-like punctuation to an otherwise
  literal line.

The factual frame improved discrimination; it did not make every evidence
field exact.

## Cost

The adaptive run made 10 calls:

- 14,831 prompt tokens;
- 2,107 completion tokens;
- 16,938 total tokens;
- 1,080 cached tokens; and
- 139.96 seconds of summed HTTP/model time.

These totals describe this diagnostic ladder, not a fair cost comparison to a
complete reviewer. The ladder examined only four known defect/control pairs.

## Decision

The result earns prospective testing of **clause-level factual verification**
as a removable post-construction method. It does not earn a generic reviewer,
a semantic compliance label, or an automatic context router.

The next prospective method should use fresh code tasks and preserve the
complete work boundary:

1. Qwen constructs its first candidate normally.
2. A task-author factual checklist asks one directly decidable question per
   written contract group.
3. Each question starts with the full relevant file or package; narrower exact
   views are requested only after an incorrect or indeterminate finding.
4. A fresh actor receives the factual findings and may repair.
5. Complete task-faithful executable checks establish the final behavior.

That next study must separately score factual capture, evidence fidelity,
finding-to-repair uptake, final behavior, and cost. The present known-case
scout does not establish any of those prospective rates.
