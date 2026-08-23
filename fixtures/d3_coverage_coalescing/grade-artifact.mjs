#!/usr/bin/env node
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import path from "node:path";
import { pathToFileURL, fileURLToPath } from "node:url";

const taskRoot = path.dirname(fileURLToPath(import.meta.url));
const workspace = path.resolve(process.argv[2] ?? path.join(taskRoot, "fixture"));
const checks = [];
let coalesceCoverage;

async function check(name, operation) {
  try {
    await operation();
    checks.push({ name, passed: true });
  } catch (error) {
    checks.push({ name, passed: false, error: error.message });
  }
}

await check("module_exports_coalesceCoverage", async () => {
  const module = await import(`${pathToFileURL(path.join(workspace, "src", "coalesce-coverage.mjs")).href}?grade=${Date.now()}`);
  coalesceCoverage = module.coalesceCoverage;
  assert.equal(typeof coalesceCoverage, "function");
});

await check("unsorted_overlap_and_touch_chain_coalesces", () => {
  assert.deepEqual(coalesceCoverage([
    { start: 8, end: 11, label: "gamma" },
    { start: 0, end: 5, label: "alpha" },
    { start: 4, end: 8, label: "beta" }
  ]), [{ start: 0, end: 11, labels: ["alpha", "beta", "gamma"] }]);
});

await check("nested_windows_extend_end_and_deduplicate_labels", () => {
  assert.deepEqual(coalesceCoverage([
    { start: 0, end: 10, label: "outer" },
    { start: 2, end: 3, label: "inner" },
    { start: 4, end: 12, label: "outer" }
  ]), [{ start: 0, end: 12, labels: ["outer", "inner"] }]);
});

await check("disjoint_groups_are_sorted_and_stable", () => {
  assert.deepEqual(coalesceCoverage([
    { start: 20, end: 21, label: "late" },
    { start: 0, end: 2, label: "first" },
    { start: 0, end: 1, label: "second-after-end-sort" },
    { start: 7, end: 8, label: "middle" }
  ]), [
    { start: 0, end: 2, labels: ["second-after-end-sort", "first"] },
    { start: 7, end: 8, labels: ["middle"] },
    { start: 20, end: 21, labels: ["late"] }
  ]);
});

await check("container_label_and_bounds_validation", () => {
  assert.throws(() => coalesceCoverage({}), TypeError);
  assert.throws(() => coalesceCoverage([{ start: 0, end: 2, label: "" }]), TypeError);
  assert.throws(() => coalesceCoverage([{ start: 0.5, end: 2, label: "x" }]), RangeError);
  assert.throws(() => coalesceCoverage([{ start: 2, end: 2, label: "x" }]), RangeError);
  assert.throws(() => coalesceCoverage([{ start: 3, end: 2, label: "x" }]), RangeError);
});

await check("caller_data_remains_unchanged", () => {
  const windows = [{ start: 4, end: 8, label: "b" }, { start: 0, end: 5, label: "a" }];
  const before = structuredClone(windows);
  coalesceCoverage(windows);
  assert.deepEqual(windows, before);
});

await check("empty_input_returns_fresh_empty_array", () => {
  const windows = [];
  const output = coalesceCoverage(windows);
  assert.deepEqual(output, []);
  assert.notEqual(output, windows);
});

const visibleEnv = { ...process.env };
delete visibleEnv.NODE_TEST_CONTEXT;
const visible = spawnSync(process.execPath, ["--test", "--test-reporter=tap", path.join(workspace, "test", "coalesce-coverage.test.mjs")], { cwd: workspace, env: visibleEnv, encoding: "utf8", timeout: 120_000 });
const visibleTests = { passed: visible.status === 0, exit_code: visible.status, stdout: visible.stdout, stderr: visible.stderr };
checks.push({ name: "visible_test_suite", passed: visibleTests.passed, error: visibleTests.passed ? undefined : `exit ${visible.status}` });

const manifest = JSON.parse(await readFile(path.join(taskRoot, "starting-world-manifest.json"), "utf8"));
const protectedPaths = ["AGENTS.md", "README.md", "package.json", "docs/coverage-windows.md", "src/report-coverage.mjs", "test/coalesce-coverage.test.mjs"];
const protectedFiles = [];
for (const relative of protectedPaths) {
  const expected = manifest.files.find((file) => file.path === relative);
  const bytes = await readFile(path.join(workspace, ...relative.split("/")));
  const actual = createHash("sha256").update(bytes).digest("hex");
  protectedFiles.push({ path: relative, expected_sha256: expected?.sha256 ?? null, actual_sha256: actual, passed: actual === expected?.sha256 });
}

const result = {
  schema_version: 1,
  grader: "experiment-102-coverage-coalescing-artifact",
  workspace,
  checks,
  visible_tests: visibleTests,
  protected_files: protectedFiles,
  passed: checks.every((item) => item.passed) && protectedFiles.every((item) => item.passed)
};
process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
if (!result.passed) process.exitCode = 1;
