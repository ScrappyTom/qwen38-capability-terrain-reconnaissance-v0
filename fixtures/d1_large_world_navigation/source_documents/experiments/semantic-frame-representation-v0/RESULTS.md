# Semantic Frame Representation v0 — results

## Outcome

The experiment produced a positive **semantic-content lead** and a negative
**structure-specific** result.

- `evidence_only`: 2 pass / 4 partial / 0 fail; 12/22 required-content items.
- `prose_frame`: 4 pass / 2 partial / 0 fail; 20/22 items.
- `structured_frame`: 5 pass / 1 partial / 0 fail; 21/22 items.

All 18 calls were admitted. All three conditions preserved the exact no-op and
got the central direction right in all three counterfactual pairs. Under the
stricter frozen pair guards, evidence-only passed 1/3 and each framed condition
passed 2/3 because the missingness pair required both the positive direction
and an explicit rejection of the opposite direction.

Both frames met the frozen rule for a **lead only**: prose improved two unit
grades over evidence-only with no regression, and structure improved three.
Neither passed 6/6 or all three strict pair guards, so neither fully qualifies
and recomposition remains unauthorized.

The structured form improved only U003 over content-equivalent prose, tied it
on the other five units, and finished below 6/6. It therefore failed the
frozen structure-specific promotion rule. Typed JSON is not earned over the
smaller prose form by this run.

## What was actually compared

Every call received the same system prompt, editorial task, exact current
unit, content-addressed basis version, exact bound evidence record, normalized
binding, response schema, model profile, and one-step responsibility boundary.

Only `semantic_frame` differed:

- `null` in evidence-only;
- a deterministic prose rendering of the task-author payload; or
- the same payload as a JSON object.

The saved experiment records that parsing each prose frame reconstructs its
structured payload exactly. The frame repeated and organized facts already in
the task and evidence; it did not add empirical evidence. It did add a local,
itemized statement of what content the action needed to retain. Consequently,
the evidence-only comparison identifies the effect of that explicit semantic
frame as a bundle of selection, repetition, organization, and obligation
salience. It does not isolate those four ingredients from one another.

This was not a persistence experiment. The model did not author a state,
nothing crossed a destructive context boundary, and no retrieval behavior was
available.

## Direct request, response, and artifact review

The investigator inspected all 18 exact saved requests, raw responses,
admitted results, and before/after versions after exact replay succeeded.

### Evidence-only

- U001 retained random assignment, prespecified intention-to-treat status, and
  every exact statistic, but did not explicitly say that causal attribution
  was supported: partial, 2/3 items.
- U002 included the nonrandom adoption basis, adjusted observational estimate,
  causal limitation, and residual confounding: pass, 4/4.
- U003 changed the central direction from attenuation to exaggeration but
  compressed the record to `likely exaggerated`. It omitted both coverage
  rates, lowest-score nonresponse, the mean-shift mechanism, `can`, and the
  explicit non-attenuation relation: partial, 0/4.
- U004 left the short initial `likely attenuated` line byte-for-byte unchanged.
  Its central direction was right, but it omitted the same four required
  content groups and strengthened `can`: partial, 0/4.
- U005 preserved the accurate measured result byte-for-byte: pass, 4/4.
- U006 removed the invented adherence estimate and stated the measurement
  limitation, but omitted the scheduling, completed-visit, and referral fields
  that the records did measure: partial, 2/3.

The evidence-only failures were therefore not polarity blindness. Qwen found
the central direction in all three matched pairs, but compressed away
secondary relations and an exact modality.

### Prose semantic frame

U001, U002, U005, and U006 passed. U003 and U004 each included coverage,
which patients were missing, how omission shifted the observed mean, and the
correct `can` direction. Both nevertheless omitted the explicit negative half
of the relation: U003 did not say `does not attenuate`, and U004 did not say
`does not exaggerate`. Result: 4/6 units and 20/22 items.

### Structured semantic frame

U001, U002, U003, U005, and U006 passed. U003 expressed the complete contrast
as `can exaggerate ... rather than attenuate it`. U004 still omitted `does not
exaggerate`, despite that item being present in the exact structured frame.
Result: 5/6 units and 21/22 items.

Prose and structured outputs were byte-identical on U001, U002, U005, and
U006. They differed only on the missingness pair. Structure completed U003 but
not its counterfactual U004. One one-unit difference from one deterministic
call per cell is not evidence that typing generally improves action.

## Frozen adjudication

| Unit | Evidence only | Prose frame | Structured frame | Deciding observation |
|---|---:|---:|---:|---|
| U001 randomized | partial (2/3) | pass (3/3) | pass (3/3) | Frame made causal support explicit. |
| U002 observational | pass (4/4) | pass (4/4) | pass (4/4) | Evidence alone was sufficient. |
| U003 low-score nonresponse | partial (0/4) | partial (3/4) | pass (4/4) | Frames prevented gist compression; only structure retained the negative contrast. |
| U004 high-score nonresponse | partial (0/4) | partial (3/4) | partial (3/4) | Both frames still lost `does not exaggerate`. |
| U005 measured no-op | pass (4/4) | pass (4/4) | pass (4/4) | All arms preserved exact bytes. |
| U006 unmeasured adherence | partial (2/3) | pass (3/3) | pass (3/3) | Frames retained the measured operations fields. |
| **Total** | **2 pass; 12/22** | **4 pass; 20/22** | **5 pass; 21/22** | — |

