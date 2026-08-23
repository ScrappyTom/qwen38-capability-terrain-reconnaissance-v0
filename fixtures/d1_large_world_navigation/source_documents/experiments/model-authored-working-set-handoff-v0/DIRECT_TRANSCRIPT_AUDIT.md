# Direct transcript audit

The investigator inspected all 13 exact requests, raw responses, assistant
messages, interpreted actions, literal results, capacity receipts, candidate
snapshots, runtime records, and the terminal candidate before using aggregate
metrics.

## Literal action sequence

1. `tree` on the candidate root.
2. `read_lines` 1–100.
3. `read_lines` 101–200.
4. `read_lines` 201–300.
5. `read_lines` 301–400.
6. `read_lines` 401–500.
7. `read_lines` 501–600.
8. `read_lines` 601–700.
9. `read_lines` 701–886, rejected because the slice exceeded 12,000 bytes.
10. `read_lines` 701–790.
11. `read_lines` 791–886.
12. `delta_catalog` with the empty bounded first-page query.
13. `repo_read` of `experiments/mechanical-reentry-seed-v0/RESULTS.md`.

All admitted content results received deterministic receipt IDs N-R001 through
N-R010. There was no mutation, check, submission, or handoff action. The
candidate ID remained
`d1188c233f173bf0e7920a8c35b0961bfaaf471bbb1aa3316117ada956106cc1`.

## Navigation behavior

The actor repeatedly described whole-document understanding as a prerequisite:

- turn 4: continue reading “to understand its full structure before
  determining what I need from the repository”;
- turn 5: continue before moving to custody checks;
- turn 9: finish the document, then check changes since the basis; and
- turn 11: complete candidate understanding before judgment.

No structural catalog query occurred even though the system and task exposed
`artifact_region_catalog` and `read_artifact_region` as direct operations.
Accepted target slices covered every line exactly once. The rejected 701–886
request was an additional attempted broad read, but contributes no accepted
content bytes.

After the delta page, the actor correctly shifted to the changed experiment.
Its final saved reasoning identified the result, correction record, and handoff
as the remaining sequence and accurately counted the four disclosed calls.
The next request was never sent because the preflight found insufficient full-
allowance headroom.

## Capacity behavior

The first prompt was 1,960 tokens. Prompt residency rose monotonically with the
exact target slices:

| Turn | Prompt | Full-allowance headroom |
|---:|---:|---:|
| 1 | 1,960 | 20,056 |
| 8 | 11,275 | 10,741 |
| 11 | 15,054 | 6,962 |
| 12 | 16,768 | 5,248 |
| 13 | 20,921 | 1,095 |
| 14, not sent | 22,746 | -730 |

The turn-14 capacity record says `chat_completions_called:false`. There is no
turn-14 request or response custody record. The stop is therefore correctly
classified as `capacity_censored`, not an HTTP/model transport failure.

## Outcome boundary

Semantic artifact review is not applicable because no artifact action began.
The first consequential failure is upstream:

```text
ACQUISITION ORGANIZATION / WORKING-SET FORMATION
    whole target reconstructed
        -> transcript residency grows
        -> governing result acquired late
        -> correction and handoff never reached
```

The run cannot answer the R-versus-H handoff question. It can answer that the
frozen navigator did not produce an eligible transition state.

