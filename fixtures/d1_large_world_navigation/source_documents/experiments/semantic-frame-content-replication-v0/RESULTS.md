# Semantic Frame Content Replication v0 — results

## Outcome

The semantic-content effect **met every frozen replication threshold**.

- `evidence_only`: 3 pass / 3 partial / 0 fail; 13/22 required items.
- `prose_frame`: 5 pass / 1 partial / 0 fail; 21/22 items.
- prose improved U001 and U003, regressed no unit, and added eight items.
- both conditions preserved the exact no-op and selected all three central pair
  directions correctly.

All 12 calls were admitted and exact replay passed. The prose arm therefore
met every replication criterion: six admissions, no regression, at least two
better unit grades, at least four additional items, exact no-op preservation,
and no central-polarity loss.

It did not qualify as a complete local method. U004 again omitted the explicit
negative half of the missingness relation (`does not exaggerate`), leaving
prose at 5/6 units, 21/22 items, and 2/3 strict pair guards rather than the
required 6/6, 22/22, and 3/3.

## Direct input, output, and artifact review

The investigator inspected every exact saved request, evidence record,
semantic frame, raw response, admitted result, and before/after version after
the verifier reconstructed the run.

### Evidence-only

- U001 disclosed random assignment, prespecified intention-to-treat analysis,
  and every exact statistic but did not explicitly characterize causal support:
  partial, 2/3.
- U002 carried the manager-selection basis, nonrandom design, adjusted
  association, causal limitation, and residual confounding: pass, 4/4.
- U003 changed the central direction from attenuation to exaggeration but
  reduced the entire record to `likely exaggerated`. It omitted coverage,
  low-score nonresponse, the mean shift, `can`, and explicit non-attenuation:
  partial, 0/4.
- U004 preserved the short `likely attenuated` claim unchanged. Its direction
  was right, but all four detailed requirements were absent: partial, 0/4.
- U005 preserved the accurate measured result byte-for-byte: pass, 4/4.
- U006 removed the fabricated result and retained every measured-field and
  measurement-limitation fact without a frame: pass, 3/3.

As in the first fixture, evidence-only was not blind to the deciding polarity.
It found all three central directions and failed mainly by compressing away
secondary relationships and exact modality.

### Prose frame

- U001 made causal support explicit and passed 3/3.
- U002 passed 4/4.
- U003 formed one complete causal chain: differential coverage, low-score
  nonresponse, its effect on the outreach mean, `can exaggerate`, and `rather
  than attenuate`. It passed 4/4.
- U004 similarly retained coverage, high-score nonresponse, the lowering of
  the outreach mean, and `can attenuate`, but again omitted `does not
  exaggerate`. It remained partial at 3/4.
- U005 was byte-identical to the input and passed 4/4.
- U006 passed 3/3.

In U003 and U004 the subject `nonresponse` followed the differential coverage
clause and was linked directly to a change in the outreach-practice mean. The
frozen group-specific relation was therefore present even though the noun was
not repeated before `nonresponse`. The only missing prose item was U004's
explicit rejection of the opposite direction.

## Frozen adjudication

| Unit | Evidence only | Prose frame | Change |
|---|---:|---:|---|
| U001 randomized | partial (2/3) | pass (3/3) | explicit causal support restored |
| U002 observational | pass (4/4) | pass (4/4) | no grade change |
| U003 low-score nonresponse | partial (0/4) | pass (4/4) | complete relation restored |
| U004 high-score nonresponse | partial (0/4) | partial (3/4) | three items restored; negative contrast still absent |
| U005 measured no-op | pass (4/4) | pass (4/4) | exact in both |
| U006 unmeasured outcome | pass (3/3) | pass (3/3) | complete in both |
| **Total** | **3 pass; 13/22** | **5 pass; 21/22** | **+2 pass; +8 items; 0 regressions** |

Strict pair guards improved from 1/3 to 2/3. Central pair direction remained
3/3 in both conditions. The full item judgments are in `ADJUDICATION.json`.

## Metrics

