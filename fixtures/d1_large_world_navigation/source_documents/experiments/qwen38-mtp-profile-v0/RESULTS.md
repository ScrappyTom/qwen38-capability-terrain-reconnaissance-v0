# Qwen3.8 embedded-MTP profile results

## Decision

Embedded MTP is a large, package-specific decode-speed improvement, but this
screen does not promote it into either stable profile.

- `AD-IQ2_S` / q8 KV / 25K: MTP-1 increased matched median decode throughput
  by 35.2%, but reduced active free VRAM from 606 MiB to 165 MiB and raised
  observed shared GPU memory to 266 MiB. MTP-2 bought only another 2.5% over
  MTP-1 while leaving 130 MiB free. MTP-3 crossed the frozen capacity stop
  before producing a response.
- `UD-IQ2_XXS` / q4 KV / 50K: MTP-3 increased matched median decode throughput
  by 105.5% and retained 1,274 MiB free. It is the clear speed candidate.
  However, every UD MTP depth produced the same sampled type/value regression
  on one saved decision state, so the frozen quality non-inferiority boundary
  was not met.

The stable choices therefore remain:

- use AD/q8/25K without MTP for quality-focused testing;
- use UD/q4/50K without MTP as the incumbent default;
- retain UD/q4/50K MTP-3 as a removable experimental speed profile deserving
  a fresh whole-trajectory quality check, not as a promoted default.

MTP is a runtime factor, not an information-view or semantic harness feature.
Nothing in `workbench/` changed.

## Measured matrix

Every completed condition used the same four exact saved agent decision states
at seeds 141421 and 271828. Requests were identical within a package except
for the declared model alias. The current Qwen3.8 sampler remained unchanged:
temperature 0.7, top-p 0.8, top-k 20, min-p 0, nonthinking, and a 4,096-token
response allowance.

| Package | MTP depth | Completed calls | Median decode tok/s | Matched ratio | Draft acceptance | Aggregate predicates | Aggregate subcases | Active free VRAM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AD/q8/25K | off | 8 | 18.58 | 1.000x | — | 77/96 | 420/448 | 606 MiB |
| AD/q8/25K | 1 | 8 | 25.14 | 1.352x | 4,062/4,065 (99.926%) | 77/96 | 420/448 | 165 MiB |
| AD/q8/25K | 2 | 8 | 25.77 | 1.388x | 5,437/5,440 (99.945%) | 77/96 | 420/448 | 130 MiB |
| AD/q8/25K | 3 | 0 | — | — | — | — | — | 119 MiB at stop |
| UD/q4/50K | off | 8 | 18.79 | 1.000x | — | 76/96 | 411/448 | 2,215 MiB |
| UD/q4/50K | 1 | 8 | 28.10 | 1.500x | 5,115/5,129 (99.727%) | 74/96 | 409/448 | 1,576 MiB |
| UD/q4/50K | 2 | 8 | 34.38 | 1.834x | 6,864/6,894 (99.565%) | 76/96 | 410/448 | 1,424 MiB |
| UD/q4/50K | 3 | 8 | 38.50 | 2.055x | 7,708/7,767 (99.240%) | 76/96 | 410/448 | 1,274 MiB |

These are matched local package results, not general MTP benchmarks. Decode
throughput is the primary speed metric. End-to-end duration also includes
prompt evaluation, prompt-cache state, model-file loading, and ordinary local
machine activity.

## Capacity result

### AD/q8/25K

The preceding full-offload qualification measured the no-MTP process at
10,955 MiB dedicated and 102 MiB shared GPU memory. In this study:

| Condition | Process dedicated | Process shared | Aggregate free |
|---|---:|---:|---:|
| off, prior matched capacity qualification | 10,955 MiB | 102 MiB | 631 MiB |
| MTP-1, live observation | 11,427.3 MiB | 266 MiB | 165 MiB after calls |
| MTP-2 | 11,481.5 MiB | 366 MiB | 130 MiB after calls |
| MTP-3 at stop | 11,503.8 MiB | 492 MiB | 119 MiB |

