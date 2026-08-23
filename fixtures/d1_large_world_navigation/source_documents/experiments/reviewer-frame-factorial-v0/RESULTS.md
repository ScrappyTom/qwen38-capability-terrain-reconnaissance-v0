# Reviewer frame factorial v0 — results

Date: 2026-08-12

Decision: **one-cell partial action lead; native matrix protocol-confounded; no promotion**

## Result in plain language

Qwen could use the assessor's finding, but not reliably and not completely.

The clean schema-action matrix held the task, candidate, assessment, tools,
model, and settings fixed. Three conditions read, checked, and finalized the
unchanged paper. Only the combination of:

- responsibility limited to Recommendation; and
- the initial passed mechanical receipt being visible

caused an edit. That edit accurately added L1 and L3 support, but still omitted
L2 from the Recommendation's adjusted-result claim. The paper therefore
remained incomplete on the same citation requirement.

This is a real behavioral difference on one deterministic fixture. It is not
evidence that passed checks generally help, that bounded work items should be
permanent, or that the interaction will replicate.

## Assessor gate

The fresh binary assessor returned all four frozen relations correctly:

| Unit | Expected | Observed |
|---|---|---|
| U001 Executive Summary | supported | supported |
| U002 Results | supported | supported |
| U003 Limitations | supported | supported |
| U004 Recommendation | not_supported | not_supported |

Its U004 explanation correctly said that L4 cannot support the section's
nonrandom-selection and counter-coverage claims, which depend on L1 and L3.
It was not exhaustive: it did not separately identify that the adjusted-result
claim also lacked L2. That omission matters because every useful downstream
edit repaired L1 and L3 while leaving L2 absent.

The assessor used 2,041 prompt, 754 completion, and 2,795 total tokens. The
exact assessment artifact is SHA-256
`53be36f7f88e267dbf5b7e177c4fac1baa408e3813ed756459bfb56ce28b06e0`.

## Primary schema-action matrix

All 26 schema responses were complete, schema-valid, and admitted without
normalization or retry.

| Condition | Exact action path | Mutation | Terminal Recommendation bindings | Result |
|---|---|---:|---|---|
| W0 whole, no receipt | evidence; four sections; check; finalize | 0 | L4 | unchanged partial |
| W1 whole, pass receipt | evidence; four sections; check; finalize | 0 | L4 | unchanged partial |
| S0 bounded, no receipt | four sections; check; finalize | 0 | L4 | unchanged partial |
| S1 bounded, pass receipt | evidence; Recommendation; replace rejected; replace applied; check; finalize | 1 | L1, L3, L4 | improved partial |

W0 and W1 chose the same seven-action path and produced the byte-identical
starting candidate. Initial receipt visibility had no observed action effect
under whole-artifact responsibility.

S0 began with Recommendation but then read the other three sections, never
read `evidence_update.md`, checked, and finalized unchanged. S1 read the exact
evidence and Recommendation, attempted a replacement, recovered from one
literal `new_body_contains_level_two_heading` rejection, applied the corrected
replacement, checked it, and finalized it.

Thus neither factor was sufficient alone on this run:

- bounded responsibility without the receipt did not cause a repair; and
- a visible receipt under whole-artifact responsibility did not cause a
  repair.

Only S1 diverged. The preregistered decision list explicitly anticipated S0
alone but inadvertently omitted S1 alone. This is therefore recorded as an
unlisted one-cell interaction lead, not forced into a stronger frozen label.

## Direct artifact adjudication

The starting paper and every terminal paper satisfy task requirements 1
through 5. Every terminal paper remains partial on requirement 6, which asks
for applicable L1-L4 citations where claims appear.

S1's new Recommendation accurately states:

- the assignment facts with L1;
- the coverage and missingness direction with L3; and
- the exploratory subgroup limits with L4.

It also repeats the adjusted association, confidence interval, and p-value
without L2. Exact Recommendation binding coverage therefore improved from one
of four applicable records to three of four, but the task did not become
complete. No factual regression was found.

Across the four schema conditions:

- 4/4 finalized;
- 1/4 mutated the candidate;
- 1/4 improved exact binding coverage;
- 0/4 produced a task-complete artifact; and
- all four ran a fresh mechanical check before finalization.

