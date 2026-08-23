# Information-state calibration v0 — consolidated result

Status: **complete; provenance calibrated; construction-bound conjunction
retired; no treatment run**.

## Quantitative summary

| Batch | Calls | Admitted | Prompt | Completion | Total tokens | Cached | Reasoning | Summed duration |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 12 | 11 | 5,943 | 4,062 | 10,005 | 737 | 0 | 199,958 ms |
| B | 6 | 5 | 3,748 | 3,300 | 7,048 | 402 | 0 | 164,862 ms |
| Combined | 18 | 16 | 9,691 | 7,362 | 17,053 | 1,139 | 0 | 364,820 ms |

Across 16 admitted artifacts, the direct reviews sealed 86 criterion judgments.
Both runs replay exactly from their captured apparatus.

Local validation ran 597 tests: 583 passed and 14 archived-continuation tests
were intentionally skipped. The focused calibration suite passed 16/16,
including a negative test that detects drift in hashed saved apparatus.

| Family / stage | Eligible | Gate | Decision |
|---|---:|---:|---|
| Provenance, Batch A | 4/6 | 3/6 | calibrated |
| Construction, Batch A | 0/6 | 3/6 | one revision authorized |
| Construction, Batch B | 2/6 | 3/6 | failed; family retired |

The provenance result was unusually clean: 18/18 literal facts were correct,
11/18 smallest citations were correct, and every one of the seven errors named
the line immediately before the true support.

The construction revision produced two intended cases, cache and sensor, but
not the required three. Other artifacts either had broader operand loss or did
not enter the artifact boundary. The two rejected graph-like responses both
exhausted the response channel through malformed repetition.

## Answer to the research question

This calibration does not show that information geometry has predictive
power, because it exposed no treatment. It does establish two task/failure
states that can support a future direct test:

1. exact content survives while exact provenance binding fails; and
2. compact many-to-one synthesis preserves central gist while secondary
   distinctions disappear (from the prior fresh screen).

It failed to establish a third stable construction-bound state where possessed
operands are routinely misbound in code. The original three-family selector
test therefore remains invalid.

Any next experiment must be separately preregistered as a two-family
provenance-versus-synthesis crossover, with a task-conditioned choice compared
against every universal single-view policy. A selected treatment winning only
its intended family would not be enough; the selector must beat the best
always-use-one-view policy across held-out worlds.

## Evidence

- [`BATCH-A-RESULTS.md`](BATCH-A-RESULTS.md)
- [`BATCH-B-RESULTS.md`](BATCH-B-RESULTS.md)
- [`CUSTODY-CORRECTIONS.md`](CUSTODY-CORRECTIONS.md)
- [`runs/information-state-calibration-v0-batch-a-run-001`](runs/information-state-calibration-v0-batch-a-run-001)
- [`runs/information-state-calibration-v0-batch-b-run-001`](runs/information-state-calibration-v0-batch-b-run-001)