MTP-3 processed 10,400 of a 10,912-token prompt over roughly five minutes,
had decoded zero tokens, and showed material shared-memory growth. It was
stopped under the frozen capacity rule. The exact request, server arguments,
partial log, hashes, slot state, and capacity record are preserved. This is an
infeasible profile result, not an incomplete quality cell.

AD MTP-1 technically ran and preserved all eight literal outputs, but 165 MiB
of active free VRAM is not a comfortable local operating margin on the user's
desktop. It is not promoted.

### UD/q4/50K

| Condition | Process dedicated | Process shared | Aggregate free after calls |
|---|---:|---:|---:|
| off | 9,411.0 MiB | 114 MiB | 2,215 MiB |
| MTP-1 | 10,049.1 MiB | 164 MiB | 1,576 MiB |
| MTP-2 | 10,201.1 MiB | 166 MiB | 1,424 MiB |
| MTP-3 | 10,351.1 MiB | 166 MiB | 1,274 MiB |

All UD depths retained full 66/66 CUDA offload and avoided material shared-
memory growth. MTP-3 is operationally comfortable on this 12 GB card.

## Literal behavior result

All 56 completed calls returned transport-successful, schema-valid, admitted
actions. Direct comparison found:

| Package/depth | Assistant messages identical to M0 | Candidate quality identical to M0 |
|---|---:|---:|
| AD MTP-1 | 8/8 | 8/8 |
| AD MTP-2 | 7/8 | 8/8 |
| UD MTP-1 | 5/8 | 6/8 |
| UD MTP-2 | 6/8 | 7/8 |
| UD MTP-3 | 7/8 | 7/8 |

The one AD MTP-2 divergence retained a redundant current-list duplicate-ID
loop before consulting the new lifetime-ID set. It remained 12/12 and 50/50.

The UD divergence was substantive. In the same Reservation Book success-
control state at seed 271828, all three MTP depths combined wrong-type and
empty-string validation into one branch. Compared with M0, the MTP candidate
lost required empty-string `ValueError` behavior while adding one separate ID
validation, for a net 55/58 to 54/58 subcase regression. MTP-1 also made this
same type/value collapse in the regression-integration state, moving from
11/12 and 55/58 to 9/12 and 54/58. The other divergent Retry Queue patch was
behaviorally equivalent.

At temperature 0.7, a fixed seed need not yield the same sampled continuation
when the speculative sampling path changes. The saved evidence therefore
establishes a sampled trajectory regression, not a general claim that MTP
changes the target model's underlying semantic capability. Conversely, the
roughly doubled speed does not erase the observed regression. A default
promotion requires fresh whole-trajectory quality evidence.

## Apparatus corrections

Two qualification bugs were found without losing model evidence:

1. llama.cpp `/props` reported the default request speculative type (`none`),
   not the active server MTP implementation. MTP activity is now established
   from initialization, per-response draft counts, and statistics records.
2. PowerShell preserved per-response ordered records but initially summed
   their draft counters as zero. The nested records and server statistics
   agreed on the real values; subsequent code extracts values before summing.

The original false runtime classifications are preserved. The derived
analysis reconstructs qualification from primary response and log evidence.
Neither correction changed a model-facing request or result.

## Recommendation

Do not enable MTP in the stable profiles yet.

If this line continues, run one small fresh whole-trajectory comparison of
UD/q4/50K MTP-3 against UD/q4/50K off under the same sampler, with direct
transcript and artifact review. Its question is whether the twofold decode
gain survives ordinary multi-turn work without a recurrent quality or closure
cost. Do not rerun the depth ladder, tune draft thresholds around these saved
states, or use AD MTP at the current 25K/q8 allocation.

## Evidence

- [`EXPERIMENT_FREEZE.md`](EXPERIMENT_FREEZE.md)
- [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md)
- [`runs/r1/analysis.json`](runs/r1/analysis.json)
- [`APPARATUS_CORRECTION_001.md`](APPARATUS_CORRECTION_001.md)
- [`APPARATUS_CORRECTION_002.md`](APPARATUS_CORRECTION_002.md)
- [`runs/r1/_runtime/qwen38-ad25q8-mtp3-screen/capacity-stop.json`](runs/r1/_runtime/qwen38-ad25q8-mtp3-screen/capacity-stop.json)

