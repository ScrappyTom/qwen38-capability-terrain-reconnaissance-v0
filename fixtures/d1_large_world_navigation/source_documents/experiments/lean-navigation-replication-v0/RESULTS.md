# Lean exact-navigation replication v0 — results

Date: 2026-08-12

Status: **quality null on the prospectively frozen fresh task; stop typed-navigation promotion**

Prospective freeze commit: `e682efe`

The fixed order ran once without retry or result-dependent tuning:

1. `NATIVE_FILESYSTEM`
2. `LEAN_NAVIGATION`

Both conditions used the same frozen quota-allocation world, public checker,
hidden grader, llama.cpp server, nonthinking `qwen36-27b-iq2-coding` profile,
and temperature-zero request policy. Exact evidence is under [`runs/`](runs/).
The mechanically reconstructed and verified comparison is
[`analysis-summary.json`](analysis-summary.json).

## Result

Both conditions produced usable but byte-distinct implementations. Each
passed all 6 public and all 17 hidden cases.

| Measure | Native filesystem | Lean navigation |
|---|---:|---:|
| Public grade | 6/6 | 6/6 |
| Hidden grade | 17/17 | 17/17 |
| Assistant calls | 19 | 15 |
| Tool calls | 18 | 15 |
| Prompt tokens across calls | 72,571 | 77,846 |
| Generated tokens | 1,543 | 1,658 |
| Total tokens across calls | 74,114 | 79,504 |
| Approximate model-call elapsed | 87.345 s | 95.219 s |
| Run wall time | 109.533 s | 95.409 s |
| Candidate mutations | 1 | 1 |
| Visible checks during work | 2 | 1 |
| Rejected or errored tool actions | 0 | 0 |
| Read declared authority file | no | yes |
| Read superseded/archive source | 0 | 0 |

Relative to native filesystem, lean navigation used 21.05% fewer assistant
calls and 16.67% fewer tool calls, but 7.27% more prompt tokens, 7.45% more
generated tokens, 7.27% more total tokens, and 9.01% more measured model-call
time. Its wall time was 12.89% lower. The runners have different startup and
recording paths, so wall time is descriptive rather than a clean inference
cost comparison.

These are two trajectories, not rates. Equal hidden grades satisfy the frozen
stop rule regardless of the behavioral and cost differences.

## What the model was given

The native saved prompt was byte-equal to the first provider user message. It
asked for a repair to `src/quota_lab/allocator.py` according to the current
release contract and authority records, but did not name the authority file or
any policy module. Pi supplied its ordinary coding-agent frame and `read`,
`bash`, `edit`, and `write` tools.

The lean first request was byte-equal to its saved system and task prompts. Its
system message stated that the catalog was complete and unranked, exact bytes
were request-only, and the host made no semantic selection or recommendation.
It offered only:

- `artifacts` for the complete factual catalog;
- `whole` for one exact frozen artifact;
- `candidate_read` and `candidate_write` for the mutable target;
- `check` bound to the current candidate; and
- `submit` bound to the current candidate.

The catalog exposed path, byte count, SHA-256 version, mechanically derived
artifact type, and lifecycle. It contained no gist, semantic tag, relevance,
ranking, relation, history, recommended action, or selected packet.

## What the native trajectory did

Native Pi first listed the repository, `src`, `src/quota_lab`, and the current
rules directory. The root listing exposed `release_catalog.json`, but the
model never read it. It instead read:

- the target allocator;
- `models.py` and `bindings.py`;
- all six current rule modules imported by `bindings.py`;
- the public checker; and
- package `__init__.py`.

It read no archive file. It ran the public checker before mutation and received
the literal 0/6 result. Its next substantive message accurately enumerated the
six current operations and validation boundaries. It made one exact edit,
reran the checker, received 6/6, and stopped normally. Tree custody shows that
only the target allocator changed.

## What the lean trajectory did

Lean navigation read candidate `C000`, requested the complete 20-item catalog,
then selected exact bytes for:

- `release_catalog.json`;
- `bindings.py` and `models.py`;
- the public checker; and
- all six `release_bound_current` rule modules named by the authority record.

It requested no superseded source. After describing the concrete rule
composition in its own message, it wrote `C001` once, checked that exact
candidate once, received 6/6, and submitted the same candidate and SHA-256
version. There were no malformed, repaired, rejected, or unbound calls.

The complete saved history preserves every returned assistant message with
its native `tool_calls`, JSON-encoded arguments, matching `tool_call_id`, and
literal result. The analyzer verified all 15 protocol links, exact whole-file
hashes, both candidate snapshots, check/submission identity, final copy, and
request/response counts.

## Direct artifact adjudication

Both final artifacts:

- validate `requested_units` through the current rule;
- preserve raw `account_ref`, `region`, and `expedite` at their owning rule
  boundaries;
- resolve the current account key and service class;
- compose base, region, and expedite capacity;
- calculate approved and overflow units; and
- obtain the reason code from the current encoder.

The only substantive byte difference is that lean navigation names
`total_cap = regional + bonus`, while native Pi places the same expression
directly inside `min`. The lean import retains the fixture's pre-existing
`# noqa: F401` comment; the native edit removes it. Neither difference changes
behavior. Independent grading confirms identical public and hidden outcomes,
including ten invalid-input boundaries.

## Interpretation

The first atlas scout's one-case quality advantage did not replicate. On this
fresh work shape, an ordinary filesystem ecology and a lean factual-navigation
ecology both found the current rule set, avoided the superseded set, composed
the owning functions without duplicating their contracts, and produced fully
passing artifacts.

The typed ecology did change sourcing. It made the release authority explicit
in the actual trajectory; native Pi inferred the same current module set from
`bindings.py` and directory contents without consulting the authority file.
That is evidence that a factual index can alter how Qwen acquires exact source,
not evidence that it improves work. The typed path also reduced turns while
increasing cumulative tokens and measured model time.

This whole-ecology comparison cannot attribute any behavioral difference to
one component. It bundles system frame, tool schemas, catalog availability,
retrieval operation, candidate identity, checker binding, submission, and
Pi's ordinary shell/edit environment. The result does not establish that
typed identity, authority metadata, stable candidate operations, or any
particular prompt is causally inert. It establishes that the complete lean
bundle produced no terminal-quality advantage here.

## Decision

Do not add typed navigation to the workbench, do not tune this fixture, and do
not run further task variants merely to seek another win. The prospectively
frozen replication rule was clear: equal or worse artifact quality stops
promotion from these scouts.

Retain the two source-project ideas as design inspiration and removable
research operands:

1. typed artifact/provenance identity with model-selected exact retrieval;
2. operation-specific return types with stable candidate/check/submission
   identity.

The experiments show that both are implementable without semantic host
selection. They may be useful for transparent custody, controlled research,
or a task ecology that operationally needs them. They have not earned status
as the general Qwen performance mechanism. The stable project result remains
the laboratory's ability to expose those distinctions truthfully.

## Local validation

- the prospective qualification reran successfully;
- focused Ruff checks passed for the experiment's Python apparatus;
- the analyzer reconstructed both saved trajectories and verified every
  declared custody invariant;
- `python -m unittest discover -s tests -q` passed 248 tests with 14 skips; and
- `python -m pytest -q` passed 270 tests with 14 skips.

This is local validation, not GitHub Actions verification.
