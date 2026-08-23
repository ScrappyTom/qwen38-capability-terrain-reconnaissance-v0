# Operation ecology scout v0 — results

## Outcome

The fixed `DISCOVER -> CONSTRUCT -> check -> EVALUATE` ecology did not improve
Qwen3.6-27B on these two tasks.

- On the code task it constructed a correct candidate that passed all public
  cases and, in a post-run held-out diagnostic, all held-out cases. The forced
  evaluation turn then added 727 bytes of commentary before an unchanged copy
  of that candidate. The strict action parser correctly rejected the final
  response as `substantive_text_outside_envelope`.
- On the release-brief task the model ignored `DISCOVER`'s instruction not to
  construct. It emitted the complete candidate immediately, then returned the
  same 259 response bytes in `CONSTRUCT` and `EVALUATE`.
- Native Pi produced a host-usable, explicitly correct artifact on both tasks.
  The input-corrected code run used one failing public receipt to make one
  repair and then passed. The brief run wrote one candidate and passed its
  public check.

This is negative path evidence for this fixed staged bundle, not evidence that
decomposition, fresh context, or checker feedback can never help. The tasks
were also too easy to discriminate semantic construction quality: both methods
formed correct candidate content before any useful treatment contrast could
emerge.

## Apparatus qualification and correction

Before inference:

- the candidate parser accepted a valid fenced envelope and rejected missing,
  duplicated, and extra-text envelopes;
- known-good code and brief candidates passed public and held-out checks; and
- known-bad candidates failed the public checks.

The first `delivery_fee__native_pi` trajectory exposed an apparatus defect.
The intended `invocation.json` contained quoted dictionary keys in source
record A3, while the exact session and provider request did not. PowerShell's
native argument marshalling had removed the embedded quotes. The artifact was
still valid because Pi immediately read the correct file, but the run is not
an input-matched arm.

The defect and original trajectory remain preserved. The launcher was changed
to a direct Node argument array, a zero-completion probe round-tripped 139 UTF-8
bytes containing quotes, backticks, braces, Unicode, and newlines, and one
predeclared replacement run was made. In the replacement, `prompt.txt` and the
first provider-request user text are byte-equal at 2,034 UTF-8 bytes. See
[`EXECUTION_CORRECTION.md`](EXECUTION_CORRECTION.md).

No workbench code, task, grader, model setting, operation text, or response
allowance changed.

## Endpoint results

| Task and condition | Final action usable | Public | Held out | Direct explicit-task judgment |
|---|---:|---:|---:|---|
| Delivery fee — native Pi, original | yes, but input arm disqualified | 8/8 | 16/16 | Correct artifact; do not use as matched evidence. |
| Delivery fee — native Pi, corrected | yes | 8/8 | 16/16 | Correct implementation of A1–A4. |
| Delivery fee — operations + feedback | **no** | initial 8/8 | initial 16/16 post-run diagnostic | Candidate content was correct; final response violated the frozen envelope. |
| Release brief — native Pi | yes | 6/6 | 8/9 | Correct against every explicit B1–B5 obligation. |
| Release brief — operations + feedback | yes | 6/6 | 8/9 | Correct against every explicit B1–B5 obligation. |

The release held-out failure is a grader defect for the stated task, not a
model-content failure. The hidden contract requires the summary itself to
contain the substring `hold`. B5 requires a practical reason and a separate
`DECISION: HOLD` field; it does not require that lexical duplication. Pi wrote
“candidate cannot be released,” and the staged candidate wrote “Build held.”
Both are faithful, concise reasons. The hidden check's `summary_mentions_hold`
therefore remains preserved but is excluded from the explicit-task judgment.
The pre-run oracle happened to use the word “Hold,” so qualification did not
expose this semantic-equivalence gap.

## Quantitative observations

Pi token accounting sums its recorded uncached input, cache reads, and output
across turns. The staged records are llama.cpp totals for three independent
complete contexts. Their total-token columns are not directly comparable.
Generated tokens and wall time are the closest descriptive comparisons, still
with only one path per cell.

| Task and condition | Assistant/model calls | Tool calls | Generated tokens | Recorded total tokens | Wall/model seconds |
|---|---:|---:|---:|---:|---:|
| Delivery — native Pi, original/disqualified | 6 | 5 | 1,014 | 20,821 | 68.518 |
| Delivery — native Pi, corrected | 5 | 4 | 901 | 14,441 | 49.063 |
| Delivery — operations + feedback | 3 | 0 | 1,272 | 4,841 | 61.759 |
| Release — native Pi | 4 | 3 | 521 | 10,172 | 31.197 |
| Release — operations + feedback | 3 | 0 | 228 | 2,664 | 13.811 |

Additional exact observations:

- The corrected delivery Pi run recorded 5 provider requests, 4 tool results,
  and 0 tool errors. Its tools were `read`, `bash`, `write`, `bash`.
- The release Pi run recorded 4 provider requests, 3 tool results, and 0 tool
  errors. Its tools were `read`, `write`, `bash`.
