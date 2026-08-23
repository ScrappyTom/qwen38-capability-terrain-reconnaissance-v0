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
let foldDeviceEvents;

async function check(name, operation) {
  try {
    await operation();
    checks.push({ name, passed: true });
  } catch (error) {
    checks.push({ name, passed: false, error: error.message });
  }
}

await check("module_exports_foldDeviceEvents", async () => {
  const module = await import(`${pathToFileURL(path.join(workspace, "src", "fold-device-events.mjs")).href}?grade=${Date.now()}`);
  foldDeviceEvents = module.foldDeviceEvents;
  assert.equal(typeof foldDeviceEvents, "function");
});

await check("per_device_sequence_controls_out_of_order_input", () => {
  const events = [
    { deviceId: "a", sequence: 3, kind: "patch", changes: { zone: null, online: false } },
    { deviceId: "b", sequence: 1, kind: "snapshot", state: { online: true } },
    { deviceId: "a", sequence: 1, kind: "snapshot", state: { zone: "west", online: true } },
    { deviceId: "a", sequence: 2, kind: "patch", changes: { zone: "east" } }
  ];
  assert.deepEqual(foldDeviceEvents(events), [
    { deviceId: "a", sequence: 3, state: { online: false } },
    { deviceId: "b", sequence: 1, state: { online: true } }
  ]);
});

await check("first_appearance_order_and_terminal_delete_integrate", () => {
  const events = [
    { deviceId: "z", sequence: 2, kind: "delete" },
    { deviceId: "a", sequence: 1, kind: "snapshot", state: { value: 1 } },
    { deviceId: "z", sequence: 1, kind: "snapshot", state: { value: 9 } },
    { deviceId: "m", sequence: 1, kind: "snapshot", state: { value: 3 } },
    { deviceId: "a", sequence: 2, kind: "patch", changes: { value: 2 } }
  ];
  assert.deepEqual(foldDeviceEvents(events), [
    { deviceId: "a", sequence: 2, state: { value: 2 } },
    { deviceId: "m", sequence: 1, state: { value: 3 } }
  ]);
});

await check("container_identifier_kind_state_and_change_shapes_are_rejected", () => {
  assert.throws(() => foldDeviceEvents({}), TypeError);
  assert.throws(() => foldDeviceEvents([null]), TypeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: " x ", sequence: 1, kind: "snapshot", state: {} }]), TypeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "unknown", state: {} }]), TypeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "snapshot", state: [] }]), TypeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "snapshot", state: {} }, { deviceId: "x", sequence: 2, kind: "patch", changes: [] }]), TypeError);
});

await check("sequence_and_protocol_errors_are_rejected", () => {
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 0, kind: "snapshot", state: {} }]), RangeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "patch", changes: {} }]), RangeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "snapshot", state: {} }, { deviceId: "x", sequence: 3, kind: "patch", changes: {} }]), RangeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "snapshot", state: {} }, { deviceId: "x", sequence: 1, kind: "patch", changes: {} }]), RangeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "snapshot", state: {} }, { deviceId: "x", sequence: 2, kind: "snapshot", state: {} }]), RangeError);
  assert.throws(() => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "snapshot", state: {} }, { deviceId: "x", sequence: 2, kind: "delete" }, { deviceId: "x", sequence: 3, kind: "patch", changes: {} }]), RangeError);
});

await check("caller_data_and_nested_references_remain_independent", () => {
  const events = [
    { deviceId: "x", sequence: 1, kind: "snapshot", state: { nested: { value: 1 }, remove: true } },
    { deviceId: "x", sequence: 2, kind: "patch", changes: { nested: { value: 2 }, remove: null } }
  ];
  const before = structuredClone(events);
  const output = foldDeviceEvents(events);
  assert.deepEqual(events, before);
  assert.deepEqual(output, [{ deviceId: "x", sequence: 2, state: { nested: { value: 2 } } }]);
  output[0].state.nested.value = 99;
  assert.deepEqual(events, before);
});

await check("empty_input_returns_fresh_empty_array", () => {
  const events = [];
  const output = foldDeviceEvents(events);
  assert.deepEqual(output, []);
  assert.notEqual(output, events);
});

const visibleEnv = { ...process.env };
delete visibleEnv.NODE_TEST_CONTEXT;
const visible = spawnSync(process.execPath, ["--test", "--test-reporter=tap", path.join(workspace, "test", "fold-device-events.test.mjs")], { cwd: workspace, env: visibleEnv, encoding: "utf8", timeout: 120_000 });
const visibleTests = { passed: visible.status === 0, exit_code: visible.status, stdout: visible.stdout, stderr: visible.stderr };
checks.push({ name: "visible_test_suite", passed: visibleTests.passed, error: visibleTests.passed ? undefined : `exit ${visible.status}` });

const manifest = JSON.parse(await readFile(path.join(taskRoot, "starting-world-manifest.json"), "utf8"));
const protectedPaths = ["AGENTS.md", "README.md", "package.json", "docs/device-events.md", "src/materialize-devices.mjs", "test/fold-device-events.test.mjs"];
const protectedFiles = [];
for (const relative of protectedPaths) {
  const expected = manifest.files.find((file) => file.path === relative);
  const bytes = await readFile(path.join(workspace, ...relative.split("/")));
  const actual = createHash("sha256").update(bytes).digest("hex");
  protectedFiles.push({ path: relative, expected_sha256: expected?.sha256 ?? null, actual_sha256: actual, passed: actual === expected?.sha256 });
}

const result = {
  schema_version: 1,
  grader: "experiment-103-device-event-folding-artifact",
  workspace,
  checks,
  visible_tests: visibleTests,
  protected_files: protectedFiles,
  passed: checks.every((item) => item.passed) && protectedFiles.every((item) => item.passed)
};
process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
if (!result.passed) process.exitCode = 1;
