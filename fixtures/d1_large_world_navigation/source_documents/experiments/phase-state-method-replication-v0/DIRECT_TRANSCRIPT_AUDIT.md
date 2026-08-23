# Direct prompt, action, and artifact audit

Status: **complete for coherent measured run r3**

Date: 2026-08-16

The exact r3 requests, responses, interpreted actions, tool results,
candidate snapshots, checkpoints, checks, and terminal artifacts were
inspected after replay verification. This report records facts that aggregate
status and grader fields conceal.

## Integrity and execution

- Source lock: 106 files verified.
- Replayed standard runs: 6/6 verified.
- Transcript continuations: 2/2 verified with exact turn boundaries.
- Checkpoint transports: 2/2 successful and schema-valid.
- Model responses: 91 under one server process.
- Runtime: Qwen3.8-27B AD-IQ2_S, q8 KV, 25,088 context, MTP off,
  llama.cpp b10434, full 66/66 offload.
- GPU process after load: 10,953 MiB dedicated and 102 MiB shared.
- GPU after clean stop: 551 MiB used.

The exact post-run verifier output is in
[`POSTRUN_VERIFICATION.json`](POSTRUN_VERIFICATION.json). Runs r1 and r2 are
preserved apparatus corrections and are not measured evidence. r3 is the only
coherent full campaign.

## What each first continuation request contained

| Arm | Messages | First prompt tokens | Prior transcript | Checkpoint capsule | Shared Phase-B task/receipt |
|---|---:|---:|---:|---:|---:|
| Lease T | 33 | 14,180 | yes | no | yes |
| Lease W | 2 | 880 | no | no | yes |
| Lease P | 2 | 4,745 | no | yes | yes |
| Freight T | 31 | 10,566 | yes | no | yes |
| Freight W | 2 | 1,033 | no | no | yes |
| Freight P | 2 | 5,612 | no | yes | yes |

Every exact first system message says `bounded local artifact workbench`; no
condition received the old code-only label. T retained the exact Phase-A
action/result history. W received only the current task, mechanical boundary
receipt, world, and tools. P received the same fresh boundary plus its
explicitly non-authoritative checkpoint and selected exact current files.

## Common Phase-A trunks

Lease Phase A used 15 calls:

`tree → five reads → registry patch → test read/patch → failed check → model
patch → registry reread/patch → passed check → submit`

It submitted and passed 10/10 Phase-A audit groups. Freight Phase A used 14
calls:

`tree → seven source reads → memo read/patch → failed check → patch → passed
check → submit`

It submitted and passed its 9/9 supporting audit. The Phase-B branches for a
task began from one byte-identical derived candidate.

## Lease-registry continuation

### Exact action sequences

| Arm | Phase-B sequence |
|---|---|
| T | tree; read change request; read registry; replace registry; read tests; incomplete test-patch response |
| W | tree; read change request, contract, registry, tests, init, models; replace registry; reread tests; three bounded test patches with an intervening reread; failed check; reread; final test patch; passed check |
| P | read registry; replace registry; read tests; incomplete test-patch response |

P's separate checkpoint call had already inspected the Phase-A transcript and
current world. It correctly stated that renew must preserve ID and ordinal,
that rename must preserve the remaining lease fields, and that the old
replacement-renewal tests must be revised. Its exact selected files totaled
6,755 bytes; it did not select the package test, so the actor reopened that
file before trying to edit it.

### Product and self-test outcomes

A post-run audit was executed against each verified terminal candidate with
bytecode generation disabled for the evaluator and its child process. It used
the frozen complete Phase-B audit but kept its 11 external product groups
separate from the model-authored package-test group. An initial cache-hygiene
mistake and the successful custody restoration are preserved in
[`AUDIT_CORRECTION.md`](AUDIT_CORRECTION.md).

