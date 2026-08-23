# Direct transcript audit

The investigator inspected every saved request, response, interpreted action,
tool result, candidate receipt, and the terminal HTTP error for the single Q3
XL trajectory.

## Turn sequence

1. Q3 XL requested the complete candidate file. The tool rejected it because
   51,678 bytes exceeded the 12,000-byte read limit. No state changed.
2. It queried the complete delta catalog. In reasoning, it correctly identified
   `mechanical-reentry-seed-v0` as the likely governing addition and described
   the likely update to the working model.
3. It read candidate lines 1–50.
4. It read lines 50–180.
5. It read lines 180–330.
6. It read lines 330–500.
7. It read lines 500–620.
8. It attempted another model request with the accumulated transcript. The
   server rejected the 26,227-token prompt against the 25,088-token context.
   No assistant action exists for this turn.

All seven interpreted actions were reproduced by custody replay. The candidate
ID remained
`d1188c233f173bf0e7920a8c35b0961bfaaf471bbb1aa3316117ada956106cc1`.

## Behavioral observations

- The model understood the likely evidence update before reacquiring the broad
  candidate.
- It explicitly noticed the call limit and formulated a plan, but the plan
  assumed that broad document reconstruction plus later source reading,
  mutation, checking, and submission would fit.
- The model was not shown live prompt occupancy, so the capacity failure is not
  evidence that it ignored an explicit token warning.
- It did not use the external 33-region catalog. It used sequential `read_lines`
  ranges instead.
- It did not reopen any of the carried blocks through their stable IDs, but its
  broad ranges duplicated 71 carried target lines.
- It acquired no new repository source content after the handoff. The only
  additional noncandidate acquisition was path-level delta metadata.

## Custody qualification

The measured runner's automatic post-run replay initially stopped on a
bookkeeping mismatch: the study-local Q3 XL renderer placed three reasoning
fields into literal requests that were omitted from the run-started
inference-settings summary. The separate post-run adapter reconstructs those
literal fields and verifies all 34 immutable records without changing them or
calling the model. See `VERIFIER_CORRECTION.md` and
`runs/r1/POSTRUN_REPLAY.json`.

