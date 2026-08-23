# Virtualized context residency v0 — results

Date: 2026-08-17

Verdict: **mechanical virtualization preserved capacity at both seeds, but did
not produce construction or a valid artifact**

## What ran

The frozen bank executed four Q3 XL episodes in the declared order:

| Seed | Arm | Calls | Terminal state | Mutation | Check | Submit |
|---:|---|---:|---|---|---|---|
| 42 | append-only | 11 | capacity-censored before turn 12 | no | no | no |
| 42 | virtualized | 20 | model-call limit | no | no | no |
| 314159 | append-only | 11 | capacity-censored before turn 12 | no | no | no |
| 314159 | virtualized | 20 | model-call limit | no | no | no |

There were 62 model calls, one attempt per episode, and no retry. The runtime
loaded the frozen Q3 XL package with all 66 layers on the GPU, used the exact
25,088-token context, and shut down cleanly.

Immediate same-process custody replay passed for every episode. A later fresh-
process replay exposed one reproducibility defect: the projection ledger's
expanded/collapsed receipt arrays inherited Python set iteration order. Raw
requests and receipts are exact, but byte-for-byte reconstruction in a process
with a different hash seed changed only those array orders. Sorting the arrays
by receipt ID made all 62 requests and receipts match. This does not change the
capacity or action result, but future projection renderers must sort every
model-visible collection and pass replay in a fresh process.

## Primary comparison

The capacity effect replicated. Append-only accumulated enough literal result
history that turn 12 failed the full-allowance gate at both seeds. Virtualized
history kept exact resident content below the frozen 24,000-byte limit and
completed all 20 allowed calls at both seeds.

| Seed | Append final/failed headroom | Virtual minimum headroom | Append max exact residency | Virtual max exact residency |
|---:|---:|---:|---:|---:|
| 42 | +2,127 / -778 tokens | +388 tokens | 40,672 bytes | 23,458 bytes |
| 314159 | +73 / -99 tokens | +4,055 tokens | 25,134 bytes | 23,642 bytes |

This did not become an action-quality benefit. Neither virtualized actor
modified the candidate, invoked the visible check, or submitted. The method
changed the stop boundary from context capacity to the 20-call limit.

## Acquisition behavior

The virtualized actors used exact reopening correctly at the mechanical
boundary: each made five accepted `reopen_receipt` calls. No stale or invented
summary substituted for the exact source. Neither actor pinned or released a
receipt.

Virtualization did not reduce total acquisition. Across the two seeds:

- append-only used 257,480 successful inference tokens;
- virtualized used 482,569, an 87.4% increase;
- append-only initially transferred 65,806 exact-content bytes;
- virtualized initially transferred 89,172 bytes and reopened another 46,076;
- virtualized target coverage was seed-dependent: 551 of 970 lines at seed 42
  and 183 at seed 314159, versus 351 and 200 in append-only.

The model therefore did not simply keep reading because old bytes were forced
to remain visible. Once older bytes became handles, it spent additional calls
faulting evidence back in and acquiring more target regions.

## What the transcripts show

Both virtualized actors understood the governing update before they stopped.

- At seed 42, turn 15 contained a detailed account of both source studies,
  where each trajectory stopped, the package boundaries, the no-promotion
  limits, and a concrete plan for updating observations, design consequences,
  and open questions.
- At seed 314159, turn 13 produced the same substantive synthesis and identified
  the exact document regions that should change.

They nevertheless continued gathering. The seed-42 actor explicitly counted
19 used calls, recognized that patch, check, and submit could not fit in the
one remaining call, and still chose another source read. The seed-314159 actor
had the four governing result/audit documents and key target regions, then
returned to reopening sources and seeking broader target coverage.

This localizes the observed boundary more precisely:

```text
exact external custody              worked
mechanical collapse and reopening   worked
bounded literal residency           worked
governing-result interpretation     worked
operative acceptance of a sufficient set / transition to construction
                                      did not occur
```

## Interpretation

This is a stable capacity result and a negative whole-method result on one
authentic development anchor.

The evidence supports keeping exact history externally reopenable rather than
requiring every literal result to remain resident. It does not support the
claim that mechanical eviction alone makes the model work selectively or act
sooner. The dominant remaining problem was acquisition-frame and action
organization: the model treated additional document understanding as safer
than beginning a bounded edit, even after it could state the correct update
and a plausible edit plan.

The result does not establish that the 24,000-byte budget, least-recently-
accessed policy, pin ceiling, or 20-call limit is optimal. It provides no
artifact-quality comparison because construction never began.

The process-local array-order defect also prevents calling the exact renderer
byte-deterministic across processes. It is a custody limitation, not an
explanation for the unchanged candidates: the measured requests are preserved,
the unordered ledger carries the same mechanical records, and normalized
fresh-process replay reproduces every other field.

## Decision

Do not promote LRU eviction, pinning, automatic virtualization, a context
compiler, or a resident-set controller into `workbench/`.

Retain the architectural distinction between complete exact custody and
bounded literal residency. If this line continues, the next controlled
question should concern the transition from a model-understood evidence set to
construction, not another eviction-policy tuning exercise.

See the [`direct transcript audit`](DIRECT_TRANSCRIPT_AUDIT.md), frozen
[`protocol`](../../FREEZE.md), and exact
[`post-run verification`](POSTRUN_VERIFICATION.json).
