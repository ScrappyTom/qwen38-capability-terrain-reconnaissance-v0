# Atomic claim edit v0 — results

Date: 2026-08-12

Decision: **protocol passed; artifact qualification failed; preserve and do not rerun**

## Result

All four stateless local edit calls completed normally and passed the strict
three-scalar response contract. The host applied the returned strings exactly,
the resulting candidate preserved all bytes outside the four frozen spans, and
the visible mechanical check passed.

The artifact gate failed because the model added none of the three missing
individual citation handles.

| Claim | Bound record | Model action | Bound handle after |
|---|---|---|---|
| C001 adjusted association | H2 | added exact 95% CI and p-value | none |
| C002 nonrandom selection | H1 | unchanged | none |
| C003 geocoding completeness | H3 | added exact 72% and 93% rates | none |
| C004 housing-density caveat | H4 | unchanged | H4 |

Thus 2/4 claim strings changed, 1/4 ended with its one exact bound handle, and
0/3 previously missing handles were added. Policy Implications still contains
only the original H4 citation.

The calls used 3,714 prompt tokens, 213 completion tokens, and 3,927 total
tokens. The summed HTTP duration was 17.856 seconds. No reasoning tokens,
retry, repair, normalization, voting, fallback, or prompt variation occurred.

## Direct input/output finding

The model did not ignore the evidence.

- For C001/H2 it changed the claim to add the correct confidence interval
  `0.7 to 4.1` and `p=0.007`.
- For C003/H3 it changed the claim to add the correct group completeness rates,
  `72%` and `93%`.
- For C002/H1 it retained the already accurate nonrandom-selection phrase.
- For C004/H4 it retained the already accurate claim and existing `[H4]`.

Each request also contained the prior exact `supports` relation and a scalar
`declared_handle` such as `[H2]`. Nevertheless, C001–C003 omitted that handle.
This is therefore not an awareness or acquisition failure on those pairs. It
is a failure to select citation binding as the local edit objective.

## Human artifact adjudication

The two added facts are faithful to H2 and H3 and fit grammatically in the
target paragraph. No contradictory or causal claim was introduced. The edit
does, however, redundantly repeat details that the full paper already reported
in Findings and Caveats. The local model could not know that because the
experiment deliberately withheld surrounding sections.

Requirement 6 remains unmet in Policy Implications for H1, H2, and H3. The
mechanical visible checker is only a structural check and correctly did not
pretend otherwise.

## Interpretation

The atomic matcher result and this edit result separate two capabilities:

1. With one claim and one record, Qwen can determine the relationship exactly.
2. With the same pair plus the unchanged six-part task, Qwen may use the record
   to enrich content without performing the missing binding operation.

The local request supplied all six global requirements. For C001 and C003,
the model chose requirements 1 and 3 over requirement 6. The atomic information
unit was therefore narrower than the task frame. Exact evidence alone did not
specify which of several valid transformations was currently wanted.

This does not refute atomic claim work. It shows that a useful atomic work item
may need an explicit local obligation in addition to exact claim and evidence
identity. That obligation is semantic experimental input; custody cannot derive
it merely from hashes or versions.

## Earned follow-up

A single adaptive follow-up may hold the claim, record, prior relation, output
schema, model, and settings fixed while marking the task's existing citation
requirement as the active local obligation. It must remain one claim and one
record per stateless call.

If that changes the outputs, the result supports task-frame salience as the
missing variable on this known fixture. Because the follow-up is designed from
this failure, any success requires prospective replication on a new task. It
does not earn a host-generated obligation selector or a harness feature.

