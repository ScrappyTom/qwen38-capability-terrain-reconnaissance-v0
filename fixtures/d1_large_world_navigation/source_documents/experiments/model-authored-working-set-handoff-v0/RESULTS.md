# Model-authored working-set handoff v0 results

Date: 2026-08-17

Verdict: **upstream navigation failed; the matched handoff comparison was not
run**

## Result

Q3 XL did not construct a bounded working set or seal an action-boundary
record. It used 13 model calls to reconstruct all 886 lines / 51,678 bytes of
the maintained artifact, query the broad delta, and read the 5,734-byte
governing result. Before it could read the required correction/audit evidence
or invoke `seal_action_handoff`, the literal turn-14 request reached 22,746
prompt tokens. Preserving the frozen 3,072-token response allowance would have
exceeded the 25,088-token context by 730 tokens.

The per-turn capacity safeguard stopped before a fourteenth inference. No
handoff packet was created, neither fresh action arm ran, and the candidate
remained unchanged.

This is not a result about whether a model-authored objective or sufficiency
record improves working-set acceptance. The experiment stopped one stage
earlier: **the navigator did not organize acquisition into a bounded set before
ordinary transcript residency consumed the action envelope.**

## Exact trajectory

| Measure | Observed |
|---|---:|
| Model calls / interpreted actions | 13 / 13 |
| Accepted target reads | 9 |
| Rejected target reads | 1 |
| Unique target materialized | 886/886 lines (100%) |
| Accepted target content | 51,678 bytes |
| Repository source objects | 1 |
| Repository source content | 5,734 bytes |
| Read receipts created | 10 |
| Handoff sealed | no |
| Action arms executed | 0 |
| Candidate mutation/check/submit | 0 / 0 / 0 |
| Maximum admitted prompt | 20,921 tokens |
| Minimum admitted full-allowance headroom | 1,095 tokens |
| Censored next prompt | 22,746 tokens |
| Censored next full-allowance headroom | -730 tokens |
| Total measured tokens | 128,688 |
| Recorded model-call time | 237.2 seconds |

Turn 1 listed the candidate. Turns 2–8 read lines 1–700 sequentially. Turn 9
requested lines 701–886 as one slice and received the declared 12,000-byte
rejection. Turns 10–11 successfully split that range and completed the whole
artifact. Turn 12 opened the first bounded delta page. Turn 13 read
`experiments/mechanical-reentry-seed-v0/RESULTS.md`.

The model never queried `artifact_region_catalog` and never used
`read_artifact_region`. Thus the external address space was available but did
not become the acquisition method.

## What the reasoning establishes

The model was not unaware of the task or call limit. After the delta read it:

- identified the mechanical-reentry-seed study as the likely material update;
- connected it to the existing phase-continuity/open-question material;
- counted that four disclosed calls remained;
- planned to read the result, then a correction record, then seal the handoff;
  and
- explicitly said it needed to be efficient.

That plan came too late. Whole-artifact reconstruction had already occupied
the transcript. After the result was acquired, the next request could not
retain the complete response allowance.

This reproduces a useful distinction:

```text
external addressability available
        !=
model adopts an address-based acquisition strategy
        !=
model constructs a bounded action working set
```

It also makes the task frame relevant. “Safely maintain this integrated
document” again elicited a whole-document orientation policy from Q3 XL. The
current result does not establish that this policy was irrational in general;
it establishes that it prevented the frozen bounded-handoff method from
reaching its transition on this task and context.

## Relationship to earlier evidence

The earlier Qwen3.8 inline-projection actor used mechanical region identities
to read only 219/886 target lines, but keeping the full registry resident then
crowded out action. Q3 XL's earlier transferred-window actor received selected
exact bytes but reacquired 768/886 lines. In the present run, the registry was
external and queryable, yet Q3 XL did not use it and reconstructed 886/886.

Those are contextual comparisons across different methods and, in one case,
different packages—not a matched causal matrix. Together they localize three
different possible failures:

1. inline maps can improve selection but consume residency;
2. selected bytes do not automatically control a fresh actor's acquisition
   policy; and
3. an external map does not help if the navigator never adopts it.

The intended fourth test—whether a model-authored information policy survives
the phase boundary—remains unexecuted.

## Apparatus and custody

The first execution command stopped before server start because the
execution-ready checker used the model hash field name for the llama.cpp
binary. That field binding was corrected, the complete offline suite passed,
and the measured sequence then ran once. The failed command made zero model
calls and created no run directory.

After the measured run, generic replay initially rejected three Q3 XL request
fields omitted from the recorded inference-settings summary. A post-run
adapter supplied only those reconstruction fields. It verified all 70 custody
records, 13 requests/actions/results, the unchanged candidate, and 130 artifact
references without modifying records or making a model call. See
`APPARATUS_CORRECTION.md`.

The GPU runtime reported 25,088 context, 66/66 model layers offloaded, bounded
shared memory, and clean shutdown.

## Decision

The frozen gate worked: no action comparison was manufactured from an
incomplete navigation state. Do not enlarge context, force catalog use, inject
the required source, repair the navigation transcript, or rerun this cell and
call it the same experiment.

No handoff, working-window controller, scheduled phase transition, semantic
state, or architecture component is promoted. The useful project-level result
is narrower: on this authentic integrated-maintenance frame, Q3 XL's default
acquisition policy remained global even when a sparse exact address space was
available externally.

