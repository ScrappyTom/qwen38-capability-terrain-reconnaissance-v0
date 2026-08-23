# Factual Question × Source Scope Crossover v0 — Results

## Outcome

The study completed cleanly but did **not** earn a factual-review method for
repair.

All three authentic Qwen3.8 ordinary candidates qualified with both satisfied
and violated task groups. All 58 factual calls admitted, the server identity
matched the pinned package, the run verified without custody errors, and the
five focused apparatus tests passed.

The main result is narrower than a rejection of granular review:

> The tested isolated-question package did not make Qwen3.8 a more reliable
> factual verifier. It changed question granularity **and** removed the sibling
> requirements that formed the grouped task frame; scoped cells could also
> remove needed definitions. The observed package added inconsistent labels
> and substantially greater cost, but it does not establish that a focused
> predicate is harmful when a sufficient task frame is retained.

Question-bound source packets inside one grouped response produced the best
raw result, but their only improvement had a confused explanation and does not
yet justify a repair stage.

## Ordinary candidates

| Candidate | Passing groups | Failing groups |
|---|---:|---|
| Version codec | 6/8 | `V01`, `V02` |
| Work queue | 8/9 | `Q02` |
| Access policy | 6/9 | `P02`, `P03`, `P08` |

These were Qwen-authored artifacts from the unchanged ordinary workbench, not
task-author defect variants.

## Raw factual results

| Condition | Correct | Defects detected | Controls confirmed | False support | False defect | Cannot determine | Literal evidence |
|---|---:|---:|---:|---:|---:|---:|---:|
| grouped/full | 23/26 | 3/6 | 20/20 | 3 | 0 | 0 | 24/26 |
| grouped/scoped | **24/26** | **4/6** | **20/20** | 2 | 0 | 0 | **26/26** |
| atomic/full | 21/26 | 3/6 | 18/20 | 3 | 2 | 0 | 23/26 |
| atomic/scoped | 21/26 | 3/6 | 18/20 | 2 | 2 | 1 | 25/26 |

The frozen paired contrasts were:

- atomic versus grouped at full scope: 1 improved, 3 regressed, 22 unchanged;
- atomic versus grouped at scoped presentation: 0 improved, 3 regressed, 23
  unchanged;
- scoped versus full when grouped: 1 improved, 0 regressed, 25 unchanged; and
- scoped versus full when atomic: 2 improved, 2 regressed, 22 unchanged.

## Named-task results

| Task | grouped/full | grouped/scoped | atomic/full | atomic/scoped |
|---|---:|---:|---:|---:|
| Version codec | 7/8 | 7/8 | 7/8 | 7/8 |
| Work queue | 8/9 | **9/9** | 7/9 | 7/9 |
| Access policy | 8/9 | 8/9 | 7/9 | 7/9 |

Version immutability was missed in every view. Access replacement validation
was missed in every view. The only grouped/scoped gain was work-queue `Q02`.
Direct audit found that this correct label was accompanied by an inverted or
confused account of the exception distinction, so it is not strong mechanism
evidence.

## Cost

| Condition | Calls | Prompt tokens | Completion tokens | Total tokens | Summed HTTP time |
|---|---:|---:|---:|---:|---:|
| grouped/full | 3 | 4,941 | 3,497 | 8,438 | 184.4 s |
| grouped/scoped | 3 | 18,842 | 3,528 | 22,370 | 222.1 s |
| atomic/full | 26 | 33,421 | 6,057 | 39,478 | 329.7 s |
| atomic/scoped | 26 | 26,267 | 6,134 | 32,401 | 366.4 s |

Atomic scoping reduced atomic prompt tokens by 21.4% but did not improve the
21/26 result. Atomic/full used 4.68 times the total tokens of grouped/full and
scored lower. Grouped/scoped duplicated shared files beside each question; it
used 2.65 times grouped/full's total tokens for one additional raw label.

## Investigator boundary

The executable `Q05` control is not semantically clean enough to decide the
method. The task says every failed enqueue is atomic, while the check covers
validation failures only and the golden is not rollback-safe for arbitrary
runtime exceptions. Raw results remain above. Excluding `Q05` gives:

- grouped/scoped 23/25;
- grouped/full 22/25; and
- both atomic conditions 21/25.

The ordering and decision do not change. See `DIRECT_AUDIT.md` and
`investigator-adjudication.json`.

## What was learned

1. **Task frame is an information variable.** Grouped calls supplied all
   sibling requirements together. Atomic calls supplied only the active
   requirement, so the study changed the model's account of the whole job as
   well as decision granularity. Too little frame can remove governing context,
   contrasts, or dependency cues; too much may dilute salience or induce
   compression. Those effects must be varied separately.
2. **“Atomic” was still too coarse.** Several one-question cells contained
   multiple independent predicates: type versus value exception, mutation
   order, immutability, return value, and failure atomicity. Qwen continued to
   compress these clusters.
3. **Separate inference is not equivalent to better discrimination.** `Q07`
   yielded a status that contradicted an explanation establishing every asked
   behavior. `Q05` exposed an apparatus ambiguity rather than a clean false
   defect.
4. **Some scoped packets were not dependency-complete.** Atomic/scoped `P01`
   omitted the definitions of two imported exports. Grouped/scoped happened to
   include them in sibling packets. Its divergence is direct evidence of
   task/source starvation, not evidence against focused review.
5. **Source scope remains non-monotonic.** Grouped question-bound packets made
   one no-regression raw gain but at substantial duplication cost.
6. **Correct labels are insufficient.** The recovered `Q02` label did not
   carry a sound explanation of why the candidate was wrong.
7. **The stable custody method worked.** It exposed a cascading checker bug,
   preserved the original grade, separated a disputed rubric item, and made
   output/rationale contradictions inspectable.

## Decision and next question

Do not promote the tested isolated-question package, scoped review, a repair
handoff, or an adaptive router. Retain grouped/full as the lean factual
comparator. Preserve grouped/scoped as a development lead only. Do not infer
that focused predicates are intrinsically worse: the atomic cells confounded
focus with task-frame removal, and one scoped packet removed needed source.

The next useful isolation is smaller than another whole requirement:

```text
complete sufficient task frame
+ one active concrete executable predicate
+ dependency-complete exact definitions for that predicate
→ one factual answer
```

Use the saved `V02`, `Q02`, `P02`, `P03`, and `P08` artifacts as development
calibration only. Hold the complete task/requirement frame and sufficient
source constant while splitting composite clusters into independently
decidable predicates such as wrong-type exception, empty-value exception,
assignment immutability, and replacement position. Only afterward vary frame
breadth or source scope. Require the explanation to identify the actual branch,
not merely the correct label. Only after that method works should it be tested
prospectively on fresh candidates and then handed to a repair actor.

No change to `workbench/` is earned.

## Validation boundary

The study-local suite passed 5/5 tests and the independent verifier replayed
all 58 factual calls with zero custody errors. A repository-wide discovery run
executed 634 tests but is not a green gate on this checkout: it reported 36
errors (and 14 skips) in unchanged historical experiment replay/fixture-shape
checks. None originated in this study. Accordingly, this report claims focused
study validation and exact saved-run replay, not a repository-wide clean test
suite.
