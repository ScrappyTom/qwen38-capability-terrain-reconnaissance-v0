# Qwen3.8 AD/q8 whole-trajectory comparison results

## Result in one sentence

AD-IQ2_S/q8/25K showed a meaningful but not promotion-gate-level quality lead
over UD-IQ2_XXS/q4/50K: it won three of six fresh matched trajectories, tied
three, lost none, produced the only complete artifact, and avoided UD's sole
turn-limit collapse.

## Validity

- All twelve measured `r2` runs replay-verified.
- Both runtime records qualified llama.cpp b10434 and full 66/66 CUDA offload.
- AD used q8/q8 KV at 25,088 context; UD used q4/q4 KV at 50,176 context.
- MTP and host prompt caching were off.
- All 117 responses ended normally with `finish_reason: stop`.
- Maximum prompt tokens were 10,464 for AD and 13,450 for UD, so every call
  remained below the frozen 20,992-token capacity boundary.
- Starting candidates failed and goldens passed every task's visible check and
  12-predicate audit before calls.
- The stable `workbench/` was unchanged.

Two apparatus corrections are preserved. Correction 001 removed ignored
fixture bytecode after a pre-call Windows path-length failure; no model request
occurred in that attempt. Correction 002 fixed the study-local post-run replay
adapter after all calls; it changed no model-facing or custody evidence.

## Matched quality

| Task | Seed | AD/q8 | UD/q4 | Pair result |
|---|---:|---:|---:|---|
| Access Pass Registry | 141421 | 6/12 | 6/12 | tie |
| Access Pass Registry | 271828 | 6/12 | 6/12 | tie |
| Priority Dispatch | 141421 | 9/12 | 8/12 | AD |
| Priority Dispatch | 271828 | 9/12 | 9/12 | tie |
| Usage Windows | 141421 | 11/12 | 5/12 | AD |
| Usage Windows | 271828 | 12/12 | 11/12 | AD |

AD won 3/6 pairs across two task families, tied 3/6, and lost 0/6. The frozen
gate required at least four wins, so `promotion_gate_passed` is false.

## Aggregate facts

| Measure | AD-IQ2_S/q8/25K | UD-IQ2_XXS/q4/50K |
|---|---:|---:|
| Task predicates | 53/72 | 45/72 |
| Complete terminal artifacts | 1/6 | 0/6 |
| Submitted trajectories | 6/6 | 5/6 |
| Total model turns | 61 | 56 |
| Rejected actions | 0 | 1 |
| Regressed predicates | 0 | 3 |
| Cumulative prompt tokens | 253,597 | 229,571 |
| Cumulative completion tokens | 13,615 | 15,437 |
| Cumulative total tokens | 267,212 | 245,008 |
| Summed model time | 835.8 s | 901.7 s |
| Maximum prompt | 10,464 | 13,450 |

AD used 22,204 more reported total tokens (9.1%) because several of its normal
trajectories took more turns. Despite that, its summed model-call time was
65.9 seconds lower (7.3%), partly because UD's failed Usage trajectory emitted
6,266 completion tokens across fourteen calls. These are realized package-path
costs, not controlled throughput estimates.

## Runtime fit

| Package | Dedicated process VRAM after load | Shared process memory | Free VRAM after load | Offload |
|---|---:|---:|---:|---:|
| AD/q8/25K | 10,953 MiB | 102 MiB | 672 MiB | 66/66 |
| UD/q4/50K | 9,393 MiB | 114 MiB | 2,232 MiB | 66/66 |

Both servers stopped normally and returned the GPU to its idle allocation.
AD fits, but its 672 MiB observed headroom remains a quality-focused bounded
profile rather than a generous multitasking allocation.

## What changed behaviorally

The eight-predicate aggregate gap must not be read as a uniform improvement.
Six points came from one UD Usage Windows trajectory that entered a malformed
rewrite/reread/no-op loop, never ran a check, and hit the turn limit. AD's two
Usage trajectories instead reached 11/12 and 12/12. One additional point came
from AD avoiding a UD regression from a frozen dataclass to a custom class.
The final point came from AD correctly splitting account wrong-type and empty
validation in one Usage seed.

The most stable cross-package behavior was negative: all four Access runs and
all four Priority runs accepted arbitrary constructor iterables and collapsed
wrong text types plus empty strings into `ValueError`. Both packages therefore
continued to lose explicit independent distinctions even with the whole task
and exact source present.

See [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md) for the literal
trajectory analysis.

## Decision

The frozen promotion gate did not pass, so this study does not establish AD as
a general primary research profile and does not change the stable harness.
The descriptive evidence nevertheless leans clearly toward AD/q8/25K for
quality-sensitive work that fits comfortably below 25K: it was never worse,
produced the only complete result, and avoided UD's only catastrophic
trajectory.

Operationally:

- prefer **AD-IQ2_S/q8/25K, full 66/66, MTP off** for bounded quality-focused
  experiments;
- retain **UD-IQ2_XXS/q4/50K, full 66/66, MTP off** when the larger context
  window or greater VRAM headroom is actually needed;
- describe the choice as package-specific and provisional, not as proof that
  q8 KV or the AD weight quant alone caused the gain;
- do not rerun these valid trajectories or tune the harness around the one UD
  collapse.

The next model-facing research question remains upstream of quantization:
why complete explicit validation distinctions repeatedly compress into one
combined branch, and what bounded task frame lets those distinctions survive
construction and verification without flooding the transcript.
