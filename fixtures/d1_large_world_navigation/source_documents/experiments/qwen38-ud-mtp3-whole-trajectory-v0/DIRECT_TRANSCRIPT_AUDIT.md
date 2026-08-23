# Direct transcript audit

## Scope

I directly inspected the complete task texts and starting candidates, all 62
new MTP3 requests and raw responses, every interpreted action and literal tool
result, all terminal files and diffs, and all twelve paired external audits.
The previously committed MTP-off trajectories had already received the same
literal audit; their custody and source lock were verified again before this
comparison.

The normalized first request was identical between MTP-off and MTP3 in all six
pairs after replacing only the declared model alias. Seeds, sampler, tools,
task, source state, action schema, and completion allowance matched. Later
requests properly diverged as the sampled actions changed.

All 62 MTP3 responses ended with `finish_reason: stop`; none was truncated.
Every response was a schema-valid admitted action, every turn had positive
draft activity, and no action was rejected or repaired by the client. The
largest MTP3 completion was 1,589 tokens and the largest prompt was 11,631
tokens. The final request in the 13-turn Usage trajectory still contained the
complete original task, all source reads, mutations, check receipts, and the
current aggregate reread.

## Access Pass Registry

All four MTP-off/MTP3 artifacts remained 6/12. Every one preserved the frozen
model, repaired lifetime-ID reuse, passed the narrow visible check, and then
submitted. Every one also retained the same central omissions: arbitrary
constructor iterables and a single `_text` branch that converts both wrong
types and empty strings into `ValueError`.

The tie at seed 141421 was behaviorally close. Both paths read the three files,
made one registry patch, checked once, and submitted in seven turns. Their
only terminal code difference was `pop(index)` versus `del` plus return.

The seed-271828 tie was less equivalent than the 6/12 score suggests. MTP3
checked the untouched candidate, repaired lifetime identity in two patches,
reread twice, checked again, and submitted in eleven turns. Unlike MTP-off, it
never changed `_time` to reject `bool`. The external audit therefore showed
additional wrong actual behavior inside already-failed predicates: `bool`
times were admitted, a failed replacement mutated state, and `active` accepted
a bool time. A grouped predicate count hid that extra damage because those
predicates already failed for the text-type distinction.

This is not a new recurring MTP-specific failure, but it is a concrete warning:
equal predicate totals do not imply equal artifacts. Literal subcases and
state effects remain necessary evidence.

## Priority Dispatch

Both matched pairs tied: 8/12 at seed 141421 and 9/12 at seed 271828. MTP3 used
22 turns versus MTP-off's 17 and did not improve a predicate.

At seed 141421 both sampled paths replaced the required frozen dataclass with a
hand-written property class. MTP3 then repaired position, selection, bool, and
lifetime behavior through board edits; its first visible check disclosed
cancelled-ID reuse and its second passed. It still regressed the frozen-model
predicate and kept the shared constructor/text-validation failures. The
terminal 8/12 equality is real at the executable boundary.

At seed 271828, MTP3 briefly added two irrelevant top-level freeze functions,
then removed them before editing the board. Its final model file was cleaner
than the MTP-off artifact's inert top-level `__post_init__`, but both reached
9/12. Both still accepted arbitrary constructor iterables and collapsed wrong
text types with empty strings. MTP3 passed the visible check and submitted
without an external-quality gain.

The MTP paths did not reveal a general repair-quality improvement. They mostly
reorganized more work around the same governing omissions.

## Usage Windows

This family produced both the only MTP3 win and the only MTP3 loss.

### Seed 141421: 5/12 -> 10/12

MTP-off had previously read all four files, emitted an internally inconsistent
aggregate rewrite, repeatedly reread and repatched only that file, never ran a
check, and exhausted fourteen turns at 5/12.

MTP3 began from the same exact input. It read all four files, rewrote the
aggregate and formatter, and ran the visible check. The check truthfully
reported `KeyError: 'revision'`. MTP3 reread the current aggregate, added the
missing revision field, reran the check successfully, and submitted in thirteen
turns. Its terminal candidate reached 10/12 without regressing a starting
predicate.

This is a meaningful trajectory improvement: a coherent multi-file attempt,
an executed diagnostic, a local repair, and closure replaced the old broken
same-file loop. It is also incomplete. MTP3 never froze either dataclass and
retained the wrong-type/empty-account conflation, despite both requirements
being present in the task and the original model file having been read.

### Seed 271828: 11/12 -> 10/12

MTP3 froze both dataclasses and made a coherent aggregate repair, then passed
the narrow visible check and submitted in nine turns. It never edited or
reread the formatter after its initial read. Consequently `digits=True`
remained accepted and the `format_validation` predicate failed. It also kept
the shared account wrong-type/empty-string conflation.

MTP-off had edited the formatter and rejected bool digits, reaching 11/12.
The MTP3 loss is therefore an exact qualifier-retention/coverage omission, not
a protocol, context, or capacity failure.

## Runtime and action organization

MTP changed every terminal candidate. The paired paths shared four to six
semantic actions before diverging, usually at the first mutation. This confirms
that MTP3 was not behaviorally transparent under the temperature-0.7 sampler.

It was, however, operationally strong:

- 37.30 weighted decode tokens/s versus 19.74 for MTP-off (1.889x);
- 456.0 versus 901.7 seconds of recorded model-response time;
- 487.9 versus 1,263.4 seconds from server start through stop;
- 96.54% draft-token acceptance;
- 66/66 main-layer offload, 1,227 MiB free after calls, and 166 MiB process
  shared GPU memory.

MTP3 used more turns (62 versus 56) and more total tokens (263,407 versus
245,008), yet finished much sooner. It produced fewer completion tokens
(11,524 versus 15,437) but more prompt tokens because several paths took extra
turns.

## Direct-audit conclusion

The numeric decision guide passed, and the direct evidence shows no recurring
new protocol, capacity, or semantic failure class. MTP3 is therefore qualified
as an optional preferred **UD long-context speed profile** on this machine.

That recommendation is deliberately narrow:

- keep MTP-off as the reproducibility reference because MTP changes sampling;
- keep AD-IQ2_S/q8/25K MTP-off as the current bounded quality-oriented package;
- do not claim MTP3 improved Qwen's underlying capability from six sampled
  pairs;
- do not infer quality from the 49/72 aggregate alone—the gain came from one
  escaped collapse, while another pair regressed and one tie concealed worse
  subcase behavior;
- do not change the stable harness.

The central model-facing weakness survived: complete task truth was available,
but independent constructor, type/value, frozen-model, and formatting
qualifiers often disappeared during construction and false closure after a
narrow green check.
