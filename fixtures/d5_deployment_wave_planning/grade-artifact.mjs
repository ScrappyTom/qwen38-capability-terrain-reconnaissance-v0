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
let plan;

async function check(name, operation) {
  try { await operation(); checks.push({ name, passed: true }); }
  catch (error) { checks.push({ name, passed: false, error: error.message }); }
}

await check("module_exports_and_preserved_helpers", async () => {
  const module = await import(`${pathToFileURL(path.join(workspace, "src", "deployment-waves.mjs")).href}?grade=${Date.now()}`);
  plan = module.planDeploymentWaves;
  assert.equal(typeof plan, "function");
  assert.deepEqual(module.listServiceIds([{ id: "a" }, { id: "b" }]), ["a", "b"]);
  assert.equal(module.describeWave(["a", "b"]), "a+b");
});

await check("canonical_and_exhaustive_validation", () => {
  assert.throws(() => plan(["a", " a "], [{ id: "a" }], { maxParallel: 1 }), TypeError);
  assert.throws(() => plan(["a"], [{ id: "a" }, { id: " a " }], { maxParallel: 1 }), TypeError);
  assert.throws(() => plan(["a"], [{ id: "a" }, { id: "unused", priority: 1.5 }], { maxParallel: 1 }), TypeError);
  assert.throws(() => plan(["a"], [{ id: "a", dependsOn: ["missing"] }], { maxParallel: 1 }), TypeError);
  assert.throws(() => plan(["a"], [{ id: "a", dependsOn: ["a"] }], { maxParallel: 1 }), TypeError);
  assert.throws(() => plan(["missing"], [{ id: "a" }], { maxParallel: 1 }), TypeError);
  assert.throws(() => plan(["a"], [{ id: "a" }], { maxParallel: 0 }), TypeError);
});

await check("closure_and_already_deployed_stop", () => {
  const result = plan(["web"], [
    { id: "legacy", enabled: false },
    { id: "db", dependsOn: ["legacy"], alreadyDeployed: true },
    { id: "api", dependsOn: ["db"] },
    { id: "web", dependsOn: ["api"] }
  ], { maxParallel: 4 });
  assert.deepEqual(result, { requestedIds: ["web"], includedIds: ["api", "web"], alreadySatisfiedIds: ["db"], waves: [["api"], ["web"]] });
});

await check("disabled_required_member_rules", () => {
  assert.throws(() => plan(["web"], [{ id: "db", enabled: false }, { id: "web", dependsOn: ["db"] }], { maxParallel: 2 }), Error);
  const result = plan(["web"], [{ id: "db", enabled: false, alreadyDeployed: true }, { id: "web", dependsOn: ["db"] }], { maxParallel: 2 });
  assert.deepEqual(result.waves, [["web"]]);
  assert.deepEqual(result.alreadySatisfiedIds, ["db"]);
});

await check("required_cycle_detection", () => {
  assert.throws(() => plan(["a"], [{ id: "a", dependsOn: ["b"] }, { id: "b", dependsOn: ["c"] }, { id: "c", dependsOn: ["a"] }], { maxParallel: 2 }), Error);
  const result = plan(["a"], [{ id: "a", dependsOn: ["b"] }, { id: "b", dependsOn: ["a"], alreadyDeployed: true }], { maxParallel: 2 });
  assert.deepEqual(result.waves, [["a"]]);
});

await check("priority_parallelism_exclusivity_and_stable_ties", () => {
  const result = plan(["low", "first", "second", "free"], [
    { id: "low", priority: 1 },
    { id: "first", priority: 9, exclusiveGroup: "g" },
    { id: "second", priority: 9, exclusiveGroup: "g" },
    { id: "free", priority: 8 }
  ], { maxParallel: 2 });
  assert.deepEqual(result.waves, [["first", "free"], ["second", "low"]]);
  assert.deepEqual(result.includedIds, ["first", "free", "second", "low"]);
});

await check("result_shape_cloning_and_nonmutation", () => {
  const requested = [" child "];
  const services = [{ id: " base ", priority: 2 }, { id: " child ", dependsOn: [" base "], priority: 3 }];
  const options = { maxParallel: 2 };
  const before = structuredClone({ requested, services, options });
  const result = plan(requested, services, options);
  assert.deepEqual(Object.keys(result), ["requestedIds", "includedIds", "alreadySatisfiedIds", "waves"]);
  assert.deepEqual(result, { requestedIds: ["child"], includedIds: ["base", "child"], alreadySatisfiedIds: [], waves: [["base"], ["child"]] });
  result.requestedIds.push("changed");
  result.waves[0].push("changed");
  assert.deepEqual({ requested, services, options }, before);
});

const visibleEnv = { ...process.env };
delete visibleEnv.NODE_TEST_CONTEXT;
const visible = spawnSync(process.execPath, ["--test", "--test-reporter=tap", path.join(workspace, "test", "deployment-waves.test.mjs")], { cwd: workspace, env: visibleEnv, encoding: "utf8", timeout: 120_000 });
const visibleTests = { passed: visible.status === 0, exit_code: visible.status, stdout: visible.stdout, stderr: visible.stderr };
checks.push({ name: "visible_test_suite", passed: visibleTests.passed, error: visibleTests.passed ? undefined : `exit ${visible.status}` });

const manifest = JSON.parse(await readFile(path.join(taskRoot, "starting-world-manifest.json"), "utf8"));
const protectedPaths = ["AGENTS.md", "README.md", "package.json", "docs/deployment-waves.md", "test/deployment-waves.test.mjs"];
const protectedFiles = [];
for (const relative of protectedPaths) {
  const expected = manifest.files.find((file) => file.path === relative);
  const bytes = await readFile(path.join(workspace, ...relative.split("/")));
  const actual = createHash("sha256").update(bytes).digest("hex");
  protectedFiles.push({ path: relative, expected_sha256: expected?.sha256 ?? null, actual_sha256: actual, passed: actual === expected?.sha256 });
}

const result = { schema_version: 1, grader: "experiment-107-deployment-waves-artifact", workspace, checks, visible_tests: visibleTests, protected_files: protectedFiles, passed: checks.every((item) => item.passed) && protectedFiles.every((item) => item.passed) };
process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
if (!result.passed) process.exitCode = 1;

