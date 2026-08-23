# Evidence-first working set v0 — results

Date: 2026-08-12

Status: **negative prospective result; stop this exact working-set ecology**

Pre-call freeze commit: `89b892e`

## Outcome

The evidence-first treatment did not improve the paper. The ordinary section
baseline produced the only complete artifact.

| Measure | Evidence-first | Section baseline |
|---|---:|---:|
| Blind semantic grade | 6 pass / 2 partial / 1 fail | **9 pass / 0 partial / 0 fail** |
| Overall | incomplete | **complete** |
| Visible check | passed | passed |
| Supporting literal audit | failed 1 marker | passed |
| Protected bytes | exact | exact |
| Assistant/tool calls | 22 | 12 |
| Candidate mutations | 4 | 3 |
| Prompt tokens | 140,951 | 46,630 |
| Completion tokens | 3,305 | 1,462 |
| Total tokens | 144,256 | 48,092 |
| Uncached input tokens | 8,978 | 5,655 |
| Model-call elapsed | 183.042 s | 83.308 s |
| Wall time | 183.208 s | 83.443 s |

The treatment used 202.28% more prompt tokens, 126.06% more completion tokens,
199.96% more total tokens, and 119.72% more recorded model-call time. It made
83.33% more calls and 33.33% more candidate mutations.

These are two frozen trajectories, not reliability or general efficiency
estimates.

## The artifact difference

The baseline paper is complete under all nine frozen requirements. It reports
the current design, rates, adjusted result, interval, p value, ascertainment
rates, higher-risk missingness pattern, downward-bias direction, overstatement
consequence, and subgroup status with appropriate R1/R2/R3 bindings. It
preserves every protected byte.

The treatment paper handles the difficult ascertainment polarity correctly and
also preserves every protected byte. Its Synopsis, however, says:

```text
text reminders were associated with an 8.5 percentage-point reduction
```

The current locked record reports an adjusted difference of -3.1 percentage
points. The same Synopsis reports that current -3.1 value, so the paragraph is
internally contradictory and retains an unsupported superseded statistic.

Blind grading therefore assigns the treatment:

- partial for the Synopsis primary result;
- fail for unsupported content; and
- partial for coherence.

The SHA-only grades were written before the condition map was opened:

- [`15e493ad…`](blind/grades/15e493ad5263b443fdf050bc8e80014903f2098f819ff5979dc21c576dd57a22.md);
- [`dcd3f6f…`](blind/grades/dcd3f6f5675885465ba5e8cab1eeaa7227670d0d047f64837291a215a938f6d4.md).

The revealed map identifies `15e493ad…` as evidence-first and `dcd3f6f…` as
the section baseline.

## What the treatment actually did

The treatment read the complete paper, evidence update, editorial note, and
all three editable sections. It therefore acquired every governing fact before
creating the working set.

It then created eight exact selections:

| ID | Exact source lines | Model-declared target(s) | Used as write basis |
|---|---|---|---|
| E001 | evidence 5–8: R1 heading and beginning of design | Synopsis | twice |
| E002 | evidence 11–16: end of design plus R2 heading | Observations | never |
| E003 | evidence 17–21: complete R2 numeric result | Observations | once |
| E004 | evidence 23–31: first part of R3 audit | Observations, Assessment | once |
| E005 | evidence 31–36: R3 polarity and subgroup status | Assessment | once |
| E006 | editorial 5–9: Synopsis instruction | Synopsis | twice |
| E007 | editorial 9–13: Observations instruction plus start of Assessment | Observations | once |
| E008 | editorial 13–20: Assessment, citation, rollout, preservation instructions | Assessment | once |

Every stored selection is byte-exact and correctly bound to its frozen source
version and declared locator. Every write basis refers to existing selections
assigned to that section. The custody mechanism did exactly what it claimed.

The semantic map was the problem:

- the complete current R2 numbers, E003, were assigned only to Observations;
- no exact R2 evidence selection was assigned to Synopsis;
- no R3 evidence selection was assigned to Synopsis;
- E001 stopped in the middle of the R1 design record, before the
  nonrandomization and causation-boundary lines;
- E002 began in the middle of a sentence, contained no R2 values, and was never
  used; and
- the model never called `view_target_bundle`.

The treatment therefore did not instantiate the intended source-to-all-targets
map. It created a narrower, partly malformed map and then treated it as
complete.

## Exact construction path

The treatment sequence was:

