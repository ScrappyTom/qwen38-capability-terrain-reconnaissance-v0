# Atlas navigation scout v0 — results

Date: 2026-08-11

Status: **one positive ecology scout with a narrow artifact separation; retain
as a lead, not a default atlas**

Prospective freeze commit: `eed946b`

The frozen order ran once without retry or result-dependent tuning:

1. `NATIVE_FILESYSTEM`
2. `TYPED_ATLAS`

Both used llama.cpp's nonthinking `qwen36-27b-iq2-coding` profile at
temperature 0. Exact evidence is under [`runs/`](runs/), with terminal
candidates for [native filesystem](runs/native_filesystem/final-planner.py)
and [typed atlas](runs/typed_atlas/final-planner.py). The mechanical cross-run
summary is [`analysis-summary.json`](analysis-summary.json).

## Result

Both ecologies solved every visible case. The typed-atlas artifact also solved
all 16 hidden cases. The native-filesystem artifact solved 15 and violated one
source-level input contract.

| Measure | Native filesystem | Typed atlas |
|---|---:|---:|
| Public grade | 5/5 | 5/5 |
| Hidden grade | 15/16 | 16/16 |
| Assistant calls | 15 | 18 |
| Tool calls | 14 | 18 |
| Prompt tokens across calls | 55,558 | 103,046 |
| Generated tokens | 1,778 | 1,681 |
| Total tokens across calls | 57,336 | 104,727 |
| Approximate model-call elapsed | 103.366 s | 100.172 s |
| Run wall time | 105.643 s | 100.337 s |
| Candidate mutations | 1 | 1 |
| Visible checks during work | 1 | 1 |
| Rejected actions | 0 | 0 |

Relative to native filesystem, the typed ecology used 85.47% more cumulative
prompt tokens, 5.46% fewer generated tokens, and 82.65% more total tokens. It
used 20% more assistant calls and 28.57% more tool calls. Despite that token
work, measured model-call time was 3.09% lower and wall time was 5.02% lower;
the local prefix cache and the different request shapes make token counts and
elapsed time non-equivalent cost measures.

These are two trajectories, not reliability estimates. The one-case hidden
difference is a lead, not a rate or a statistical result.

## What each model actually saw and did

The Pi prompt was byte-equal to the first provider user message. It named the
target, authoritative manifest, and visible check, then supplied no source
bytes. Pi added its ordinary coding-agent system frame and `read`, `bash`,
`edit`, and `write` tools.

The native trajectory made 12 exact reads:

- the candidate;
- `policy_manifest.json`;
- `bindings.py`;
- the public checker;
- all six manifest-bound current policy modules;
- `models.py`; and
- package `__init__.py`.

It read no historical policy. It made one exact edit, ran the public check once,
received 5/5, and stopped. Tree custody shows that only `planner.py` changed.

The atlas first request was byte-equal to its saved system and task prompts.
Every returned assistant message, native `tool_calls` object, JSON-encoded
argument string, and matching tool result is linked correctly in the saved
history. There were no invalid or repaired arguments.

The typed trajectory:

- read current candidate `C000`;
- requested the complete unranked 22-artifact identity catalog;
- described the manifest and bindings artifacts;
- requested exact bytes for the manifest, bindings, candidate, models, all six
  current policy modules, and the public checker;
- wrote candidate `C001` once;
- checked `C001` once and received 5/5; and
- submitted the same `C001` version.

It requested 11 complete artifacts: six `manifest_bound_current` and five
ordinary workspace artifacts. It retrieved no historical source bytes and
made zero `relations` and zero `history` calls.

The atlas therefore did not act on the graph or lineage-query tools. It used
the typed catalog, paths, lifecycle fields, manifest, exact byte retrieval, and
stable candidate/check/submit operations. This distinction matters: the run is
not evidence that explicit relation or history projection helped.

## Direct artifact adjudication

Both artifacts implemented the current identity, duration, tier, hold, reason,
and date behavior correctly for every ordinary and visible validation case.

The native artifact additionally performed:

```python
canonical_region = region.strip().upper()
```

before calling the current region-bound helpers. That duplicated work already
owned by `region_v2.py`. The model had read the exact module, including this
boundary:

```python
if not isinstance(region, str):
    raise TypeError("region must be str")
canonical = region.strip().upper()
```

Because the native artifact called `.strip()` first, an integer region raised
`AttributeError` instead of the current source contract's `TypeError`. This was
the sole hidden miss.

The typed artifact passed the raw `region` value to `storage_tier_for`,
`adjusted_retention_days`, `hold_reason_for`, and `expiry_reason_for`. That
preserved the current policy boundary and passed 16/16. Its construction
message explicitly described those calls with the raw region before emitting
the candidate.

This is not a hidden-grader trick. The hidden case was not shown, but the type
contract was present in exact current source for both ecologies. The public
checker covered two other type boundaries, not `region`.

## Interpretation

The useful observation is not “the atlas won.” Both models acquired the same
governing sources and both understood the visible behavior. The separation
occurred when turning those contracts into code:

- Pi introduced a plausible but unnecessary normalization layer between the
  public input and the policy function.
- The typed trajectory composed the current functions without taking custody
  of their validation behavior.

Several bundled differences could have produced that separation: typed versus
filesystem retrieval, full-file construction versus exact edit, source order,
system frame, accumulated history, candidate identity, or ordinary
temperature-zero path sensitivity. This two-trajectory ecology scout does not
isolate them.

What it does establish locally is smaller:

1. Qwen can voluntarily navigate an unranked exact artifact catalog without a
   host-selected packet or semantic search.
2. It can avoid explicitly historical versions using factual identity and the
   authoritative manifest.
3. Distinct operation return types plus stable candidate identity completed a
   correct write/check/submit path without the preceding staged scout's final
   reserialization failure.
4. Merely exposing relation and history tools does not cause their selection.
5. The complete atlas bundle is prompt-expensive and has not earned default
   promotion from one hidden-case advantage.

## Decision

Do not add the atlas to the workbench and do not tune this task. Preserve the
full package as an experimental ecology.

The positive artifact separation earns one genuinely fresh replication of the
general method, not this exact result. That replication should keep:

- an unranked factual artifact index;
- model-selected exact retrieval;
- stable candidate versions;
- literal checks bound to candidate identity; and
- explicit submission without candidate reserialization.

It should remove redundant `describe` calls from the offered surface and avoid
claiming that relation/history tools matter unless the model selects them. A
fresh task should make authority or version lineage operationally relevant
without naming the relevant source files or preselecting a packet. If the
model again produces a better artifact through a coherent retrieval path, the
next question can isolate the smallest useful component. If quality ties or
regresses, stop the navigation line rather than enrich the atlas.
