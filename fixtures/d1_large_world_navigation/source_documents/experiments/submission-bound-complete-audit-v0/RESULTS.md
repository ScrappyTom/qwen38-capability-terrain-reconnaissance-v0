# Submission-bound complete-audit scout v0 results

## Verdict

The submission-bound complete audit was a **useful repair activator and a poor
complete agent method** on these development anchors.

Five of six episodes produced the frozen opportunity: Qwen3.8 attempted to
submit an incomplete candidate immediately after a visible check passed on
that candidate. From those five authentic first-submit states:

- four improved at least one independently meaningful subcase;
- the aggregate moved from 42/60 to 49/60 whole predicates and from 245/274
  to 256/274 subcases;
- the net subcase gain was +11;
- improvements occurred in both Reservation Book and Retry Queue; but
- only one episode reached a complete, admitted submission.

The intervention therefore did something real: an exact failed audit at the
model's own closure decision usually caused more work and often better code.
It did not reliably organize that work into a complete repair. Four of the
five qualified episodes reached the 24-call ceiling without an admitted
submission.

The frozen mechanical lead screen failed because it required complete
submissions in at least three of the five qualified episodes. That failure
does not erase the 4/5 improvement signal; it means the package did not earn
promotion as a complete method or default submit gate.

The stable `workbench/` remains unchanged.

## Opportunity and outcome

The exact candidate bound to each episode's first `submit` is the authentic
ordinary-loop baseline. The same history continued after the rejected submit.
There is no matched no-audit continuation control, so first-to-terminal change
describes the whole package rather than isolating audit content from rejection,
extra calls, or continued opportunity.

| Cell | First submit | Terminal | Subcase change | Submit audits | Endpoint |
|---|---:|---:|---:|---:|---|
| `rb-271828` | 9/12; 53/58 | 9/12; 54/58 | +1 | 4 | turn limit |
| `rb-161803` | 8/12; 53/58 | **12/12; 58/58** | **+5** | 2 | submitted |
| `rb-141421` | 9/12; 54/58 | 9/12; 54/58 | 0 net | 5 | turn limit |
| `rq-271828` | 7/12; 40/50 | 9/12; 44/50 | +4 | 3 | turn limit after accepted repair |
| `rq-141421` | 9/12; 45/50 | 10/12; 46/50 | +1 | 3 | turn limit |
| **Qualified total** | **42/60; 245/274** | **49/60; 256/274** | **+11** | **17** | **1/5 submitted complete** |

`rq-161803` is preserved but was not part of the frozen opportunity set because
its first submit did not follow a passing visible check. Descriptively it moved
from 9/12 and 45/50 to 11/12 and 48/50 across four rejected submissions, then
also reached the turn limit.

The machine-readable reduction is
[`runs/r1/analysis.json`](runs/r1/analysis.json).

## What improved

The strongest cell was `rb-161803`. Its first audit disclosed four failing
validation groups, including exact wrong-type versus empty-value results.
Qwen then split the previously combined branches across `models.py` and
`book.py`, reran the visible check, and attempted submission again. The second
complete audit passed 12/12 and submission was admitted on turn 17.

The Retry Queue episodes also show genuine partial uptake:

- `rq-271828` separated wrong numeric types from negative values and repaired
  peek and reschedule validation, moving 7/12 to 9/12. Its final turn applied
  another plausible constructor-item repair, but no later model-visible audit
  or action exists, so the work process was censored while still active. The
  separate terminal audit remained 9/12.
- `rq-141421` added constructor-container validation and lifetime-ID state,
  moving 9/12 to 10/12. The lifetime rule remained implemented at the wrong
  transition: IDs were recorded on claim rather than on successful insertion.
- the nonqualifying `rq-161803` added wrong-ID and constructor-container
  validation and reached 11/12. It never separated empty strings from wrong
  string types in the owning validators.

These are not merely more actions. Exact disclosed failures appeared in later
accepted mutations and changed executable outcomes.

## What failed

The common failure was not lack of facts. Each rejected submit returned the
complete task-author predicate bank with the exact candidate ID and literal
expected/observed values.

In `rb-141421`, Qwen repeatedly changed one combined string-validation branch
between `TypeError` and `ValueError`. That alternately helped wrong-type and
empty-value cases but never represented both branches at once. Candidate
identity alternated between two states and five audits remained at 9/12.

In `rb-271828`, the first repair fixed three subcases while regressing two.
Later work included one nonapplicable patch and three exact no-op patches.
The candidate remained at 9/12.