```text
read paper
read evidence
read editorial note
read Synopsis
read Observations
read Assessment
capture eight selections
replace Synopsis — rejected for outer whitespace
replace Synopsis — accepted with old rates, causal proof, rollout, and 8.5
replace Synopsis — accepted with current rates but still 8.5
replace Observations
replace Assessment
read complete current paper
check — passed
submit
```

The first accepted Synopsis was visibly obsolete. On the next turn Qwen said
it needed to replace the superseded result, then corrected 12.2%, 20.7%, the
adjusted difference, interval, causal proof, and rollout recommendation while
leaving 8.5 in place.

After rereading the complete final paper, Qwen explicitly audited its work. It
listed the current rates and -3.1 result and declared the revision complete,
without noticing the conflicting 8.5 claim. This locates the failure at three
model-owned stages:

```text
target assignment omitted R2 → Synopsis
→ construction retained one obsolete Synopsis value
→ final reread/self-audit failed to discriminate the conflict
```

The host did not create, normalize, repair, rank, or semantically grade any of
those relationships.

## What the baseline actually did

The baseline read the same three files and three editable sections. In one
free-text preparation message it identified the section-specific changes,
including both current rates, -3.1, the confidence interval, ascertainment
rates, bias direction, and subgroup status. It then:

```text
replace Synopsis
replace Observations
replace Assessment
check — passed
read complete current paper
submit
```

It made three mutations, received no rejection, and produced the complete
9/9 paper. This is direct counterevidence to the idea that an externalized
selection artifact was necessary on this fresh task.

## Measurement boundary

The visible check passed both papers. Its obsolete marker looked for the
signed substring `-8.5 percentage`, while the treatment retained the surface
form `8.5 percentage-point reduction`. The instrument therefore missed the
actual semantic defect.

The supporting audit failed the treatment only because it required the literal
word `nonconfirmatory`; the paper's statement that the comparisons “do not
establish differential associations” is semantically adequate. The supporting
audit did not identify the 8.5 conflict either. It remains explicitly
non-authoritative.

The artifact-first blind grade, not either lexical checker, determines the
semantic result.

## Interpretation

This result does **not** show that upstream work artifacts are inherently bad.
It shows that this particular implementation failed its prospective test.

Three conclusions are supported:

1. **Exact storage does not make model-authored organization exhaustive.** The
   host perfectly preserved an incomplete source-to-target map.
2. **A declared basis does not constrain semantic generation.** The treatment
   wrote current R2 values and the obsolete 8.5 claim into Synopsis even though
   neither appeared in its declared Synopsis basis. The IDs were provenance of
   what Qwen named, not proof of what its prose used.
3. **Locator ergonomics matter.** The model selected line ranges from content
   that was identified as one-based but not displayed with inline line numbers.
   Several captures cut through multiline bullets. The returned exact selection
   made each cut visible, but Qwen did not repair it.

The third point is an interface diagnosis, not permission to tune this task.
Changing to paragraph IDs, source-native blocks, automatic target bundles, or
host-selected semantic units would be a new treatment with new tradeoffs.

The result also narrows what remains untested. `view_target_bundle` was offered
but selected zero times, so there is no behavioral evidence that the rendered
bundle itself helps or harms. Forcing it now on the same fixture would tune
around a known outcome and violate the frozen stop rule.

## Decision

Apply the frozen rule for baseline complete / treatment incomplete:

- stop this exact evidence-first working-set ecology;
- do not promote it into `workbench`;
- do not add gists, semantic completeness checks, automatic assignments, or a
  forced bundle on this fixture;
- retain `working_set_lab` only as a removable experimental artifact recording
  exact selections and model-declared relationships; and
- preserve the stronger design lesson: a future upstream artifact must make
  many-to-many organization easier to perform, not merely make an incomplete
  model-authored map durable.

## Verification

[`analysis-summary.json`](analysis-summary.json) verifies:

- pre-call qualification and frozen order;
- unchanged pre-call apparatus from `89b892e`;
- exact initial messages and request settings;
- native single tool-call responses and literal argument validation;
- complete request histories and tool-call/result links;
- exact source selections, locators, target assignments, and write bases;
- all candidate snapshots and final identities;
- protected and locked-source bytes;
- check/submission binding;
- usage and elapsed totals; and
- blind artifact, grade, and condition mapping identities.

All verification predicates are true. This is local validation, not GitHub
Actions verification.

Focused Ruff and Python compilation pass. The complete local suite passes 282
tests with 14 archived-continuation tests intentionally skipped.
