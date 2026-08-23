# Model-Visible Decision Packets v0 — Results

## Outcome

The third development run is complete and interpretable. All 76 Qwen3.8 calls
were admitted. Exact verification replayed the 13 canonical packet decisions
against both saved candidate variants and reported 76 expected calls, 76 saved
calls, and zero errors. The llama.cpp server was stopped immediately after the
run; port 8080 closed and VRAM returned to the desktop baseline.

The correction changes the earlier result. Once executable truth and
model-visible evidence used the same concrete scenarios, grouped and isolated
per-packet review produced the same aggregate factual capture:

| Response organization | Exact labels | Defect labels | Control labels | Exact-evidence findings | Total tokens | Request time |
|---|---:|---:|---:|---:|---:|---:|
| One conjunction label | 8/12 | 3/6 | 5/6 | 9/12 | 86,138 | 359.338 s |
| Packet labels, grouped | **51/52** | 25/26 | 26/26 | 44/52 | 94,513 | 749.227 s |
| Packet labels, fresh calls | **51/52** | 25/26 | 26/26 | 32/52 | 414,802 | 1,658.886 s |

Grouped and isolated conditions each made every task/variant/seed packet set
exact in 11/12 cases. Across their 52 directly matched labels, isolation
improved one seed-specific Access decision, regressed one seed-specific Queue
decision, and left 50 unchanged. At seed 314159 all 26 paired packet labels
were identical.

Isolation used:

- 4.39 times the grouped total tokens;
- 4.78 times the grouped prompt tokens; and
- 2.21 times the grouped serial request time.

Grouped review used 9.72% more total tokens than the composite condition.
These are exact descriptions of a known-case development matrix, not benchmark
rates.

## What the correction fixed

The prior study's two isolated regressions were apparatus artifacts.

- Version assignment now included the exact assignment operation plus the
  Python distinction between frozen dataclasses and plain `__slots__`. Every
  grouped and isolated assignment judgment was correct across both variants
  and both seeds.
- Access unknown-ID now used concrete rules, IDs, initial order, operation, and
  criterion rather than undefined placeholders. Every grouped and isolated
  unknown-ID judgment was correct across both variants and both seeds.
- Queue wrong-ID review now exposed that `Job(7, None)` was successfully
  constructed, was a `Job`, and contained integer `job_id=7`; it also declared
  that dataclass annotations do not enforce runtime field types. This removed
  the hidden setup dependency, although one isolated sampled response still
  bound the call to the wrong guard.

The second study is therefore retained as raw custody evidence but is causally
ineligible. Its conclusion that fresh isolated review was less reliable is
withdrawn.

## Sampler stability

The two seeds produced 58 comparable semantic decision pairs:

- 52/58 labels were stable;
- 6/58 changed;
- composite was stable in only 2/6 task/variant cells;
- grouped packet labels were stable in 25/26 cells; and
- isolated packet labels were stable in 25/26 cells.

The unstable grouped cell was defective Access integer-ID validation. The
unstable isolated cell was defective Queue integer-ID validation. Both were
correct at seed 314159. Four composite task/variant cells changed label across
seeds, including three defective candidates and one satisfied control.

This validates the decision to use more than one seed with the recommended
nonzero-temperature package. A one-seed method ranking would have been wrong:
seed 42 made grouped review look uniquely better on Queue and isolated review
look uniquely better on Access.

## Evidence-string custody

Strict JSON Schema constrained the shape and source IDs but could not enforce
substring membership. Across 374 individual cited snippets:

- 333 were exact substrings;
- 24 differed only by whitespace folding; and
- 17 were genuinely nonliteral transformations.

At the finding level, 85/116 findings had only exact evidence. Several
nonliteral snippets transformed a criterion or observation expression into an
outcome-shaped statement. The harness did not repair or accept them as exact;
it recorded `evidence_valid: false`. This study did not use quote validity as a
hard rejection gate.

## Direct-audit correction to the label totals

The 51/52 grouped and isolated totals are factual-label results, not factual
authority.

- The seed-42 isolated Queue miss saw the valid `Job` receipt but applied the
  outer `isinstance(job, Job)` guard as if it validated `job.job_id`.
- The seed-42 grouped Access miss quoted the combined guard that literally
  raises `ValueError`, then asserted that it raises `TypeError`.
- A seed-314159 Access composite label was machine-correct but its explanation
  was internally contradictory and mechanism-wrong.
- A correct seed-42 Queue pre-mutation label also misnamed the exception path;
  its unchanged-state conclusion remained correct.
- Several correct composite `present` labels discussed only one or two packets
  rather than establishing the required conjunction.

See [`DIRECT_AUDIT.md`](DIRECT_AUDIT.md) for the literal input/output reading.

## Decision

The simple atomicity hypothesis remains unsupported, but for a different
reason than the invalid second run suggested.

When a sufficient task frame and canonical executable scenarios are held
constant, one fresh inference per packet did not improve aggregate capture over
one grouped packet response. It matched grouped capture at much greater cost.
The single conjunction label was substantially less accurate and much less
stable because responses could treat one representative packet as the whole
decision.

What is earned:

- canonical model-visible/executable packet parity as an experimental validity
  requirement;
- more than one seed for method comparisons under the recommended sampled
  Qwen3.8 package; and
- grouped per-packet review as the cheaper development comparator if a later
  real-work factual-review method is tested.

What is not earned:

- an always-on reviewer;
- host-authored semantic truth;
- one-predicate-per-call review;
- a claim that 51/52 labels will transfer to fresh tasks;
- a repair benefit; or
- any change to `workbench/`.

The canonical packets were task-author/executor-specified. They show that Qwen
can usually use a sufficient explicit decision scenario; they do not show that
Qwen or a mechanical host can create such scenarios reliably.

## Next boundary

Do not run a fourth wording or zoom correction. The next useful test, if
continued, is whole-method and prospective: on fresh code tasks whose explicit
requirements have frozen task-author executable packets, compare the ordinary
candidate against one grouped factual review followed by one bounded correction
opportunity. Grade the first candidate, the factual findings, finding-to-repair
uptake, and terminal candidate separately. The packet catalog must be frozen
before seeing the candidate, and executable checks remain authoritative.

