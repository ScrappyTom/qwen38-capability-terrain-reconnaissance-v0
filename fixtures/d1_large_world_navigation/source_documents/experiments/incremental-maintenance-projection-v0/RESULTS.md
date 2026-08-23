# Incremental maintenance projection v0 results

Status: **complete; structural selection lead observed, projected method did
not complete and is not promoted**

## Result

Exact basis, source-delta metadata, and mechanically defined structural
regions materially changed Qwen3.8's acquisition strategy on the authentic
large-document maintenance task. The projected actor read 25.0% of the target
bytes and six of 33 regions; the ordinary actor reconstructed the complete
51.7-KB target.

That did not produce a successful working set. The complete region registry
added 8,401 tokens to the first prompt and remained resident in every later
request. After deeper source acquisition, the projected actor reached the
25,088-token combined envelope before its first mutation. It emitted an
incomplete read action and stopped with the starting artifact unchanged.

The ordinary actor submitted, but direct semantic review prevents treating
that as a quality win. It read the complete target and the exact result report,
then reduced the new study to one central-gist paragraph. The artifact scored
3 met / 5 partial / 2 not met on the frozen ten-item maintenance rubric. It
omitted the invalid/corrected-run distinction, exact call and token magnitudes,
the stronger fresh-world test artifact, detailed no-promotion boundary, and
evidence links.

The positive-lead gate therefore failed. The projected method reduced target
materialization but was worse on action feasibility, artifact quality, and
closure. No runtime component is promoted.

## Exact trajectories

| Measure | Ordinary | Projected |
|---|---:|---:|
| Initial task bytes | 2,370 | 21,242 |
| First-prompt tokens | 1,962 | 10,363 |
| Calls / interpreted actions | 18 / 18 | 17 / 16 |
| Target lines | 886 / 886 | 219 / 886 |
| Target exact bytes | 51,678 | 12,906 |
| Target regions touched | 33 / 33 | 6 / 33 |
| Repository objects read | 1 | 4 |
| Repository exact bytes | 5,734 | 16,646 |
| Model-visible result-message bytes | 78,924 | 47,779 |
| Maximum prompt | 24,599 | 25,062 |
| Minimum combined headroom | 483 | 0 |
| Total tokens | 264,317 | 331,344 |
| Uncached prompt tokens | 24,667 | 25,126 |
| Recorded model time | 107.1 s | 92.5 s |
| Terminal state | submitted | incomplete action / protocol error |
| Semantic maintenance | 3 met / 5 partial / 2 missing | no mutation |

Both cold server cells loaded the intended AD-IQ2_S/q8/25K package, reported
66/66 offloaded layers, and used about 10.95 GiB dedicated plus 102 MiB shared
GPU process memory. Runtime setup did not explain the difference.

The projected actor's lower time is not a complete-method efficiency result.
It generated only 513 completion tokens versus ordinary's 801 and never paid
the cost of construction, checking, or submission.

## What the projection changed

The target map was behaviorally active. After one rejected whole-file read,
the projected actor directly opened:

- `What is not yet known`;
- `Phase-continuity and diagnostic update`;
- `Design consequences`;
- `Purpose`;
- the title/date/status region; and
- the earlier opportunity/verification observation.

Those accepted target reads were exact, nonoverlapping, and unrepeated. This is
a clear contrast with ordinary's five-slice reconstruction of every line.

The source path was less selective. Projected read the complete result,
prospective freeze, semantic review, and an execution-correction record. The
last record concerned a different closure/path event; the actor still had not
read the governing reducer-shape correction or direct audit. It was acquiring
more source depth than ordinary, but had not reached a dependency-complete set
when context ended.

The appropriate claim is narrow:

> Mechanically meaningful structural addresses can change Qwen3.8 from global
> large-artifact reconstruction to selective region acquisition. A verbose
> registry held permanently in the action transcript does not by itself create
> an actionable bounded working set.

This is one fixed-order development comparison on a known anchor. It does not
establish a reliability rate or a general model trait.

## What ordinary showed

Ordinary's path is not evidence that the projection was unnecessary. Its
completed artifact retained the correct central gist:

- the seed affected orientation;
- it did not replace operative reacquisition;
- it increased token traffic without reducing recorded time; and
- it did not qualify a continuation policy.

But the model had also received exact call counts, the 41.6% token increase,
the stronger fresh-world test suite, the invalid-run warning, and the explicit
no-promotion recommendation. Most disappeared during construction. Only the
precise reducer-shape cause was absent from its acquired source.

This is the same broad failure class seen elsewhere, now in authentic document
maintenance: information can be available and understood at gist level while
independent distinctions fail to survive into one compact artifact.

## Systems implication

The experiment separates three layers:

```text
EXTERNAL ADDRESS SPACE
exact basis + delta + structural identities
        ↓
SELECTION
which regions and sources the model requests
        ↓
ACTIVE RESIDENCY
what remains in the action transcript
        ↓
CONSTRUCTION
which acquired distinctions reach the artifact
```

The projection improved the second layer but harmed the third. Ordinary
completed the fourth layer, but incompletely.

This argues for keeping exact basis, deltas, and region registries as an
external queryable substrate rather than treating the full map as permanent
working-context content. It does not yet earn automatic eviction, summaries,
semantic section selection, source caps, or a context router.

## Decision and next earned test

Do not promote the inline projected method and do not repeat the same
ordinary-versus-inline-map comparison.

The next earned diagnostic is a mechanically derived selected-working-set
continuation from this exact projected trajectory:

1. preserve the complete task and exact current candidate identity;
2. include the exact target/source objects the model itself selected through
   accepted reads, with their identities and authority unchanged;
3. omit the prior conversation and full 33-region registry from the new active
   context while keeping both externally reopenable;
4. retain unrestricted exact tools and no arbitrary source-count limit; and
5. measure whether the selected material reaches a semantically adequate
   mutation, or whether the model reacquires globally again.

That would test residency after an observed selection effect. It would not
claim that the saved read set was sufficient, and any missing source request
would remain allowed and informative.

Evidence and derived records:

- [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md)
- [`SEMANTIC_REVIEW.md`](SEMANTIC_REVIEW.md)
- [`runs/r1/METRICS.json`](runs/r1/METRICS.json)
- [`runs/r1/RUNTIME_REPORT.json`](runs/r1/RUNTIME_REPORT.json)
