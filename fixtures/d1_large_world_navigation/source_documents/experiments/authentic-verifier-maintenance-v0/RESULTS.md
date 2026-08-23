# Authentic verifier maintenance v0 results

Status: **complete; real verifier defect repaired, no new live harness policy promoted**

Date: 2026-08-17

## Outcome

The R2 post-run verifier now proves complete three-way agreement among the frozen runtime-source
set, saved harness manifest, and saved source directory. It also validates the manifest's canonical
self-identity, rejects duplicate/malformed entries, compares manifest metadata to the historical
lock, and re-hashes every saved source file.

The repair passes:

- 8/8 experiment acceptance cases;
- 13/13 longitudinal unit tests;
- the 642-test default repository suite (628 passed, 14 intentional skips);
- all six standard and four transcript R2 run verifications;
- all four model-phase custody replays; and
- the existing current-source lock and post-run verification after regeneration.

The historical R2 lock and saved trajectories were not changed. The stable `workbench/` remains
unchanged.

## What the model trajectory showed

Qwen3.8 eventually produced a behaviorally correct patch, but only after four fresh phases and
629,610 successful tokens. The first three phases each ended at the 25,088 context boundary.

Fresh exact-world reentry did preserve continuity: R2 continued from R1's unchanged candidate, R3
continued from R2's partial repair, and R4 continued from R3's current artifact without a transcript,
summary, plan, or checkpoint. It was a recovery surface, not an efficiency win. The model repeatedly
reread broad source material and reconstructed much of the same context.

The decisive observed change was feedback specificity. R3 saw only the label
`malformed_manifest_identity` and interpreted it as per-file SHA metadata. R4 saw the literal setup:
the top-level `manifest_id` was replaced by 64 zeroes while entries and sources remained valid. It
then added the missing canonical manifest identity check, passed 8/8, and submitted.

This does not show that a receipt supplies semantic intelligence. It shows that the prior receipt
discarded a mechanically known discriminating operand.

## Decision

- Keep the sparse operating model: exact custody, complete task/purpose, current world, ordinary
  within-phase history, ordinary source access, and feasible exact actions.
- Keep fresh reentry removable and use it at naturally observed capacity/work boundaries, not on an
  automatic schedule.
- Preserve literal check setup and expected/observed facts when the tool has them. A case name plus
  red/green status is not equivalent to the diagnostic.
- Do not add a checkpoint, card, phase router, reviewer, or semantic host diagnosis.
- Do not chain repeated fresh phases merely because they restore headroom. Continue only when the
  exact world or receipt changes enough to create a materially different decision environment.
- Retain investigator review before integrating model code. Passing acceptance established behavior,
  not maintainability; the adopted implementation is simpler than the submitted patch.

## Evidence

- [`task.md`](task.md)
- [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md)
- [`METRICS.json`](METRICS.json)
- [`APPARATUS_CORRECTION.md`](APPARATUS_CORRECTION.md)
- [`POSTRUN_VERIFICATION.json`](POSTRUN_VERIFICATION.json)
- exact runs under [`runs/`](runs/)
