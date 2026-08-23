# Complete-audit false-closure study v0 results

## Verdict

Complete task-derived execution evidence changed Qwen3.8's behavior in every
qualified false-closure state.

The three narrow-evidence opportunity controls reread the candidate, reran the
same narrow green check, and submitted without changing a byte. The three
complete-audit branches all mutated the candidate and improved its complete
task audit without regressing a passing predicate:

- Token Buckets: 10/11 to 11/11;
- Revision Store, seed 42: 6/11 to 8/11; and
- Revision Store, seed 314159: 8/11 to 11/11.

Across the matched branches, A0 remained at 24/33 predicates while A1 reached
30/33. A1 repaired six of the nine disclosed failing predicates and produced
two complete artifacts; A0 repaired zero and produced none.

This is a coherent scout-level positive for **executed complete verification
at a false-closure boundary**. It is not evidence that one complete snapshot
guarantees complete repair. In the harder Revision seed, Qwen saw five literal
failures, fixed two, left three, reran only the narrow green check, and
submitted again.

The stable `workbench/` remains unchanged. A fresh replication is earned; an
automatic submit gate, permanent audit surface, or semantic host status is
not.

## Qualification and run shape

Six fresh ordinary-loop trunks ran across three tasks and two frozen seeds.
The predeclared branch gate required at least three eligible trunks across at
least two tasks.

| Trunk | Natural endpoint | Complete audit | Branch state |
|---|---|---:|---|
| Lease Pool, seed 42 | green check -> submit | 11/11 | ineligible: complete |
| Lease Pool, seed 314159 | green check -> submit | 11/11 | ineligible: complete |
| Token Buckets, seed 42 | green check -> submit | 10/11 | eligible |
| Token Buckets, seed 314159 | failed check -> later submit | 6/11 | ineligible: no green check bound to submission |
| Revision Store, seed 42 | green check -> submit | 6/11 | eligible |
| Revision Store, seed 314159 | green check -> submit | 8/11 | eligible |

The gate passed exactly at three trunks across Token Buckets and Revision
Store. Both Lease Pool actors demonstrated that a narrow green check can also
precede a genuinely complete artifact; the study branched only the
mechanically observed false closures.

## Matched branch result

Both branches started from the exact submitted trunk candidate in a fresh
history. They received the same full task, exact candidate files, verifier
frame, tools, seed, action allowance, and response protocol. Their prompt
prefixes through the exact candidate were byte-identical. Only the
candidate-bound execution-evidence object differed:

- `A0_NARROW` contained the four passing visible predicates;
- `A1_COMPLETE` contained all eleven task-derived predicates.

| Cell | Trunk | A0 narrow | A1 complete | A1 - A0 | A1 fixes |
|---|---:|---:|---:|---:|---|
| Token Buckets, 42 | 10/11 | 10/11 | **11/11** | +1 | constructor ID type/value split |
| Revision Store, 42 | 6/11 | 6/11 | **8/11** | +2 | frozen dataclass and frozen-result isolation |
| Revision Store, 314159 | 8/11 | 8/11 | **11/11** | +3 | dataclass/frozen isolation and empty-batch exception |
| **Total** | **24/33** | **24/33** | **30/33** | **+6** | **6/9 disclosed failures** |

Additional matched observations:

- A1 improved all 3/3 pairs; A0 improved 0/3.
- A1 mutated and submitted 3/3 candidates; A0 submitted 3/3 unchanged.
- Neither condition regressed any task-derived predicate.
- A1 produced 2/3 complete candidates; A0 produced 0/3.
- Every branch naturally submitted; no branch hit the call cap.
- Every post-mutation visible check remained green and was bound to the
  submitted candidate.

## Cost

| Condition | Calls | Total tokens | Summed model time | Fixed predicates |
|---|---:|---:|---:|---:|
| A0 narrow | 14 | 51,100 | 41,771 ms | 0 |
| A1 complete | 16 | 82,231 | 168,573 ms | 6 |

