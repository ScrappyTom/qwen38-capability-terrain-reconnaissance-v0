import assert from "node:assert/strict";
import test from "node:test";

import { coalesceCoverage } from "../src/coalesce-coverage.mjs";

test("empty coverage remains empty", () => {
  assert.deepEqual(coalesceCoverage([]), []);
});

test("an unsorted chain of overlapping and touching windows becomes one group", () => {
  assert.deepEqual(coalesceCoverage([
    { start: 8, end: 11, label: "gamma" },
    { start: 0, end: 5, label: "alpha" },
    { start: 4, end: 8, label: "beta" }
  ]), [{ start: 0, end: 11, labels: ["alpha", "beta", "gamma"] }]);
});

test("nested labels deduplicate and caller data is unchanged", () => {
  const windows = [
    { start: 0, end: 10, label: "outer" },
    { start: 2, end: 3, label: "inner" },
    { start: 4, end: 6, label: "outer" }
  ];
  const before = structuredClone(windows);
  assert.deepEqual(coalesceCoverage(windows), [{ start: 0, end: 10, labels: ["outer", "inner"] }]);
  assert.deepEqual(windows, before);
});
