# Complete-audit false-closure replication v0 results

## Verdict

The frozen replication gate **failed**. Complete candidate-bound audit evidence
beat the narrow-evidence control in 3/6 matched pairs; the predeclared rule
required 4/6.

This is not a null result. Across six fresh false-closure states:

- `A1_COMPLETE` caused candidate mutation in 6/6 branches, while `A0_NARROW`
  mutated only 1/6;
- A1 improved 3/6 pairs and tied 3/6; A0 won none;
- A1 finished at 62/70 task predicates versus A0 at 55/70;
- A1 produced two contract-audit-complete artifacts versus none for A0; and
- the three A1 wins spanned all three held-out task families.

The treatment was also expensive and unreliable as a complete method. A1 used
309,676 reported tokens versus 119,626 for A0, fixed only a subset of the
disclosed failures—or none—in four cells, and sometimes closed after a narrow
green check without rerunning the complete audit against its mutated
candidate.

The stable `workbench/` remains unchanged. No complete-audit surface, submit
gate, retry policy, card, planner, or generic action-organization mechanism is
promoted.

## Qualification

All six ordinary trunks qualified. Each naturally submitted an incomplete
candidate immediately after a four-case visible check passed against that same
candidate, and no later mutation intervened.

| Cell | Task family | Trunk complete audit |
|---|---|---:|
| `rc-271828` | Route Catalog | 9/12 |
| `rc-161803` | Route Catalog | 11/12 |
| `pg-271828` | Package Graph | 9/12 |
| `pg-161803` | Package Graph | 7/12 |
| `il-271828` | Inventory Lots | 10/11 |
| `il-161803` | Inventory Lots | 9/11 |
| **Total** | **three families** | **55/70** |

The predeclared branch gate required three qualifying trunks across two task
families. The observed six trunks across three families therefore supplied a
strong opportunity test rather than a marginal qualification.

## Matched branch outcome

Both branches began from the exact submitted trunk candidate in a fresh
history. Within each pair they received the same full task, exact files,
candidate identity, model package, seed, tools, 16-call allowance, and action
protocol. Only the execution-evidence coverage differed.

| Cell | Trunk | A0 narrow | A1 complete | A1 - A0 | A1 terminal change |
|---|---:|---:|---:|---:|---|
| `rc-271828` | 9/12 | 9/12 | **12/12** | +3 | fixed constructor container, empty address, and replacement ID type |
| `rc-161803` | 11/12 | 11/12 | 11/12 | 0 | fixed one of two failing constructor subcases |
| `pg-271828` | 9/12 | 9/12 | 9/12 | 0 | mutated, but repaired no frozen predicate |
| `pg-161803` | 7/12 | 7/12 | **9/12** | +2 | restored frozen dataclass properties |
| `il-271828` | 10/11 | 10/11 | 10/11 | 0 | exchanged two wrong-type failures for two empty-value failures inside `IL02` |
| `il-161803` | 9/11 | 9/11 | **11/11** | +2 | fixed constructor container and lifetime lot-ID behavior |
| **Total** | **55/70** | **55/70** | **62/70** | **+7** | **two complete artifacts** |

The frozen gate was:

1. A1 wins at least `ceil(2N/3)` pairs;
2. wins span at least two task families;
3. aggregate A1 quality exceeds A0; and
4. no predicate passing in the trunk regresses in A1.

With `N = 6`, A1 required four pair wins. It achieved three wins, three ties,
all three task families, a +7 aggregate difference, and zero regressions of a
previously passing **whole predicate**. The first condition failed, so the lead
does not replicate under its frozen rule.

The machine-readable result is
[`runs/r1/analysis.json`](runs/r1/analysis.json).

## Action and cost result

| Condition | Calls | Patches | Submitted | Total tokens | Model time |
|---|---:|---:|---:|---:|---:|
| A0 narrow | 28 | 1 | 6/6 | 119,626 | 121,970 ms |
| A1 complete | 43 | 14 | 6/6 | 309,676 | 579,978 ms |

A1 used 190,050 more reported tokens: 2.588 times A0, or 158.87% more. Its
summed model time was 4.755 times A0, or 375.51% more. These are local package
costs, not throughput benchmarks. Much of the difference came from actual
repair attempts, rereads, and accumulated transcript, not merely from the
larger first evidence object.

The sharpest behavioral result is activation rather than reliability:

```text
same full task + exact candidate + fresh actor
    narrow green evidence    -> 1/6 candidates mutated, 0 net predicates gained
    complete audit evidence  -> 6/6 candidates mutated, 7 net predicates gained
```

