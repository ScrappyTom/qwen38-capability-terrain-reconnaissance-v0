# Fresh code re-entry continuation result

## Outcome

The bounded continuation did **not** improve the UD candidate or reach natural
closure. Across eight additional calls, Qwen made three distinct test edits,
ran two failed checks, and ended at the absolute call-28 ceiling without
submitting. The external audit remained 13/14: product behavior stayed 13/13,
while the same contract-wrong self-authored test remained the only failure.

The continuation was nevertheless necessary. The call-20 cutoff had occurred
immediately after a new failed-check receipt. Continuing exactly established
that the next work was not a latent one-turn fix hidden by administration.
Instead, the model repeatedly changed local details while preserving the same
incorrect expected outcome.

## Quality curve

| Boundary | Product groups | Candidate tests | Status |
|---|---:|---:|---|
| Saved UD ecology endpoint | 3/13 | incomplete | 32-call cutoff after repeated rejected no-ops |
| Fresh re-entry call 20 | 13/13 | 22/23 | cutoff immediately after exact failed check |
| Exact continuation call 28 | 13/13 | 22/23 | no submission; same semantic test failure |

Fresh re-entry therefore produced a large authentic product recovery from the
saved UD endpoint. The eight-call continuation added no further quality and
cost 238,870 tokens because the exact transcript grew from 23,064 prompt
tokens on call 21 to 36,190 on call 28.

## What the transcript establishes

The remaining failure was not caused by missing task truth. The request
contained the exact issue clause, the current test, and the exact check result.
The model did not reread the issue after failure. It instead:

- swapped priorities, which broke the first lease;
- restored priorities but described the expired job as still active; and
- moved time from the exact expiry boundary to one second later, which still
  expires the job.

All three edits tried to preserve `beta-1` as the expected second lease. The
contract requires expired `acme-1` to return to its original pending position;
at priority 9 versus 8 it is correctly leased again. This is a local semantic-
comparison failure expressed through active test repair, not an action
rejection, no-op loop, absent receipt, or lack of additional calls.

## What this says about 25K phase management

The broader lead survives, but in a narrower form.

- A fresh phase can restore input headroom. AD's source request had filled its
  25,088-token slot; fresh re-entry reached only 7,435 prompt tokens before its
  attempted action.
- Input headroom does not guarantee a feasible action. AD then exhausted the
  independent 4,096-token response/action channel during a whole-file rewrite.
- Fresh state can break a mechanical fixation. UD escaped eight repeated
  rejected no-op patches, began checking, and moved product behavior from
  3/13 to 13/13.
- A fresh phase does not guarantee semantic correction. Both packages retained
  the same wrong ordering expectations in self-authored tests, and exact UD
  continuation reinforced rather than corrected that interpretation.
- Carrying a full transcript forward is expensive. Eight continuation calls
  alone used 237,399 prompt tokens and ended with a 36,190-token request.

So 25K is plausibly enough for useful **bounded phases**, especially with the
higher-quality AD quant, but only if phase design preserves sufficient
governing state and the next action fits its output channel. This study does
not earn automatic resets, summaries, cards, semantic host selection, or
forced action decomposition.

## Decision

Retain the stable workbench unchanged. Retain AD/q8/25K MTP-off as the
provisional bounded quality package and UD/q4/50K/MTP3 as the optional long-
context speed package.

For future larger workflows, measure these boundaries separately:

1. input-context occupancy at each call;
2. response/action expression demand;
3. exact state transferred across a fresh phase;
4. reacquisition work after the boundary;
5. product behavior versus model-authored verification artifacts; and
6. whether marginal work changes the governing mechanism or merely varies
   local details around the same conclusion.

The next experiment should not be another unconditional reset. The one
transcript-derived lead is a bounded comparison/reorientation phase for a
self-authored verification failure: current artifact, exact failing test or
claim, and the exact governing record must be made jointly available without
host-authored diagnosis. That should first be discussed against the project's
prior relation-alignment and reviewer failures before any GPU run.

See [DIRECT_TRANSCRIPT_AUDIT.md](DIRECT_TRANSCRIPT_AUDIT.md) for the literal
eight-call sequence and [CUSTODY_CORRECTION.md](CUSTODY_CORRECTION.md) for the
preserved runtime-reducer correction.