The complete item-level judgments and notes are preserved in
`ADJUDICATION.json`.

## Metrics

| Metric | Evidence only | Prose frame | Structured frame |
|---|---:|---:|---:|
| attempted calls | 6 | 6 | 6 |
| admitted calls | 6 | 6 | 6 |
| rejected calls | 0 | 0 | 0 |
| prompt tokens | 4,998 | 6,229 | 6,551 |
| cached tokens | 2,187 | 2,474 | 3,323 |
| completion tokens | 854 | 986 | 983 |
| reasoning tokens | 0 | 0 | 0 |
| total tokens | 5,852 | 7,215 | 7,534 |
| summed HTTP duration | 47,285 ms | 54,226 ms | 53,705 ms |
| passing units | 2/6 | 4/6 | 5/6 |
| required items | 12/22 | 20/22 | 21/22 |
| strict pair guards | 1/3 | 2/3 | 2/3 |
| central pair directions | 3/3 | 3/3 | 3/3 |
| exact no-ops | 1/1 | 1/1 | 1/1 |

Relative to evidence-only, prose used 1,363 more total tokens (+23.29%) and
structure used 1,682 more (+28.74%). Structure used 319 more total tokens than
prose (+4.42%). Prompt-token increases were +24.63% for prose and +31.07% for
structure relative to evidence-only. Summed HTTP duration increased 14.68% for
prose and 13.58% for structure. These are descriptive costs from one fixed
schedule; cache reuse varied with interleaving and is reported rather than
treated as an independent latency experiment.

Across all arms the run used 20,601 total tokens: 17,778 prompt, 2,823
completion, 7,984 reported cached, and zero reasoning tokens. Summed HTTP
duration was 155,216 ms.

## Interpretation

This result supports a narrower and more useful statement than either “truth
is enough” or “structured memory works”:

> When exact evidence was already present, an explicit local statement of the
> relations and content that had to survive construction substantially reduced
> secondary-detail loss on this six-unit fixture.

The evidence-only model was not generally unaware of the deciding facts. It
selected the correct central polarity in every pair. Its weakness was turning
the complete record and generic task into an exhaustive final claim. The
semantic frames attacked that upstream transformation directly and recovered
eight or nine of the ten item satisfactions missing from evidence-only.

But explicit state was still not authoritative action. The structured arm saw
the exact U004 negative contrast and omitted it. That is the same boundary the
project has repeatedly observed: representing a relation can improve its
chance of survival without guaranteeing execution.

The result also rejects a common architectural shortcut. Because prose carried
the same payload and produced four byte-identical outputs plus nearly the same
grade, JSON typing itself did not create the gain. If this lead transfers, the
project should preserve semantic-content ownership and evidence binding as the
question while keeping the serialization replaceable.

## Decision and next boundary

- Retain the stable custody harness unchanged.
- Preserve both semantic frames as experimental artifacts only.
- Do not promote structured state over prose.
- Do not recompose these incomplete local outputs.
- Do not tune U004 or add an explicit enforcement gate.

The next earned step is one fresh prospective replication of the semantic-
content effect with a smaller comparison: evidence-only versus the cheaper
content-equivalent prose frame. It should use new matched worlds and the same
strict negative-relation/no-op guards. If that effect transfers, then a
destructive-boundary experiment can separately test authoring and restoration:
first compare task-author oracle state with retrieval-only, and only afterward
ask whether Qwen can create a useful state itself. Starting with a five-arm
memory system now would mix a promising content effect with unqualified state
capture and persistence mechanisms.

## Limitations

- Six synthetic units and one temperature-zero call per cell do not estimate a
  population success rate or run-to-run variance.
- The semantic payload was task-author oracle content, not model-authored
  memory.
- Evidence-only versus frame combines repetition, local selection,
  organization, and obligation salience.
- The model did no discovery, retrieval, multi-action work, recomposition, or
  post-reset continuation.
- More tokens accompanied the framed inputs, so the run establishes a
  treatment effect for the complete frame, not a token-normalized mechanism.

## Evidence location

The immutable run is
`runs/semantic-frame-representation-v0-run-001/`. It contains the endpoint
snapshot, copied model profile and fixture, experiment hashes, canonical
semantic payloads, all exact request/response/HTTP/result/transition records,
condition manifests, dispatch order, and summary. `verify.py` reconstructs all
requests, admissions, transitions, manifests, usage, and identities exactly.

## Validation

- endpoint health and properties snapshots completed with no recorded errors;
- exact replay verified all 18 requests, responses, admissions, transitions,
  manifests, usage totals, fixture/profile copies, and frozen hashes;
- all 11 experiment-specific tests passed with the saved-run replay enabled;
- the complete local suite ran 441 tests: 427 passed and 14 archived-
  continuation tests were intentionally skipped; and
- `git diff --check` passed.

This is local validation, not GitHub Actions verification.
