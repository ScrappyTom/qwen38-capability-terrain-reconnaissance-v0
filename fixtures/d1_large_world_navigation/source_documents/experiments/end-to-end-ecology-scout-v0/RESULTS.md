# End-to-end workflow ecology scout v0 results

Date: 2026-08-16

Status: complete discovery scout; no harness intervention or model package is
promoted by this study.

## Result in one paragraph

The larger workflow boundary mattered, but it did not expose one general
Qwen3.8 failure. In code, AD-IQ2_S/q8 built product behavior that passed all
13 product-behavior audit groups, then wrote three incorrect regression-test
assertions, followed those assertions into repair, and exhausted its 25,088-
token context while expressing another patch. UD-IQ2_XXS/q4/MTP3 still had
context headroom but never ran a check: after one large construction it emitted
the same exact no-op rewrite eight times and ended at the 32-call limit with a
broken package. In research, both packages acquired the corpus, discriminated
current from superseded evidence, wrote useful decision memos, and correctly
accepted or rejected all eight fixed editorial comments in a fresh revision
stage. AD preserved every frozen research distinction; UD produced a shorter
memo that retained the central analysis but compressed four exact secondary
details. The ordinary loop therefore remains a capable baseline, but larger
code work exposed concrete context, self-verification, and action-organization
boundaries that the smaller workflow matrix did not.

## Measured endpoints

| Package and workflow | Endpoint | Direct quality result | Important boundary |
|---|---|---|---|
| AD/q8/25K code | Protocol error at call 21; no submission | 13/14 complete audit groups; all 13 product-behavior groups passed | Three candidate tests asserted behavior contrary to the supplied contract; the final response filled the 25,088-token window and truncated a patch action |
| UD/q4/50K/MTP3 code | 32-call limit; no check or submission | 3/14 complete audit groups | The candidate lacked a required record type and import; calls 18–32 alternated rereads with eight byte-identical no-op rewrites |
| AD/q8/25K research draft | Submitted at call 19; mechanical check passed | 18/18 frozen semantic criteria met; 1,099 words | Complete acquisition and high-detail synthesis |
| AD/q8/25K research revision | Submitted at call 18; mechanical check passed | 18/18 memo criteria retained; 8/8 editorial decisions correct | Fresh context used a targeted subset of the corpus without losing the draft's broader support |
| UD/q4/50K/MTP3 research draft | Submitted at call 18; mechanical check passed | 14/18 met, 4/18 partial, 0 unsupported; 767 words | Central interpretation survived; design, raw ridership, survey, and cost-denominator details were compressed |
| UD/q4/50K/MTP3 research revision | Submitted at call 22; mechanical check passed | Memo remained 14/18 met and 4/18 partial; 8/8 editorial decisions correct | One response claimed the memo now contained the 13,142 denominator although the artifact still omitted it |

These are six case studies, not pass rates or reliability estimates. AD and UD
also differ in weights, quantization, KV precision, context size, and MTP, so
the package differences cannot be attributed to any one setting.

## Code findings

### AD: correct product, incorrect self-verification, exhausted context

AD read the issue, API, implementation, tests, and incident log before
mutating. Its first substantive implementation correctly represented tenant
capacity, expiry-before-selection, stable retry ordering, lifetime job-ID
uniqueness, attempt limits, and lease-token validation. The external complete
audit later passed every product-behavior group.

The actor also expanded the test file from two tests to seventeen. Three new
assertions were wrong:

1. after `lease_next` returned an expired job again, the test expected that
   job to be pending rather than active;
2. a test expected merely reading `state()` to perform expiry, although the
   task specified expiry before each lease decision; and
3. after a retryable failure preserved original order, a test expected a
   lower-priority/later job to be leased next.

The visible check exposed those exact failures. Qwen treated the test suite as
authoritative enough to revise around it, briefly introduced unrelated state
logic, reverted that change, and began another test correction. The call-21
request used 25,022 prompt tokens; the 66-token completion reached the exact
25,088-token context limit with `finish_reason: length`, leaving incomplete
JSON for the patch action. This was not a malformed native-tool boundary. It
was an exact capacity failure after productive work and misleading
self-authored verification.

### UD: capacity available, action loop unbroken

UD acquired the same governing records and produced one large dispatcher
rewrite. The candidate referenced `_Record` and `bisect` without defining or
importing them, and its expiry path did not implement attempt exhaustion. It
then repeatedly reread the same file and submitted the same whole-file patch
whose old and new text were identical. Each rejection truthfully reported
`no_op_patch`. The exact patch arguments had the same SHA-256 on eight calls.
Prompt use rose from 13,628 tokens on the first no-op turn to 40,851 on the
last, still below the 50,176-token window.

This failure was not caused by missing source, hidden feedback, malformed
actions, or insufficient context. The model did not turn literal no-op
rejection into a different operation, a check, or a narrower mutation. It is
an authentic repeated-action organization failure, but one trajectory does
not yet earn a generic anti-loop mechanism.

### Product, tests, and workflow are separate outcomes

The code cells demonstrate why terminal status and one aggregate score are
insufficient:

- AD's product implementation was usable while its test artifact and workflow
  closure were not.
- UD's action protocol remained valid while its world state was broken and
  unchanged for half the trajectory.
- a requirement to add tests can introduce a second authored artifact whose
  semantic correctness must be evaluated independently of the product.

Future coding scouts must therefore report product predicates, candidate-test
correctness, action admission/effect, check use, and closure separately.

## Research findings

