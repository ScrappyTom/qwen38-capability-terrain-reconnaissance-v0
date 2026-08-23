# Direct transcript and artifact audit

Run: `r1`

This audit reads all eight literal task frames, every interpreted action and
result, every source file the model opened, all mutations, checks,
submissions, terminal candidates, and external audit outputs. It does not
infer behavior from the summary status or grader label alone.

## What each model actually saw and did

### Code feature revision — VersionedCatalog

Both packages received the full post-revision contract in the initial task.
Both followed the same seven-action shape:

```text
tree
read package export
read catalog implementation
read record model and validation
one exact catalog patch
passing visible check
submit
```

Both preserved the existing package and added an `upsert` that appends a new
key, replaces equal/higher revisions in position, ignores lower revisions,
returns the stored record, and rejects a wrong record type before mutation.
The terminal implementations differ only in method placement relative to
`snapshot`. Both passed all 12 complete-audit predicates.

This is a genuine success on feature revision, but its boundary matters. The
existing frozen `CatalogRecord` already owned field validation, so the new
method could accept a validated value object rather than reconstruct every
field distinction itself.

### Code error correction — RetryLedger

The user frame reported symptoms rather than the full repair. Both actors
opened `CONTRACT.md` before changing code. Both then inspected the owning
ledger implementation and record models.

AD first ran the visible check and received three concrete failures: duplicate
retry entries, changed retry position/sequence, and sequence consumption after
a rejected retry. It then patched, rechecked successfully, and submitted. UD
patched directly after reading the contract and implementation, checked once,
and submitted.

Both produced the same terminal `ledger.py`: validate before allocating a
sequence, replace equal/higher retries in their original list position with
their original sequence, ignore lower retries, and allocate/increment only for
a genuinely new event. Both passed all 12 complete-audit predicates.

This establishes that, in this bounded package, repository-local contract
discovery plus symptom-led diagnosis was sufficient. The model did not need
the host to restate the solution or provide a semantic card.

### Research creation — Harbor memo

Both actors opened the blank memo, then H1 through H5 in order, then emitted
one whole-document patch, ran the structural check, and submitted. Neither
skipped a record. Both documents are coherent decision memos rather than fact
lists and preserve the study design, estimates, uncertainty, missingness,
post-hoc subgroup status, measured/unmeasured outcomes, finance forecast, and
anecdotal boundary.

Direct rubric review finds 14 of 16 criteria fully met in each memo, one
partially met, and one not met. The defects are different:

- AD correctly says the missingness *can* exaggerate the apparent benefit and
  that the audit cannot establish or quantify bias. Its final recommendation,
  however, says to reassess using complete-record analysis—the very analysis
  H3 warns can be distorted. The recommendation remains cautious overall, but
  that proposed method is not supported by the record.
- UD likewise states the qualified H3 finding first, but then calls the
  observed estimate an “upper bound” and says a correction's direction is
  definitely toward a smaller advantage. H3 expressly says the audit cannot
  establish that exaggeration occurred or determine its magnitude. This is a
  modality/identification overreach.

The errors are not missing-corpus or central-gist failures. They occur after
broadly successful synthesis, when the actor turns a possible bias mechanism
into a stronger analytic or decision claim.

### Research error correction — mixed-validity water review

Both actors opened the six review comments, current report, response template,
and all four locked records before mutation. Both corrected the report and
answered every comment. Direct review finds all 18 semantic criteria met in
both terminal artifacts:

- Q1 accepted: the design was nonrandom;
- Q2 rejected: the review reversed the nitrate direction;
- Q3 accepted with the unequal-completion, rainfall-clustering, and qualified
  possible-bias mechanism;
- Q4 rejected: statistical significance did not establish causation;
- Q5 accepted with post-hoc/noninteraction qualification; and
- Q6 accepted because illness and related outcomes were unmeasured.

Both reports retain the exact estimates, design, uncertainty, missingness,
subgroup status, and measured-outcome scope without treating confidently
worded criticism as authoritative.

The shared machine failure is not a semantic failure. The checker recognized
statuses only when they appeared in each heading, while the supplied template
placed the status below the heading. Both actors followed the template. UD
submitted after seeing the mismatch. AD reread the complete response, proposed
an exact no-op replacement that the harness rejected, searched for
`ACCEPTED`, and then submitted. The bad check cost AD four extra calls without
changing its already-correct artifact. See `CUSTODY_CORRECTIONS.md`.

## Cross-trajectory observations

1. **The basic workflow matrix is no longer empty.** Bounded code creation,
   revision, and error correction plus bounded research creation, revision,
   and mixed-critique correction now all have at least one authentic ordinary-
   loop trajectory in the portfolio.
2. **The recurring Qwen qualifier problem is conditional, not universal.**
   Both code tasks were contract-audit complete, and both water corrections
   were semantically complete. The harbor creation task exposed narrower
   over-strengthening after synthesis.
3. **Task structure can perform useful decomposition without host semantic
   intervention.** The Q1-Q6 review/response frame gave the model six concrete
   claims to judge and preserve. Both models used that structure correctly.
   This is a property of the user/task frame, not a new harness card.
4. **Repository-local authoritative artifacts can be enough.** Both debug
   actors sought the contract and made the same complete repair from symptoms.
5. **Verification quality remains part of the decision environment.** The
   malformed water checker falsely contradicted two semantically complete
   artifacts. One actor wasted work attempting to satisfy it; neither allowed
   it to erase the substance.
6. **Quantization/runtime was not the dominant variable here.** The two
   packages tied on both code audits and on water semantic review. Their harbor
   errors differed, but both had the same review-status count. One trajectory
   per package/task cannot establish equivalence.

## Remaining coverage boundaries

The scout closes the missing cells only at bounded local scale. It does not
cover:

- multi-owner code integration, refactoring, migration, performance work, or
  model-authored test design;
- diagnosis from noisy runtime logs without a clean repository contract;
- external source acquisition, large-corpus research navigation, conflicting
  source versions, or long-form report construction;
- iterative user feedback across changing requirements; or
- long-horizon work in which sources, candidates, checks, and obligations
  cross a destructive context boundary.

Those are scale and ecology boundaries. They should be explored as authentic
workflows before another narrow display-format intervention is justified.
