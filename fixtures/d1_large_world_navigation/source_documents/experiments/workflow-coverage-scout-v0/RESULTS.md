# Workflow coverage scout results

Run: `r1`

Status: **exploratory scout complete; basic code/research workflow cells now
covered at bounded local scale; no harness intervention promoted**

## Question

Before drilling further into one failure boundary, what happens when the
unchanged ordinary custody loop is used for the four under-covered prime
workflows: code feature revision, code diagnosis/repair from symptoms,
research creation from a blank artifact, and research correction after
mixed-validity critique?

This is a coverage scout, not a package ranking or causal comparison. It uses
one trajectory per package/task cell.

## Conditions

| Package | Model allocation | Context / KV | MTP |
|---|---|---|---|
| AD | Qwen3.8-27B AD-IQ2_S, full 66/66 offload | 25,088 / q8 | off |
| UD | Qwen3.8-27B UD-IQ2_XXS, full 66/66 offload | 50,176 / q4 | depth 3 |

Both use the same nonthinking sampler, stable schema-action ordinary loop,
tools, 4,096-token response allowance, and 24-call ceiling. No card, reviewer,
audit feed, semantic transform, plan, retry repair, or host coaching is added.

## Outcomes

| Workflow | AD | UD | Direct interpretation |
|---|---:|---:|---|
| Code feature revision | 12/12 executable predicates | 12/12 | complete in both |
| Code symptom-led repair | 12/12 executable predicates | 12/12 | complete in both; identical terminal implementation |
| Blank research memo | 14 met, 1 partial, 1 not of 16 | 14 met, 1 partial, 1 not of 16 | broadly complete; one different over-interpretation each |
| Mixed-validity research correction | 18/18 semantic criteria | 18/18 | complete in both; frozen mechanical failure was false |

The semantic counts are direct investigator review against the frozen rubrics,
not automated lexical grades. Exact judgments and their boundaries are in
`DIRECT_TRANSCRIPT_AUDIT.md`.

## Workflow and cost

| Run | Calls | Prompt tokens | Completion tokens | Total tokens |
|---|---:|---:|---:|---:|
| AD catalog | 7 | 15,606 | 757 | 16,363 |
| AD retry | 9 | 21,762 | 584 | 22,346 |
| AD harbor | 10 | 30,582 | 1,544 | 32,126 |
| AD water | 16 | 74,206 | 2,335 | 76,541 |
| UD catalog | 7 | 15,608 | 757 | 16,365 |
| UD retry | 7 | 15,791 | 787 | 16,578 |
| UD harbor | 10 | 30,814 | 1,599 | 32,413 |
| UD water | 13 | 47,654 | 1,446 | 49,100 |

AD used 42 calls and 147,376 total tokens. UD used 37 calls and 114,456 total
tokens. The package-level cost difference mixes hardware speed with different
action paths and is descriptive, not a controlled efficiency effect.

Corrected runtime reduction gives 18.81 weighted decode tokens/s for AD and
33.60 for UD MTP3. UD generated 3,966 draft tokens and accepted 3,263 (82.27%).
The raw UD runtime record's zero timing fields are a reducer defect documented
in `CUSTODY_CORRECTIONS.md`.

## What was learned

### 1. The earlier failure model was too broad

“All requirements are available, Qwen compresses them to a gist, independent
distinctions disappear” remains a real phenotype in prior construction tasks.
It is not a general description of every creation, revision, or repair
workflow. Here, both code tasks were fully correct, and the itemized mixed-
critique research workflow was fully correct under direct review.

### 2. The effective unit is workflow ecology, not domain alone

The successful code revision reused a correct value model that already owned
validation. The successful debug task had symptoms, a discoverable local
contract, and one clear state-owning implementation. The successful research
correction had six explicit review claims and a corresponding response
structure. Those decision environments made independent requirements easier
to keep operational without any host semantic layer.

### 3. Research creation still exposed a useful boundary

Both memo writers acquired every source and preserved almost all distinctions.
Their mistakes came at interpretation-to-recommendation binding: AD proposed
reuse of a potentially biased complete-record analysis; UD promoted a possible
bias direction into a definite upper-bound claim. The next relevant research
question is not whether the source was present. It is how a model preserves
epistemic limits while turning evidence into a decision artifact.

### 4. A task-authored review frame can outperform an undifferentiated request

The Q1-Q6 structure is effectively a natural decomposition: each external
claim remains separately addressable, while the full report and all evidence
remain available. Both actors correctly accepted supported criticism and
rejected confident false criticism. This suggests a useful user/workflow
pattern, not an earned automatic host intervention.

### 5. Bad checks can be more damaging than missing checks

The water checker contradicted the written task and template. It made two
correct artifacts appear mechanically failed and induced wasted work. The
project must continue to audit checks against the literal contract and direct
artifact, not merely trust `passed:false`.

## Decision

- Keep the stable ordinary harness unchanged.
- Do not promote a card, semantic transform, reviewer, audit feed, or routing
  policy from this scout.
- Retain AD/q8/25K MTP-off as the bounded quality-oriented package and UD/q4/
  50K MTP3 as the optional speed/long-context package. This scout does not
  establish a package-quality difference.
- Treat the basic create/revise/address-errors matrix as covered only at small
  local scale.
- Before another microfactorial, explore one larger authentic code ecology and
  one larger authentic research ecology. The purpose should be to locate where
  the strong ordinary-loop behavior here breaks as dependencies, source
  competition, and iteration increase.

No rerun is warranted for either corrected apparatus label. The exact
trajectories and artifacts are already sufficient to distinguish model
behavior from the two reducer/checker defects.