In `rq-141421` and `rq-161803`, Qwen reached a narrower remaining defect and
then repeatedly proposed exact no-op work, edited the wrong owning function,
or resubmitted unchanged. The audit remained truthful; semantic discrimination,
repair binding, action effect, and closure still failed at separate boundaries.

## Timing did not eliminate accumulation

The design avoided a new full audit after every ordinary mutation. It did not
create a latest-only state surface. Every rejected submit result remained in
the ordinary transcript, so later requests contained all earlier full audits.

| Cell | Full audits visible in last request | Audit bytes | Last request bytes | Audit share |
|---|---:|---:|---:|---:|
| `rb-141421` | 5 | 30,643 | 155,908 | 19.7% |
| `rb-161803` | 1 | 6,123 | 72,321 | 8.5% |
| `rb-271828` | 4 | 24,510 | 138,430 | 17.7% |
| `rq-141421` | 3 | 17,649 | 115,591 | 15.3% |
| `rq-161803` | 3 | 17,525 | 96,633 | 18.1% |
| `rq-271828` | 3 | 17,549 | 104,440 | 16.8% |

Those are literal UTF-8 sizes of complete-audit result messages within the
saved request, not model-token estimates. Old audits were correctly bound to
old candidates, but they were still visible. This may have contributed to the
later decision environment; the run does not isolate accumulation as the
cause of oscillation or no-op behavior. Importantly, the first wrong broad
repair in `rb-141421` occurred after only one audit, so removing old audits
would not by itself explain or solve the core type/value discrimination
failure.

## Cost and work curve

Across the five qualified episodes:

| Interval | Reported tokens |
|---|---:|
| Through first submit | 277,325 |
| After first submit | 1,260,131 |
| Total | 1,537,456 |

Post-submit continuation used 4.54 times the tokens spent through the first
submit. Across all six preserved episodes the total was 1,837,940 tokens and
3,851,112 ms of summed model time. These are local package costs, not
throughput benchmarks.

The extra cost bought +11 net qualified subcases and one complete submission.
That is meaningful repair value, but poor economics and poor closure. More
turns might have allowed `rq-271828` to expose the result of its final accepted
patch, but cannot retroactively make the other repeated no-op or oscillating
paths an efficient method. The run should not be rescued by enlarging every
budget after seeing the endpoints.

## Research decision

Do not promote the full-audit-on-every-submit package into the stable harness.
Do not describe it as useless either.

The supported bounded conclusion is:

> Executing complete factual verification at Qwen3.8's attempted closure is a
> strong way to prevent acceptance of known-incomplete code and usually
> reactivates repair. It is not enough to make the subsequent repair complete,
> non-regressive, economical, or terminating.

The audit is therefore best retained as a removable **verification and
admission instrument**. Its trustworthy contribution is that an incomplete
candidate is not mislabeled as complete. It is not an agent policy that should
be assumed to repair arbitrary failures.

The next study should not simply repeat more complete truth or increase every
turn limit. The transcripts identify two narrower research objects:

1. how to preserve one current, complete audit at closure without accumulating
   every historical audit; and
2. how Qwen organizes a repair when literal subcases require splitting one
   combined implementation branch.

The first is a factual visibility-policy question. The second is an action-
organization question and must preserve the full task frame; earlier atomic
experiments showed that stripping context can reduce accuracy. Neither is yet
earned as a stable feature. A fresh experiment would need an opportunity-
matched control and should not use these same completed trajectories as
behavioral evidence.

## Validation boundary

- The exact copied source and golden candidates passed preflight for both the
  real visible check and complete grader; source failed and golden passed.
- All 6 episodes replay-verify.
- All 21 submit actions have one corresponding exact audit record.
- All 21 audits rerun to the saved candidate-bound evidence; every saved tool
  result matches.
- The current apparatus and dependency hashes exactly match the frozen
  `source-lock.json` used before model calls.
- No audit artifact exists before an episode's first submit.
- Every terminal audit reruns exactly, and every episode has one method record.
- 5/5 targeted apparatus tests passed before model calls.
- The repository-wide local discovery suite ran 634 tests successfully, with
  14 intentional archived-continuation skips; the five experiment tests also
  passed directly.
- Every request, response, action, result, audit, candidate transition, check,
  submission, terminal file, and diff was inspected directly before this
  interpretation. See
  [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md).
- The run used Qwen3.8-27B IQ2, llama.cpp b10434, the frozen nonthinking
  sampler, and seeds 271828, 161803, and 141421.
- The server was stopped after the run; no llama process or port listener
  remained and dedicated GPU memory returned to the desktop baseline.
- Validation is local, not GitHub Actions verification.
