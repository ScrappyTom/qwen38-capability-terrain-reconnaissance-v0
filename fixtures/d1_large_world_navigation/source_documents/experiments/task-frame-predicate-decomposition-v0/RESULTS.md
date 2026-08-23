# Task-Frame-Preserving Predicate Decomposition v0 — Results

> **Superseded interpretation:** A post-publication model-visible-entailment
> audit found that the executable answer key knew concrete setup and runtime
> facts not fully represented in several model-facing predicates. The
> decomposition also changed semantic wording, operand definition, and active
> obligation signal. The grouped-versus-isolated comparison is therefore
> causally ineligible. The counts below remain exact descriptions of the saved
> run; the claimed grouped-decomposition lead is withdrawn. See
> [`CUSTODY_CORRECTION.md`](CUSTODY_CORRECTION.md).

## Outcome

All 38 Qwen3.8 calls were admitted, the saved run verifies exactly, and the
server was stopped after the calls. Those are custody facts, not validation of
the comparison.

The run cannot reject or support an atomic-review policy. Restoring the full
task and source bytes did not fix the source-sufficiency confound at the active
decision boundary: several questions still omitted concrete operands or
runtime facts used by the executable answer key.

The original descriptive totals were:

| Condition | Exact task/variant clusters | Defective clusters exact | Control clusters exact | Individual labels | Total tokens |
|---|---:|---:|---:|---:|---:|
| Composite requirement | 4/6 | 1/3 | 3/3 | 4/6 | 11,895 |
| Decomposed, grouped | **5/6** | **2/3** | **3/3** | **25/26** | 14,277 |
| Decomposed, isolated | 3/6 | 1/3 | 2/3 | 23/26 | 56,411 |

Grouped and isolated calls received the same original task, complete candidate,
and complete predicate catalog. Across their 26 matched predicate judgments,
isolation produced:

- 0 improvements;
- 2 regressions; and
- 24 unchanged outcomes.

Isolation used 3.95 times the tokens and 2.11 times the elapsed request time of
grouped review. Grouped review used 20.0% more tokens than the composite
condition.

These are development cases selected from known failures. They are not a
reliability estimate or a benchmark result.

## What changed when the requirement was decomposed

The three failure shapes diverged.

### Version immutability

The composite response falsely asserted that `__slots__` prevents assignment.
Both decomposed conditions correctly distinguished validation from assignment
immutability and found the defect.

### Queue ID type validation

The composite response correctly traced `Job(7, None)` into `_validate_id` and
found that the candidate raised `ValueError` instead of `TypeError`.

Both decomposed conditions instead latched onto the outer
`isinstance(job, Job)` guard. That guard is irrelevant because `Job(7, None)`
is a `Job`; its `job_id` is the wrong type. They therefore missed the defect.
The same mistaken mechanism appeared on the control candidate, where it
produced a coincidentally correct `present` label.

### Access-policy replacement

The composite response compressed the combined type/value guard into generic
"validation" and missed that an integer ID raises `ValueError` rather than
`TypeError`.

Grouped decomposition evaluated all seven cases correctly. Isolated review
caught the actual ID-type defect but invented a separate failure: it treated a
valid, unknown string ID as though it were an invalid ID and overlooked the
later `KeyError` branch.

## Explanation and evidence audit

The investigator opened the complete task frames, candidate packages, truth
probe observations, literal requests, and all 58 returned findings.

- Machine label accuracy was 52/58.
- Mechanism-correct explanations were 50/58.
- Two labels were correct for the wrong reason: both queue-control judgments
  for the wrong-ID-type predicate cited the `Job` object-type guard rather than
  `_validate_id(job.job_id)`.
- Six labels were wrong, and each wrong label's explanation exposed the actual
  reading or inference error.
- Literal evidence was byte-valid in 54/58 findings. Four otherwise readable
  excerpts changed indentation and were retained as invalid; none was silently
  normalized.

The composite response schema allowed at most four evidence excerpts. That is
enough to bind a label but not to prove every member of the larger compound
requirements. Composite evidence coverage should therefore not be interpreted
as a completeness measure.

## Original interpretation — withdrawn

The run was initially interpreted as establishing three things.

1. **Task-frame sufficiency is necessary.** The prior atomic/source-scope
   result could not support a claim about atomic review because some calls had
   lost governing context. This experiment removed that confound.
2. **Available context is not the same as operational context.** Grouped and
   isolated calls contained identical task, source, and predicate catalogs, yet
   activating only one predicate changed how Qwen interpreted the code.
3. **Decomposition is useful but non-monotonic.** It repaired two compound-gist
   failures, but it also redirected attention toward the wrong local branch in
   the queue case. More specificity did not guarantee a better trace.

It originally proposed this lead:

> A compact, grouped set of concrete predicates can expose distinctions hidden
> by a compound requirement while preserving sibling contrasts and task-level
> meaning.

That causal claim no longer survives. Exact byte availability did not establish
that every active decision was entailed by the model-visible packet. The two
isolated regressions occurred on predicates with hidden or implicit setup and
runtime dependencies, and the Queue decomposition weakened the direct
`job_id` signal found in the composite wording.

## Corrected next boundary

Do not move to a repair handoff. First rebuild the development comparison from
canonical decision packets whose concrete setup, pre-operation facts, exact
operation, observed fields, allowed runtime semantics, and criterion are all
model-visible and are the same inputs used by executable truth. Composite and
decomposed questions must reuse those packet strings without paraphrase. Only
after that corrected calibration may a prospective factual-review method be
considered.
