# Action-basis persistence v0 — direct transcript audit

Date: 2026-08-18

The investigator inspected all 60 exact requests, responses, interpreted
actions, literal tool results, action bases, current-work surfaces, capacity
receipts, projection receipts, candidate snapshots, record chains, and the
runtime stop before using aggregate metrics.

## Custody and runtime

- Q3 XL ran with the frozen Qwen3.8-27B UD-Q3_K_XL profile, q8 KV, 25,088
  actual context, medium thinking, and a 4,096-token response allowance.
- All 66 model layers were offloaded.
- Sixty responses were created: 20 in each observed episode.
- No retry, replacement response, mutation, check, or submission occurred.
- All final candidate IDs equal the starting candidate ID
  `19296f821cc2bf7e32384ec88080ba49aedc4afe1f1f9961c31d57c2e1dc24fd`.
- The server stopped after the verifier error and GPU use returned to its
  pre-run level.

## Literal seed-42 comparison

The first request and first action are byte-identical across the two arms. The
first action was an invalid candidate-tree request for `experiments`; the
literal rejection was delivered on turn 2.

### Audit-only

The actor used three tree calls, eight catalog calls, one search, two artifact
catalog calls, one artifact-region read, three repository reads, one rejected
whole-artifact read, and one exact reopen.

It obtained the selected-working-window result at turn 7, the operational
artifact region at turn 15, the handoff result at turn 17, and the residency
result at turn 18. It ended by searching for audits and reopening its first
result. Every action basis continued to name unresolved evidence or artifact
requirements.

### Persisted

The exact prior basis appeared in every request after turn 1. The actor used
12 catalog calls and two searches before beginning a sequence of five exact
repository reads at turns 16–20. It ended with five governing files and no
candidate-region content.

The displayed prior basis remained internally coherent, but it repeatedly
encoded the same acquisition frame: locate paths, read all six files, then
inspect the candidate. The model did not externalize a completed synthesis or
construction-ready continuation for the treatment to preserve.

The treatment therefore functioned mechanically but carried acquisition state,
not an action commitment.

## Literal seed-314159 audit-only trajectory

The actor's sequence was:

1. inspect the candidate tree;
2. query repository paths;
3. read the design-consequence region;
4. refine repository location;
5. read handoff results;
6. read the open-question region;
7. read selected-window results;
8. query again;
9. read residency results;
10. locate direct audits;
11. read the selected-window audit;
12. reopen the handoff result;
13. read the handoff audit;
14. read the residency audit;
15. request candidate lines 1–260, rejected above the 12,000-byte read limit;
16. reopen the selected-window result;
17. reopen the residency result;
18. read candidate lines 864–970;
19. request the whole candidate, rejected above the read limit; and
20. reopen the handoff result.

The turn-18 action basis said all six governing files were in evidence and
that exact tail text was the remaining requirement for authoring old/new patch
strings. Turn 18 returned that exact tail and its current file binding. On turn
19 the actor nevertheless created a new requirement to reconfirm a complete
file hash and to restream collapsed evidence. The final action continued that
reacquisition.

This is not a capacity artifact. Prompt occupancy peaked at 16,379 tokens and
the smallest headroom after reserving the complete response was 4,613 tokens.
Nor is it missing-result delivery: the current-object ledger shows each
accepted exact result on the required next request.

The observed boundary is:

```text
governing evidence acquired
    -> target region acquired
    -> patch-oriented intention authored
    -> intention not externally returned in audit-only arm
    -> new acquisition requirement formed
    -> construction not entered
```

Because `s314159-persisted` never started, the last two transitions cannot be
attributed to loss of semantic state or to action commitment.

## Capacity and cost

| Episode | Prompt tokens | Completion tokens | Total | Cached prompt | Initial exact bytes | Reopened bytes |
|---|---:|---:|---:|---:|---:|---:|
| s42 audit-only | 210,118 | 15,455 | 225,573 | 136,513 | 25,434 | 4,004 |
| s42 persisted | 185,619 | 9,600 | 195,219 | 131,846 | 21,802 | 0 |
| s314159 audit-only | 264,697 | 27,280 | 291,977 | 154,184 | 44,167 | 22,310 |

The current-object surface prevented event-transcript capacity growth from
ending these episodes early, but it did not produce a transition to action.
Across the three trajectories, 712,769 successful inference tokens produced no
candidate change.

## Frozen verifier failure

The first two episode reports include successful completion-time fresh replay.
After the third episode's 20 calls and terminal snapshot were already saved,
the same verifier stopped at turn 18.

The defect is deterministic and localized. Live receipt registration and
reopening both advance one access counter. Frozen replay instead reconstructed
new receipts from receipt count and only separately advanced reopened receipts.
After several reopens, the two orders diverged. With a binding exact-byte
budget, replay expected four different resident objects than the measured
request.

The post-run adapter changes no measured request, response, action, result, or
candidate. It reconstructs new and reopened receipt access using the live rule,
then verifies every saved request and projection receipt byte-for-byte. All 60
turns pass. The raw runtime remains failed because the fourth episode was
correctly not started after the frozen integrity gate fired.

## Judgment

The completed evidence is descriptively negative for passive persistence on
seed 42 and inconclusive for the intended two-seed treatment effect. The
experiment also demonstrates a process safeguard working as intended: an
apparatus discrepancy stopped later calls rather than being silently ignored.

No semantic review is applicable because no candidate changed and no artifact
was submitted.
