# File-version handle v0 results

Date: 2026-08-16

Decision: **do not promote the handle and do not run a fresh replication.**
The stable SHA-bound patch interface and `workbench/` remain unchanged.

## What was tested

The study first audited every preserved non-checkpoint
`file_version_mismatch`, then compared two removable action contracts on two
known development repairs and two seeded samples:

- `H0_SHA256`: patch repeats the raw SHA returned by `read`;
- `H1_HANDLE`: patch supplies a short run-scoped ID mechanically bound to one
  path and SHA.

H1 retained the raw SHA in the read result and preserved strict stale-write
rejection. It did not repair, normalize, or advance an invalid basis.

## Retrospective boundary

The audit found 12 non-checkpoint mismatch results in seven distinct saved
trajectory locations: five corrupted, invented, or otherwise unbound
identities and two legitimate stale-basis cases. Three trajectories recovered
immediately, two reread and recomposed, and two did not recover. Only one
rejected action was independently shown to be a complete executable repair:
the saved Retry Queue patch moves the exact complete audit from 11/12 to 12/12
predicates and from 48/50 to 50/50 subcases when replayed with the actual
current SHA. The saved Priority patch was no longer applicable because its old
span occurred zero times.

That evidence earned a small prospective screen. It did not establish that a
handle would generally improve task quality.

## Prospective run and apparatus boundary

The first two attempted runs are preserved as qualification failures:

- `fvh-q38-r001` stopped before inference because a separately referenced
  golden was absent from the source lock;
- `fvh-q38-r002` completed four cells and one additional trajectory, then the
  stable final-diff path encountered ignored `.pyc` files accidentally copied
  as task source.

`fvh-q38-r003` completed all eight cells and every trajectory replay verifies.
Direct transcript inspection then found a third apparatus defect: all five
Priority visible checks crashed because the frozen snapshot omitted
`packet_runtime.py`. The external complete audit did not use that module and
therefore failed to detect the missing model-visible runtime.

Accordingly:

- Priority quality, timing, closure, and token differences are ineligible as
  treatment evidence;
- Retry Queue quality and visible-check paths are valid;
- exact patch-admission evidence remains usable; and
- the raw run manifest is preserved without retrospective rewriting.

See [`APPARATUS_CORRECTION_3.md`](APPARATUS_CORRECTION_3.md) and the preserved
[`run-audit.json`](runs/fvh-q38-r003/run-audit.json).

## Exact action-boundary findings

The screen had sufficient action opportunity: H0 emitted 13 patch attempts in
four trajectories and H1 emitted 10 in four.

| Observation | H0 | H1 |
|---|---:|---:|
| Patch attempts | 13 | 10 |
| Accepted patches | 12 | 9 |
| Avoidable unbound raw-hash failures | 1 | 0 |
| Unknown or wrong-path handles | n/a | 0 |
| Legitimately stale handles | n/a | 1 |

The sole H0 identity-expression failure occurred on Priority seed 42. Qwen
copied a 64-character SHA with an internal/tail corruption. On the immediately
following turn it repeated the same path, old text, new text, and semantic
patch with the exact current SHA; the patch was accepted. The handle therefore
would have saved one turn, but it did not unblock terminal work.

The sole H1 mismatch was legitimate. On Retry seed 314159, Qwen tried to apply
an import repair using `FV0003` after an earlier patch had changed that file to
`FV0004`. The host rejected the stale handle, disclosed the exact binding and
current version, and did not mutate the candidate. Qwen reread the file,
reissued the patch with `FV0004`, passed the visible check, and submitted.

## Quality and cost are descriptive only

The raw manifest totals are retained for custody, not interpreted as a valid
whole-study comparison:

| Raw aggregate | H0 | H1 |
|---|---:|---:|
| Terminal complete-audit predicates | 110/130 | 99/130 |
| Reported tokens | 248,753 | 164,805 |
| Complete task passes | 0/4 | 0/4 |

The 83,948-token H1 reduction is not an efficiency effect. Priority actors
received broken checks and several H1 actors simply stopped earlier after less
semantic work. On the valid Retry cells, H0 reached 19/24 terminal predicates
and H1 reached 18/24. Neither condition completed either task. This provides
no quality benefit for the handle.

## Frozen gate

| Criterion | Result |
|---|---|
| H1 admits no stale, wrong-path, or unknown basis | Pass: the one stale handle was rejected, not admitted |
| H1 has fewer avoidable expression failures | Descriptively pass: 0 versus 1 |
| Reduction in at least two pairs, or one blocked correct patch is unblocked | **Fail: one pair; immediate recovery; no blocked terminal patch** |
| No aggregate quality loss | Not evaluable for the complete study; no Retry benefit |
| Direct review attributes the difference to the handle boundary | Pass only for the one saved turn, not for quality or total cost |

Criterion 3 fails independently of the invalid Priority quality comparison.
Another GPU run cannot turn the observed one-pair, immediately recovered event
into the predeclared lead. A new run is therefore not earned.

## Apparatus correction and project lesson

Future frozen studies must execute the fixture-declared visible checks and
grader on both starting and golden candidates from the exact snapshot before
the first model call. Validating a separate external audit is insufficient.
The forward preflight is now implemented and tested in this removable
experiment.

The substantive lesson is narrow: raw SHA reproduction can create an
occasional action-expression error, and a short exact handle can remove that
class without weakening custody. In this screen the nuisance was rare,
immediately recoverable, and not worth another interface. Reopen the handle
only if a future authentic trajectory shows repeated or terminal identity-
expression blockage.

See [`DIRECT_TRANSCRIPT_AUDIT.md`](DIRECT_TRANSCRIPT_AUDIT.md) for the literal
request/action/result review.
