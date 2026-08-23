# Direct transcript and artifact audit

This audit was written after reading the literal task, every saved action and
result, the terminal artifacts, the visible-check output, and the external
audit. Reducer labels alone were not used to diagnose either model.

## Model-visible boundary

Both packages received the same task and ordinary tool schemas within each
workflow. No hidden grader, rubric, source-control file, semantic card,
summary, reviewer agent, or host diagnosis was present. Research revision was
a fresh inference containing the exact prior memo, a fixed editorial review,
the same source corpus, and a blank response file.

## AD code trajectory

| Calls | Literal work |
|---|---|
| 1–9 | Tree; read issue, API, package, dispatcher, models, policy, tests, and incident log |
| 10 | Replace dispatcher with the substantive product repair |
| 11–12 | Reread and expand tests from 2 to 17 |
| 13 | Run visible check; receive three exact assertion failures |
| 14–16 | Reread tests, revise assertions, reread dispatcher |
| 17–19 | Add unrelated state logic, inspect it, then restore the correct product implementation |
| 20 | Reread tests |
| 21 | Begin another test patch; response ends at the context boundary before a complete action exists |

The final request reported 25,022 prompt tokens and allowed a 4,096-token
completion, but the server could emit only 66 tokens before total use reached
25,088. The saved response has `finish_reason: length` and an incomplete patch
object. The harness correctly admitted no action and recorded
`incomplete_action_response`.

The external complete audit passed all product behavior. The only failed group
ran the candidate-authored tests. Inspection of those tests and the supplied
API contract establishes that three expectations, not the dispatcher, were
wrong. The visible check was factually reporting test failures; it could not
tell the actor that its own assertions contradicted the task.

## UD code trajectory

| Calls | Literal work |
|---|---|
| 1–10 | Tree; read all governing issue, API, implementation, test, error, and log files |
| 11–15 | Attempt a model change, add a private record class, inspect it, then remove it |
| 16 | Replace dispatcher with a large implementation |
| 17 | Reread dispatcher |
| 18–32 | Alternate identical whole-file no-op patches with rereads of the same dispatcher |

The eight rejected patches had byte-identical arguments and SHA-256
`49c09da...`. Every result stated that old and new text were identical. The
candidate did not change after call 16. The final prompt used 40,851 tokens,
leaving substantial space in the 50,176-token profile.

The code referenced `_Record` and `bisect` without definitions/imports, so
core operations raised `NameError`; it also lacked attempt exhaustion during
expiry. The actor never called `check` and never edited the two starting tests.
The 3/14 passing external groups were public-shape/policy, input validation,
and locked-document integrity—not working dispatch behavior.

## Research acquisition and construction

AD draft read the memo, index, C01–C10, S01, A01, and A02 before one memo
patch, a check, and submission. UD read the same governing corpus and A01 but
skipped the irrelevant A02 archive. Both checks passed mechanically.

The terminal artifacts show that acquisition alone does not explain the
package difference. Both had the critical evidence. AD preserved the complete
set of exact numerical and methodological distinctions. UD rendered a more
compact account and omitted four secondary details while preserving the main
direction, uncertainty, and recommendation.

## Research revision

AD revision read the memo, review, response, and only the records relevant to
the comments: C02, A01, C03, C04, S01, C07, C06, C08, and C10. It added the
adjusted confidence interval and nonrandom-design qualification to the
executive section, completed the response, checked, and submitted.

UD revision read the memo, review, response, C02, A01, C03–C10, and S01. It
also added the main executive qualifications and correctly classified all
eight comments. It did not revisit every omission in its draft because the
fixed review did not name them. Most importantly, its Q5 response said the
memo clarified that `$14` used 13,142 boardings, but the final memo still said
only `$14 per completed boarding`. This directly demonstrates:

```text
correct evidence acquisition
  + correct reviewer decision
  + correct textual explanation
  does not guarantee
artifact mutation contains the claimed distinction
```

## Cross-workflow pattern

The same model family did not show one fixed information capacity:

- AD integrated a fourteen-record research corpus and revised it cleanly, but
  its cumulative code transcript exhausted 25K after following incorrect
  self-authored checks.
- UD produced and revised a useful research memo at low cost, but its larger
  code context preserved an exact nonproductive action loop.
- explicit, task-author review comments were behaviorally useful; a review
  could still leave unnamed omissions untouched and permit claimed-but-absent
  uptake.

The decision environment therefore includes not just available facts, but
artifact ownership, verification authority, accumulated history, current
operation, and expression headroom.

## Audit process correction

Direct evaluation itself must preserve custody. Executing Python inside the
materialized AD candidate created bytecode and initially broke exact replay.
The derived directories were removed and replay reverified. Future audits must
use a verified copy or a side-effect-free execution environment.
