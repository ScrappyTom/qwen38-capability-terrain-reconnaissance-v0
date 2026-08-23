# Submission-boundary cited-evidence judge v0: results

Date: 2026-08-12

Status: **qualification failed; no judge output was relayed**

## Result in one sentence

The fresh judge correctly explained both the unsupported submission and the
supported control, but the asymmetric response frame converted the control's
positive explanation into `relation: contradicted` and `verdict: revise`.

This is a failed qualification with a useful action-frame diagnosis, not a
performance result and not evidence for a semantic submission gate.

## Exact outcomes

| Case | Frozen truth | Model verdict | Finding | Qualification |
|---|---|---|---|---|
| K01 | revise | revise | Correctly identified `8.5` as conflicting with R2's `-3.1`. | pass |
| K02 | accept | revise | Explained that every submitted claim was supported, then labeled it contradicted. | fail |

Both calls returned HTTP 200, `finish_reason: stop`, schema-valid JSON, exact
submission-review IDs, known artifact/evidence IDs, and one admitted finding.
Both replay with five custody records and 18 artifact references each.

The frozen rule required both cases to pass. The result is therefore
`not_qualified`, and no prospective builder branch is authorized.

## Direct input/output review

The judge saw one exact `Synopsis` block and the complete R1, R2, and R3
records cited by that block. It did not see the source run name, builder
transcript, task, prior grade, hidden expectation, full paper, or uncited
records. The two requests had the same system role and evidence records; only
the submitted block and opaque content identity differed.

K01 returned one substantively correct finding:

> The block claims an 8.5 percentage-point reduction ... R2 explicitly states
> the adjusted difference was -3.1 percentage points.

It also noticed that the raw rate difference was 4.8 rather than 8.5. The
finding was bound to A001 and exact evidence IDs.

K02's explanation was also substantively correct. It explicitly said the
numbers were confirmed by R2, the nonrandomized design by R1, and differential
ascertainment by R3, concluding:

> Therefore, the claim that these factors limit causal inference is supported
> by the provided evidence.

The same object nevertheless used `relation: contradicted` and
`verdict: revise`.

This was not an invented semantic defect like the earlier complete-control
disconfirmation failure. It was an inconsistency between the model's analysis
and the only finding labels available in the output frame.

## Why the frame failed

The schema permitted `accept` only as an empty finding list. If the model chose
to record its evaluation, every finding was forced to be either
`contradicted` or `unsupported`. K02 filled the explanatory structure with a
positive support assessment and then selected one of the allowed negative
labels.

The model could legally have returned `accept` with no findings, so this is
still a real model-output failure. But the interface made positive analysis
structurally silent and negative analysis richly expressible. It was not a
balanced judgment action space.

That distinction matters:

- **semantic comparison:** correct in both raw explanations;
- **structured decision:** correct in K01, wrong in K02;
- **host admission:** correct mechanically; the host did not inspect semantic
  agreement between prose and labels;
- **behavioral effect:** none, because the failed qualification prevented
  relay.

## Relation to prior evidence

This result should not trigger a fresh series of generic reviewer prompts.
Whole-artifact audits, fresh reviewers, disconfirmation, and model-authored
ledgers already failed for different reasons.

It does connect to one earlier positive sub-result: the semantic-contrast probe
gave the model a balanced `entailed` / `contradicted` / `undetermined` action
space. Qwen classified all eight entailed controls correctly and seven of
eight contradicted controls correctly, including the numeric/value cases. Its
remaining robust misses were polarity and version-evidence relations, not this
kind of numeric contradiction.

The earned next variant is therefore not “more judge prompting.” It is a
different submission-review action frame:

1. mechanically freeze artifact units and their literally cited records;
2. have a fresh judge classify each unit in a balanced relation vocabulary;
3. omit an authoritative overall verdict and omit a semantic gate;
4. relay the raw model-authored classifications as a tool result; and
5. let the builder decide whether to inspect, edit, or finalize.

That variant must use genuinely new cases. The frozen v0 rule forbids
rewording, retrying, or splitting K01/K02 around this observed output.

## Quantitative record

| Case | Request bytes | Response bytes | Prompt | Cached | Completion | Total | Duration |
|---|---:|---:|---:|---:|---:|---:|---:|
| K01 | 5,278 | 12,419 | 1,255 | 0 | 277 | 1,532 | 15.474 s |
| K02 | 5,191 | 13,172 | 1,233 | 167 | 355 | 1,588 | 19.018 s |
| **Total** | **10,469** | **25,591** | **2,488** | **167** | **632** | **3,120** | **34.492 s** |

No prompt exceeded 1,255 tokens and no completion exceeded 355 of 1,024
allowed tokens. Context pressure, truncation, transport failure, tools, and
argument repair were not involved.

## Server preflight correction

The first attempted launch was blocked before any model request because the
live external server exposed fallback defaults temperature 0.7, top-p 0.8,
and presence penalty 1.5 while the committed project profile requires 0, 1,
and 0. The endpoint receipt is preserved under
`experiment_runs/submission-evidence-judge-v0/preflight-default-mismatch/`.

The project lifecycle scripts then stopped that matching process and started
the committed deterministic nonthinking profile. The executed calls repeated
temperature 0 and the other settings at request level. This was a pre-call
environment correction, not a retry.

## Boundary and decision

The stable `workbench` is unchanged and has no dependency on
`submission_review_lab`. The lab contains a zero-argument
`submit_for_review` transition definition, exact packet renderer, judge role,
schema, call custody, and replay. None is active in the baseline harness.

Stop v0. Do not relay these outputs, reinterpret K02's prose as an admitted
`accept`, loosen the frozen qualification, or make the judge authoritative.

The balanced assessment-only variant is a justified next experiment, not a
fix to these saved calls. It should remain removable and should be tested on a
fresh submitted artifact before any default integration.

## Evidence

- pre-call freeze and stop rule: `FREEZE.md`;
- exact cases and hidden expectations: `cases.json`, `ground-truth.json`;
- frozen packets and requests: `packages/`;
- raw requests, responses, admitted objects, endpoint facts, and records:
  `experiment_runs/submission-evidence-judge-v0/`;
- direct adjudication: `adjudication.json`;
- metrics: `metrics.json`; and
- pre-call commit: `1f32738`.

Validation is local, not GitHub Actions verification. Before calls, the full
suite passed 290 tests with 14 intentional archival skips; focused Ruff and
compile checks also passed.
