# Action-basis persistence v0 — results

Date: 2026-08-18

Verdict: **incomplete bank; no demonstrated construction benefit from passive
action-basis persistence**

## What executed

The frozen order began correctly and made 60 of the authorized maximum 80
model calls. Three episodes completed their 20 model calls. The fourth episode
never started because the frozen post-episode replay raised an integrity error
after `s314159-audit_only`.

| Seed | Arm | Calls | Terminal behavior | Mutation | Check | Submit |
|---:|---|---:|---|---|---|---|
| 42 | audit-only | 20 | call limit | no | no | no |
| 42 | persisted | 20 | call limit | no | no | no |
| 314159 | audit-only | 20 | call limit; report interrupted by verifier | no | no | no |
| 314159 | persisted | 0 | never started | — | — | — |

There were no retries. The runtime loaded Q3 XL with the frozen 25,088-token
context and all 66 layers on the GPU. It stopped the server after the integrity
gate failed, and GPU memory returned to its pre-run level.

The complete four-cell causal comparison therefore did not execute. Only the
seed-42 arm pair may be compared directly, and one pair cannot establish a
replicated treatment effect.

## The persistence mechanism crossed the interface

The two seed-42 arms had byte-identical first requests and byte-identical first
actions. Thereafter:

- every persisted request from turns 2–20 contained the exact prior
  model-authored action basis;
- every audit-only request from turns 2–20 contained only the basis hash and
  authorship turn; and
- neither arm referenced an unknown evidence receipt.

The negative seed-42 result is therefore not explained by failure to return
the treatment.

## Seed-42 matched result

Both actors spent all 20 calls acquiring and locating information and neither
entered construction.

| Measure | Audit-only | Persisted |
|---|---:|---:|
| Model calls | 20 | 20 |
| Repository catalog/search calls | 9 | 14 |
| Exact repository reads | 3 | 5 |
| Candidate/artifact-region reads | 1 | 0 |
| Initial exact bytes acquired | 25,434 | 21,802 |
| Exact bytes reopened | 4,004 | 0 |
| Total inference tokens | 225,573 | 195,219 |
| Minimum headroom after reserving the full response | 6,114 | 8,289 |
| Mutations/checks/submissions | 0/0/0 | 0/0/0 |

The persisted actor used 13.5% fewer total tokens, but that is not an action
benefit. It spent its first 15 calls navigating catalogs and searches before
opening the first exact governing file. By turn 20 it had opened five of the
six requested result/audit files but had not inspected the maintained
artifact. The audit-only actor opened exact governing evidence earlier but
also remained incomplete.

Most importantly, neither seed-42 actor authored a basis that said the work
was ready for construction. Their bases continued to describe missing paths,
unread governing files, or unread artifact regions. Returning such a basis
preserved an acquisition plan; it did not supply a previously formed action
commitment. This cell therefore shows that passive persistence does not by
itself create readiness or terminate acquisition.

## The unpaired seed-314159 lead

The audit-only actor at seed 314159 made more substantive progress:

- it acquired all six governing result/audit files by turn 14;
- it held the relevant design and open-question regions;
- after one oversized range rejection, it acquired the exact current tail at
  turn 18; and
- its turn-18 basis explicitly said that the tail was needed so it could author
  the patches.

After that exact tail was delivered, it did not patch. It attempted a complete
file read to reconfirm the hash, received the disclosed read-limit rejection,
and used its final call to reopen an earlier result. Capacity did not stop it:
the minimum full-allowance headroom remained 4,613 tokens.

This is the clearest observed synthesis-to-action phenotype in the bank. It is
also exactly the cell whose persisted counterpart never ran. The trajectory
therefore supports retaining the semantic-persistence versus action-commitment
question; it does not answer it.

## Verifier correction and custody

The frozen verifier failed at turn 18 of `s314159-audit_only`. Its replay logic
assigned a newly reconstructed receipt a last-access value based on the number
of receipts. The live executor increments an access counter, which can already
be larger after exact reopen operations. Once the resident budget became
binding, the wrong replay order selected a different exact-versus-collapsed
set.

The measured request was not regenerated or changed. A post-run adapter using
the live access-counter rule reproduces all 20 requests and projection receipts
for each of the three observed episodes byte-for-byte. All three record chains
and every referenced artifact also verify.

This correction does not turn the runtime record into a pass. The bank remains
incomplete because the frozen integrity gate stopped before the fourth episode.
See [`POSTRUN_VERIFICATION.json`](POSTRUN_VERIFICATION.json) and the
reproducible [`postrun_analyze.py`](postrun_analyze.py).

## Interpretation

The evidence supports four narrow statements:

1. A canonical current-object surface kept all three observed trajectories
   within the 25K envelope for 20 calls.
2. Exact prior action-basis content can be carried into every later request
   without a separate memory action.
3. On the one complete matched seed, that passive persistence did not cause
   construction and did not end acquisition.
4. The strongest action-ready-looking transition occurred only in the
   audit-only seed whose persisted counterpart was prevented from running.

It does **not** support promoting action-basis persistence, current-object
projection, an acquisition gate, a plan/memory facility, or a semantic
controller. It also does not establish that persistent semantic state is
irrelevant.

## Decision

Do not retry any of the 60 measured calls and do not report the missing cell as
a model failure. Before any reuse, correct and regression-test the replay
access-counter rule.

If this exact line is completed, the smallest defensible continuation is a
separately authorized, explicitly labeled successor containing only the
never-started `s314159-persisted` cell under the frozen model/task/treatment
limits. Its value is narrow: determine whether returning the model's prior
action basis helps when the matched audit-only trajectory had already formed a
specific patch-oriented continuation. A completion would not retroactively
make this interrupted bank a clean four-cell run.

See the [`direct transcript audit`](DIRECT_TRANSCRIPT_AUDIT.md), frozen
[`protocol`](../../FREEZE.md), and exact [`analysis ledger`](ANALYSIS.json).
