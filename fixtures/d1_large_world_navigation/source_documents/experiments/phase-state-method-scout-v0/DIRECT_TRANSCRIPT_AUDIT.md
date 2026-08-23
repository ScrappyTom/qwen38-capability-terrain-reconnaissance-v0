# Phase-state method scout direct transcript audit

Status: **complete**

Date: 2026-08-16

## Evidence inspected

I inspected both common trunks, both checkpoint-production calls, every
continuation request, response, interpreted action, tool result, candidate
effect, check result, submission, and all six terminal artifacts. The split
post-run verifier replayed four standard r1 runs, two r1 transcript runs, two
r2 standard runs, and the corrected r2 transcript run.

The original research transcript failure and correction were also inspected
literally. Turns 16–25 of r2 are byte-identical to r1 for every request,
assistant action, and pre-submit tool result. Both produced terminal candidate
`d4aee507...`. In r1, a 261-character experiment-owned submission path failed
after the model emitted `submit`; in r2, the shortened path allowed the same
candidate to receive its submission and passing grade receipts. See
[`EXECUTION_CORRECTION.md`](EXECUTION_CORRECTION.md).

## What the model first saw

| Task | Condition | First-request messages | Request bytes | First prompt tokens | Model-visible state |
|---|---|---:|---:|---:|---|
| Code | Transcript | 21 | 20,328 | 5,293 | Complete 9-turn Phase-A action/result history plus the Phase-B task |
| Code | World | 2 | 5,586 | 920 | Fresh system + Phase-B task/current candidate |
| Code | Process | 2 | 14,678 | 3,485 | Fresh task + checkpoint, manifest, and three selected exact files |
| Research | Transcript | 33 | 33,964 | 9,075 | Complete 15-turn Phase-A action/result history plus the Phase-B task |
| Research | World | 2 | 6,354 | 1,086 | Fresh system + Phase-B task/current candidate |
| Research | Process | 2 | 18,817 | 4,801 | Fresh task + checkpoint, manifest, and six selected exact files |

Every later request was the exact cumulative result of its saved prior
request/action/result chain. All 46 measured continuation responses ended
normally with `finish_reason: stop`. There were no rejected actions, no no-op
mutations, no response truncations, and no context-limit failures.

Direct prompt review found one held apparatus defect: the shared system
message called the environment a “code-repair workbench” during the research
task. The action contract itself remained factual and usable, and all three
research conditions shared the wording, so it does not explain their
differences. It is nevertheless an inaccurate cross-domain host sentence and
must be corrected or overridden with task-neutral wording before a fresh
cross-domain replication.

## Common trunks

The code trunk used:

`tree → SPEC read → three package reads → ledger read → patch → passing check → submit`

It completed all 10 Phase-A executable groups in nine calls.

The research trunk used:

`tree → index → R1/R2/R3/R4/R5/R6 → memo → patch → failed check → two patches → passing check → submit`

It completed its nine literal audit groups in fifteen calls. Direct review of
that Phase-A memo found a model-authored recommendation requiring a later
finalized positive effect before expansion. That statement was not a source
record. It became important in Phase B because the editable memo—not only
task-authoritative sources—crossed every condition's boundary.

## Code continuation

All three branches started from candidate `d7ac86e9...` and passed all 16
executable v1/v2 groups.

### Transcript

Action sequence:

`CHANGE_REQUEST read → ledger read → one whole-file exact patch → passing check → submit`

The patch factored account/unit validation into helpers and added both methods
without consuming identifiers or ordinals. It used five calls and 36,957
tokens. The complete Phase-A history avoided a tree and SPEC reread, but made
each request larger.

### Fresh world

Action sequence:

`tree → change read → SPEC read → ledger read → patch → passing check → submit`

It implemented the same behavior with inline validation. It used seven calls
and 19,700 tokens, the lowest code cost.

### Process checkpoint

The checkpoint accurately selected `CHANGE_REQUEST.md`, `SPEC.md`, and
`allocation/ledger.py`, stated three correct v2 relations, and reported no
unresolved item. The actor then used:

`ledger read → patch → passing check → submit`

It used four actor calls plus one checkpoint call. The method cost was 26,695
tokens: fewer actions than world, but more total work because checkpoint
production cost 6,936 tokens. No code-quality difference resulted.

## Research continuation

All three branches started from candidate `a408c51e...`, removed superseded
[R2]/[R5] content, preserved the complete required factual core, passed the
12-group literal audit, and submitted. Direct semantic differences are in
[`RESEARCH_QUALITATIVE_REVIEW.md`](RESEARCH_QUALITATIVE_REVIEW.md).

### Transcript

Action sequence:

`index → editorial review → R7 → R8 → memo → patch → failed check → patch → passing check → submit`

The first artifact missed only the audit's exact `not system-wide` wording.
The second patch added it. Ten new calls used 127,467 tokens and reached a
17,119-token maximum prompt. The terminal memo was the cleanest direct
semantic result.

### Fresh world

Action sequence:

`tree → editorial review → index → memo → R7 → R8 → patch → failed check → memo reread → patch → failed check → patch → passing check → submit`

Its first check missed `no difference` and `not system-wide`; its second still
missed the latter. It used fourteen calls and 96,813 tokens. The terminal memo
preserved all required content but introduced an unsupported caveat that the
final fully allocated cost might omit other operational costs.

### Process checkpoint

The checkpoint accurately described [R7]/[R8] and the supersession but did not
select their exact bytes under its six-path limit. The actor reopened both. Its
sequence was:

`memo → R7 → R8 → patch → passing check → submit`

It used six actor calls plus one checkpoint call and 58,534 method tokens. It
passed the literal audit on its first construction. Its terminal memo still
retained a stale Phase-A decision rule about needing a later finalized,
materially positive estimate. Thus the checkpoint improved operational
organization without certifying semantic revision.

## Capacity and cost

| Task | Condition | Actor calls | Method calls | Method tokens | Max actor prompt | Recorded model time | Failed checks |
|---|---|---|---|---:|---:|---:|---:|
| Code | Transcript | 5 | 5 | 36,957 | 9,099 | 98.75 s | 0 |
| Code | World | 7 | 7 | 19,700 | 4,666 | 37.90 s | 0 |
| Code | Process | 4 | 5 | 26,695 | 5,838 | 73.31 s | 0 |
| Research | Transcript | 10 | 10 | 127,467 | 17,119 | 186.11 s | 1 |
| Research | World | 14 | 14 | 96,813 | 12,466 | 186.19 s | 2 |
| Research | Process | 6 | 7 | 58,534 | 10,774 | 189.54 s | 0 |

“Method calls/tokens” include the checkpoint producer in P. Recorded model
time includes prompt processing and decoding reported by llama.cpp. The
process method's research token reduction did not reduce elapsed model time:
its checkpoint was an uncached extra inference and its one construction was
long. Prompt caching also made transcript history cheaper in time than its
cumulative token count alone suggests.

All maximum prompts remained below 25,088 and every mutation fit inside the
4,096-token response allowance. This scout therefore tested continuity and
work organization, not input or output exhaustion.

## Direct interpretation

The complete transcript was not required for mechanical continuity on either
workflow. Fresh current world alone was sufficient, and the process package
reduced actor reacquisition and check/repair cycles. The process package was
not a semantic replacement for history or exact authority. Its model-authored
state was accurate in the two checkpoints, but an old semantic derivative
inside the current research artifact survived anyway.

This is a promising complete-method lead for fresh replication, not evidence
for a canonical plan, automatic reset, semantic card, or stable checkpoint.
