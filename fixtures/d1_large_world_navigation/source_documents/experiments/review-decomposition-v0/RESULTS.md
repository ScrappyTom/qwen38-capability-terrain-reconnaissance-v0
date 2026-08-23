# Qwen3.8 review decomposition v0 results

Date: 2026-08-14

## Result

Foregrounding one frozen task-author requirement per fresh review call changed
exactly one of 26 verdicts. The change was correct and substantive: atomic
review noticed that Reservation `reschedule()` returns a replacement `Booking`
without storing it, while aggregate review certified the same code.

That local gain did not generalize across the remaining defects. Aggregate
review detected 2/7 known violations; atomic review detected 3/7. Both methods
missed two resource-validation defects and both Stock lifetime-ID defects.
Atomic review used 6.97 times the total tokens and 2.28 times the summed model
time.

The result supports a narrow claim: changing one requirement from background
task text into the sole active review unit can sometimes expose a missed world
effect. It does not support a general construct-then-atomic-review method.

## Apparatus

The exact submitted Qwen3.8 Reservation Calendar and Atomic Stock candidates
were frozen from the fresh package bank. Twenty-six task-author feature units
were reviewed in two conditions:

- `aggregate`: one call per candidate reviewed all 13 units;
- `atomic`: thirteen independent calls per candidate each reviewed one unit.

Both conditions received the full original task and exact candidate. Atomic
review changed which one requirement was declared active, not the underlying
world. Model-facing requirement strings were byte-identical across conditions.
No call had tools, code execution, editing, repair advice, a readiness verdict,
or access to the truth table.

Before the endpoint was contacted, direct executable observations confirmed
19 fully satisfied and seven not-fully-satisfied units. Only requirements
stated in the task were scored. Grader-only exception-class conventions were
excluded.

All 28 Qwen3.8 responses were schema-admitted. The model package was the pinned
UD-IQ2_XXS Qwen3.8-27B profile with its recommended nonthinking sampler and
seed 42.

## Quantitative findings

| Outcome | Aggregate | Atomic |
|---|---:|---:|
| Calls admitted | 2/2 | 26/26 |
| Correct verdicts | 21/26 (80.8%) | 22/26 (84.6%) |
| Known violations detected | 2/7 (28.6%) | 3/7 (42.9%) |
| False support on violations | 5 | 4 |
| False defects on satisfied units | 0/19 | 0/19 |
| Uncertain verdicts | 0 | 0 |
| Mechanically literal evidence strings | 26/26 | 23/26 |
| Prompt tokens | 4,983 | 53,643 |
| Completion tokens | 3,661 | 6,586 |
| Total tokens | 8,644 | 60,229 |
| Summed HTTP/model time | 194.38 s | 444.03 s |

The high overall accuracy is misleading if read without the confusion matrix:
19 of 26 units were already satisfied, and both methods labeled all 19
correctly. The difficult boundary was defect recall, not indiscriminate false
alarm generation.

By task:

| Candidate | Aggregate | Atomic | Known violations found |
|---|---:|---:|---:|
| Reservation | 10/13 | 11/13 | 2/5 -> 3/5 |
| Stock | 11/13 | 11/13 | 0/2 -> 0/2 |

No uncertainty was expressed despite four atomic false-support judgments.

## The one useful divergence

For Reservation R09, aggregate review cited the entire method and concluded:

> The reschedule method validates the new interval, checks for overlaps, and
> returns a new Booking without mutating state if invalid.

It marked the requirement fully satisfied, overlooking that successful state
must change.

Atomic review examined the same method under R09 alone and correctly stated:

> The reschedule method returns a new Booking but does not update the stored
> booking in self._bookings.

This is the precise construction defect that the original hidden grader also
missed. Requirement foregrounding therefore changed real discrimination once.

## What atomic review still missed

### Helper behavior did not propagate to caller requirements

Both methods found Reservation R02 because it directly exposed the defective
`_validate_string` helper: wrong types and empty strings both raise
`ValueError`, while the task distinguishes `TypeError` from `ValueError`.

Yet both methods certified R10 and R11 because `is_available()` and
`bookings(resource)` call `_validate_string`. They treated the presence of a
validator call as satisfaction without carrying the already-visible helper
defect into those callers.

### State bookkeeping was mistaken for invariant enforcement

Both methods certified Stock S08 and S12. The code adds successful IDs to
`_used_ids`, but `apply()` never checks `_used_ids`; consequently both apply
IDs and reversal IDs can be reused through `apply()`.

The atomic S08 explanation is especially diagnostic. It explicitly said:

> apply does not check for duplicate IDs

and nevertheless concluded `fully_satisfied`, rationalizing that reverse
checks the set. The relevant fact was semantically present inside the same
response but did not govern its verdict.

This is not an acquisition or aggregation failure. It is a relation/verdict
binding failure under a confirmatory compliance frame.

## Decision

Do not promote atomic review as a default stage. It found one additional
critical defect, but it missed four of seven violations, changed only one
verdict, and multiplied token cost by 6.97.

The result also does not refute staged review generally. It narrows the open
question. A broad or atomic **compliance verdict** invites the model to confirm
surface evidence such as a validator call or bookkeeping set. A genuinely
different review method would ask for a concrete counterexample or executable
observation for one requirement, not another supported/not-supported label.

One bounded action-binding calibration on R09 would be scientifically valid:
the model produced a correct self-review that can be handed to a fresh repair
seat. It would test whether this exact finding governs a mutation, not whether
atomic review is generally useful. A larger repair-stage rollout is not
earned.

For code requirements that are executable, complete task-faithful factual
verification remains the higher-return method. It would catch R09, S08, and
S12 without trusting a semantic support label. Any future check must be
constructed from the written task and audited against it before model calls.