| Metric | Evidence only | Prose frame |
|---|---:|---:|
| attempted calls | 6 | 6 |
| admitted calls | 6 | 6 |
| rejected calls | 0 | 0 |
| prompt tokens | 5,054 | 6,334 |
| cached tokens | 2,911 | 2,318 |
| completion tokens | 870 | 1,020 |
| reasoning tokens | 0 | 0 |
| total tokens | 5,924 | 7,354 |
| summed HTTP duration | 46,450 ms | 55,774 ms |
| passing units | 3/6 | 5/6 |
| satisfied items | 13/22 | 21/22 |
| strict pair guards | 1/3 | 2/3 |
| central pair directions | 3/3 | 3/3 |
| exact no-ops | 1/1 | 1/1 |

Prose used 1,430 additional total tokens (+24.14%), 1,280 additional prompt
tokens (+25.33%), and 150 additional completion tokens (+17.24%). Summed HTTP
duration was 9,324 ms higher (+20.07%). Cache reuse varied with the frozen
interleaving, so these are descriptive costs rather than a latency estimate.

The complete run used 13,278 total tokens: 11,388 prompt, 1,890 completion,
5,229 reported cached, and zero reasoning tokens. Summed HTTP duration was
102,224 ms.

## Cross-fixture evidence

The prospective screen and this replication now show the same prose effect on
two different six-unit fixtures:

| Combined descriptive measure | Evidence only | Prose frame |
|---|---:|---:|
| passing units | 5/12 | 9/12 |
| satisfied items | 25/44 | 41/44 |
| central pair directions | 6/6 | 6/6 |
| exact no-ops | 2/2 | 2/2 |
| total tokens | 11,776 | 14,569 |

Across the two fixtures, prose added four passing units and sixteen satisfied
items with no unit regression, while using 2,793 more total tokens (+23.72%).
These are paired descriptive totals, not a success-rate estimate.

The repeated error is equally important. In both fixtures prose omitted the
explicit negative contrast from the high-score/attenuation unit. The frame is
helpful but not an enforcement surface, and visible itemization does not make
every item survive construction.

## Interpretation

The result strengthens the prior mechanism claim:

> Qwen had the evidence and recovered the central polarity without help, but a
> concise task-author rendering of the local relationships substantially
> improved how much of that evidence survived into the action.

This is not merely the structured-state hypothesis in weaker form. Typed JSON
was already stopped; the effect transferred using prose. What replicated is
the value of an upstream, local semantic preparation artifact—a bundle of
selection, repetition, organization, and obligation salience—not a particular
serialization.

The result still does not establish that Qwen can create this state, maintain
it, or restore it after a destructive boundary. The task author supplied the
correct content. Custody verified identities and bytes, not semantic truth.

## Decision

- The prose semantic-content effect is prospectively replicated.
- Prose remains an experimental treatment, not a default harness view, because
  it is still incomplete at 5/6 and 21/22.
- Structured state remains unearned.
- Recomposition remains unauthorized.
- Do not tune the repeated U004 omission or add a semantic enforcement gate.
- The evidence now earns a destructive-boundary study in which this
  task-author prose payload is the oracle arm and model-authored capture is a
  separate treatment. Exact retrieval must remain available to every arm.

The next study must not attribute oracle content to the host as machine-derived
truth. It should first determine whether a model-authored summary or generic
semantic artifact captures content comparable to the qualified oracle, then
use fresh inference to test downstream restoration and action. Capture quality
and downstream use must be scored separately.

## Limitations

- Six new synthetic units and one temperature-zero call per cell do not
  estimate run-to-run variance or population performance.
- The semantic classes matched the prior fixture; this is replication across
  new facts and prose, not transfer to another task class or domain.
- Evidence-only versus prose still combines repetition, selection,
  organization, obligation salience, and added tokens.
- The state was task-author oracle content; the model did not author it.
- No context reset, retrieval choice, multi-action work, or recomposition was
  tested.

## Evidence and validation

The immutable evidence is under
`runs/semantic-frame-content-replication-v0-run-001/`: copied inputs and
profile, endpoint snapshots, frozen hashes, canonical payloads, all 12 exact
requests and raw responses, HTTP receipts, admitted results, transitions,
condition manifests, dispatch, and summary.

Exact replay verified the requests, responses, admissions, transitions,
manifests, usage, fixtures, profile, base apparatus, and frozen identities.
All 11 experiment tests pass with replay enabled. The complete local suite ran
452 tests: 438 passed and 14 archived-continuation tests were intentionally
skipped. Git whitespace validation passed. This is local validation, not
GitHub Actions verification.
