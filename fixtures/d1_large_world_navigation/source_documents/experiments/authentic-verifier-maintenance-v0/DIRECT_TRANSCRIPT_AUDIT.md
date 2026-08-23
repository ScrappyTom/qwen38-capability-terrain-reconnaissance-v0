# Authentic verifier maintenance direct transcript audit

Date: 2026-08-17

Status: **complete; every request/action/result boundary inspected**

## Evidence boundary

This is an authentic repository-maintenance case study, not a controlled phase comparison or a
reliability estimate. The investigator read the literal task, every model request and returned
schema action, every tool result or rejection, every candidate transition, every check receipt,
the terminal artifacts, and the saved runtime records before adopting or interpreting the repair.

All four model phases used Qwen3.8-27B AD-IQ2_S with q8 KV, 25,088 context, MTP off, and 66/66 GPU
offload. The stable `workbench/` was not changed. Each fresh phase received the complete task,
exact current candidate, ordinary tools, and only the literal prior boundary receipt described
below. It received no semantic checkpoint, plan, summary, selected-file list, or prior transcript.

## Apparatus incidents

- `r0` made zero model calls. A long Windows custody path failed before the first request.
- The initial manual R2 acceptance invocation wrote 15 Python cache files into the candidate. The
  paths, sizes, and hashes are recorded in `OUT_OF_BAND_BYTECODE_MANIFEST.json`; moving those
  derived files restored candidate `97d731...` exactly. The resulting zero-call `r3a` failure is
  preserved.
- The acceptance loader now disables bytecode generation. This changes no acceptance predicate.
- After R3, the receipt renderer was corrected to disclose each case's literal input mutation.
  The acceptance programs, task, tools, candidate, and pass/fail rules were unchanged.

Neither zero-call incident is model evidence.

## Literal phase audit

### R1: ordinary acquisition, no mutation

The first request contained the complete maintenance task and the ordinary schema-action system
contract. Qwen opened the repository tree, `verify_r2.py`, both R2 source locks, `run_study.py`,
and finally the complete 26,894-byte `workbench/replay.py`. It also searched for saved R2 run
directories that were intentionally absent from the task workspace and ran the acceptance check.

The 13 admitted actions were three trees, four searches, five reads, and one check. No action
mutated the candidate. Turn 14 was rejected by llama.cpp before inference because its 25,145-token
prompt exceeded the 25,088 context. Candidate identity remained `046518...`.

### R2: fresh exact-world reentry, broad repair, one unresolved case

R2 began from the unchanged `046518...` candidate. The only continuity object was the literal R1
capacity receipt. Qwen reread the verifier, historical lock, `run_study.py`, and provider source,
then replaced the old per-file loop with an expected-runtime-set, manifest, duplicate-path, exact
metadata, directory-agreement, and byte-identity check.

The first patch moved the acceptance result from two passing cases to seven. The sole remaining
failure was `malformed_manifest_identity`. Qwen's second patch added entry-field and SHA formatting
checks, but omitted `import re` and did not validate the top-level `manifest_id`. Turn 16's prompt
was 26,923 tokens and was rejected before inference. The admitted candidate was `97d731...`.

### R3: exact current defect visible, ambiguous case label misbound

After removing the out-of-band bytecode, R3 began from exact candidate `97d731...`. Its boundary
receipt included the literal valid-case failure `NameError: name 're' is not defined`. Qwen added
the import immediately. The next check reported only one case label and result:
`malformed_manifest_identity: incorrectly accepted`.

The model then treated “identity” as per-entry file metadata. It added duplicate entry checks,
emitted one exact no-op replacement, searched for absent saved-run material, and partially reverted
and restored redundant validations. It never checked the actual top-level manifest identity. The
net useful effect was the `re` import. Turn 17's 25,343-token prompt was rejected before inference;
candidate `5e1856...` remained.

This trajectory does not establish that Qwen ignored the exact malformed-manifest setup. That
setup had not crossed the model boundary.

### R4: literal case mutation, correct repair, check, submit

R4 began from exact candidate `5e1856...`. The receipt now stated that `manifest_id` had been
replaced with 64 zeroes while the manifest entries and saved sources remained valid. Qwen read the
verifier and nearby test/lock material, ran the 7/8 check, added top-level manifest-identity
validation, reran the check at 8/8, and submitted current candidate `961ca4...`.

The 12 admitted actions were two trees, three searches, three reads, two checks, one patch, and one
submission. The run grade and replay both passed.

## Candidate lineage and cost

| Phase | Initial | Final | Requests | Admitted actions | Successful tokens | Terminal state |
|---|---|---|---:|---:|---:|---|
| R1 | `046518...` | `046518...` | 14 | 13 | 139,947 | context error |
| R2 | `046518...` | `97d731...` | 16 | 15 | 175,198 | context error |
| R3 | `97d731...` | `5e1856...` | 17 | 16 | 207,684 | context error |
| R4 | `5e1856...` | `961ca4...` | 12 | 12 | 106,781 | submitted, passed |

Across the four model phases: 59 requests, 56 admitted actions, three context-limit requests,
622,005 successful prompt tokens, 7,605 completion tokens, and 629,610 total successful tokens.
Fresh reentry restored capacity but was not efficient in this task; the model repeatedly reacquired
broad material and saturated the same 25K envelope three times.

## Product review and adopted repair

The submitted model patch passed all eight adversarial cases. It was not copied verbatim into the
repository. Direct code review found avoidable complexity: it introduced `re`, coupled expected
manifest construction to lock ordering, and mixed top-level identity validation with entry-shape
validation.

The adopted repair keeps the model-discovered behavior while simplifying the implementation:

- derive the frozen runtime-source set mechanically from the historical lock;
- require exact equality among expected, declared, and saved source sets;
- validate the actual manifest's canonical self-identity;
- reject duplicate or malformed entries;
- require manifest metadata to equal the historical lock; and
- re-hash every saved source byte sequence.

Durable tests cover the valid snapshot and seven independent corruption/mismatch cases. The
current verifier passes all ten historical R2 runs at 17 runtime-source files per run. The current
source lock now includes `verify_r2.py` itself; the historical lock and saved runs are unchanged.

## Bounded interpretation

This case supports three observations:

1. Fresh exact-world reentry can continue authentic maintenance after a natural capacity boundary.
2. A complete task frame plus exact current world is not automatically a small working set; repeated
   broad reacquisition can make fresh phases expensive and saturate them again.
3. A pass/fail label is not a discriminating diagnostic when the checker changed a concrete nested
   value. Showing the literal test mutation changed the decision environment and preceded the
   correct repair. This is a receipt-specific finding, not a claim that more context or more truth is
   always better.

No automatic reset, context router, checkpoint, reviewer, card, or semantic host diagnosis is
earned. The specific systems correction is narrower: when a check mechanically knows the exact
setup, expected value, and observed result, its receipt should preserve those literal facts.
