# Direct request, response, and artifact audit

## Scope

This audit was performed from the saved literal `request.json`, raw response,
assistant message, interpreted action, candidate snapshot, and executable
audit for every completed condition. Server summaries alone were not used to
diagnose model behavior.

Within each weight/KV package, all model requests match their M0 counterpart
after replacing only the declared model alias. Seeds, messages, task text,
action schema, exact source views, complete-audit facts, sampler, thinking
policy, response allowance, and action boundary are otherwise identical.

The saved states cover four different immediate decisions:

- a Reservation Book type/value repair after exact failure evidence;
- a Retry Queue lifetime-ID transition repair;
- a Reservation Book integration state vulnerable to sibling regression; and
- a positive-control repair boundary.

## AD-IQ2_S / q8 / 25K

### MTP-1

All eight assistant messages are literally equal to M0 after transport-only
metadata is excluded. Actions, completion lengths, candidate hashes, and
executable audits are also identical. This is strong local evidence that
MTP-1 changed only execution speed for these saved calls.

### MTP-2

Seven assistant messages are identical. The sole divergence is Retry Queue at
seed 271828. Both patches correctly create a lifetime `_used_ids` set and pass
12/12 predicates and 50/50 subcases. M0 checks only `_used_ids` during enqueue;
MTP-2 first scans current jobs and then checks `_used_ids`. The extra scan is
redundant but does not alter the measured contract.

This establishes that depth 2 was no longer literally transparent, even
though its executable quality was non-inferior in all eight cells.

### MTP-3

The first exact request was saved, but no assistant output was produced. The
slot had processed 10,400/10,912 prompt tokens and decoded zero tokens when the
capacity stop was applied. There is no model behavior to grade.

## UD-IQ2_XXS / q4 / 50K

### Shared success-control regression

In `rb-success-control--s271828`, M0 preserves separate branches:

```python
if not isinstance(value, str):
    raise TypeError(...)
if not value:
    raise ValueError(...)
```

Every MTP depth instead emits the combined form:

```python
if not isinstance(value, str) or not value:
    raise TypeError(...)
```

The MTP patches also add validation to `reschedule`. The combined helper loses
the required empty-string distinction while the new check fixes a different
case, producing a net change from 55/58 to 54/58 subcases at the same 9/12
whole-predicate count.

This is the familiar task-level failure in literal form: Qwen compresses two
explicit validation classes into one generic branch. It was not inferred from
an aggregate score.

### Additional MTP-1 regression

In `rb-regression-integration--s271828`, M0 reaches 11/12 and 55/58. It keeps
wrong-type and empty-value checks separate in `available()` and
`reservations()`. MTP-1 combines each pair into `ValueError`. It does fix the
constructor container shape, but regresses both wrong-room type cases, ending
at 9/12 and 54/58.

MTP-2 and MTP-3 reproduce the M0 patch exactly in this state, so this additional
regression is specific to the sampled MTP-1 path.

### Behaviorally equivalent divergence

Retry Queue seed 271828 differed under MTP-1 and MTP-2 only in how `cancel()`
returns the removed object: returning `pop(index)` versus popping and then
returning the already-bound `job`. Both candidates pass 12/12 and 50/50.
MTP-3 reproduces M0 literally.

## What can and cannot be concluded

The speed effect is direct and large. The target model accepted 99.24% to
99.95% of proposed draft tokens, and every MTP depth materially increased
decode throughput inside its package.

The quality boundary is narrower:

- MTP did not corrupt the action schema or execution protocol;
- AD MTP-1 was literally behavior-preserving on this set;
- UD MTP conditions changed some sampled continuations at the frozen 0.7
  temperature; and
- one exact semantic regression recurred under all three UD depths.

This is insufficient to estimate a general quality rate. It is sufficient to
withhold default promotion under the frozen non-inferiority rule and to define
a focused whole-trajectory follow-up for the UD MTP-3 speed candidate.

## Apparatus observations

The first two MTP runtime records were falsely marked failed by investigator
qualification code, not by llama.cpp or the model. Primary evidence remained
complete and internally consistent. Both bugs are separately disclosed, and
the final analysis derives qualification from the literal response draft
counters, server initialization/statistics, 66/66 offload record, and action
evidence.
