# Receipt information campaign v0 — results

Authoritative run: `ric-q38-r002`

Status: **complete development scouts; no stable-harness change**

## Verdict

The two scouts produced different decisions.

1. **The passing-sibling contrast is a credible local-repair lead.** A failed
   receipt alone made all four targets actionable, but frequently repaired an
   empty-value case by breaking the neighboring wrong-type case. Adding the
   exact passing sibling reduced that collateral failure and improved complete
   contract outcomes. It did not prevent the same regression in every cell,
   so it is not a default treatment.
2. **The exact temporal trace is mixed and is not selected.** At the frozen
   ten-call cutoff it repaired two of three focus predicates versus one for a
   final receipt and zero without a receipt. Exact continuation later showed
   that the final-only Priority branch was censored: it repaired its target and
   submitted on call 17. Final and trace therefore each reached 2/3 temporal
   targets at natural submission. The trace branch used 26 calls, still failed
   the visible replacement-order check, and submitted after `passed:false`.
   More temporal truth did not reliably supply the missing state
   representation or action plan.

The stable `workbench/` remains unchanged. These were known development states
and not independent estimates of reliability.

## Run integrity

- Qwen3.8-27B UD-IQ2_XXS, alias `qwen38-27b-iq2-coding`;
- llama.cpp external server, pinned nonthinking profile;
- temperature 0.7, `top_p` 0.8, 4,096 response tokens;
- 21/21 conditions completed;
- 133 model responses;
- 18 submissions and three disclosed turn-limit endings;
- 9 rejected actions, all preserved without repair;
- 680,943 prompt tokens and 18,924 completion tokens;
- 699,867 total reported tokens;
- 21/21 exact replay and post-run verification, zero errors; and
- goldens 180/180 on the complete task-contract audit.

Focused validation passed 27/27 stable substrate tests and 11/11 campaign
apparatus tests. The campaign test validates the pre-call source lock against
the authoritative run's captured repository, not the live experiment folder
where post-run analysis is intentionally added.

A separate repository-wide sweep completed 634 tests with 36 errors and 14
skips. The errors were confined to older archived experiment byte/fixture
comparisons that expect LF while this Windows checkout uses
`core.autocrlf=true`; they are not campaign replay or workbench failures. This
is local validation, not CI verification, and the repository-wide suite should
not be described as green on this checkout.

The first partial run, `ric-q38-r001`, is preserved and excluded after a
pre-request Windows path-length failure. The corrected replacement changed
only experiment storage paths and retained byte-identical model prompts.

## Scout A — local contrast

All four source candidates had a failed empty-value target and a passing
wrong-type sibling in the same local validation branch.

| Arm | Target passes | Sibling passes | Joint passes | Contract fixes | Regressions | Terminal predicates | Tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| No receipt | 0/4 | 4/4 | 0/4 | 2 | 0 | 215/254 | 107,730 |
| Failed receipt | 4/4 | 1/4 | 1/4 | 7 | 5 | 215/254 | 84,697 |
| Failed + passing sibling | 4/4 | 3/4 | 3/4 | 13 | 2 | **224/254** | 133,329 |

The four matched source candidates began at 213/254 predicates. Failed-only
and contrast both repaired every named target. Their difference was collateral
behavior:

- Failed-only regressed the passing sibling in three of four cells.
- Contrast regressed it in one of four cells.
- In two cells, contrast changed a combined condition into separate type and
  empty-value branches while failed-only changed the whole condition's error.
- In one Session cell, contrast generalized the distinction across all related
  validators and reached 67/67.
- In one Config cell, Qwen ignored the passing control and produced the same
  wrong combined edit as failed-only.

Contrast used 57.42% more tokens than failed-only. Much of that increase came
from the Session trajectory that continued from the local target to a complete
67/67 repair. The extra receipt itself was tiny; the resulting action path was
larger. Cost is therefore a package outcome, not prompt-size overhead alone.

The earned claim is narrow:

> On these four saved local type/value repairs, an exact passing sibling made
> Qwen3.8 more likely to preserve the neighboring valid distinction than the
> failed receipt alone, but it did not guarantee preservation.

## Scout B — temporal state

All three source candidates failed one exact history/order probe.

| Arm | Target/trace passes | Contract fixes | Regressions | Terminal predicates | Rejections | Tokens |
|---|---:|---:|---:|---:|---:|---:|
| No receipt | 0/3 | 6 | 1 | 151/180 | 0 | 127,197 |
| Final receipt | 1/3 | 1 | 0 | 147/180 | 2 | 106,589 |
| Full stepwise trace | 2/3 | 3 | 1 | 148/180 | 5 | 140,325 |

The terminal totals do not rank the temporal interventions: the no-receipt
actors made unrelated broad repairs while missing every temporal target.
Focus behavior is more informative.

- Session user ordering: final and trace both produced the same effective
  mechanism. The trace added no benefit.
- Priority category ordering at call 10: only the trace had yet passed the
  focus predicate. Exact continuation showed that final-only repaired it by
  call 17 and submitted with five net saved predicate gains, while trace
  remained incomplete through call 26 and submitted after the same failed
  visible check. Both retained collateral failures.
- Config failed-amend ordering: neither receipt worked. The final receipt
  prompted an ineffective current-state ordering helper; the full trace
  prompted four consecutive exact no-op patches and an unchanged submission.

At the original cutoff the trace used 31.65% more tokens than the final
receipt and produced more rejected actions. With exact censored-trajectory
continuation, final-only used 152,011 reported tokens through call 17; trace
used 367,587 through call 26. The original 2/3 versus 1/3 direction was a
turn-budget artifact. The literal trajectories do not support promoting or
simply enlarging temporal receipts.

## What this changes

The earlier receipt study showed that exact failed execution truth usually
made Qwen act, while a complete contract audit later exposed sibling
regressions. This campaign identifies one concrete way to reduce that risk:
show the exact passing boundary that the local repair must not erase.

The result is not “more receipts are better.” A useful contrast must be
mechanically exact and locally discriminating. Even then, Qwen may ignore it.
Likewise, a full temporal trace can locate the first divergent transition but
does not itself state what persistent representation or mutation is required.

## Integration decision

The local contrast arm, not the temporal trace, clears the development gate
for one fresh integration study. It matched failed-only target repair at 4/4,
improved joint target/sibling preservation from 1/4 to 3/4, reduced full-audit
regressions from five to two, and produced two literal branch-separation
divergences.

That does **not** authorize an always-on contrast provider. The next study is
a fresh common-trunk re-verification comparison described in
[`NEXT_INTEGRATION_STUDY.md`](NEXT_INTEGRATION_STUDY.md). It must branch the exact same
first-pass terminal candidate, expose only newly failed machine predicates to
the second actor, and measure whether regression repair preserves the original
target. Unchanged source failures must not be included, or the study would
become a broad second correction pass.

## Evidence

- [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md)
- [`analysis-summary.json`](runs/ric-q38-r002/analysis-summary.json)
- [`manifest.json`](runs/ric-q38-r002/manifest.json)
- [`qualification.json`](runs/ric-q38-r002/qualification.json)
- [`APPARATUS_CORRECTION.md`](APPARATUS_CORRECTION.md)
- [`continuation/RESULTS.md`](continuation/RESULTS.md)
- [`continuation/DIRECT_TRAJECTORY_AUDIT.md`](continuation/DIRECT_TRAJECTORY_AUDIT.md)
- authoritative literal records under `runs/ric-q38-r002/c/`
