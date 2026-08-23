# Current complete-audit v0 results

## Verdict

The frozen current-audit gate **failed**.

Across five fresh common-prefix false-closure pairs, automatically rerunning
and appending the complete task audit after every accepted mutation beat the
static-audit control in only 1/5 pairs. The predeclared rule required at least
3/5 wins spanning both task families. Four pairs tied, no static branch won,
and the only current-audit win occurred in Reservation Book.

The treatment produced a real but non-general quality signal:

- terminal subcases were 260/274 for `C1_CURRENT` versus 256/274 for
  `S0_STATIC`;
- terminal whole predicates were 52/60 versus 49/60;
- C1 produced two contract-complete candidates versus one for S0; and
- C1 introduced zero trunk-passing subcase regressions versus four for S0.

Those gains were concentrated in one pair. C1 used 947,616 reported tokens
versus 310,626 for S0, took 3.17 times the summed model time, and caused one
18-turn non-submission plus nine rejected/no-op patch attempts. The stable
`workbench/` remains unchanged. Automatic post-mutation complete-audit
refresh is not promoted.

## Qualification

Six ordinary Qwen3.8 trunks ran on two new repair tasks and three frozen
seeds. Five naturally produced the required false-closure transition:

```text
incomplete candidate
-> visible check passed against that candidate
-> no later mutation
-> model submitted that candidate
```

| Cell | Task | Trunk predicates | Trunk subcases | Qualified |
|---|---|---:|---:|---|
| `rb-173205` | Reservation Book | 7/12 | 49/58 | yes |
| `rb-223607` | Reservation Book | 7/12 | 52/58 | yes |
| `rb-314159` | Reservation Book | 8/12 | 53/58 | yes |
| `rq-223607` | Retry Queue | 8/12 | 44/50 | yes |
| `rq-314159` | Retry Queue | 9/12 | 44/50 | yes |
| `rq-173205` | Retry Queue | 9/12 | 46/50 | no: no passing check bound to submission |

The branch gate required at least four trunks across both task families. It
passed with five. The nonqualifying trunk is preserved and received no branch
calls.

## Matched branch outcome

Both branches received the complete written task, exact submitted trunk
files, exact candidate identity, and one complete initial audit. Their
model-facing requests, responses, actions, and results were byte-identical
through the first accepted mutation. Only C1 then received a fresh complete
audit after each accepted mutation.

Scores below show whole predicates followed by independently meaningful
subcases.

| Cell | Trunk | S0 static | C1 current | C1 - S0 subcases | C1 audits | End state |
|---|---:|---:|---:|---:|---:|---|
| `rb-173205` | 7/12; 49/58 | 8/12; 50/58 | 8/12; 50/58 | 0 | 3 | both submitted |
| `rb-223607` | 7/12; 52/58 | 9/12; 54/58 | **12/12; 58/58** | **+4** | 5 | both submitted |
| `rb-314159` | 8/12; 53/58 | 9/12; 54/58 | 9/12; 54/58 | 0 | 9 | S0 submitted; C1 turn limit |
| `rq-223607` | 8/12; 44/50 | **12/12; 50/50** | **12/12; 50/50** | 0 | 1 | byte-identical submitted artifact |
| `rq-314159` | 9/12; 44/50 | 11/12; 48/50 | 11/12; 48/50 | 0 | 1 | byte-identical submitted artifact |
| **Total** | — | **49/60; 256/274** | **52/60; 260/274** | **+4** | **19** | C1 complete 2/5; S0 complete 1/5 |

The frozen gate required C1 to win at least three pairs, with wins spanning
both tasks. It won one pair in one task, tied four, and lost none. Aggregate
quality, complete-candidate count, and regression conditions favored C1, but
the primary frequency and task-span conditions failed.

The machine-readable result is
[`runs/r1/analysis.json`](runs/r1/analysis.json).

## Cost and closure

| Condition | Calls | Submitted | Turn-limit endings | Prompt tokens | Completion tokens | Total tokens | Model time |
|---|---:|---:|---:|---:|---:|---:|---:|
| S0 static | 39 | 5/5 | 0 | 300,174 | 10,452 | 310,626 | 670,270 ms |
| C1 current | 60 | 4/5 | 1 | 914,282 | 33,334 | 947,616 | 2,127,965 ms |

C1 used 636,990 additional tokens: 3.05 times S0, or 205.05% more.
Its summed model time was 3.17 times S0, or 217.47% more. These are local
package costs, not throughput benchmarks.

The expense was not just the bytes of one audit. Because each current audit
was appended to the ordinary transcript, old and new complete audits remained
visible together. Repeated audits increased later prompt cost and changed the
decision environment. In two cells that environment sustained work without
quality progress.

## What the literal trajectories establish

### One genuine currentness win

In `rb-223607`, the common prefix ended with the same first patch and a 7/12
current audit. The branches then diverged. S0 repaired constructor conflict
and one ID-type case, ran the narrow check, and submitted at 9/12 and 54/58.