A1 used 31,131 more reported tokens, or 60.92% above A0. Its first-prompt
material was also larger: 33,924 bytes across the three cells versus 25,807
for A0, a difference of 8,117 bytes. Most of the cumulative-token and time
difference came from producing actual patches, especially the partial
Revision repair; it should not be interpreted as pure prompt overhead.

The complete six-trunk plus six-branch study used 100 model calls and 484,975
reported tokens. These are local package costs, not throughput benchmarks.

## What the direct audit changes

The aggregate gain was not a generic fresh-verifier effect. Every A0 verifier
had the full task and exact source, reread relevant files, observed a green
check, and closed unchanged. The A1 verifier used the extra failed execution
facts to select concrete edits.

The successful repairs were mechanically specific:

- Token Buckets split `not isinstance(id, str)` from `not id`, changing only
  the wrong-type exception while preserving empty-ID behavior.
- Revision seed 314159 restored the required frozen dataclass and split empty
  tuple handling from wrong-container handling. Those two edits repaired all
  three disclosed failing predicates.

The partial Revision branch is equally important. Its initial evidence named
five failing predicates and included literal expected and observed values.
Qwen restored `@dataclass(frozen=True)`, which fixed two predicates. It then
changed `latest` to another combined type/empty branch that still returned
`ValueError` for a wrong type. It did not repair the shared key/content/number
validators or empty-batch distinction. After the ordinary four-case check
passed, it submitted with three of the original failures still present.

Thus:

```text
complete executed failure set
-> related repair activity
-> some independent distinctions survive
-> narrow recheck turns green
-> remaining disclosed distinctions can still disappear at closure
```

Complete truth improved salience and action selection. It did not make
semantic possession equivalent to complete action binding.

See [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md) for the literal
requests, actions, receipts, patches, and source-level interpretation.

## Regression and action-organization boundaries

One broader trunk did create a natural intermediate regression: freezing the
`Bucket` dataclass moved the Token Bucket audit from 4/11 to 1/11 while the old
store still attempted in-place mutation. Qwen then replaced the store before
running any check and recovered to 7/11, eventually reaching 10/11. This was a
coherent cross-file migration, not false closure on a passing narrow check.
It does not reopen the parked regression-containment intervention.

The noneligible Token Bucket seed submitted after a failed check and a
rejected stale-basis patch. The literal transcript exposes no missing tool or
unavailable information: Qwen reread the exact file and still chose submit.
That is another closure failure, but it does not identify a concrete missing
action affordance. Generic action-organization interventions remain parked.

## Research decision

The result meets the frozen scout criterion for a fresh replication:

- A1 improved every matched case;
- no A1 branch regressed a passing predicate; and
- the effect was absent from the opportunity-matched A0 branches.

The next earned study is a fresh held-out replication of the same candidate-
bound complete-verification method on new authentic false-closure states. It
should retain a narrow opportunity control and direct transcript review.

Only if that replicates should the project compare:

1. one complete snapshot at first closure; and
2. a rerunnable complete task audit bound to the post-mutation candidate.

The second question is motivated by the partial Revision branch, but has not
yet earned stable integration. Do not add an automatic gate, retry loop,
completion card, semantic diagnosis, or repair advice.

## Validation boundary

- 8/8 study apparatus tests pass.
- 12/12 saved episodes replay-verify.
- 12/12 terminal complete audits rerun to the saved result.
- The pre-call source lock is unchanged and verifies against the frozen
  apparatus, fixtures, profile, and stable workbench sources.
- The model server was stopped after the run; both process and port counts
  returned to zero.
- The broader repository suite ran 634 tests: 584 passed, 14 skipped, and 36
  errored in archived-experiment integrity checks whose historical artifact
  shapes no longer satisfy current loaders. This is the previously documented
  archive boundary, not a passing repository-wide suite and not a failure of
  this study's apparatus.
- Results are local validation, not GitHub Actions verification.
