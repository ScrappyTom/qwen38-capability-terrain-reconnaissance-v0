# Sparse runtime field study v0 — direct transcript audit

Date: 2026-08-17

## Audit boundary

The investigator inspected the literal system and task messages, every raw
assistant message, every parsed action, every tool result, every rendered
request, the unchanged candidate, and the terminal transport errors for all
three saved runs. The model was nonthinking, so the saved assistant content is
the complete model output exposed by the API.

All three completion-time replay reports recorded `verified:true`. None of the
runs changed the starting candidate
`d1188c233f173bf0e7920a8c35b0961bfaaf471bbb1aa3316117ada956106cc1`.

## r1: invalid unfiltered/whole-read pilot

Qwen called `tree`, read the complete 51,678-byte target, read the complete
37,891-byte `docs/CURRENT_STATE.md`, and queried the catalog for
`phase-working-set-longitudinal-v0`. The catalog searched authoritative paths
and saved custody copies together, reported 5,445 matches, and returned a
25,595-byte first page. Turn 5 contained 33,712 prompt tokens and llama.cpp
rejected it against the 25,088-token context.

The model had no line-range read. This run is apparatus evidence only.

## r2: invalid optional-slice/unbounded-line pilot

The corrected action catalog visibly included `read_lines` and
`repo_read_lines`. Qwen did not select them. It read the same complete target
and current-state document. One `repo_search` with the normal directory prefix
`experiments/` was rejected because the validator required `experiments`.
Qwen recovered with a root search for `2026-08-17`.

That search found only 11 lines but returned 43,342 bytes. Two minified JSON
lines contained 14,066 and 24,588 characters. Turn 6 contained 38,185 prompt
tokens and was rejected. Making bounded reads available had not made bounded
transfer part of the method, and a line-count limit had not bounded literal
search bytes.

This run is apparatus evidence only.

## r3: mechanically bounded transfer

The third apparatus disclosed and enforced a 12,000-byte limit on whole reads
and line slices. Search returned exact bounded match windows, and normal
trailing-slash directory prefixes were accepted.

Qwen's complete action sequence was:

| Turn | Prompt tokens | Literal action | Result |
|---:|---:|---|---|
| 1 | 1,742 | whole target read | rejected: 51,678 > 12,000 bytes |
| 2 | 1,893 | target lines 1–400 | rejected: 20,449 > 12,000 bytes |
| 3 | 2,060 | target lines 1–250 | rejected: 12,071 > 12,000 bytes |
| 4 | 2,227 | target lines 1–245 | accepted, 11,900 bytes |
| 5 | 5,179 | target lines 246–450 | accepted, 11,264 bytes |
| 6 | 8,040 | target lines 451–650 | accepted, 11,759 bytes |
| 7 | 10,993 | target lines 651–800 | accepted, 10,419 bytes |
| 8 | 13,768 | target lines 801–886 | accepted, 6,336 bytes |
| 9 | 15,320 | whole `docs/CURRENT_STATE.md` read | rejected: 37,891 > 12,000 bytes |
| 10 | 15,470 | candidate `read_lines` on repository path | rejected: not a candidate file |
| 11 | 15,625 | repository lines 1–400 | rejected: 23,288 > 12,000 bytes |
| 12 | 15,791 | repository lines 1–250 | rejected: 14,336 > 12,000 bytes |
| 13 | 15,957 | repository lines 1–200 | accepted, 11,543 bytes |
| 14 | 18,822 | repository lines 201–400 | accepted, 11,745 bytes |
| 15 | 21,750 | repository lines 401–620 | rejected: 14,603 > 12,000 bytes |
| 16 | 21,918 | repository lines 401–550 | accepted, 9,514 bytes |
| 17 | 24,416 | repository lines 551–620 | accepted, 5,089 bytes |
| 18 | — | next request | rejected: 25,970 > 25,088 tokens |

The accepted slices cover every target line 1–886 exactly once and every
current-state line 1–620 exactly once. Qwen transferred 89,569 accepted slice
bytes. It used no catalog, search, or history action in r3 and read no
underlying experiment result, direct audit, or raw trajectory.

`docs/CURRENT_STATE.md` tells the reader that it is an entry point rather than
an evidence source. Qwen exhausted the active context immediately after
reconstructing that complete entry point, before following its evidence links.

## Task-selection audit

The task treated the target's `Date: 2026-08-15` header as its evidence cutoff.
Git history contradicts that premise. The target blob at the pinned source had
last changed at commit
`e56769a1fc5734f424ecaa053563f14c519ff353` on 2026-08-17, after the phase-
working-set and authentic-reentry results were already incorporated. Only one
later commit existed through the pinned source head:
`c700faabc45f066684c875a3866317ccaa1355ed`, the mechanical reentry-seed study.

Therefore the task overstated the actual delta. The header date was stale
metadata, not a valid source-basis receipt. No claim about Qwen's ability to
integrate all post-August-15 evidence is admissible from these runs.

## Admissible behavioral interpretation

The r3 behavior establishes a narrower point: enforcing a per-result byte cap
did not induce a selective active working set. Qwen used the slices to
reconstruct two whole broad objects in the ordinary transcript. Per-transfer
bounding changed action feasibility but not acquisition strategy.

The literal actions also show that Qwen was not failing to use bounded access.
After discovering the limit it successfully tiled both objects with exact,
nonoverlapping slices. The observed failure was that every accepted slice
remained resident in transcript history while the acquisition policy remained
global. Smaller transfers therefore changed paging behavior without reducing
the resident working set.

This trajectory does not establish that Qwen is generally unable to select
relevant information. The model-facing environment did not expose the exact
artifact basis, the complete changed-source set since that basis, or a
structural target map. The task broadly asked it to reconcile a maintained
document with current project evidence. Under that information environment,
full acquisition of the target and its named orientation entry point was a
coherent, if resource-infeasible, strategy.

This boundary is reinforced by independent, cross-package evidence rather
than inferred from the reducer. In a separate Q3 XL study, the literal task
frames exposed 14–18 meaningful objects with stable metadata and exact reads.
Direct inspection of all six prompts, accepted/rejected actions, final
artifacts/code, and reviews found task-dependent acquisition breadth (13/14
for both research tasks; 12/14 and 8/14 for writing; 6/14 and 5/14 for code),
zero duplicate accepted reads, 6/6 correct central decisions, and 25/26
semantic criteria passed with one partial. The four recovered read rejections
were interface friction: the actor already named a stable ID, but the provider
required it to appear in a prior query result. See the
[pinned primary result](https://github.com/ScrappyTom/custody-cards-experimental-workbench/blob/3c651b66d1f991b686b4ddcaf9cc4fb3df55dfd4/studies/authentic-working-set-assembly-baseline-v1/reports/RESULTS.md).

That result does not change any literal fact about r3 and is not a same-model
replication. It rules out using r3 as evidence for an inherent global-reading
trait. A better joint interpretation is that the actor can select when the
address space exposes decision-relevant units; when the addressable objects
are large and insufficiently differentiated, it may use slices to reconstruct
them globally.

The first consequential boundary was navigation/acquisition/coverage. The run
never reached authoritative evidence integration, artifact construction,
verification, or closure. There is no terminal semantic artifact to grade.

The next admissible question is therefore structural selection, not eviction:
whether an exact external basis/delta map plus stable, directly readable target
region IDs changes which regions Qwen chooses to acquire. Measure object
breadth, per-object depth, and cumulative residency separately. Automatic
summaries, semantic section assignments, and active-context eviction remain
unearned until that simpler package is tested.
