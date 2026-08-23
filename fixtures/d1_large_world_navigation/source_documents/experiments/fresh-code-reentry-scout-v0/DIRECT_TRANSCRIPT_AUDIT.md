# Direct transcript audit at the frozen cutoff

## Scope

This audit reads the literal requests, responses, actions, results, source
endpoint trajectories, candidate files, and executable receipts. Aggregate
audit counts are not used as a substitute for those records.

Both fresh runs began from the exact saved endpoint candidate. The first model
request contained the original 846-character task and the ordinary schema
action surface. It contained no parent transcript, summary, prior check,
diagnosis, selected source, card, or suggested action. Temperature was 0.7,
top-p 0.8, seed 314159, and each response allowed 4,096 tokens.

## AD-IQ2_S / q8 / 25K / MTP off

AD used nine admitted actions to list the tree and read the issue, API,
package exports, dispatcher, models, policy, tests, and errors. It did not run
a check and did not read the incident log. Its call-10 request was only 7,435
prompt tokens. The response then used all 4,096 allowed completion tokens and
stopped with `finish_reason:length` in the middle of a whole-file replacement
for `tests/test_dispatcher.py`. The partial JSON content was 14,342 characters
and no action was admitted. The candidate therefore remained byte-identical.

This is not a second 25K context-bound failure. The fresh phase recovered
substantial context headroom, but the model selected an action larger than the
fixed response/action channel.

The attempted rewrite also did not demonstrate a correct semantic repair. It
included assertions that a lower-priority job should follow a retry of a
higher-priority job, that a low-priority job should follow a retry of a
high-priority job, and that a lower-priority same-tenant job should follow a
retryable failure of its higher-priority sibling. Those expectations conflict
with descending priority plus preservation of the original ordering position.

The saved endpoint and unchanged terminal candidate pass all 13 external
product-behavior groups. Their only complete-audit failure is the candidate's
own test suite, where three assertions encode similarly incorrect state or
ordering expectations. Fresh capacity did not resolve that interpretation.

## UD-IQ2_XXS / q4 / 50K / MTP3

UD listed the tree and read the issue, API, exports, dispatcher, models,
policy, tests, errors, and incident log. It then made four admitted mutations
with no rejection:

1. a large dispatcher rewrite;
2. a local correction after rereading it;
3. a second local correction after the first visible check exposed an
   `_Record.job_id` error; and
4. a large regression-test rewrite.

It ran three visible checks. The first failed on the concrete attribute error,
the second passed, and the final check ran 23 model-authored tests and exposed
one failing assertion. The terminal external audit moved from 3/14 at the
saved endpoint to 13/14. All 13 product-behavior groups pass; the sole failure
is the model-authored test suite, with 22/23 tests passing.

The remaining test expects `beta-1` after higher-priority `acme-1` expires.
The supplied contract instead returns expired work to its original ordering
position; with priority 9 versus 8, `acme-1` is correctly leased again. The
literal final receipt showed this exact mismatch on call 20. The fixed call
ceiling then stopped the run before the model could respond, so this endpoint
is administratively censored rather than a natural terminal choice.

## Comparison with the source endpoints

The source AD run ended with a 25,022-token prompt and only 66 completion
tokens before exactly filling 25,088 tokens. Fresh re-entry restored the full
4,096-token response allocation, but the chosen whole-file action still did
not fit. Context reset and feasible action expression are therefore distinct.

The source UD run never checked. Its last sixteen calls alternated rereading
`dispatcher.py` with eight byte-identical patches rejected as
`no_op_patch`. Fresh re-entry broke that exact action fixation: every one of
its 20 interpreted actions was admitted, the product moved from 3/13 to 13/13
external behavior groups, and executable feedback became part of the work.

## Cutoff interpretation

Fresh ordinary-loop re-entry is not a universal completion method. It produced
a strong saved-case recovery from an exact rejected-action loop and no terminal
gain from the already product-correct AD endpoint. It also required broad
reacquisition in both cases and did not cure the shared semantic confusion in
self-authored ordering tests.

The 25K lead is therefore conditional: a fresh phase can recover input-context
capacity, but useful workflow capacity also depends on what exact state crosses
the boundary and whether the next intended action fits the response/tool
channel. No automatic reset, summary, card, or action decomposition is
promoted from these two cases.

UD's exact cutoff was continued under the project's censoring rule. Across
calls 21 through 28 it made three different test patches and ran two more
failed checks, but every patch preserved the same false expectation that
expired higher-priority `acme-1` should yield to lower-priority `beta-1`.
Quality remained 13/14 and the model did not submit. This resolves the cutoff
ambiguity without establishing natural closure: the model was still changing
bytes at call 28, but its marginal work repeated one ineffective semantic
mechanism. AD's incomplete action remains a natural protocol boundary and was
not continued. See
[`continuation/DIRECT_TRANSCRIPT_AUDIT.md`](continuation/DIRECT_TRANSCRIPT_AUDIT.md)
and [`continuation/RESULTS.md`](continuation/RESULTS.md).
