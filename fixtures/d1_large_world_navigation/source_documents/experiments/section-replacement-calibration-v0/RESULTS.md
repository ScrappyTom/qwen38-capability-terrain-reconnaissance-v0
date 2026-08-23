# Artifact-native section replacement calibration v0 — results

Date: 2026-08-12

Status: **complete known-case calibration; fresh prospective comparison earned**

Pre-call apparatus commit: `29a4e9b`

Run: `runs/section_replacement_known_case`

## Outcome

The section-replacement ecology produced the first complete artifact on the
known-resistant School Attendance task:

| Ecology | Semantic result | Visible | Supporting | Protected bytes |
|---|---:|---:|---:|---:|
| Historical schema action | 5 pass / 4 partial | passed | passed | exact |
| Ordinary native Pi | 5 pass / 4 partial | passed | passed | **not exact** |
| Artifact-native sections | **9 pass / 0 partial** | 6/6 | 8/8 | **exact** |

The final artifact is 2,352 bytes at SHA-256
`53c49731172bc7617466ac58e8de6f2666ee4c09c53e701541302b5333204282`.
It is not the authored oracle and does not need to be: it independently
satisfies all nine frozen semantic requirements.

This result satisfies every predeclared promotion condition. It earns one
genuinely fresh prospective comparison. It does **not** promote section tools
to the workbench default.

## What the model received

The user message was the exact 1,777-byte historical task at SHA-256
`2f1981fa5342d721844724a3605302d41f3e3298a0f66a21049183770331adaa`.
The system message was the 375-byte mechanical interface contract frozen in
the qualification receipt. The only tools were:

1. `read_file(path)` for `paper.md`, `evidence_update.md`, or
   `editorial_memo.md`;
2. `read_section(section_id)` for Abstract, Results, or Discussion;
3. `replace_section(section_id, expected_section_sha256, new_body)`;
4. `check()`; and
5. `submit()`.

The host exposed no rubric, oracle, task checklist, semantic status, relevance
label, missing requirement, recommended action, or required action order.
Protected material was mechanically outside the writable operation boundary.

All 12 provider requests used native OpenAI-style function calling with model
alias `qwen36-27b-iq2-coding`, `tool_choice: required`, no parallel calls,
temperature 0, `top_p: 1`, `top_k: 20`, `min_p: 0`, and thinking disabled.
All 12 responses were HTTP 200 native `tool_calls` messages with a single
JSON-string argument object. No argument was repaired.

## Artifact-first judgment

The artifact passed all nine requirements:

1. preservation;
2. design and claim strength;
3. Abstract attendance result;
4. Results attendance result;
5. response-bias relation;
6. grade-subgroup status;
7. citation binding;
8. unsupported-content removal; and
9. coherence and prose.

The Abstract names the staggered difference-in-differences design,
nonrandomized limitation, current means, adjusted difference, confidence
interval, and survey-response limitation. Results preserves the exact revised
attendance result and the full lower-response/upward-bias relation and says the
subgroup comparison was exploratory and not prespecified. Discussion is
noncausal, rejects adoption, preserves the response-bias direction, and treats
the subgroup result as nonconfirmatory.

Raw-byte custody independently confirms:

- title prefix: exact;
- Background: exact;
- Methods: exact;
- References: exact;
- `evidence_update.md`: exact;
- `editorial_memo.md`: exact;
- 41 LF endings, zero CRLF endings; and
- final candidate, snapshot, world, check, and submission identities agree.

The exact requirement rationales are in
[`runs/section_replacement_known_case/semantic-adjudication.md`](runs/section_replacement_known_case/semantic-adjudication.md).

### Review-process qualification

The final paper, task, locked records, and rubric were read before the model
dialogue. A command-group mistake also displayed `manifest.json` during that
review. The manifest exposed the condition, candidate count, final identity,
machine-check outcome, termination, timing, and token totals, but no assistant
prose, tool arguments, or source/action sequence. Semantic judgments were
fixed before `messages.json`, events, turn requests, or raw responses were
opened. The grade is therefore artifact-first and pre-dialogue, but not fully
manifest-blind.

## Exact trajectory

The model used 12 actions in this order:

```text
read_file(paper)
read_file(evidence)
read_file(memo)
read_section(Abstract)
read_section(Results)
read_section(Discussion)
replace_section(Abstract)
replace_section(Results)
replace_section(Discussion)
check
read_file(paper)
submit
```

After the three complete file reads and three exact section reads, the model
authored its own construction checklist. It separately identified the required
Abstract, Results, and Discussion changes, including the corrected numbers,
noncausal language, response-rate direction, upward-bias mechanism,
not-prespecified subgroup status, and removal of the adoption claim. The host
did not generate that checklist.

