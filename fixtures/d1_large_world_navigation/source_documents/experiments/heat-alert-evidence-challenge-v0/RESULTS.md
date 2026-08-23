# Heat-alert evidence challenge v0 — results

Date: 2026-08-12

Status: **native baseline completed the task; retain as a successful challenge,
do not add a treatment**

Prospective freeze commit: `89a39ed`

Exact run: [`runs/native_pi_baseline/`](runs/native_pi_baseline/)

Verified reconstruction: [`analysis-summary.json`](analysis-summary.json)

## Outcome

The unchanged native Pi baseline produced a semantically complete evidence
brief in one construction pass:

- visible mechanical checker: **7/7 pass**;
- artifact-first investigator rubric: **12 pass, 0 partial, 0 fail**;
- changed files: **only `brief.md`**; and
- protocol, tool, check, and custody errors: **0**.

This is one trajectory, not a success rate. It is also not evidence for a new
view, card, stage, or tool. Under the frozen decision rule, a complete baseline
ends this challenge without a model-facing treatment.

## What the model was given

The saved task was byte-equal to the first provider user message. Pi supplied
its ordinary coding-agent system frame and native `read`, `bash`, `edit`, and
`write` tools. It supplied no card, plan, semantic selector, source packet,
ledger, reviewer, automatic checklist, or recommendation.

All 11 requests used:

- llama.cpp alias `qwen36-27b-iq2-coding`;
- temperature 0, top-p 1, top-k 20, min-p 0;
- thinking and reasoning preservation disabled;
- parallel tool calls disabled; and
- a 4,096-token maximum completion.

The model-visible world contained one outdated brief, five separately stored
current records named by a release manifest, two plausible superseded archive
records, and a visible mechanical checker. The semantic rubric, supporting
audit, and reference artifact were outside the workspace and not named in the
task.

## Exact action path

```text
read brief
→ read release manifest
→ read H1 design
→ read H2 primary analysis
→ read H3 measurement audit
→ read H4 subgroup appendix
→ read H5 implementation record
→ read visible checker
→ write brief once
→ run visible checker once
→ stop normally
```

The model read every release-bound current record and neither superseded
record. It did not list the directory, reread a file, inspect a prior version,
make an exact edit, retry, or receive a failed check. The single whole-file
write payload is byte-identical to the final saved brief. Every returned
assistant tool call and tool result retained its native ID and linked exactly
through the provider histories and Pi session.

## Artifact-first adjudication

The final brief correctly:

- identifies the staggered difference-in-differences design, nonrandomized
  rollout, association boundary, and noncausal interpretation with H1;
- reports 42.7 versus 50.9, adjusted difference -6.8, confidence interval
  -11.9 to -1.7, and p = 0.009 in the required sections with H2;
- reports 64% versus 82% capture, no capture adjustment or weighting, the
  possible exaggeration direction, and unknown magnitude with H3;
- describes the age comparison as exploratory, not preregistered, unadjusted
  for multiplicity, and nonconfirmatory with H4;
- separates 73% opening performance and $4,800 site-day cost from
  effectiveness and citywide-adoption evidence with H5; and
- preserves the title, Background, Methods, References, heading order, locked
  records, and file set.

The complete requirement-by-requirement judgment was written before the
trajectory was opened and is preserved in
[`semantic-adjudication.md`](runs/native_pi_baseline/semantic-adjudication.md).

## The supporting audit failed, and the artifact did not

The frozen supporting literal audit reported only 8/13 despite the 12/12
semantic adjudication. Direct inspection identifies five phrase-policy false
negatives:

1. it does not recognize `association rather than causation` as a noncausal
   boundary;
2. it requires the literal intermediate phrase `too low` in the Executive
   Summary even when the lower group capture and exaggeration direction are
   explicit;
3. it demands an H1-tagged association sentence inside Findings even though
   the task requires that design boundary in Executive Summary and
   Limitations and Findings makes no causal claim;
4. it demands the literal phrase `staggered difference-in-differences` inside
   Limitations even though that exact design is preserved in Methods and the
   required nonrandomized/noncausal boundary is explicit in Limitations; and
5. it fails to recognize `No capture adjustment or weighting was applied`
   because its substring rule looks for the contiguous phrase `no weighting`.

The audit remains frozen and its failed receipt remains part of the evidence.
It was explicitly marked `semantic_grade_authority:false`; changing it after
seeing this artifact would turn qualification into target fitting. The result
is a useful measurement warning: an oracle can pass a lexical instrument while
a semantically equivalent live artifact exposes the instrument's narrowness.

## Quantitative record

| Measure | Observation |
|---|---:|
| Assistant/model calls | 11 |
| Provider requests / HTTP 200 responses | 11 / 11 |
| Tool calls | 10 |
| Read / write / bash / edit | 8 / 1 / 1 / 0 |
| Current source reads | 5 of 5 |
| Superseded source reads | 0 |
| Candidate mutations | 1 |
| Visible checks during work | 1 |
| Tool errors | 0 |
| Visible checker | 7/7 pass |
| Investigator semantic rubric | 12 pass, 0 partial, 0 fail |
| Supporting literal audit | 8/13 fail, non-authoritative |
| Prompt tokens across calls | 46,221 |
| Uncached input / cache-read tokens | 6,730 / 39,491 |
| Completion tokens | 1,602 |
| Reasoning tokens | 0 |
| Total tokens across calls | 47,823 |
| Approximate model-call elapsed | 92.909 s |
| Run wall time | 115.890 s |
| Initial / final brief bytes | 2,451 / 4,070 |

Cumulative tokens count the growing history at every call, as in the prior Pi
reports. Timing is descriptive local-server timing, not a benchmark.

## Comparison with the resistant School Attendance case

Heat Alert and School Attendance are similar enough to make the contrast
useful but not controlled enough to identify a cause. Both require a
multi-section paper rewrite from exact evidence, current numbers, design
limits, missing-data direction, subgroup restraint, citations, and protected
sections. Qwen completed Heat Alert but left four partial semantic requirements
in the earlier School artifact.

Three differences are plausible leads:

- Heat Alert's task states more section-local relationships directly,
  including where the design and capture boundaries must appear.
- Each Heat Alert claim class is a separate current record and therefore a
  separate read/result turn; School combines three evidence classes in one
  record plus an editorial memo.
- The School defect includes a response/nonresponse complement inversion that
  Qwen later repeated even in a compact atomic probe. Heat Alert's capture-bias
  chain does not require that complement reversal.

The two runs also use different model-facing ecologies: ordinary Pi native
tools here versus the strict bare schema-action loop in the School
acquisition. None of these differences can be credited individually from this
comparison.

## Decision

Retain Heat Alert as a successful native research-evidence baseline. Do not
add or tune a treatment on it.

Use the exact known-resistant School Attendance task next as an **archive
calibration** under native Pi. That asks whether the ordinary ecology changes
the same failure shape before inventing a feature. Because the task and its
defects are already known, any improvement is method calibration only. If a
method lead emerges, it must transfer prospectively to a fresh complement- or
polarity-bearing evidence task before any promotion.

## Local validation

- prospective qualification is true;
- the analyzer verifies every declared prompt, provider, protocol, source,
  candidate, check, and custody invariant;
- focused Ruff and Python compilation pass; and
- `python -m unittest discover -s tests -q` passes 248 tests with 14 skips;
- `python -m pytest -q` passes 270 tests with 14 skips; and
- no GitHub Actions claim is made.