These are condition counts over one non-exchangeable fixture, not success-rate
estimates.

## Native run and apparatus correction

The initially frozen runner reused native OpenAI-style functions from the
reviewer-seat experiment. Direct raw-output inspection found the known Qwen /
llama.cpp delimiter failure:

- W0 had 10 argument-schema rejections in 14 calls and reached the turn limit;
- S0 had one such rejection and recovered;
- S1 had two and recovered; and
- W1 had none.

In the malformed responses, Qwen emitted multiple XML-like calls despite
`parallel_tool_calls: false`. llama.cpp returned one standardized call whose
`path` argument contained the closing tags and later calls. The harness did not
repair it; it returned the exact allowed-path rejection. W0 repeatedly emitted
the same malformed shape and never acquired the evidence file or reached an
editorial decision.

W0 is therefore ineligible for semantic scope/receipt interpretation. The
native run remains useful action-ecology evidence:

| Condition | Outcome |
|---|---|
| W0 | protocol-bound turn-limit failure; no submission |
| W1 | valid partial L1/L3 repair; L2 still absent |
| S0 | rewrite used undeclared combined handle `[L1, L3]`; exact binding coverage did not improve |
| S1 | valid partial L1/L3 repair; L2 still absent |

The native run also supplied another clean mechanical-rejection observation.
W1's first replacement incorrectly included the retained `## Recommendation`
heading, received only `new_body_contains_level_two_heading`, and immediately
retried with the heading removed. Schema S1 did the same. No coaching or
argument normalization was required.

## Quantitative observations

| Measure | Native matrix | Schema matrix |
|---|---:|---:|
| Model calls | 42 | 26 |
| Admitted actions | 29 | 26 |
| Protocol rejections | 13 | 0 |
| Execution rejections | 1 | 1 |
| Candidate mutations | 3 | 1 |
| Finalized conditions | 3 | 4 |
| Prompt tokens | 162,326 | 77,704 |
| Completion tokens | 3,873 | 855 |
| Total tokens | 166,199 | 78,559 |
| Cached prompt tokens | 145,899 | 63,502 |
| Summed HTTP duration | 221.436 s | 75.875 s |

The schema matrix used 52.73% fewer summed tokens and 65.73% less summed HTTP
time, largely because it did not enter the native malformed-call loops. This
is descriptive, not a pure protocol-performance estimate: schema actions also
suppress natural-language prose and use user-role result envelopes.

Schema per-condition totals were:

| Condition | Calls | Total tokens | Mutation turn | Final SHA-256 prefix |
|---|---:|---:|---:|---|
| W0 | 7 | 21,378 | — | `b3310ab4` |
| W1 | 7 | 22,566 | — | `b3310ab4` |
| S0 | 6 | 15,626 | — | `b3310ab4` |
| S1 | 6 | 18,989 | 4 | `5a3c70e2` |

## What this changes

The earlier statement “correct review information is inert in a broader
editor frame” was too general. On this fixture, the same assessment was inert
in three schema frames and actionable in one. Model-facing task scope and
status context can alter whether an available local judgment reaches an edit.

But the result is narrower than “salience solves it”:

1. S1 alone changed behavior; there is no replicated main effect.
2. The change was partial, not task-complete.
3. The downstream omission matched an omission in the assessor itself.
4. The native action representation changed trajectories dramatically and can
   mask the semantic question altogether.

The strongest current description is:

> Qwen can discriminate a local evidence defect and can sometimes act on that
> discrimination. Whether it does so is sensitive to the combined task and
> action frame. Even when it acts, it tends to repair the relationships made
> explicit rather than independently recover every remaining obligation.

## Decision

Do not add a permanent bounded work-item view, hide passed checks, or promote a
reviewer stage. Preserve the matrix as a positive-but-incomplete interaction
lead.

If this lead is pursued, the next clean test is one independent schema-action
fixture with:

- the same four-cell matrix;
- a frozen assessor finding that exhaustively identifies the target unit's
  applicable bindings; and
- the same direct artifact adjudication.

That replication would ask whether S1's conjunction recurs, not tune wording
around the library task. The stable harness and custody substrate require no
change.