The model then produced one replacement for each editable section. Each action
used the exact section hash returned while candidate `C000` was current. The
Abstract mutation created `C001`; because the untouched Results bytes retained
their identity, the earlier Results section hash remained a valid basis for
the next operation. The same held for Discussion. The three transitions changed
only their declared section:

```text
C000 --Abstract--> C001
C001 --Results----> C002
C002 --Discussion-> C003
```

The visible check passed on `C003`. The model reread the complete current paper
and submitted the same checked candidate. There were no invalid calls,
rejections, no-op mutations, failed checks, or retries.

## Quantitative findings

### Section run

- assistant/provider calls: 12;
- tool calls: 12;
- file reads: 4;
- section reads: 3;
- section replacements: 3;
- checks: 1;
- submissions: 1;
- rejected/error tool results: 0;
- candidate versions: 4, including the initial candidate;
- cumulative prompt tokens: 44,542;
- cached prompt tokens: 39,162;
- uncached input tokens: 5,380;
- completion tokens: 1,235;
- reasoning tokens: 0;
- cumulative total tokens: 45,777;
- model elapsed time: 70.399 seconds; and
- run wall time: 70.531 seconds.

Prompt and total counts are cumulative growing-history counts, not unique
context bytes.

### Descriptive comparison

| Measure | Schema action | Native Pi | Sections |
|---|---:|---:|---:|
| Assistant calls | 7 | 26 | 12 |
| Semantic pass / partial | 5 / 4 | 5 / 4 | **9 / 0** |
| Total cumulative tokens | 20,331 | 156,434 | 45,777 |
| Provider/model time | 62.613 s | 147.283 s | 70.399 s |
| Run wall time | 63.745 s | 150.853 s | 70.531 s |

Relative to ordinary native Pi, section replacement used 29.26% as many total
tokens, 47.80% as much model time, and 46.75% as much wall time. Relative to
schema action, it used 2.252 times the tokens, 1.124 times the provider/model
time, and 1.106 times the wall time.

These are descriptive cross-ecology costs. The ecologies differ in tool menu,
protocol, permissions, action granularity, and model-facing contract, so the
ratios do not isolate a causal component.

## What this result supports

This run supports a concrete lead: on this known failure, making the artifact's
declared revision units into exact, separately mutable objects coincided with
complete semantic construction and exact preservation. The useful change was
not additional evidence. All three ecologies had the same task and source
facts. Nor was it a downstream closure message. The section ecology altered
the work the model had to formulate and commit during construction.

The trajectory gives a plausible mechanism worth testing:

```text
exact source acquisition
→ exact per-section bases
→ model-authored section checklist
→ three bounded commitments
→ whole-artifact check and reread
```

The locality was real, not cosmetic. A mutation to Abstract could not alter
protected bytes or invalidate the still-unchanged Results and Discussion
section identities. This removed whole-file serialization and preservation
from the model's burden while leaving semantic content and workflow order under
model control.

## What this result does not support

It does not establish that section replacement caused the improvement or that
it generalizes. This was one temperature-zero run on the exact case used to
select the intervention. The treatment also bundles several differences from
Pi: a smaller typed tool menu, no shell, section-scoped write authority,
section reads, and conditional section hashes. The artifact was graded by the
investigator against a frozen rubric, not by an independent prospective grader.

Do not rerun or tune this task, add cards, promote persistent state views, or
modify the stable workbench from this result.

## Decision

The predeclared threshold was met. Preserve this interface as a removable
experimental module and run one fresh paired comparison that holds the native
function-calling loop, exact reads, checks, submission, model settings, and
task fixed while changing only the construction boundary:

- whole-document conditional replacement; versus
- declared-section conditional replacement.

The new fixture must be authored and qualified before either model call, use a
different domain and heading vocabulary, contain at least one polarity-bearing
evidence relation, and have a frozen artifact-first semantic rubric. No result
on the known School case should influence wording after the prospective freeze.

## Verification

`analysis-summary.json` verifies every pre-call apparatus blob, initial
message, provider request, native response, action/result link, schema
argument, section basis, candidate transition, snapshot, check binding,
submission binding, raw protected byte, locked source byte, machine receipt,
semantic receipt, usage total, and timing total. Every verification predicate
is true.

Local validation after the run:

- focused Ruff and Python compilation pass;
- `python -m unittest discover -s tests -q`: 248 passed, 14 intentionally
  skipped;
- `python -m pytest -q`: 270 passed, 14 intentionally skipped; and
- no GitHub Actions verification is claimed.