| Arm | Terminal status | External product | Package tests | Full audit | Submitted |
|---|---|---:|---:|---:|---:|
| T | protocol error | 11/11 | fail: 2 stale renew assertions | 11/12 | no |
| W | turn limit | 11/11 | pass | 12/12 | no |
| P | protocol error | 11/11 | fail: 2 stale renew assertions | 11/12 | no |

All three implementations correctly encoded the new Phase-B product
contract. They preserve lease ID, ordinal, name, and priority on renewal; use
`max(existing expiry, clock) + ttl`; add rename with the required exception
and preservation behavior; and pass all external product cases.

T and P left the Phase-A test bytes unchanged. Those tests still require a
new lease ID/ordinal on renew and contain two failing assertions. This was not
because either actor lacked the new rule. Both read the test; P's checkpoint
also explicitly named the required test revision. Each then attempted one
large exact patch containing a complete replacement of the 7,309-byte test
file.

The T failure occurred at a combined-window boundary: 21,282 prompt tokens +
3,806 completion tokens = exactly 25,088. The P actor had only 10,609 prompt
tokens but consumed its separate 4,096 completion-token allowance. Both JSON
objects ended before a valid action existed, so custody admitted no mutation.

W instead used bounded substring patches. Its first rewritten test block
invented a case that advanced the clock beyond expiry and nevertheless
expected renew to succeed. The visible complete audit rejected that
model-authored test. W reread it, removed the contradictory case, and passed
12/12 on call 16. Because the frozen limit was exactly 16 calls, it had no
remaining call to submit.

This is not a semantic product failure. It is a three-way separation among
correct product construction, derivative-test revision, action-expression
feasibility, and closure.

## Freight-memo continuation

| Arm | Phase-B sequence | Terminal |
|---|---|---|
| T | tree; index/review/R7/R8/R9 reads; memo patch; failed check; patch; passed check; submit | submitted |
| W | tree; memo/index/R7/R8/R9/review reads; memo patch; failed check; memo reread/patch; passed check; submit | submitted |
| P | memo/R7/R8/R9 reads; memo patch; failed check; memo reread/patch; passed check; submit | submitted |

The P capsule selected 6,883 exact bytes: the Phase-A memo, editorial review,
current index, and R1/R3/R4. Its checkpoint accurately represented R7/R8/R9
but did not project their bytes; the fresh actor reopened those three records.
This is faithful use of exact source as authority and checkpoint prose as a
non-authoritative transform.

All three first memo rewrites contained the required substantive meaning. All
three failed only the supporting audit's lexical requirement for the word
`unmeasured`, despite already saying the outcomes were `not measured`. Each
made a small harmless wording patch, passed 14/14, and submitted.

Direct source-to-artifact review found T and W at 11/11 semantic rubric
criteria. P correctly replaced the stale R6 rule and retained the full factual
core, but its last sentence ambiguously made coverage and citywide-evidence
work prerequisites before the limited extension. It is rated ten met plus one
partial; details are in
[`RESEARCH_QUALITATIVE_REVIEW.md`](RESEARCH_QUALITATIVE_REVIEW.md).

## Checkpoint uptake and action organization

The checkpoint package produced a repeated orientation effect:

- code's first mutation occurred on P actor call 2, T call 4, and W call 8;
- research's first mutation occurred on P actor call 5 (method call 6 when the
  producer is counted), T call 7, and W call 8.

It did not produce a repeated complete-method advantage. In code, early
readiness was followed by an oversized test rewrite. In research, the
checkpoint reduced actor calls but its production and repeatedly projected
6.9 KB made it more expensive and slower than on-demand W.

## Literal audit conclusion

The important outcome is not represented by terminal status alone:

- W's code artifact was fully correct but unsubmitted at an administrative
  boundary.
- T and P had correct product implementations but stale tests because no
  complete edit action crossed the response channel.
- all three research artifacts revised the superseded authority correctly;
  P had one bounded over-strengthening rather than the prior stale-rule
  failure.

The process package therefore remains an accurate experimental instrument
with an organizational effect, but it is not a reliable complete method.
