# Direct transcript and artifact audit

This audit was performed from the saved first and terminal requests, every
assistant message, normalized action, literal tool result, candidate snapshot,
check, submission, and runtime record. Metrics were derived only after those
model-boundary records were read.

## What the actors actually received

Both arms used the same Qwen3.8 AD-IQ2_S package, nonthinking schema-action
contract, 25,088-token combined context, 4,096-token nominal response limit,
66/66 GPU-layer offload, q8 KV cache, tools, task requirements, exact starting
candidate, current repository head, and 28-call ceiling.

The ordinary first task message was 2,370 UTF-8 bytes and its first prompt was
1,962 tokens. The projected message was 21,242 bytes and its first prompt was
10,363 tokens. Its additional 18,872 bytes were exclusively the frozen
mechanical projection: exact artifact basis and source-head identities, one
intervening commit record, delta-manifest identity/count and path-prefix
counts, and 33 structural region records. It contained no source prose,
summary, relevance label, recommended region, or source-count limit.

Because the workbench uses an ordinary action-result conversation, the first
user message remained in every later request. The map was therefore a
persistent 8,401-token initial-prompt cost, not a one-time out-of-band index.

## Ordinary trajectory

The ordinary actor initially requested the complete 51,678-byte target. After
the disclosed read cap rejected that request and two oversized line ranges, it
read the exact target in five accepted, nonoverlapping slices:

| Turn | Exact target range | Returned bytes |
|---:|---:|---:|
| 4 | 1-245 | 11,900 |
| 5 | 246-450 | 11,264 |
| 6 | 451-650 | 11,759 |
| 7 | 651-800 | 10,419 |
| 8 | 801-886 | 6,336 |

It therefore materialized 886/886 lines, 51,678/51,678 bytes, and all 33
mechanical regions before consulting the changed source.

Turn 9 queried the complete delta catalog with an empty substring. The bounded
first page exposed 32 of 1,513 changed paths, including the mechanical-reentry
result, audit, semantic review, freeze, and both correction records. After one
invalid 1-200 line request, the actor read only
`experiments/mechanical-reentry-seed-v0/RESULTS.md` in full. It also queried
history for that result and the maintained target. An attempted region read
used the nonexistent ID `date`; the rejection disclosed no content.

On turn 15 it changed only the document date. On turn 16 it appended one
integrated paragraph to the existing phase-continuity section. The exact new
substance was:

> A custody-derived mechanical seed then tested a middle ground between bare
> fresh-world reentry and carrying the full transcript. It reduced orientation
> calls relative to bare fresh-world restart while preserving terminal quality,
> but it did not replace reacquisition of the exact files governing new work.
> Its repeated payload increased token traffic without reducing recorded model
> time, so no continuation policy was qualified. This separates mechanical
> orientation from content continuity: a seed can make mutation begin earlier
> without becoming a durable working set or an efficiency mechanism.

It passed the mechanical link/file check on turn 17 and submitted on turn 18.
The machine check did not assess the paragraph's completeness or truth.

The actor received the result report's exact counts, qualitative code-test
difference, invalid-run warning, and recommendation before writing. It did not
receive the exact reducer-shape cause because that detail lives in
`SEED_RECORD_BINDING_CORRECTION.md`, which it never opened. Its action retained
the report's central interpretation but omitted several exact distinctions it
had received. This is an authentic many-to-one maintenance example of broad
source availability followed by gist-level construction.

## Projected trajectory

The projected actor also first requested the complete target and received the
same disclosed size rejection. It then used the supplied address space rather
than reconstructing the file sequentially. Its six accepted target reads were:

| Turn | Region | Lines | Bytes |
|---:|---|---:|---:|
| 3 | `What is not yet known` | 812-886 | 5,029 |
| 6 | `Phase-continuity and diagnostic update` | 739-790 | 2,745 |
| 8 | `Design consequences` | 791-811 | 1,997 |
| 11 | `Purpose` | 7-33 | 814 |
| 13 | title/date/status | 1-6 | 143 |
| 16 | observation 26, opportunity/verification boundaries | 582-619 | 2,178 |

It materialized 219/886 target lines and 12,906 bytes: 24.7% of the lines,
25.0% of the bytes, and six of 33 regions. Accepted target reads never
overlapped or repeated.

The actor read four repository objects totaling 16,646 bytes:

- the complete result report, in two exact nonoverlapping ranges;
- the complete prospective freeze, in two exact nonoverlapping ranges;
- the complete semantic review; and
- `EXECUTION_CORRECTION.md`.

The first two are useful study records and the semantic review establishes the
terminal-quality distinction. `EXECUTION_CORRECTION.md` concerns a separate
common-trunk closure and Windows path event. It is not the reducer-shape
correction named by the result report. The actor never opened the direct audit
or `SEED_RECORD_BINDING_CORRECTION.md`, so it had not yet assembled the exact
cause required by rubric item 1.

After 16 interpreted actions, the seventeenth request contained 25,062 prompt
tokens. Qwen began another `repo_read_lines` action under the experiment root,
but the combined 25,088-token envelope allowed only 26 completion tokens. The
saved literal output ends at:

```json
{"action":"repo_read_lines","end_line":40,"path":"experiments/mechanical-reentry-seed-v0
```

No path completion can be inferred. The workbench correctly rejected the
incomplete action as unrecoverable. The actor had made no mutation, run no
check, and submitted nothing. Its terminal candidate is the byte-identical
starting artifact.

## Acquisition and residency comparison

| Measure | Ordinary | Projected |
|---|---:|---:|
| Target lines materialized | 886 / 886 | 219 / 886 |
| Target content bytes | 51,678 | 12,906 |
| Target regions touched | 33 / 33 | 6 / 33 |
| Repository objects read | 1 | 4 |
| Repository content bytes | 5,734 | 16,646 |
| Model-visible result-message bytes | 78,924 | 47,779 |
| Calls / interpreted actions | 18 / 18 | 17 / 16 |
| Maximum prompt tokens | 24,599 | 25,062 |
| Minimum remaining combined headroom | 483 | 0 |
| Total reported tokens | 264,317 | 331,344 |
| Uncached prompt tokens | 24,667 | 25,126 |
| Recorded prompt + generation time | 107.1 s | 92.5 s |
| Cold-server arm wall time | 135.1 s | 110.7 s |
| Mutation / closure | turn 15 / submitted | none / protocol error |

The structural projection changed selection materially: target
materialization fell 75.0%, and total returned result-message bytes fell
39.5%. It did not create a successful bounded working set. The persistent map
cost, deeper source acquisition, and ordinary transcript residency exhausted
the execution envelope before construction. Projected total token traffic was
25.4% higher despite fewer returned exact bytes.

The lower recorded time is not an efficiency win: the projected actor emitted
fewer completion tokens because it never constructed or verified an artifact.

## Boundary established

The run supports neither “the projection works” nor “structural addressability
does not help.” It establishes both sides of the boundary:

1. mechanically meaningful regions were sufficient to change Qwen from global
   target reconstruction to selective target acquisition;
2. putting the complete region registry permanently in the action transcript
   consumed enough active capacity to prevent the selected evidence from
   reaching an artifact;
3. selection was imperfect: the actor acquired one non-governing correction
   record and had not yet acquired the governing reducer correction; and
4. the completed ordinary artifact was only a gist-level semantic update, so
   its mechanical submission is not the quality comparator required for a
   positive projection result.

The first unresolved systems question is therefore no longer whether Qwen can
use mechanical structural addresses. It did. The unresolved question is
whether the address space can remain external or be projected compactly enough
that model-selected exact regions become an actionable working set rather than
another permanently resident prompt object.
