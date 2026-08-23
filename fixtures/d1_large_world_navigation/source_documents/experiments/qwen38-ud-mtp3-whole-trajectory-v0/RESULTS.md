# Qwen3.8 UD/q4/50K MTP3 whole-trajectory results

## Decision

UD/q4/50K/MTP3 qualifies as the preferred optional **UD speed profile** for
long-context local work. It nearly doubled weighted decode throughput, stayed
fully on the GPU with usable headroom, completed and submitted all six tasks,
and passed the frozen numeric decision guide.

It is not promoted as a quality profile and does not replace either reference:

- AD-IQ2_S/q8/25K MTP-off remains the bounded quality-oriented package;
- UD-IQ2_XXS/q4/50K MTP-off remains the reproducibility baseline because MTP
  changes the sampled trajectory.

No stable harness or existing profile changed.

## Primary results

| Measure | UD MTP-off | UD MTP3 |
|---|---:|---:|
| Terminal task predicates | 45/72 | **49/72** |
| Complete artifacts | 0/6 | 0/6 |
| Submitted | 5/6 | **6/6** |
| Starting-predicate regressions | 3 | **1** |
| Turns | 56 | 62 |
| Total tokens | 245,008 | 263,407 |
| Prompt tokens | 229,571 | 251,883 |
| Completion tokens | 15,437 | 11,524 |
| Recorded model-response time | 901.7 s | **456.0 s** |
| Weighted decode throughput | 19.74 tok/s | **37.30 tok/s** |
| End-to-end server interval | 1,263.4 s | **487.9 s** |

MTP3's weighted decode ratio was 1.889x and its recorded response time fell
49.4%, despite 7.5% more total tokens. All 62 responses had positive MTP draft
activity; 8,550 of 8,856 drafted tokens were accepted (96.54%).

## Paired quality

| Task | Seed | MTP-off | MTP3 | Delta |
|---|---:|---:|---:|---:|
| Access Pass | 141421 | 6/12 | 6/12 | 0 |
| Access Pass | 271828 | 6/12 | 6/12 | 0 |
| Priority Dispatch | 141421 | 8/12 | 8/12 | 0 |
| Priority Dispatch | 271828 | 9/12 | 9/12 | 0 |
| Usage Windows | 141421 | 5/12, no submit | **10/12, submitted** | +5 |
| Usage Windows | 271828 | **11/12** | 10/12 | -1 |

MTP3 won one pair, lost one, and tied four. The aggregate improvement is almost
entirely the avoided Usage seed-141421 construction collapse. It is not a
general quality lift.

## Literal findings

The direct transcript audit is required context for the table:

- the improved Usage path read all files, made a coherent multi-file repair,
  used an exact failed check to fix its missing revision field, rechecked, and
  submitted; the old path never checked and exhausted the loop;
- the regressed Usage path skipped formatter repair and therefore accepted a
  bool `digits` value;
- one Access 6/12 tie concealed worse MTP3 bool and atomicity subcases inside
  already-failed grouped predicates;
- all Access and Priority candidates retained the recurring arbitrary-iterable
  constructor and wrong-type/empty-text conflation;
- no MTP3 artifact was complete, and five incomplete artifacts submitted after
  a green narrow check.

These are sampled package trajectories at temperature 0.7. They establish
that MTP3 can be much faster without a recurring observed quality penalty in
this small family. They do not establish that MTP improves model capability.

## Capacity and integrity

The runtime qualified with:

- llama.cpp b10434;
- full 66/66 main-layer CUDA offload;
- 50,176 context, q4/q4 main KV;
- MTP maximum depth 3 with f16 draft KV and all draft layers on GPU;
- 10,353.1 MiB process dedicated GPU memory and 166 MiB shared after calls;
- 1,227 MiB aggregate free VRAM after calls;
- no host prompt-cache reserve;
- six exact replay successes;
- 62/62 `finish_reason: stop`, zero rejected actions, no client repair.

The largest prompt was 11,631 tokens, far below the 46,080-token prompt ceiling
that preserves the declared 4,096-token completion allowance.

## Recommendation

Use MTP3 when the UD 50K package is selected and local turnaround matters.
Use MTP-off when repeatability and comparison to preserved evidence matter.
Continue using AD/q8/25K MTP-off for bounded quality-sensitive experiments.

Do not rerun this family, tune MTP around individual failures, or infer that
the speed path solved Qwen's qualifier-retention and false-closure weaknesses.

## Evidence

- [`FREEZE.md`](FREEZE.md)
- [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md)
- [`runs/r1/analysis.json`](runs/r1/analysis.json)
- [`runs/r1/_runtime/mtp3/runtime-record.json`](runs/r1/_runtime/mtp3/runtime-record.json)