C1's mutation-bound audits progressed 7/12 -> 8/12 -> 9/12 -> 11/12 ->
12/12. Its later patches separated wrong-type from empty-value validation in
the constructor, availability, rescheduling, and view paths. It submitted the
only additional complete candidate. The timing, literal expected/observed
objects, and matched prefix make refreshed audit use a plausible cause of this
gain.

### Current truth did not guarantee a usable effect

In `rq-314159`, the first refreshed audit disclosed exactly two constructor
subcases: a wrong container raised no exception and a wrong item raised
`AttributeError` instead of `TypeError`. Qwen first emitted an exact no-op.
It then authored a whole-file patch containing both correct guards, but used
an invented file hash. The tool returned the exact current hash. Qwen repeated
the same wrong hash six times, including after rereading the file, and finally
submitted the unchanged 11/12 candidate. S0 reached the same artifact in five
turns; C1 used thirteen.

This is not semantic absence. The intended action contained the missing
mechanism, but it failed at the exact action-admission boundary and never
changed the candidate.

### Repeated truth could sustain nonprogress

In `rb-314159`, every refreshed audit continued to show the same three
validation predicates failing. Qwen repeatedly changed a combined validation
branch between `TypeError` and `ValueError`, alternately helping wrong-type or
empty-value subcases without splitting the condition. It made nine accepted
mutations, stayed at 9/12 and 54/58, and hit the 18-turn cap without checking
or submitting.

S0 also ended at 54/58, but its combined-branch edit fixed four wrong-type
subcases while regressing four previously passing empty-value subcases. C1
ended with no trunk-passing subcase regression, but that containment came with
oscillation and no completed workflow. A grouped whole-predicate headline
alone would miss this difference.

In `rb-173205`, C1 received three refreshed audits, then made two exact no-op
whole-file rewrites before submitting at the same 8/12 and 50/58 as S0. In
`rq-223607`, both branches generated the same five actions and the same
contract-complete artifact; the one passing current audit was inert.

See [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md) for the literal
pair-by-pair review.

## Research decision

The automatic append-after-every-mutation treatment is closed. Do not add it
to the stable harness, tune its wording, make it a default card, or infer that
verification currentness alone solves false closure.

The bounded conclusion is:

> A current complete audit can sometimes carry exact failures through several
> repairs and can expose newly exchanged subcases, but automatically appending
> the full audit after every mutation is neither reliable nor economical. The
> model can still compress distinct cases into one branch, generate a correct
> intended repair that fails action admission, repeat no-op work, or continue
> without closure.

The next high-value method question, if continued, is not another persistent
audit feed. It is a fresh **closure-bound complete-audit method scout**:

```text
ordinary work
-> model attempts submit
-> run complete audit on that exact candidate
-> if incomplete, return the complete expected/observed audit, including
   passing controls
-> ordinary repair continues
-> every later submit is checked against its exact candidate
```

That would test complete verification where false closure actually occurs
while avoiding an audit after every ordinary mutation. It is a removable
whole-method experiment, not a promoted gate. It must preserve the first
submit candidate, later work curve, regressions, rejected actions, and cost;
task adapters without independently reviewed complete executable coverage do
not qualify.

The transcripts also expose two separate research objects—type/value
condition splitting and exact patch-basis copying—but they do not earn generic
action coaching or protocol repair. Keep them as observed failure phenotypes
until a fresh broader method reproduces them.

## Validation boundary

- Both task-author goldens pass 12/12 complete predicates; both starting
  candidates fail their visible and complete checks.
- Five qualifying common trunks across both task families produced ten branch
  episodes; the sixth trunk is preserved as ineligible.
- 16/16 saved trunk and branch episodes replay-verify.
- All 19 automatic audits rerun to the saved expected/observed result and
  candidate identity.
- All five common-prefix comparisons pass.
- 10/10 targeted apparatus tests pass.
- The repository-wide local suite initially exposed a Windows checkout
  mismatch: source `.txt` fixtures were materialized with CRLF while frozen
  run copies and recorded identities used LF. `.gitattributes` now pins tracked
  text fixtures to LF while the later run-custody override remains binary.
  Only working-tree files whose LF form exactly matched their indexed blob were
  normalized. The complete suite then ran 634 tests successfully, with 14
  intentional archived-continuation skips.
- The first completed C1 episode exposed a replay-only seam: stable replay did
  not know the experiment-added audit message. The saved trajectory was not
  rerun. A removable adapter now reconstructs that exact message and delegates
  all ordinary records to stable replay; the stable `workbench/` is unchanged.
  See [`APPARATUS_CORRECTION.md`](APPARATUS_CORRECTION.md).
- Every qualifying trunk and branch was directly inspected from exact
  requests, responses, parsed actions, tool results, audits, snapshots, diffs,
  checks, submissions, and terminal files.
- The run used Qwen3.8-27B IQ2 through llama.cpp b10434 with the frozen
  nonthinking profile and seeds 314159, 173205, and 223607.
- The model server was stopped after the run; the process and port were absent
  and dedicated VRAM returned to the desktop baseline.
- Validation is local, not GitHub Actions verification.
