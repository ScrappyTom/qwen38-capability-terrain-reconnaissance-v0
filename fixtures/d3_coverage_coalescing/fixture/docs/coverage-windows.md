# Coverage-window contract

`coalesceCoverage(windows)` returns a new canonical array for labeled half-open numeric windows.

- `windows` must be an array. Each entry must have integer `start` and `end` values with `start < end`, plus a non-empty string `label`.
- Process entries after a stable sort by ascending `start`, then ascending `end`, then original input position.
- Merge windows when they overlap or touch: the next window joins the current group when `next.start <= current.end`.
- A merged result has `{ start, end, labels }`, where `end` is the furthest covered endpoint and `labels` contains distinct labels in first-encounter order during the sorted sweep.
- Disjoint groups remain in ascending order. An empty input returns an empty array.
- Do not mutate the input array or any input entry.

Invalid container or label shapes throw `TypeError`. Invalid numeric bounds throw `RangeError`.
