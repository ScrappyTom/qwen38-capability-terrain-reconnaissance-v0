# Direct transcript and artifact audit

Date: 2026-08-16

## What the model actually received

The quality screen did not give Qwen a shortened diagnostic prompt. Each cell
replayed the complete saved request immediately before a historical repair
action. The request included the full task, ordinary action/result history,
the current candidate identity, the rejected submission's complete 12-case
audit, and the model's immediately preceding exact file read. Conditions
changed only the declared model alias and frozen seed.

The four boundaries were:

- Reservation Book type/value discrimination after the complete audit showed
  the exact expected and observed wrong-type and empty-value results.
- Retry Queue lifetime identity after the complete audit showed constructor,
  lifetime-reuse, and view-isolation failures and after the current queue file
  had been read exactly.
- Reservation Book regression integration after a complete audit exposed the
  remaining constructor/available/view distinctions.
- A Reservation Book positive-control boundary taken from a trajectory that
  later reached 12/12.

The saved requests were preflighted by rerunning the complete audit against the
exact candidate and requiring exact equality with the model-visible audit.

## What the model actually emitted

All 32 calls returned schema-valid admitted actions. Action hashes show that
many cells were literally identical across profiles; the observed differences
are model outputs, not normalizer or executor behavior.

### Type/value boundary

The common unsuccessful pattern was to change a compound check such as:

```python
if not isinstance(room, str) or not room:
    raise TypeError(...)
```

into the same compound check raising `ValueError`. That fixed empty-string
subcases while regressing wrong-type subcases. Several cells therefore stayed
at 9/12 and 54/58 even though four subcases changed in each direction.

The one complete repair was AD-IQ2_S/q8 at seed 271828. Its literal patch split
every affected check:

```python
if not isinstance(room, str):
    raise TypeError(...)
if not room:
    raise ValueError(...)
```

It applied the same distinction to reservation IDs and every relevant room
validation site and reached 12/12, 58/58.

This is the familiar qualifier-collapse phenotype in code: the complete audit
and source were present, but most actions retained only the central gist that
empty values were invalid and failed to preserve the independent type/value
branch.

### Lifetime-transition boundary

The recurrent wrong patch, emitted identically by UD/q4 seed 141421 and UD/q8
at both seeds, added constructor validation but attached ID bookkeeping to
`claim()`:

```python
job = self._jobs.pop(index)
self._used_ids.add(job.job_id)
```

It never initialized `_used_ids`. It fixed constructor shape, failed the actual
lifetime rule, and regressed claim/cancel behavior. The resulting transition
was 9/12 -> 9/12 and 45/50 -> 37/50.

AD/q4 seed 141421 attempted a broader `_ever_seen_ids` implementation, but its
raw provider response literally contained `n        for index, job ...`. The
parser preserved that byte sequence, the patch executor applied it exactly,
and Python then raised `SyntaxError`. This was model expression failure, not a
protocol conversion defect. The same patch also discarded IDs on claim and
cancel, contrary to the lifetime rule.

Three cells produced complete 12/12 lifetime repairs: AD/q4 seed 271828,
AD/q8 seed 271828, and UD/q4 seed 271828. Their exact implementations differed,
but each established a set from constructor IDs, rejected reuse during
enqueue, and retained lifetime membership after removal. AD/q8 seed 141421
only added constructor container validation; it improved 9/12 -> 10/12 but did
not address the governing lifetime relation.

### Regression and positive-control boundaries

All AD cells and seed 141421 in both UD cells chose an exact file `read`; they
did not mutate the candidate. That is valid action selection, not a no-op
patch, but it means those one-action cells contain no mutation-quality test.

At regression seed 271828, UD/q4 split wrong-type and empty-value handling and
reached 11/12, 55/58. UD/q8 made a smaller patch that mixed the distinction and
remained at 9/12, 54/58.

At positive-control seed 271828, UD/q4 and UD/q8 emitted the same patch byte for
byte, split two model validators, and reached 9/12, 55/58. The four AD cells
read instead, leaving the candidate at 8/12, 53/58.

## Evaluation-boundary correction

The first AD/q4 lifetime action made its candidate syntactically invalid. The
frozen audit subprocess could not import that candidate, and the initial
experiment reducer raised instead of preserving the outcome. The raw request,
response, admitted patch, tool result, and broken candidate were already saved.

The experiment-only evaluator was corrected so a nonzero audit subprocess is
recorded as:

- `audit_executed: false`;
- exact return code, stdout, and stderr;
- zero executable predicates/subcases for the un-runnable candidate;
- no claim that individual tests actually executed.

A unit test covers this boundary. The incomplete reducer run remains preserved
and excluded. The profile was rerun from a clean root after the correction.

## Audit conclusion

Higher-precision KV did not supply new facts. It changed which action the
sampled model expressed from an identical decision environment. In the larger
AD weight package those changed actions were materially better in two saved
weakness cells. In the smaller UD package q8 selected the wrong lifetime patch
at a seed where q4 selected a complete one and made a weaker regression repair.

The evidence therefore supports a package interaction, not a universal rule
that q8 KV improves Qwen3.8.
