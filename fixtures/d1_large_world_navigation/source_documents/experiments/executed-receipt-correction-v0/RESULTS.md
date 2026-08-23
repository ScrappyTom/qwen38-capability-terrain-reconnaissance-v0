# Executed receipt correction v0 — results

Date: 2026-08-15

Status: **complete; partial saved-state benefit, task-contract boundary corrected; next study not selected**

## Result in one sentence

On the frozen packet programs, literal host-executed failure receipts moved
five saved candidates from 35/47 to 40/47, with five packet repairs and no
packet regression. A later task-contract audit found a different boundary:
254/307 became 260/307 through 11 repaired predicates and five regressed
predicates, with no task-contract-complete candidate.

## What was tested

This was a conditional saved-state targeted method comparison, not a fresh
benchmark. A fresh ordinary Qwen3.8 correction actor received each of the five
defective first candidates preserved by the prior grouped-review study. It saw
the complete task, exact candidate, full task-author executable catalog, and
literal receipts for failed packets. It did not see the prior model review or
a host diagnosis/recommendation.

The historical grouped-review correction repaired zero of these 12 failures.
The new package asks a different question: once the host has actually executed
the packet, can Qwen use the exact result to repair the artifact?

## Corrected measured result

Authoritative run: `runs/erc-q38-r002`

| Cell | Source | Prior review terminal | Receipt terminal | Repairs | Remaining | Calls | Total tokens |
|---|---:|---:|---:|---|---|---:|---:|
| `s42-sv` | 7/10 | 7/10 | 8/10 | `S01` | `S05`, `S09` | 8 | 62,790 |
| `s42-pc` | 7/9 | 7/9 | 7/9 | — | `P07`, `P08` | 10 | 87,415 |
| `s42-co` | 6/9 | 6/9 | 8/9 | `C01`, `C07` | `C08` | 7 | 56,614 |
| `s314159-sv` | 8/10 | 8/10 | **10/10 packets** | `S01`, `S05` | — | 6 | 43,942 |
| `s314159-co` | 7/9 | 7/9 | 7/9 | — | `C01`, `C08` | 6 | 45,751 |
| **Total** | **35/47** | **35/47** | **40/47** | **5** | **7** | **37** | **296,512** |

Other exact totals:

- prompt tokens: 289,801;
- completion tokens: 6,711;
- model HTTP duration: 471,880 ms;
- mutated candidates: 5/5;
- submitted candidates: 5/5;
- packet-complete terminal candidates: 1/5;
- task-contract-audit-complete terminal candidates: 0/5; and
- regressions among 35 initially passing packets: 0.

All five trajectories, source packet results, and terminal packet results
replay with zero verification errors. The one 10/10 packet terminal also
passes the task's submission grader because that grader executes the same
packet catalog; it is not an independent complete-task verifier.

## Post-run task-contract audit correction

The original packet programs were exact but sampled. Their broad purpose
labels did not prove the sibling behaviors they never executed. A separate
offline audit mapped the written contracts to 180 independently scored
predicates, qualified all three task-author goldens at 180/180, and then ran
the same suites against the five exact source/terminal pairs.

| Cell | Source | Terminal | Fixed predicates | Regressed predicates |
|---|---:|---:|---:|---:|
| `s42-sv` | 58/67 | 58/67 | 1 | 1 |
| `s42-pc` | 41/53 | 41/53 | 1 | 1 |
| `s42-co` | 47/60 | 51/60 | 6 | 2 |
| `s314159-sv` | 60/67 | 62/67 | 3 | 1 |
| `s314159-co` | 48/60 | 48/60 | 0 | 0 |
| **Total** | **254/307** | **260/307** | **11** | **5** |

The validation edits in both Session Vault cells fixed empty-user behavior but
regressed wrong-type users from `TypeError` to `ValueError`. The seed-42
Config edit similarly fixed empty keys while regressing non-string keys in
Layer construction and amendment. Priority Catalog fixed one failed-add
category-position behavior while regressing replacement-established category
order.

See the qualified [`contract audit`](contract_audit/RESULTS.md), its
[`requirement map`](contract_audit/REQUIREMENT_MAP.md), and its
[`machine-readable summary`](contract_audit/results/contract-audit-summary-v1.json).

