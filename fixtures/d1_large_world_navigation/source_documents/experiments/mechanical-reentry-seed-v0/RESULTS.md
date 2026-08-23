# Mechanical reentry seed v0 results

Status: **complete; mechanical orientation effect observed, no continuation
policy qualified**

## Result

The proposed middle ground exists, but its value is narrower than expected.
A corrected custody-derived seed reduced orientation actions relative to bare
fresh-world reentry while preserving terminal quality. It did not carry enough
substance to replace reacquisition of the exact files that governed the new
work, and its repeated payload increased token traffic without reducing
recorded model time.

The first M executions are excluded because a reducer defect erased their
Phase-A action facts. Direct prompt inspection found the defect before result
interpretation. The exact invalid cells, correction, and corrected M-only
rerun are all preserved; see `SEED_RECORD_BINDING_CORRECTION.md`.

## Terminal quality

- Code: T, W, and corrected M each passed all 10/10 external groups and
  submitted. W produced the most complete model-authored test suite; all three
  test suites still omitted part of the explicit validation matrix.
- Research: all three passed the 12/12 supporting audit and submitted. Direct
  review scored W and corrected M at 11/11 semantic criteria. T had 10 met and
  1 partial due one unsupported explanation of the cost planning range.
- No primary continuation had a rejected action, failed check, incomplete
  response, stale-source citation, or superseded-policy recommendation.

## Measured continuation behavior

| Task | Arm | Calls | First mutation | Reads / bytes | Phase-A paths reread | Total tokens | Uncached prompt | Max prompt | Model time |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Code | T | 6 | 2 | 2 / 4,265 | 2 | 62,763 | 5,839 | 12,708 | 102.6 s |
| Code | W | 11 | 8 | 6 / 6,155 | 4 | 50,211 | 8,257 | 8,661 | 120.6 s |
| Code | M | 9 | 6 | 5 / 5,990 | 4 | 62,866 | 10,398 | 10,366 | 117.2 s |
| Research | T | 9 | 7 | 6 / 4,619 | 2 | 102,986 | 7,002 | 14,571 | 74.8 s |
| Research | W | 10 | 8 | 6 / 4,619 | 2 | 53,942 | 7,998 | 8,605 | 73.5 s |
| Research | M | 9 | 7 | 6 / 4,619 | 2 | 84,620 | 11,573 | 12,184 | 78.7 s |

Across both workflows:

| Arm | Calls | Read bytes | Total tokens | Uncached prompt | Model time |
|---|---:|---:|---:|---:|---:|
| T | 15 | 8,884 | 165,749 | 12,841 | 177.4 s |
| W | 21 | 10,774 | 104,153 | 16,255 | 194.1 s |
| M | 18 | 10,609 | 147,486 | 21,971 | 195.9 s |

Relative to W, M used three fewer calls (14.3%) but 43,333 more total tokens
(41.6%) and essentially the same recorded model time (+0.9%). Relative to T,
M used three more calls, 11.0% fewer total tokens, and 10.4% more model time.
Prompt caching explains part of the apparent transcript paradox: 92.1% of T's
prompt tokens were cached, versus 83.9% for W and 84.8% for M.

## What the seed did

M skipped `tree` in both workflows. In code it also skipped one 165-byte model
definition. It did not reduce rereads of the code target, contract, tests,
editorial review, index, or new governing evidence. The model treated the seed
as orientation metadata, not as a substitute for exact operative content.

That is a real whole-method effect: mutation began two calls earlier in code
and one call earlier in research. It is not a general efficiency win. The
4.6-KB and 7.8-KB canonical seeds occupied every later request, raised maximum
prompt occupancy, and produced no terminal-quality advantage over W.

T behaved differently. It reused exact still-current Phase-A observations in
code and therefore needed only two rereads. In research, H7/H8/H9 were new, so
T reacquired the same six substantive objects as W and M. This directly
supports the distinction between content continuity and mechanical
orientation.

## Decision

Corrected M did **not** satisfy the strict frozen qualification gate. It
matched best product and research quality, introduced no stale or unsupported
claim, reduced calls to mutation/closure relative to W, and kept more per-call
headroom than T. But W produced the stronger linked code-test artifact, and M
did not improve semantic reacquisition, total token cost, or recorded model
time. The complete method therefore does not match the best observed outcome
across the separately declared quality and efficiency boundaries.

The practical ranking is multidimensional:

- T is best when still-current exact observations are reusable and its history
  remains within the working envelope.
- W is the simplest and lowest-token restart when current world plus task can
  be reacquired cheaply.
- M is a bounded map-like compromise when reducing orientation calls matters,
  but this implementation does not reduce GPU time or semantic reacquisition.

No component of the seed is isolated. The result does not earn a summary,
checkpoint, automatic reset, phase detector, router, semantic invalidator, or
permanent card. It also does not justify shrinking the complete task frame.

## Recommendation

Stop synthetic phase-policy comparisons here. Preserve M as removable
experimental apparatus, with W as the minimum restart rather than turning the
seed into architecture. On the next authentic multi-phase
coding or research job that naturally creates a meaningful boundary, record
the same facts and choose the continuation prospectively. The next study
should be triggered by a real observed cost or continuity failure, not by a
desire to tune the seed.

The main engineering requirements remain simpler and better supported:
durable exact custody, a complete task/purpose frame, exact current world,
ordinary navigation, literal discriminating receipts, and mechanically
feasible actions. Transcript is phase-local working memory; it is neither the
durable world nor automatically disposable noise.
