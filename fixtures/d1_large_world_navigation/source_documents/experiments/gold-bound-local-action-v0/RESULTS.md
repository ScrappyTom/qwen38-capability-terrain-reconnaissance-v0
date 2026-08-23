# Gold-bound local action v0 — results

Date: 2026-08-12

Status: **complete; active-obligation treatment stopped at v0**

## Outcome

The prospectively frozen comparison is a semantic-grade null:

| Condition | Unit pass | Partial | Fail | Complete artifact |
|---|---:|---:|---:|---:|
| A0 — correct task-author binding + full task | 3 | 3 | 0 | no |
| A1 — identical input + active local obligation | 3 | 3 | 0 | no |

Both conditions corrected the central defect in every flawed unit and
preserved the correct no-op exactly. Both also omitted the same three
pass-level details: the raised-observed-mean step in the missingness mechanism,
the nonrandom-assignment disclosure, and an explicit statement that an
unmeasured injury outcome cannot be established.

The active obligation changed wording on U004 and U006 but changed no grade.
Per the frozen decision rule, it is unnecessary on this task and earns no
replication or wording adjustment.

## Prospective integrity

Commit `8a6b0a9` froze and pushed the fixture, task-author gold bindings,
task-author obligation assignments, treatment boundary, deterministic request
construction, model settings, application logic, rubric, verifier, and tests
before any model response. The numeric identifiers were deliberately permuted
before freezing so unit, evidence, and requirement numbers could not reveal
the assignment.

The run used:

- Qwen3.6-27B UD-IQ2_XXS;
- alias `qwen36-27b-iq2-coding`;
- llama.cpp b10331;
- nonthinking, temperature 0, top-p 1, top-k 20, min-p 0;
- strict JSON Schema output;
- A0 U001–U006 followed by A1 U001–U006; and
- no retry, repair, normalization, tools, history, voting, or fallback.

Endpoint inspection matched the frozen model alias, build, and model path.

## Mechanical result

- 12 of 12 responses ended with `finish_reason: stop` and were admitted.
- 2 of 2 condition artifacts were constructed.
- Both visible structural checks passed.
- Both outside-span proofs matched exactly: 415 protected bytes with SHA-256
  `b0b3034d99e5e284a3721b219b2645309636b89bdd5004edc7bdf9a6f30a92b8`.
- Each condition changed five units and preserved U005 byte for byte.
- No reasoning tokens were reported.
- Replay verifies the requests, raw responses, results, candidate bytes,
  checks, metrics, and source copies.

These are custody and mechanical facts, not the semantic grade.

## Direct unit review

The primary agent read all 12 saved requests, all 12 raw responses, all six
source units, all six complete evidence records, and both composed artifacts.
[`ADJUDICATION.json`](ADJUDICATION.json) records the frozen-rubric judgment.

| Unit | Operation | A0 | A1 | Direct finding |
|---|---|---|---|---|
| U001 / N3 | numerical correction | pass | pass | Both produced exact 7.2%, 2.1–12.3%, p = 0.008, and `[N3]`. |
| U002 / N1 | citation insertion | pass | pass | Both added `[N1]` without changing facts. |
| U003 / N5 | bias polarity | partial | partial | Both changed understated to exaggerated but omitted the explicit raised-mean step. |
| U004 / N2 | causal qualification | partial | partial | Both removed causality but omitted nonrandom assignment. |
| U005 / N6 | no-op preservation | pass | pass | Both were byte-identical to C000. |
| U006 / N4 | unmeasured outcome | partial | partial | Both removed the false no-increase claim but omitted the explicit cannot-establish conclusion. |

Four of six paired outputs were byte-identical. U004 and U006 differed only in
phrasing and remained in the same rubric category.

## Quantitative telemetry

| Measure | A0 | A1 | A1 − A0 |
|---|---:|---:|---:|
| Calls | 6 | 6 | 0 |
| Prompt tokens | 5,522 | 6,422 | +900 |
| Completion tokens | 429 | 419 | -10 |
| Total tokens | 5,951 | 6,841 | +890 (+14.96%) |
| Cached prompt tokens | 965 | 1,158 | +193 |
| Summed HTTP/model time | 40.927 s | 31.162 s | -9.765 s (-23.86%) |
| Changed units | 5 | 5 | 0 |
| Byte-identical no-op | 1 | 1 | 0 |

The time difference is not interpreted as a treatment effect: A1 ran second
against the same server and benefited from a different cache state. Aggregate
usage was 11,944 prompt tokens, 848 completion tokens, 12,792 total tokens,
and 72.089 seconds of summed HTTP time.

## Interpretation

### What this supports

Prospectively correct bindings plus one exact artifact unit were sufficient
for Qwen to select and execute the central operation across five different
defect types without an explicit active-obligation field. It also recognized
the no-op and preserved it exactly. That is a meaningful transfer from the
known heat-response calibration.

Atomic local action remained incomplete. The model often made the smallest
central correction while dropping a second explicitly required qualification
from the same record. Exact binding and local scope therefore reduce the work
selection problem; they do not guarantee exhaustive use of one record.

### What this does not support

- The task-author active-obligation object did not improve a grade.
- Gold task-author bindings are not a proposed runtime feature.
- The run did not test model-created or model-verified bindings.
- One mechanically coherent composition does not qualify a recomposition
  policy or submission tool.
- The result does not authorize semantic host selection or certification.

## Decision and next boundary

Stop `active_local_obligation` v0. Do not replicate it, tune its wording, or
make it a default model-facing object.

The local-action boundary is productive but imperfect: zero failures, five
directionally correct repairs, one exact no-op, and three strict passes in both
conditions. That is enough to test the next isolated upstream question without
pretending the editor is perfect:

> Can a model create or verify correct claim–record bindings without admitting
> plausible semantic-neighbor false positives?

The next experiment must be assessment-only. It may not edit or relay a
binding downstream. False positives are the primary stop condition.
