# Information-enrichment crossover v0 - result

Date: 2026-08-13

Status: **mechanically complete; formal crossover ineligible after the final
pooled blind review failed to reconfirm the synthesis baseline state; no
selector or view is promoted**.

## Bottom line

The intended quality-profile claim cannot be made. The screen initially
qualified six citation worlds and five synthesis worlds, but the independent
condition-blind review of all 44 measured artifacts found genuine unsupported
or over-strengthened meaning in every saved synthesis baseline. Under the same
frozen eligibility rule, the six citation baselines remained eligible and
**0/5 synthesis baselines remained eligible**.

The complete factorial remains useful descriptively:

- deterministic line addresses changed exact smallest-line citations from
  **9/18 to 18/18** in the citation family;
- task-author semantic coverage changed synthesis secondary coverage from
  **54/70 to 68/70 points**, central-criterion passes from **2/5 to 5/5**, and
  semantic unsupported entries from **6 to 1**;
- the predicted family crossover appeared descriptively: V10 beat V01 in
  citation quality, while V01 beat V10 in synthesis quality; but
- the universal combined view V11 matched each specialized benefit and beat
  the frozen selector on quality: **0.000 versus 0.091 mean regret**, with
  **1 versus 2 hard-gate failures**.

Thus the measured data do not support an adaptive information-profile
controller. If these small task-author enrichments were available at no other
cost, always showing both was better than routing. V11 required 18.62% more
prompt tokens and 15.94% more total tokens than the selector, but the selector
did not meet the frozen quality-equivalence tolerance, so no efficiency
profile passed either.

## Question and frozen design

The study asked a conditional question:

> Given a held-out task already shown to occupy one of two calibrated failure
> states, does a frozen state-conditioned enrichment beat every universal
> always-use-one-view policy?

The two factors were crossed on every eligible world:

| View | Deterministic line addresses | Task-author semantic coverage |
|---|---|---|
| V00 exact source | no | no |
| V10 addressed source | yes | no |
| V01 coverage transform | no | yes |
| V11 addressed + coverage | yes | yes |

Every condition retained byte-identical authoritative source and current
target. V10 and V11 shared the exact same line map. V01 and V11 shared the
exact same semantic clauses. Coverage clauses contained no source addresses or
evidence bindings. Retrieval, tools, retries, feedback, model-authored state,
and mutation choice were absent.

The frozen selector chose V10 for citation-boundary tasks and V01 for compact
many-to-one synthesis. It was compared with always V00, V10, V01, and V11.

## Execution

- Untreated screen calls: **12/12 admitted**.
- Fresh crossover treatment calls: **33/33 admitted**.
- Measured cells: **44** (eleven saved V00 baselines plus 33 treatments).
- Repairs, retries, tool calls, and feedback turns: **0**.
- Measured output-contract passes: **44/44**.
- Thinking/reasoning tokens: **0**.
- Exact saved-run replay: **passed**, including all eleven copied baselines.
- Focused experiment tests after the custody correction: **16/16 passed**.

The complete 45-call execution, including the screened-out irrigation world,
used 36,027 prompt tokens, 9,267 completion tokens, and 45,294 total tokens,
with 4,224 cached tokens. Summed endpoint duration was 523,693 ms.

The 44 measured cells used 35,487 prompt tokens, 8,989 completion tokens, and
44,476 total tokens.

## Review and custody correction

An independent reviewer scored all 44 artifacts using opaque packet IDs before
opening the condition mapping:

- semantic judgments: **304**;
- `met`: **255**;
- `partial`: **26**;
- `not_met`: **23**;
- low-confidence decision-changing judgments: **0**.

The first reduction exposed a taxonomy problem. The reviewer had placed 18
correct facts with wrong citation coordinates in the generic
`unsupported_or_contradictory_content` list. That would zero the citation cell
both through the provenance criterion and through the semantic hard gate.

The original sealed review was not edited. Still blind to conditions, the
reviewer classified every one of its 29 entries in a separate sealed
adjudication:

- **18 provenance-only coordinate errors**; and
- **11 genuine semantic unsupported/contradictory claims**.

The reducer now validates exact multiset coverage of that adjudication, counts
only the latter against the semantic hard gate, and records the hashes of the
post-run reducer, review validator, and adjudication. This is a custody
correction, not a treatment or semantic repair.

The correction also exposed a more consequential problem: the original screen
review and the final pooled blind review disagreed about whether the synthesis
baselines contained unsupported meaning. The final reviewer identified:

- causal wording for a selected linked subset in `MS-VACCINE` and
  `MS-OVERDUE`; and
- categorical attenuation wording where the source required `can` modality in
  `MS-TUTOR`, `MS-NOISE`, and `MS-ERGONOMIC`.

Three of those disagreements also changed the central criterion from `met` to
`partial`. The final pooled review therefore reconfirmed **6/6 citation** but
**0/5 synthesis** baseline states. The preregistered two-family causal
comparison is ineligible.

## Descriptive family results

These tables preserve the complete measured behavior. They do not revive the
failed eligibility gate.

### Citation-boundary family

| View | Exact citations | Hard-gate passes | Mean quality | Artifact words |
|---|---:|---:|---:|---:|
| V00 exact source | 9/18 | 6/6 | 0.500 | 106 |
| V10 addressed source | 18/18 | 5/6 | 0.833 | 110 |
| V01 coverage transform | 9/18 | 6/6 | 0.500 | 137 |
| V11 addressed + coverage | 18/18 | 6/6 | 1.000 | 137 |

