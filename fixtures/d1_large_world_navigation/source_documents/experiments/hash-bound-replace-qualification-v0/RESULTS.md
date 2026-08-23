# Hash-bound replacement qualification v0 results

Status: **qualified for removable experiment use**

Date: 2026-08-17

The experiment-local provider adds one factual mutation:

```text
replace_file(path, expected_file_sha256, new_content)
```

It keeps the exact current-file basis check while transmitting the old file only as a hash. It
does not change `workbench/`, select a mutation for the model, interpret task semantics, or add
repair advice.

The deterministic contract suite passed 6/6 tests, including strict schema enforcement,
multiline/quote/backslash/Unicode and empty successors, stale-hash/path/binary/no-op/size
rejection without mutation, exact candidate succession/diff custody, and stable dependency
direction.

At the saved 7,309-byte failure boundary:

| Action representation | Serialized bytes |
|---|---:|
| Old-plus-new exact patch | 18,107 |
| Hash plus new complete file | 10,436 |

The replacement representation was 57.6% of the prior patch size.

In the development-only live qualification, Qwen read the authoritative and working files,
selected `replace_file` from a menu that also contained `patch`, produced the exact 8,740-byte
successor, passed the visible check, submitted, and replayed exactly in six calls. The
authoritative copy remained unchanged.

This establishes action feasibility and custody, not a task-quality advantage. The provider is
qualified for opt-in experiments and remains removable from the stable harness.

`SOURCE_LOCK.json` preserves the exact live-qualification apparatus. The forward validation
lock is `CURRENT_SOURCE_LOCK.json`, so later documentation does not rewrite the historical
measurement identity.

Evidence:

- [`FREEZE.md`](FREEZE.md)
- [`PREFLIGHT.json`](PREFLIGHT.json)
- [`runs/q1/data/QUALIFICATION.json`](runs/q1/data/QUALIFICATION.json)
- exact run custody under [`runs/q1/`](runs/q1/)
