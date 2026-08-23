# Agent Method Scout v0 Results

Status: **exploratory scout complete; no method promoted**

The broad result is not that one of four agent methods won. It is that the
same Qwen model behaved very differently depending on whether a method was
actually adopted, what its intermediate role produced, what the visible check
made salient, and how the action boundary organized the next move.

The stable custody workbench remains unchanged.

## Evidence set

The frozen scout ran one fresh trajectory for each combination of:

- three authentic development anchors: blank package construction, multi-file
  repair, and evidence-grounded paper revision;
- four removable whole methods: ordinary actor, optional artifact workspace,
  reviewer + actor, and staged preparation/workspace/review.

This is 12 heterogeneous development trajectories, not 12 exchangeable
benchmark samples. No success percentage, confidence interval, or reliability
claim is reported.

An initial reviewer-response grammar failed at the llama.cpp boundary after
valid D0 and D1 cells had completed. The exact incident is preserved in
`agent-method-scout-v0-run-001`. The schema was simplified without changing
model-facing reviewer content, qualified independently, and the remaining ten
cells ran in `agent-method-scout-v0-run-002`. No valid cell was rerun.

`combined-manifest.json` records the inclusion boundary. Its verifier pins the
two source apparatuses to commits `058f925d` and `e22ae5e0`, validates literal
actions/results, candidate chains, captures, reviewer responses, submissions,
and terminal artifacts, and passes all 12 cells with zero errors.

## Terminal observations

| Task | Ordinary | Optional workspace | Reviewer + actor | Staged hybrid |
|---|---|---|---|---|
| Dispatch construction | 8/12 executable groups; red submit | 5/12; workspace unused; red submit | 8/12; 13/13 review findings said supported; red resubmit | 10/12; one preparation item; green visible check |
| Support repair | 9/11 | 9/11; workspace unused | 7/11; 6/6 review findings said supported | 9/11; useful five-defect preparation item |
| Wetland revision | supporting audit 8/8; semantic incomplete | supporting audit 8/8; workspace unused; semantic incomplete | supporting audit 8/8; review helped escape one literal-check loop; semantic incomplete | no submit; 24-turn cap; terminal supporting audit 7/8; semantic incomplete |

The paper's primary human review found a shared omission that the 8/8
supporting audits did not: every method's Summary omitted the explicitly
required 95% confidence interval. See `PAPER_QUALITATIVE_REVIEW.md`.

## Quantitative custody metrics

| Method | Model calls across its three cells | Prompt tokens | Completion tokens | Total tokens | Model/server duration (ms) |
|---|---:|---:|---:|---:|---:|
| ordinary | 42 | 233,714 | 9,126 | 242,840 | 543,018 |
| optional artifact workspace | 46 | 343,192 | 17,468 | 360,660 | 1,028,187 |
| reviewer + actor | 52 | 345,508 | 23,658 | 369,166 | 1,367,339 |
| staged hybrid | 76 | 447,421 | 11,412 | 458,833 | 712,421 |

These sums describe different tasks and paths; they are not method-efficiency
estimates. Relative to ordinary on this exact schedule, optional workspace used
48.5% more total tokens, reviewer + actor 52.0% more, and staged hybrid 89.0%
more.

Across the complete evidence set:

- 29 actor actions were rejected;
- 28 were exact no-ops;
- one used a stale file hash;
- no rejected action was repaired or dispatched silently;
- all three optional-workspace actors used zero workspace actions;
- staged preparation produced three captures and two model-authored items in
  total;
- four code reviewers emitted 36 `supported`, zero `not_supported`, and zero
  `uncertain` findings, while their candidates later failed 12 executable case
  groups in aggregate;
- the paper reviewer emitted seven supported, one not-supported, and one
  uncertain finding.

## Main findings

### Optionality did not create adoption

Adding capture and working-item tools did not cause Qwen to use them on any
task. The M1 cells therefore do not test the usefulness of a good artifact;
they test exposure to an optional artifact surface. That exposure added prompt
surface and cost without establishing a work method.

### Preparation quality varied more than the container

The three preparers produced:

1. a broad, incomplete dispatch requirement summary;
2. a well-grounded support diagnostic naming five central bugs;
3. only an exact copy of the paper draft.

The fresh actors then produced best-in-family dispatch, tied ordinary support,
and a paper turn-cap failure, respectively. A preparation stage is not itself
useful semantic state. What it chooses to externalize—and what it omits—must be
measured as an outcome.

### Generic review was usually false closure

The code reviewers repeatedly described custom constant classes as enums,
accepted broken release ordering, missed lifetime uniqueness and exception
types, and certified a hard-coded unassigned count. Each actor immediately
resubmitted unchanged.

The paper reviewer did identify a literal visible-check mismatch and the actor
eventually rephrased it. That is a genuine local recovery. The same reviewer
missed the Summary confidence-interval omission, so it was not a semantic
backstop.

### Diagnostics and actions formed part of the effective method

Dispatch's assertion-only visible failure led to repeated local rewrites and
red submission. The paper check rejected a correct negation because it matched
an obsolete literal; W3 then emitted 13 consecutive exact no-op patches. These
trajectories were not primarily starved of facts. The check result, action
schema, response allocation, and closure rule changed the decision
environment.

### Ordinary remains the reference method

The ordinary loop was cheapest, tied the best support artifact, matched the
reviewer dispatch artifact, and produced a strong paper with the same shared
Summary omission as the larger methods. The staged dispatch artifact was the
only clear local improvement, and that compound bundle did not transfer across
the other anchors.

## Decision

Do not promote:

- optional workspace tools;
- a generic fresh reviewer;
- a mandatory preparation phase;
- the staged hybrid bundle;
- any new workbench dependency or default model-facing surface.

Retain:

- the stable custody substrate and ordinary loop as comparator;
- the removable experiment-local method seams;
- the exact split-run incident and combined verifier;
- preparation artifacts and reviews as inspectable behavioral products, not
  authoritative state.

## Research update

The narrow semantic-format line had treated the intermediate representation as
the likely lever. This scout shows that the broader unit is the whole decision
environment:

```text
role + exact inputs + available operations + intermediate product
     + check/feedback + response allocation + closure
                         ↓
                    model behavior
```

The next high-value exploration should compare a few coherent decision
organizations on fresh tasks, with equal total response opportunity and direct
measurement of whether the model actually adopts the method. It should not add
another optional wrapper to the same actor or infer a mechanism from one
promising dispatch trajectory.

The full literal path-by-path account is in
`DIRECT_TRAJECTORY_AUDIT.md`. Raw evidence remains under `runs/`.
