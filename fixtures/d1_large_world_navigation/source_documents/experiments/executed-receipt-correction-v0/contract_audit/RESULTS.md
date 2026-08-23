# Executed receipt correction v0 — offline task-contract audit

Date: 2026-08-15

Status: complete offline evaluation correction; no model calls

## Result

The frozen packet result remains exact for the 47 programs it executed:
35/47 became 40/47, with five packet transitions and no regression among
previously passing packets.

That result did not cover the complete written contracts. The broader
task-contract audit qualified 180/180 predicates on the three task-author
goldens, then applied each task's suite to five exact source/terminal candidate
pairs. That produced 307 matched predicate comparisons—307 source executions
and 307 terminal executions. With golden qualification, the preserved full
matrix contains 794 candidate-predicate observations.

| Cell | Source | Terminal | Fixed predicates | Regressed predicates |
|---|---:|---:|---:|---:|
| `s42-sv` | 58/67 | 58/67 | 1 | 1 |
| `s42-pc` | 41/53 | 41/53 | 1 | 1 |
| `s42-co` | 47/60 | 51/60 | 6 | 2 |
| `s314159-sv` | 60/67 | 62/67 | 3 | 1 |
| `s314159-co` | 48/60 | 48/60 | 0 | 0 |
| **Total** | **254/307** | **260/307** | **11** | **5** |

No terminal candidate passed its complete task-contract audit. The historical
10/10 Session Vault candidate is packet-complete, not task-complete.

## Regressions hidden by the original packet groups

The five directly executed task-predicate regressions were:

- `s42-sv` and `s314159-sv`: `SV08_USER_TYPE`. Both edits changed the
  combined wrong-type-or-empty user guard to `ValueError`. Empty user became
  correct, but a non-string user changed from the required `TypeError` to
  `ValueError`.
- `s42-pc`: `PC32_REPLACE_CATEGORY`. The new view-time grouping repaired one
  failed-add category-position case but broke the ordering produced when a
  replacement established a new category.
- `s42-co`: `CO09_KEY_TYPE` and `CO43_AMEND_KEY_TYPE`. Changing the shared
  wrong-type-or-empty key guard to `ValueError` fixed empty keys while making
  non-string keys wrong in both Layer construction and amendment.

These are task-contract regressions, not reinterpretations of prose. The
auditor executed the literal sibling cases against the exact saved source and
terminal candidates. In each validation case the source produced the required
`TypeError` and the terminal produced `ValueError`.

## What the broader audit changes

The correction package still has a real effect. It produced 11 concrete
repairs and a net gain of six predicates. Exact failed receipts therefore
remain useful evidence for salience and some local correction.

The stronger prior statements do not survive:

- “five repairs, zero regressions” is valid only at the original packet level;
- “one complete candidate” means only one candidate passed all original
  sampled packet programs and the grader that reused them; and
- a broad packet purpose such as “validates exact types and values” cannot
  certify sibling cases its program never executed.

The transcript interpretation becomes more specific. Qwen commonly repaired
the observed representative by changing a combined branch instead of
preserving the type/value contrast. For temporal behavior, it sometimes
changed a view-time grouping in a way that fixed one scenario and broke
another. The remaining boundary is therefore not simply receipt uptake. It is
preservation of related constraints across mutation plus verification broad
enough to observe the affected neighborhood.

## Apparatus and evidence

- [`REQUIREMENT_MAP.md`](REQUIREMENT_MAP.md) maps every written contract clause
  to predicate IDs.
- [`run_contract_audit.py`](run_contract_audit.py) executes each candidate in a
  fresh subprocess and records candidate manifests.
- The saved compact result is
  [`results/contract-audit-summary-v1.json`](results/contract-audit-summary-v1.json).
- The complete per-predicate observations are preserved in
  [`results/contract-audit-matrix-v1.json`](results/contract-audit-matrix-v1.json).
- Its full deterministic matrix SHA-256 is
  `4f7d59e8b5bb546eeae0a33722fa979abac397af071c89d67d8f100933f5f27f`.
- Seven audit regression tests qualify all goldens, require predicate identity,
  freeze the observed source-to-terminal transitions, and ensure added paths
  outside the expected package remain visible to the path predicate. They also
  require every declared requirement group to be represented.

This remains broader sampled executable coverage, not proof over every
possible input. Its vocabulary is deliberately bounded: packet-complete,
contract-audit complete, and task-complete are not interchangeable.