Complete evidence made repair much more likely. It did not make repair
complete, well targeted, or economical.

## Required reporting correction: grouped predicates can hide regressions

The frozen reducer defines a regression as a predicate that passed in the
trunk and failed terminally. Under that definition A1 had zero regressions.
That statement is accurate but incomplete.

In `il-271828`, predicate `IL02` was already failing. Its expected/observed
object contained separate wrong-type and empty-value subcases. Qwen replaced a
combined `ValueError` branch with a combined `TypeError` branch:

- `id_type` and `sku_type` changed from wrong to correct;
- `id_empty` and `sku_empty` changed from correct to wrong; and
- the grouped predicate therefore remained failing.

No aggregate whole-predicate transition recorded either the two fixes or the
two regressions. Future evaluation must report subcase transitions whenever a
predicate contains independently meaningful expected/observed fields. A claim
of “zero regressions” must state whether it means whole predicates, subcases,
or both.

This is an evaluation-governance correction. It does not change the saved
run, frozen gate, or stable harness.

## What the literal trajectories show

The direct audit found three distinct response classes.

### Complete and local use

`rc-271828` received three literal mismatches and made three targeted patches,
reaching 12/12. `il-161803` repaired both disclosed predicate groups and
reached 11/11. These cells show that a one-time complete audit can select and
support correct repair when the expected/observed distinctions remain active
through construction.

### Partial use followed by stale closure evidence

`rc-161803` repaired the item-type half of a constructor predicate but omitted
the container-type half. `pg-161803` restored a frozen dataclass and thereby
fixed two predicates, but left exception-type, tuple-freshness, and name-type
requirements wrong. `il-271828` exchanged type/value subcases within one
predicate.

All then reran only the ordinary four-case visible check. The initial complete
audit was still exact about the branch basis candidate, but after mutation it
was no longer a current audit of the new candidate. The model saw green
current narrow evidence and old complete evidence, then submitted.

### Activity not aligned with the literal mismatch

In `pg-271828`, the complete evidence said that the wrong name type produced
`ValueError` rather than `TypeError`, alongside two other failing predicates.
Qwen instead edited removal/dependency behavior, briefly removed and restored
snapshot code, encountered an exact no-op rejection, reran the green narrow
check, and submitted at the original 9/12. The action followed a plausible
package-graph concern but not the literal expected-versus-observed mismatch.

See [`DIRECT_TRAJECTORY_AUDIT.md`](DIRECT_TRAJECTORY_AUDIT.md) for the full
request/action/effect comparison.

## Research decision

The replicated package is **not promoted**. The correct bounded conclusion is:

> A complete candidate-bound audit is a strong repair activator in authentic
> narrow-check false-closure states, but one static snapshot is not a reliable
> or efficient complete-repair method.

The direct transcripts now identify a concrete missing affordance that was not
available in the tested branches: after mutation, the actor could rerun only
the narrow visible check, not the same complete audit against the current
candidate. That makes a **static complete snapshot versus rerunnable complete
audit** comparison a defensible new question. It is not a successful-
replication promotion and should not be smuggled in as one. Saved cells may
calibrate the interface mechanically; behavioral evidence should use fresh
authentic false-closure tasks and an opportunity-matched branch design.

Generic action organization remains parked. The transcript identifies a
specific verification-currentness affordance, not a need for a plan, staged
workflow, coaching, or next-action advice.

Regression containment also remains parked. No broader trajectory created the
predeclared whole-predicate source-pass to terminal-fail state. The Inventory
subcase exchange is preserved as a measurement and local-repair warning, not
silently relabeled as that separate opportunity.

## Validation boundary

- 9/9 targeted apparatus tests pass.
- All three task-author goldens pass their full audits; all three starting
  candidates fail both visible and complete verification as designed.
- 18/18 saved trunk and branch episodes replay-verify.
- 18/18 terminal audits rerun to the saved result.
- Every qualifying trunk and all twelve branches were directly inspected from
  literal request, response, action, result, candidate, diff, check, and audit
  records.
- A pre-commit custody check found that Git's default Windows text handling
  would normalize some extensionless content-addressed artifacts in the
  staged copy. The repository now marks all `experiments/*/runs/**` as binary
  byte custody; the run was restaged and all 1,367 staged content-addressed
  artifact identities were verified. No saved working-tree byte or model
  result was changed.
- The run used Qwen3.8-27B IQ2 through llama.cpp b10434 with the frozen
  nonthinking profile and seeds 271828/161803.
- The model server was stopped after the run; its process and port were
  verified absent and dedicated VRAM returned to the desktop baseline.
- Validation is local, not GitHub Actions verification.