- Delivery staging used 3,569 prompt tokens and release staging used 2,436.
- Delivery `DISCOVER` consumed its full 512-token ceiling and ended with
  `finish_reason: length`; the note stopped mid-sentence.
- Delivery `CONSTRUCT` stopped normally after 287 tokens and produced an
  891-byte candidate. `EVALUATE` stopped normally after 473 tokens but its
  final action was unusable.
- The candidate embedded after the invalid evaluation commentary was exactly
  equal to the checked initial candidate, SHA-256
  `8ef3ad8e4582c9c4d3c3b4b0de8e011d3cdd29b22a0db95351bd32f014f82e1b`.
- All three release-stage responses were byte-identical, 259 bytes each,
  SHA-256
  `c6f0f266796fbc00bbb4fd8264d3259c07619f9580e21307a20ae5f29da16ffd`.
- Relative to corrected Pi, staging generated 41.18% more tokens and took
  25.87% longer on delivery while losing final usability. On the tiny brief it
  generated 56.24% fewer tokens and took 55.73% less time, with no explicit
  quality difference.

These percentages describe two individual trajectories, not efficiency
estimates.

## What the model actually did

### Delivery — corrected native Pi

The exact initial provider request retained all RAW bytes. Qwen:

1. read the current candidate;
2. ran the public checker;
3. received two literal failures: expected 300/750, observed 0/200;
4. wrote one revised function;
5. reran the checker and received `PASS`; and
6. stopped.

The final function keeps the base waiver separate from the two never-waived
charges. Direct review found no mismatch with A1–A4.

### Delivery — operations + feedback

`DISCOVER` identified all four rule groups but expanded into an unnecessary
scenario analysis and exhausted its ceiling. The truncated note ended while
discussing waiver/discount interaction. Despite that, `CONSTRUCT` returned a
complete correct candidate. The public receipt passed every named check.

`EVALUATE` then explained why no revision was needed before repeating the exact
candidate. The current-turn instruction explicitly prohibited commentary, but
the model produced it anyway. The host did not strip or repair those bytes, so
there was no final candidate.

### Release brief — native Pi

Qwen derived `HOLD`, `data-platform`, the checksum remediation, and B1–B4
before reading the existing file. It replaced the incorrect release brief,
ran the public checker once, received `PASS`, and stopped. Its summary states
the recorded failure and practical consequence without inventing status.

### Release brief — operations + feedback

The first response to `DISCOVER` was already a complete candidate envelope,
contrary to “Do not produce the candidate in this turn.” The host preserved it
as an attributed model note. `CONSTRUCT` copied it byte for byte; the public
check passed. `EVALUATE` copied it a third time.

Thus the nominal three-stage procedure performed no observable decomposition,
construction change, or evaluation change on this task.

## Interpretation

The most useful result is not a method ranking. It is an action-frame result:

> Naming an operation did not reliably make that operation the model's public
> action, and forcing a second serialization of a passing candidate created a
> new failure boundary.

The exact truth was sufficient for candidate construction in both ecologies.
The staged failures were about what action the model emitted:

- `DISCOVER` became overlong analysis on code;
- `DISCOVER` became premature construction on the brief; and
- `EVALUATE` became commentary plus candidate on code.

This is consistent with the user's broader framing: information view, tools,
and action affordances are interventions. A prose operation label is a weak
affordance. It does not mechanically separate discovery from construction.

The result does **not** earn a live card, semantic host, prompt tuning around
these tasks, conditional retries, relaxed envelope parsing, or automatic
promotion of Pi. It also does not refute exact checker feedback: the corrected
Pi run used a literal failing receipt productively. The staged run only showed
that a forced review after a pass can be unnecessary and harmful.

## Decision and next track

Stop this exact fixed staged bundle after the scout. Do not rerun it with a
longer work note or softer parser on these tasks.

Retain two design lessons for future coherent methods:

1. If distinct operations matter, their return types or tools must make those
   actions genuinely distinct; labels alone are not evidence of decomposition.
2. A checked candidate should have an exact reusable identity. Requiring a
   model to reserialize unchanged bytes introduces avoidable corruption risk.

Those are design constraints, not yet retained mechanisms. The next
independent experiment should use the other preserved inspiration track:
model-directed exact navigation over a typed artifact/provenance atlas on a
fresh task large enough that navigation matters. Keep custody and external
grading unchanged; compare complete navigation ecologies before decomposing
components.

## Preserved evidence

[`runs/`](runs/) contains:

- every staged request payload, exact response JSON, model-facing context,
  parse record, candidate, public receipt, and held-out receipt;
- every Pi invocation and exact prompt custody file;
- every Pi provider request, response header, session message, tool call,
  result, event stream, workspace, and final artifact;
- both machine-grade layers; and
- the original disqualified prompt-transport trajectory plus the corrected
  replacement.

The experiment branch preserves the prospective freeze at `ed804da` and the
transport correction before replacement inference at `65d049f`.
