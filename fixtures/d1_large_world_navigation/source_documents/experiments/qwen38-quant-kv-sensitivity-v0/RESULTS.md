# Qwen3.8 quant and KV sensitivity screen results

Date: 2026-08-16

## Verdict

Full offload and q8 KV are both viable at 25K for the two tested Qwen3.8-27B
weight packages. Quality, however, is not monotonic in KV precision:

- q8 strongly improved the measured next-action outcomes inside the larger
  AtomicChat AD-IQ2_S package;
- q8 was worse than q4 inside the smaller Unsloth UD-IQ2_XXS package;
- no condition earns default promotion from this saved-boundary screen.

The useful result is a **weight-quant × KV interaction**, not “q8 is better.”

## Measured matrix

Each profile received the same four exact saved decision states at seeds
141421 and 271828. All 32 responses were schema-valid and admitted.

| Profile | Calls | Candidate changes | Net predicate delta | Net subcase delta | Audit-execution failures | Completion tokens | Model-call time |
|---|---:|---:|---:|---:|---:|---:|---:|
| AD-IQ2_S / q4 | 8 | 4 | -6 | -40 | 1 | 8,135 | 539.9 s |
| AD-IQ2_S / q8 | 8 | 4 | +7 | +10 | 0 | 8,132 | 541.0 s |
| UD-IQ2_XXS / q4 | 8 | 6 | +6 | +1 | 0 | 10,368 | 667.9 s |
| UD-IQ2_XXS / q8 | 8 | 6 | +1 | -13 | 0 | 10,306 | 643.2 s |

The AD/q4 aggregate includes one literal syntax-invalid candidate, so its
negative total must not be read as a smooth estimate of general model quality.
The per-state transitions below are the primary evidence.

## Per-state findings

### AD-IQ2_S: q8 versus q4

- Type/value, seed 141421: both were net neutral and traded correct wrong-type
  behavior for correct empty-value behavior.
- Type/value, seed 271828: q8 reached 12/12; q4 remained 9/12.
- Lifetime, seed 141421: q8 reached 10/12 by fixing constructor shape but did
  not solve lifetime identity; q4 emitted a syntax-invalid and semantically
  wrong whole-file patch.
- Lifetime, seed 271828: both reached 12/12.
- Regression and positive-control cells: both KV variants chose the same reads
  and left the candidate unchanged.

Within this weight package, q8 has a clear local lead across two weakness
states without a positive-control loss.

### UD-IQ2_XXS: q8 versus q4

- Type/value: both KV variants remained 9/12 at both seeds.
- Lifetime, seed 141421: q4 and q8 emitted the same wrong patch and regressed
  claim/cancel subcases.
- Lifetime, seed 271828: q4 reached 12/12; q8 repeated the wrong seed-141421
  patch and remained 9/12 with the same regression.
- Regression, seed 271828: q4 reached 11/12; q8 remained 9/12.
- Positive control, seed 271828: both emitted the same patch and reached 9/12.
- The remaining regression/control cells were identical reads.

Within this weight package, q8 has no quality lead and shows two consequential
losses.

### Larger package versus the current smaller-q4 baseline

AD/q8 produced the best aggregate net transition and the only complete
type/value repair. It nevertheless left a positive-control candidate at 8/12
where UD/q4 improved it to 9/12, and it read rather than repaired the regression
state where UD/q4 reached 11/12. Under the frozen rule requiring recurrent
advantage without a substantive positive-control regression, it is not a
default replacement.

## What q8 changed

q8 did not change the prompt, context window, task facts, tools, output budget,
or sampling policy. It changed the numerical precision of cached keys and
values. At temperature 0.7, small logit changes can redirect the sampled action
non-monotonically. The saved actions show exactly that: q8 selected better
branches with AD-IQ2_S and worse branches with UD-IQ2_XXS.

This screen cannot establish the internal cause. It establishes the external
package interaction under exact custody.

## Capacity and cost

At 25K, q8 consumed 392 MiB more dedicated VRAM than q4 for either weight
package. The authentic AD/q8 calls remained stable at about 11.49 GB dedicated
use with roughly 0.63 GB free and no growth in shared allocation. Model-call
time and completion tokens were essentially identical between q4 and q8 inside
AD. UD/q8 was modestly faster in this run, but its outputs were different, so
that is not an isolated throughput effect.

At 50K, both KV variants fit comfortably with UD-IQ2_XXS. AD-IQ2_S/q4 fits only
tightly, and AD-IQ2_S/q8 cannot fit fully offloaded without spill. See
`FULL_OFFLOAD_CAPACITY_RESULTS.md`.

## Run custody

Measured quality roots:

- AD/q8: `runs/r2/qwen38-27b-ad-iq2s-25k-q8-nocache-screen/`
- AD/q4: `runs/r3/qwen38-27b-ad-iq2s-25k-q4-nocache-screen/`
- UD/q8: `runs/r3/qwen38-27b-ud-iq2xxs-25k-q8-nocache-screen/`
- UD/q4: `runs/r3/qwen38-27b-ud-iq2xxs-25k-q4-nocache-screen/`
- combined analysis: `runs/quality-screen-v0-analysis.json`

Excluded but preserved:

- `runs/r1/` contains the interrupted pre-correction 60-layer attempt and is
  not part of the full-offload evidence.
- the partial AD/q4 directory under `runs/r2/` contains the reducer-crash
  trajectory and is not part of the measured matrix. Its literal invalid model
  output is also present in the clean `runs/r3/` rerun.

## Recommendation

Keep UD-IQ2_XXS/q4 as the operational incumbent. Do not switch the smaller
quant to q8 merely because memory allows it.

AD-IQ2_S/q8 at 25K is the one earned challenger. Its next defensible test is a
small fresh whole-trajectory comparison against UD-IQ2_XXS/q4 on tasks that
exercise the same type/value, lifetime-state, and multi-requirement repair
failures. The comparison must retain full task frames and inspect literal
actions and artifacts. This screen earns that comparison, not a default model
change.
