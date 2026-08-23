# Direct transcript audit

## Scope

I directly inspected the saved task messages, starting source, all 117 raw
assistant responses, interpreted actions, literal tool results, terminal
candidates, final diffs, and twelve external predicate audits in measured run
`r2`. I also opened the final request in the sole turn-limit trajectory to
check what remained available to the model rather than inferring its state
from the terminal score.

All 117 responses ended with `finish_reason: stop`. Every response was a
schema-valid bare action. There was no response truncation, transport failure,
context exhaustion, or client-side repair. One UD action was truthfully
rejected as an exact no-op. The largest prompt was 10,464 tokens for AD and
13,450 for UD, below the frozen 20,992-token eligibility ceiling.

## Access Pass Registry

### What both packages saw

Both packages received the same full contract. It explicitly separated wrong
types (`TypeError`) from empty strings (`ValueError`), restricted the
constructor to a list or tuple, required lifetime ID exclusion, and described
atomic replace/revoke/filter behavior. Every trajectory read the package
exports, dataclass, and complete registry implementation before mutating.

### What they did

All four trajectories added a lifetime `_used_ids` set, repaired bool handling
for integer fields, preserved positions, ran the narrow visible check, saw it
pass, and submitted. AD seed 141421 additionally added validation to the
`AccessPass` constructor; this cost two extra turns but did not improve the
external audit.

Every terminal candidate used the same compressed text validator:

```python
if not isinstance(value, str) or not value:
    raise ValueError(...)
```

That single branch erased the requested wrong-type/empty-value distinction.
Every constructor also called `list(passes)` instead of first requiring a list
or tuple. Those two local choices caused the same six failed predicates in all
four cells: constructor container, value validation, replace validation,
active validation, revoke validation, and filtered snapshot validation.

### Finding

AD and UD tied 6/12 at both seeds. The larger package did not improve this
recurring discrimination failure. Extra model work in AD seed 141421 changed
where validation lived without changing the missed distinction.

## Priority Dispatch

### What both packages saw

The exact task distinguished wrong text types from empty strings, required a
list-or-tuple constructor, lifetime ID exclusion, stable board positions,
three-part ready-item ordering, and atomic mutations. Every trajectory read
the exports, dataclass, and complete board before editing.

### Common behavior

All four trajectories implemented lifetime ID tracking, repaired bool
handling, retained position for reprioritize/defer, and made selection use
priority, ready time, and current board order. They then passed the narrow
visible check and submitted.

All four again collapsed wrong-type and empty text values into one
`ValueError` branch and accepted arbitrary constructor iterables through
`list(items)`. Consequently the common terminal state was 9/12, failing the
constructor, value-validation, and take/cancel-validation predicates.

### Package divergence

UD seed 141421 replaced the required frozen dataclass with a hand-written
property class. The public-model audit then failed with an `AttributeError`
under the frozen-field probe. This regressed a predicate that passed in the
starting candidate and produced the one-point AD win, 9/12 versus 8/12.

UD seed 271828 made a different construction error: it wrote a top-level
function named `__post_init__` rather than attaching it to the dataclass. The
function was inert. Board-side validation happened to preserve a 9/12 score,
so the pair tied despite the malformed intended repair.

### Finding

AD avoided one Q4 regression but did not solve the difficult shared contract
distinctions. The result is evidence of a modest construction-stability
advantage, not a broad validation-capability change.

## Usage Windows

### What both packages saw

Both packages received the complete multi-file contract and read the exports,
models, aggregator, and formatter. The task required frozen models, distinct
type/value errors, tied-revision replacement, first-account order, sorted
windows, immutable outputs, numeric summaries, and exact formatting.

### AD seed 141421

AD edited all three relevant files, ran the visible check, and received exact
failures for selection/order and formatting. It reread the aggregator, changed
the account/window organization, reran the check successfully, and submitted.
The terminal candidate passed 11/12 predicates. Its only miss was the familiar
combined text validator, which returned `ValueError` for a non-string account
instead of `TypeError`.

### AD seed 271828

AD edited the models, aggregator, and formatter, passed the visible check on
its first run, and submitted a complete 12/12 candidate. In this trajectory it
split account validation into two branches: non-string to `TypeError`, empty
string to `ValueError`.

### UD seed 271828

UD followed a coherent path similar to AD: it edited all three files, passed
the visible check, and submitted. It reached 11/12, missing only the same
account type/empty distinction as AD seed 141421.

### UD seed 141421

UD had all necessary source bytes before its first edit, but its first
aggregator rewrite introduced several internally inconsistent structures:

- it later indexed `current["revision"]` although stored records had no
  `revision` member;
- it created groups but never appended retained unit values;
- it appended new entries to the `order` list while iterating that list.

It then reread only `aggregate.py` and attempted four further whole-file
patches. One was an exact no-op and was rejected as such. Later patches removed
some surface inconsistencies but retained the missing-revision lookup and
empty value groups. It never returned to `models.py` or `formatting.py`, never
ran even the visible check, never submitted, and reached the 14-turn limit.

The final turn request still contained the complete original task at message
index 1, every original read, every mutation/result pair, and the most recent
full aggregator read. Its prompt was 13,450 tokens, all responses ended
normally, and no action was truncated. The failure therefore was not missing
task information or capacity. The trajectory failed to organize and verify a
coherent mutation after creating its own broken intermediate state.

Its terminal candidate passed 5/12, failed to freeze either model, and
regressed two predicates that the starting candidate had passed. This single
pair accounts for six of AD's eight aggregate predicate advantage.

## Cross-trajectory findings

1. **The recurring hard failure survived both packages.** Seven of the twelve
   candidates used one branch for wrong-type and empty text values. Access and
   Priority therefore tied at three of four pairs even though the distinction
   was stated literally in the task.
2. **AD's clearest advantage was construction stability, not universal semantic
   discrimination.** It introduced no predicate regression, completed all six
   trajectories, and produced the only 12/12 artifact. UD introduced three
   predicate regressions and had the only non-submission.
3. **The large UD loss was a genuine operational trajectory failure.** The
   exact transcript shows malformed state construction, repeated narrow
   rereads, one no-op, no check, and turn-limit termination. It was not caused
   by context pressure, response truncation, tool rejection, or absent source.
4. **Visible success still induced false closure in eleven submitted runs.**
   Both packages normally submitted immediately after a green narrow check.
   Ten of those eleven submissions were incomplete under the task-faithful
   audit. Better weights/KV precision did not remove the need to study
   verification and requirement retention.
5. **The result compares deployable packages.** The GGUFs carry different
   weight quantization, KV precision, context allocation, and packaged chat
   templates. The saved evidence cannot attribute the behavior to any one of
   those factors alone.

## Direct-audit conclusion

The literal evidence leans toward AD-IQ2_S/q8/25K for bounded, quality-sensitive
work: it was never worse, avoided the Q4 regression, and was much more coherent
on one difficult multi-file trajectory. It does not show that AD fixes Qwen's
general tendency to compress exact validation distinctions into a central
gist. That failure was nearly identical across packages and remains the more
important model-facing research problem.
