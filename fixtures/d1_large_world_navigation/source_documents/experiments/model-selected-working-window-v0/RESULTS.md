# Q3 XL transferred working-window result

Date: 2026-08-17

Verdict: **the transferred window did not become a bounded action window**

## What happened

The live first request fit comfortably: 12,855 prompt tokens plus the complete
3,072-token response allowance left 9,161 tokens of headroom. Q3 XL then made
eight requests in the one authorized trajectory. Seven returned valid actions;
request 8 was rejected by the local server because its 26,227-token prompt
exceeded the 25,088-token context. No retry or replacement run occurred.

Before the capacity stop, the model:

- tried to read the complete 51,678-byte candidate despite receiving 219 exact
  resident lines and a complete candidate receipt;
- received the expected 12,000-byte read-limit rejection;
- opened the complete path-level delta catalog;
- read the candidate sequentially through line 620 in five calls;
- materialized 768 of 886 candidate lines in total (86.7%), including 549
  lines that were not resident initially and 71 resident lines read again; and
- made no mutation, check, or submission.

The candidate remained byte-identical to its starting state.

## What the reasoning shows

The model did not simply overlook the supplied evidence. Before broad
reacquisition, it correctly identified the mechanical-reentry experiment as
the likely material update, summarized its no-promotion conclusion, connected
it to a specific open question in the working model, noticed the 20-call
limit, and said it should be strategic.

It nevertheless adopted a stronger operative frame: understand the complete
886-line maintained document before deciding what to change. The subsequent
actions followed that frame by reading successive broad line ranges. The
transferred exact set influenced interpretation, but did not control the
acquisition strategy.

## Capacity boundary

The initial capacity gate was valid only for turn 1. Prompt residency then grew
with exact tool results and the phase transcript:

| Turn | Prompt tokens | Headroom before response | Headroom after reserving 3,072 |
|---:|---:|---:|---:|
| 1 | 12,855 | 12,233 | 9,161 |
| 3 | 17,159 | 7,929 | 4,857 |
| 6 | 21,834 | 3,254 | 182 |
| 7 | 24,268 | 820 | -2,252 |
| 8 | 26,227 | -1,139 | -4,211 |

Turn 7 completed only because its actual answer was short. Turn 8 could not be
admitted at all. The server and all 66 model layers were healthy; this was
context exhaustion, not a GPU load or model transport defect.

## Interpretation

This is a negative result for the exact tested handoff. It does not support the
claim that another actor's exact selected subset will automatically become Q3
XL's resident working set when ordinary transcript accumulation remains in
place.

It also does not establish that the selected set was semantically insufficient.
The model's own reasoning extracted the central update from it. The unresolved
question is whether complete-artifact reconstruction was necessary for safe
maintenance or was an overly broad task frame.

No artifact-quality comparison is possible because construction never began.
The result therefore localizes the observed boundary before semantic
construction: **working-set acceptance and acquisition organization under
growing residency**.

Because the 12 carried blocks were selected by a historical AD-IQ2_S actor,
this result says nothing about whether Q3 XL would select a better subset for
itself.

## Process consequence

Future multi-turn experiments should measure capacity before every request and
record a distinct capacity-censored terminal state before sending an oversized
request. That safeguard would improve diagnosis; it would not make this
trajectory a success or authorize a retry.

The next architecture test, if pursued, should cross the missing mechanism
directly: keep the exact larger world externally addressable while preventing
the entire acquisition transcript and large tool results from remaining
resident. Do not rerun this cell with a larger cap and call it a repair.

