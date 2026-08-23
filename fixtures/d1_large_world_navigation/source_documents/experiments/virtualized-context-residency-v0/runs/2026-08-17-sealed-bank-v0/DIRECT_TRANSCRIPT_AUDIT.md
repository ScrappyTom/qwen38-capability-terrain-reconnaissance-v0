# Virtualized context residency v0 — direct transcript audit

Date: 2026-08-17

## Custody

The audit inspected all 62 exact requests, responses, interpreted actions,
tool results, capacity receipts, projection receipts, terminal records, and
final candidate identities under
`runs/2026-08-17-sealed-bank-v0/`.

All four immediate same-process residency replays passed. The runtime record
confirms Q3 XL UD-Q3_K_XL, q8 KV, 25,088 context, llama.cpp b10434, and 66/66
GPU layers. There were no retries. The server stopped after the bank and GPU
memory returned to its pre-run level.

A separate fresh-process replay then failed on model-visible projection-ledger
array order. The renderer formed the resident IDs as a Python set before
serializing `expanded_exact_receipts` and `collapsed_exact_receipts`; iteration
order therefore depended on the process hash seed. Inspection found no content,
membership, request-history, action, result, or capacity difference. A replay
that canonicalized those mechanically unordered arrays by `receipt_id`
reconstructed all 11, 20, 11, and 20 requests respectively. The exact measured
requests remain authoritative. This is a real cross-process determinism defect
that must be fixed before reusing the renderer, but it does not require a model
retry or alter the observed stop boundaries.

## Mechanical findings

| Episode | Accepted / rejected actions | Target lines acquired | Initial exact bytes | Reopened exact bytes | Max collapsed receipts |
|---|---:|---:|---:|---:|---:|
| s42 append-only | 10 / 1 | 351 | 40,672 | 0 | 0 |
| s42 virtualized | 18 / 2 | 551 | 62,198 | 23,038 | 8 |
| s314159 append-only | 11 / 0 | 200 | 25,134 | 0 | 0 |
| s314159 virtualized | 19 / 1 | 183 | 26,974 | 23,038 | 5 |

The append-only rejections were one invalid tree path at seed 42; the terminal
capacity gates themselves occurred before inference. Each virtualized run
first attempted an inadmissible whole-file read. Seed 42 later requested one
12,852-byte line range above the disclosed 12,000-byte read limit. These
rejections were visible and did not change the candidate.

Every accepted reopen returned the original exact content with its original
source/version binding. The following request either retained that receipt
literally or represented it by its exact handle according to the frozen
resident budget. No semantic summary was generated. Neither virtualized actor
used `pin_receipts` or `release_receipts`.

## Append-only trajectories

Seed 42 opened the design-consequence region, the four governing result/audit
documents, and the final three large artifact regions. Its next request was
blocked before turn 12 with -778 tokens of full-allowance headroom.

Seed 314159 opened the four governing result/audit documents, target lines
1–200, and searched the target. Its next request was blocked before turn 12
with -99 tokens of full-allowance headroom.

Neither actor mutated, checked, or submitted. The capacity diagnosis is exact:
the runner did not send an oversized request.

## Virtualized trajectory, seed 42

The actor's first whole-file read was rejected as disclosed. It then acquired
all four governing documents, target lines 1–200, the operational, phase-
continuity, design-consequence, and open-question regions, and additional
middle target material. It made five accepted reopen calls and repeated two
repository reads.

At turn 15 its reasoning already contained an adequate source synthesis and a
specific edit plan. It correctly preserved that the two earlier studies
stopped before construction and did not justify promoting a map, handoff,
controller, or phase policy. Rather than edit, it continued reading.

At turn 20 it accurately counted that 19 calls had been used and stated that
one call could not cover the remaining reads, patch, check, and submit. It
still selected another governing-source read. The episode ended at the exact
20-call ceiling with an unchanged candidate.

## Virtualized trajectory, seed 314159

The actor's whole-file read was also rejected. It acquired all four governing
documents, selected the phase-continuity and design-consequence regions from
the mechanical outline, and opened target lines 1–33. It made five accepted
reopen calls.

At turn 13 it had already distinguished both studies, their stop boundaries,
their package/method limits, three separate earlier failure modes, the
unexecuted handoff question, and the required no-promotion conclusion. It also
identified the regions it intended to revise.

It then reopened each governing source and sought additional target context.
The final action was another reopen. The episode ended at 20 calls without a
mutation, check, or submission.

## Boundary judgment

The virtualized failures were not caused by missing governing evidence,
incorrect receipt restoration, GPU transport, response truncation, or hidden
capacity failure. They occurred after the model could describe the correct
update and before action expression.

Primary observed boundary: **action organization / transition from acquisition
to construction**.

Contributing frame: the maintained integrated document was treated as needing
broader understanding before safe modification. Mechanical residency created
room for that policy to continue; it did not change the policy.

No semantic artifact score is reported because all four final candidates are
byte-identical to their starting candidates.
