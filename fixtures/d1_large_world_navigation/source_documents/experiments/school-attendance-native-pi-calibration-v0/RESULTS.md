# School Attendance native-Pi calibration v0 — results

Date: 2026-08-12

Status: **known-case calibration complete; native Pi changes the error profile
but does not dominate the schema-action ecology**

Prospective apparatus freeze: `e580cdc`

Exact run: [`runs/native_pi_known_case/`](runs/native_pi_known_case/)

Verified reconstruction: [`analysis-summary.json`](analysis-summary.json)

## Outcome

On the exact task and exact three starting files from the already-resistant
School Attendance case, native Pi submitted a different but still incomplete
paper.

| Result | Historical schema action | Native Pi calibration |
|---|---:|---:|
| Investigator requirements | 5 pass / 4 partial / 0 fail | 5 pass / 4 partial / 0 fail |
| Overall | incomplete | incomplete |
| Visible checker | 6/6 pass | 6/6 pass |
| Supporting literal audit | 8/8 pass | 8/8 pass |
| Paper SHA-256 | `16c7ae71…` | `a6a0f5b…` |

Neither artifact dominates the other. Native Pi improves three requirements,
regresses three, and leaves three unchanged. This calibration gives no basis
to promote native Pi, schema action, or either whole-document editor for this
work shape.

## Exact requirement tradeoff

| Requirement | Schema action | Native Pi | Delta |
|---|---|---|---|
| Preservation | pass | partial | regressed |
| Design and claim strength | partial | partial | same |
| Abstract attendance result | pass | partial | regressed |
| Results attendance result | pass | pass | same |
| Response bias | partial | pass | improved |
| Grade subgroup | pass | partial | regressed |
| Citation binding | pass | pass | same |
| Unsupported content | partial | pass | improved |
| Coherence and prose | partial | pass | improved |

Native Pi repaired the historical response/nonresponse inversion. Results and
Discussion now correctly say response was lower in later-start schools and
that this could bias respondent-only sleep duration upward. That also removes
the historical unsupported-content and internal-coherence defects.

It introduced different omissions:

- Abstract omits the required confidence interval and does not explicitly
  label 1.7 days as the adjusted difference;
- Abstract still omits the nonrandomized/noncausal design limitation; and
- no revised section says the grade comparison was not prespecified.

The initial artifact-visible grade was 6 pass / 3 partial. Raw-byte custody
then changed preservation from pass to partial: every one of the paper's 39
line endings changed from LF to CRLF. Both stages are preserved in
[`semantic-adjudication.md`](runs/native_pi_known_case/semantic-adjudication.md).

## What the model was given

Qualification establishes that the task and all three starting artifacts are
byte-identical to the historical schema-action acquisition. The native prompt
contains the exact 1,777-byte task after an ordinary Pi preamble. Pi supplies
native `read`, `bash`, `edit`, and `write` tools. It adds no card, plan,
semantic selector, packet, ledger, reviewer, checklist, or recommendation.

All 26 provider requests used the frozen nonthinking Qwen profile at
temperature 0, top-p 1, top-k 20, min-p 0, no parallel tool calls, and 4,096
maximum completion tokens. The saved prompt is byte-equal to the first
provider user message, and every native tool-call/result link verifies.

The ecology difference is intentionally broad:

- historical: strict bare schema actions, one exact whole-paper patch, typed
  check and submit;
- calibration: Pi native tool calls, shell access, whole-file write, no native
  submission action, and a visible checker stored outside the candidate.

This run does not attribute the artifact tradeoff to any one component.

## Exact native action path

Qwen first read `paper.md`, `evidence_update.md`, and `editorial_memo.md` in
full. It then used 22 more tools:

1. called the checker without its required candidate argument;
2. called it with `paper.md` as though the file were the candidate directory;
3. listed the workspace;
4. ran the correct initial check and received the obsolete-literal failure;
5. wrote one complete 2,191-byte draft;
6. ran the checker and received a protected-References failure;
7. inspected the file tail, visible checker, and checker constants through
   several shell/read calls;
8. emitted the same 2,191-byte whole-file write again;
9. received the same protected-References failure;
10. diagnosed the absent terminal newline;
11. used Python text-mode I/O to append it;
12. received a visible pass; and
13. reread the final paper and stopped.

Both `write` payloads are byte-identical and lack a terminal newline. The Pi
write tool wrote the supplied bytes; it did not strip a newline. The second
write therefore did not change the draft. The later Python shell mutation
made the normalized text equal to that payload plus one newline, while Windows
text-mode output converted all LF endings to CRLF.

The task preamble supplied the exact correct command
`python ../control/visible_check.py .`. Qwen's first two invocations did not
copy it. These are model action-selection errors, not missing host information.

## Where the semantic defects arose

All three task artifacts were acquired before construction. The first write
already contains every final semantic omission:

- no Abstract confidence interval;
- no explicit Abstract nonrandomized/noncausal limitation; and
- no not-prespecified subgroup statement.

The remaining 17 assistant calls were entirely about checker invocation,
protected References, the terminal newline, and final confirmation. The
second write reused the first draft byte-for-byte. The final full-paper reread
did not lead to another change.

This rules out missing task/source availability, source-version selection,
context pressure, truncation, protocol degeneration, or stale-candidate
submission as explanations for this specific draft. It supports a narrower
description:

> Under both tested ecologies, Qwen acquired the exact operands and then
> serialized one monolithic revision that dropped different explicit
> relations. Once the visible mechanical boundary passed, no semantic
> reconsideration occurred.

## Verbatim-preservation measurement defect

The visible checker reported protected Background, Methods, and References as
passing after the newline mutation. Its implementation reads the whole paper
with Python `read_text()` and compares decoded strings. Universal-newline
decoding converts CRLF to LF, so its “protected material” predicate does not
establish byte identity.

Raw custody shows:

| Paper | LF-only endings | CRLF endings |
|---|---:|---:|
| Initial fixture | 39 | 0 |
| Historical schema-action final | 39 | 0 |
| Native Pi final | 0 | 39 |

All three protected section byte comparisons are false in the native final.
The source records remained exact and only `paper.md` changed. The frozen
checker and receipts are not rewritten; the investigator rubric records
preservation as partial.

For future fixtures, a claim of verbatim protected material must use raw-byte
spans or precommitted byte hashes. Text-normalized comparison can remain useful
only if labeled as text equality.

## Quantitative record

| Measure | Historical schema action | Native Pi |
|---|---:|---:|
| Assistant/model calls | 7 | 26 |
| Tool/admitted actions | 7 | 25 |
| Read calls | 3 | 6 |
| Patch / write calls | 1 | 0 / 2 |
| Shell calls | 0 | 17 |
| Visible-check invocations | 1 | 6 |
| Parsed visible receipts, fail/pass | 0 / 1 | 3 / 1 |
| Tool errors | 0 | 6 |
| Prompt tokens across calls | 19,179 | 153,757 |
| Completion tokens | 1,152 | 2,677 |
| Total tokens across calls | 20,331 | 156,434 |
| Record/run wall time | 63.745 s | 150.853 s |

Native Pi used 7.694 times the cumulative tokens and 2.366 times the wall
time. The methods have different harnesses and tool semantics, so these are
descriptive costs, not isolated effects. Prompt totals count the growing
history on every call.

Native Pi made 25 linked tool calls: 17 bash, 6 read, and 2 write. Six tool
results were errors: two malformed checker invocations, three ordinary failed
checker receipts, and one unavailable `python3` command. It made one shell
mutation. The final paper is 2,231 bytes; its first/second write body was 2,191
bytes before newline conversion.

## Interpretation

Changing the full ecology altered semantic discrimination: it fixed the hard
response/nonresponse complement relation that schema action missed. It did not
increase task completion because other explicit relations fell out of the
same monolithic draft. More flexibility also created a new byte-custody defect
and substantial mechanical wandering.

This reinforces three earlier lessons without collapsing them into “methods
do not matter”:

1. the frame and action ecology materially affect which errors Qwen makes;
2. ordinary flexibility is not monotonic improvement; and
3. passive closure truth is downstream of the observed loss, which occurs
   during construction.

## Decision and next specific method

Do not promote native Pi and do not return to closure cards, task repetition,
semantic self-audits, or submission gates on this case.

The next distinct calibration changes the **construction unit**, not the
information supply. Use a removable artifact-native interface with exact
reads plus one mechanical operation:

```text
replace_section(
  section_id,
  expected_section_sha256,
  new_body
)
```

The allowed section IDs are mechanically declared by the task adapter from
the three editable headings: Abstract, Results, and Discussion. The host owns
exact section boundaries, hashes, candidate succession, checks, and receipts.
It does not supply claim checklists, evidence relevance, semantic status, or
recommended actions. The model chooses section order, source reads, content,
checking, and termination.

This tests whether aligning action granularity with the artifact's explicit
revision structure changes what survives construction. It is neither another
factual display nor a forced Discover/Construct/Evaluate sequence. Run it first
on this known case as calibration; only a clearly better paper earns a fresh
polarity-bearing prospective comparison.

## Local validation

- prospective qualification passes;
- the analyzer verifies every declared prompt, provider, protocol, source,
  action/result, candidate, machine-grade, semantic-grade, and historical
  comparison invariant;
- focused Ruff and Python compilation pass;
- `python -m unittest discover -s tests -q`: 248 passed, 14 intentionally
  skipped;
- `python -m pytest -q`: 270 passed, 14 intentionally skipped; and
- no GitHub Actions claim is made.