## What the aggregate hides

Qwen made a mutation related to 11 of 12 failed receipts. Only five mutations
made the complete packet pass. Six were topically relevant but
mechanism-incomplete, and one receipt was not acted on.

The common incomplete patterns were:

- combining wrong-type and empty-value validation into one branch, thereby
  fixing one expected exception while preserving or creating the other error;
- representing persistent insertion/category/user order with a temporary
  sort or grouping operation that could not preserve the required history;
- responding to a concrete failed check with an exact no-op patch; and
- rereading the current file but then binding a later patch to an older file
  hash.

The original packet grouping described local validation/lifetime improvement
as 5/9 versus 0/3 history/order. The broader audit preserves a local-versus-
history mechanism lead, but it also shows that local representative repairs
can exchange one sibling behavior for another. Packet repair, task-predicate
repair, regression, and net quality must therefore remain separate outcomes.

## Apparatus correction

The first attempt, `erc-q38-r001`, is preserved but excluded. Its copied
visible-check and grader scripts used a fixed directory depth and could not
find `packet_runtime.py` from the frozen run layout. Independent terminal
packet replay remained valid, but the actors saw an infrastructure error in
place of the intended check.

The correction made runtime discovery path-independent and added a regression
test that executes every visible check and grader on every golden candidate
from the exact snapshotted run layout. The replacement run received a new
source lock and run ID. See [`APPARATUS_CORRECTION.md`](APPARATUS_CORRECTION.md).

The corrected result matters: Priority Catalog's intended check exposed the
still-failing `P07`, and Qwen used ten calls rather than seven. It nevertheless
submitted the same 7/9 candidate. The invalid check was therefore not harmless,
even though the terminal score happened not to change.

## Decision

The result meets the frozen discovery threshold only in the narrower sense
that several literal receipts produced concrete repairs. The post-run audit
withdraws the earlier no-regression and complete-candidate claims. It does not
yet justify freezing an unchanged prospective package: future work must first
choose whether it is testing receipt value, contrastive sibling preservation,
or temporal-state presentation, with task-contract coverage qualified before
calls.

It does **not** earn:

- a change to stable `workbench/`;
- an always-on task-author packet system;
- host-authored semantic diagnosis or repair advice;
- a default reviewer;
- automatic retries or argument repair; or
- a claim that exact truth is sufficient for correction.

## Follow-up boundary

No follow-up model run is selected by this report. Any next study must:

1. map written requirements to independently scored executable predicates;
2. qualify those predicates on known-good artifacts from the exact frozen
   layout;
3. preserve grouped presentation separately from predicate-level scoring;
4. compare both fixes and regressions from the exact source candidate; and
5. directly inspect every saved prompt, raw response, action/result sequence,
   terminal artifact, and verifier before interpreting aggregate counts.

## Evidence

- [`FREEZE.md`](FREEZE.md)
- [`PRECALL_AUDIT.md`](PRECALL_AUDIT.md)
- [`CORRECTED_PRECALL_AUDIT.md`](CORRECTED_PRECALL_AUDIT.md)
- [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md)
- [`contract_audit/RESULTS.md`](contract_audit/RESULTS.md)
- [`runs/erc-q38-r002/verification.json`](runs/erc-q38-r002/verification.json)
- [`runs/erc-q38-r002/analysis.json`](runs/erc-q38-r002/analysis.json)

## Local validation boundary

- The study's seven focused tests pass, including golden execution from the
  exact frozen run layout.
- The separate contract audit's seven tests pass and all three goldens qualify
  at 180/180 predicates.
- Independent verification of all five corrected trajectories and their
  source and terminal packet catalogs reports zero errors.
- All local links in the updated evidence documents resolve, and staged diff
  validation is clean.
- The repository-wide offline suite is not green: 634 tests ran, with 584
  passing, 14 archived-continuation skips, and 36 errors from pre-existing
  frozen-fixture or review-artifact mismatches in unrelated historical
  experiments. This study changes none of those failing paths and does not
  claim repository-wide validation.