Both packages read the index and all ten governing records. AD also read both
archives; UD read the relevant superseded ridership archive and skipped the
irrelevant cost archive. Neither request exposed a rubric, control artifact,
or answer key.

AD's draft preserved the matched nonrandom design, adjusted and raw ridership,
wearable denominator and missingness mechanism, survey denominator and
response rate, equity scope, operational limits, complete cost denominator,
safety evidence, and a proportionate continuation recommendation. Its two
numerical reliability thresholds were explicitly proposed decision
conditions, not represented as observed source facts.

UD's draft was also coherent and appropriately cautious. Its four partial
criteria were omissions rather than contradictory claims: it omitted the
matched-neighborhood count/readiness details, raw ridership comparison, survey
sample/respondent/response-rate figures, and the 13,142-boarding denominator.
This is the previously observed central-gist/secondary-detail compression
shape, now inside an otherwise successful authentic research workflow.

The fresh revision stage was operationally useful. Both actors received the
exact terminal memo bytes, the same corpus, and the same preauthored review.
Both correctly accepted comments Q1, Q3, Q5, Q6, and Q8 and rejected Q2, Q4,
and Q7. AD retained all prior distinctions. UD improved the executive summary
but did not recover omitted details outside the review's active scope; it also
correctly explained the cost denominator in its response without actually
adding that denominator to the memo.

This is stronger than prior generic submit-time reviewer results, but the
cause is a complete method package: itemized task-author comments, mixed valid
and invalid claims, exact source access, a concrete artifact, and a fresh
revision role. It does not show that an autonomous same-model reviewer can
generate equally useful comments. It does show that review uptake must be
measured in the artifact, not inferred from a correct response.

## Cost and runtime

Reported token counts are cumulative request accounting across calls, not
unique corpus size.

| Package/workflow | Calls | Prompt | Completion | Total | Model time |
|---|---:|---:|---:|---:|---:|
| AD code | 21 | 229,059 | 5,947 | 235,006 | 322.56 s |
| AD research draft | 19 | 98,453 | 2,151 | 100,604 | 112.21 s |
| AD research revision | 18 | 121,272 | 1,505 | 122,777 | 79.83 s |
| UD code | 32 | 501,296 | 22,692 | 523,988 | 625.95 s |
| UD research draft | 18 | 87,611 | 1,666 | 89,277 | 57.96 s |
| UD research revision | 22 | 149,856 | 2,530 | 152,386 | 72.68 s |

UD MTP3 accepted 19,890 of 20,934 drafted tokens across 72 responses and
decoded at a weighted 35.54 tokens/s. That throughput did not prevent its code
loop. AD decoded at about 18.44 tokens/s in code and 19.04 tokens/s across the
separate research continuation. Speed, context capacity, and artifact quality
remained distinct properties.

## Custody and apparatus corrections

The frozen package coordinator incorrectly coupled the independent research
stages to the preceding code transport status. AD's exact context-limit
failure stopped the first process. A separately committed continuation ran
only the untouched AD research stages under a second recorded server
lifecycle. No model-facing task, profile, method, or fixture changed.

A direct Python audit initially created `__pycache__` in AD's materialized code
candidate. The exact two directories were removed, no recorded source changed,
and replay passed. Post-run evaluation must henceforth operate on a verified
copy or explicitly disable bytecode and all other side effects.

The frozen verifier continues to preserve the original AD aggregate failure.
The post-run verifier separately establishes three recorded server lifecycles,
six exact run replays, locked sources, and exact draft-to-revision byte
transfer. See [CUSTODY_CORRECTIONS.md](CUSTODY_CORRECTIONS.md) and
[POSTRUN_VERIFICATION.json](POSTRUN_VERIFICATION.json).

## Decision

No card, semantic transform, automatic reviewer, retry, no-op repair, audit
feed, or closure policy is promoted. The stable harness remains unchanged.

The broad scout does earn a narrower next developmental question: whether a
fresh ordinary-loop code phase can recover from two mechanically identifiable
endpoints without semantic host guidance—an exhausted context window and an
exact repeated rejected action. That should be tested as fresh re-entry from
the saved current artifact with the original task, ordinary tools, and no
summary. The two triggers must be reported separately; success on one would
not justify a universal reset controller.

The research result does not currently earn another information-format study.
It instead provides a strong successful comparison case and one bounded UD
detail-compression case for any later work on source competition or review
coverage.

## Evidence

- [Freeze](FREEZE.md)
- [Direct transcript audit](DIRECT_TRANSCRIPT_AUDIT.md)
- [Research qualitative review](RESEARCH_QUALITATIVE_REVIEW.md)
- [Custody corrections](CUSTODY_CORRECTIONS.md)
- [AD code records](runs/r1/ad25q8/code/records.jsonl)
- [UD code records](runs/r1/ud50q4m3/code/records.jsonl)
- [AD terminal memo](runs/r1/ad25q8/research-revision/candidate/decision_memo.md)
- [UD terminal memo](runs/r1/ud50q4m3/research-revision/candidate/decision_memo.md)

## Local validation

- focused study tests: 4/4 passed;
- repository `unittest` discovery: 634 passed, 14 intentionally skipped;
- corrected post-run verification: six exact run replays and three server
  lifecycles passed with zero errors;
- `git diff --check`: passed; and
- port 8080 was free with no `llama-server` process after execution.

Repository-wide `pytest` discovery is not a valid project gate in the current
archive layout: it collects duplicated `test_study.py` modules and fixture/run
copies as live tests, producing import-file mismatches and package-path errors.
Those are collection errors, not failed stable-harness or study assertions.
The documented stable gate remains `unittest` discovery plus the study's
focused verifier.