Addressability perfectly repaired the narrow coordinate error in both V10 and
V11. It did not guarantee factual completeness by itself: V10's harbor answer
said `Three container ships` but omitted the requested `waiting at 07:00`, so
its semantic gate failed. V11 retained that content. Semantic coverage without
addresses left citation accuracy unchanged at 9/18; in the library world it
even emitted three nonconforming `[DOCUMENT:...]` references.

### Compact many-to-one family

| View | Secondary points | Central passes | Semantic unsupported | Hard-gate passes | Mean quality |
|---|---:|---:|---:|---:|---:|
| V00 exact source | 54/70 | 2/5 | 6 | 0/5 | 0.000 |
| V10 addressed source | 59/70 | 4/5 | 3 | 3/5 | 0.543 |
| V01 coverage transform | 68/70 | 5/5 | 1 | 4/5 | 0.800 |
| V11 addressed + coverage | 68/70 | 5/5 | 1 | 4/5 | 0.800 |

Coverage decomposition was the important descriptive factor in these compact
syntheses. V01 and V11 were identical on aggregate semantic scoring. The one
shared failure was `MS-OVERDUE`, where both said that branches “randomized
patrons,” changing the unit of randomization. Line addresses added no measured
synthesis benefit beyond coverage.

## Policy comparison

Quality is family-normalized per world. Oracle quality is the best of the four
views for that world. A hard-gate failure has quality zero.

| Policy | Mean quality | Mean regret | Hard-gate failures | Prompt tokens | Total tokens |
|---|---:|---:|---:|---:|---:|
| Always V00 | 0.273 | 0.636 | 5 | 5,764 | 7,906 |
| Always V01 | 0.636 | 0.273 | 1 | 8,165 | 10,504 |
| Always V10 | 0.701 | 0.208 | 3 | 9,574 | 11,741 |
| Always V11 | **0.909** | **0.000** | **1** | 11,984 | 14,325 |
| Frozen state-conditioned selector | 0.818 | 0.091 | 2 | 9,752 | 12,042 |

The family means did show the predicted descriptive crossover:

- citation: V10 0.833 > V01 0.500;
- synthesis: V01 0.800 > V10 0.543.

But routing did not beat the union. V11 achieved each specialized benefit,
and the selector missed the harbor content that V11 preserved. Both the frozen
quality-profile gate and the separate efficiency-profile gate are `false`.

## Interpretation

1. **The smallest-line addressability effect is real and narrow.** A literal
   deterministic line map repaired all 18 citation boundaries. This supports
   exact addressing for tasks that explicitly require smallest-line
   coordinates; it does not establish general provenance or a default view.

2. **External semantic decomposition remains a strong oracle control.** It
   substantially improved compact synthesis coverage and modality. It is
   task-author semantic content, not machine custody, and therefore cannot be
   promoted as host inference.

3. **The two enrichments were complementary, not usefully routable here.** The
   task-state labels predicted which single factor mattered, but always
   combining the factors dominated the selector on quality. That is evidence
   against an adaptive controller for these small worlds, not evidence for it.

4. **Qualification policy was the real failure.** One permissive screen review
   admitted artifacts that a later independent blind review found contained
   overclaims. A conditional treatment experiment needs the same semantic
   policy at selection and scoring, or an independent baseline adjudication
   before treatments are authorized.

5. **No stable harness change is earned.** The exact workbench, custody,
   transport, and ordinary action loop remain unchanged. The line map,
   semantic coverage, blind-review apparatus, and reducer all remain removable
   experiment code.

## Decision

- Promote no information-profile selector, router, card, semantic host field,
  or default combined view.
- Retain deterministic line addressability as a narrow experimental primitive
  for explicit coordinate tasks.
- Retain task-author coverage as an oracle semantic-transform control, not a
  deployable host capability.
- Do not spend another run on V00/V10/V01/V11 formatting. The union already
  answers the architectural routing question for this bounded setup.
- Any future conditional screen must resolve decision-changing semantic
  disagreements before treatment calls, while keeping semantic review outside
  machine custody logic.

## Evidence

- Freeze: [`FREEZE.md`](FREEZE.md)
- Screen result: [`SCREEN_RESULTS.md`](SCREEN_RESULTS.md)
- Direct request/output audit: [`AUDIT.md`](AUDIT.md)
- Frozen protocol: [`PROTOCOL.md`](PROTOCOL.md)
- Exact crossover summary:
  [`runs/information-enrichment-crossover-v0-run-001/summary.json`](runs/information-enrichment-crossover-v0-run-001/summary.json)
- Original sealed blind review:
  [`runs/information-enrichment-crossover-v0-run-001/blind/semantic-reviews.sealed.json`](runs/information-enrichment-crossover-v0-run-001/blind/semantic-reviews.sealed.json)
- Blind adjudication overlay:
  [`runs/information-enrichment-crossover-v0-run-001/blind/review-adjudication.sealed.json`](runs/information-enrichment-crossover-v0-run-001/blind/review-adjudication.sealed.json)
- Corrected reduction:
  [`runs/information-enrichment-crossover-v0-run-001/analysis.json`](runs/information-enrichment-crossover-v0-run-001/analysis.json)
- Replay verification:
  [`runs/information-enrichment-crossover-v0-run-001/verification.json`](runs/information-enrichment-crossover-v0-run-001/verification.json)
