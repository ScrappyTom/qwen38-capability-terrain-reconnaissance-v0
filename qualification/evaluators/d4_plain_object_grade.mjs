#!/usr/bin/env node
import assert from "node:assert/strict";
import path from "node:path";
import { pathToFileURL } from "node:url";

const workspace = path.resolve(process.argv[2] ?? "");
if (!workspace) throw new Error("usage: node d4_plain_object_grade.mjs <workspace>");

const checks = [];
async function check(name, operation) {
  try {
    await operation();
    checks.push({ name, passed: true });
  } catch (error) {
    checks.push({ name, passed: false, error: error.message });
  }
}

const module = await import(`${pathToFileURL(path.join(workspace, "src", "fold-device-events.mjs")).href}?plain=${Date.now()}`);
const foldDeviceEvents = module.foldDeviceEvents;

for (const [name, invalid] of [
  ["date", new Date(0)],
  ["map", new Map([["x", 1]])],
  ["class_instance", new (class State { constructor() { this.x = 1; } })()]
]) {
  await check(`snapshot_state_rejects_${name}`, () => {
    assert.throws(
      () => foldDeviceEvents([{ deviceId: "x", sequence: 1, kind: "snapshot", state: invalid }]),
      TypeError
    );
  });
  await check(`patch_changes_rejects_${name}`, () => {
    assert.throws(
      () => foldDeviceEvents([
        { deviceId: "x", sequence: 1, kind: "snapshot", state: {} },
        { deviceId: "x", sequence: 2, kind: "patch", changes: invalid }
      ]),
      TypeError
    );
  });
}

await check("null_prototype_plain_objects_are_supported", () => {
  const state = Object.assign(Object.create(null), { a: 1 });
  const changes = Object.assign(Object.create(null), { b: 2 });
  assert.deepEqual(
    foldDeviceEvents([
      { deviceId: "x", sequence: 1, kind: "snapshot", state },
      { deviceId: "x", sequence: 2, kind: "patch", changes }
    ]),
    [{ deviceId: "x", sequence: 2, state: { a: 1, b: 2 } }]
  );
});

await check("non_array_class_instance_event_container_is_supported", () => {
  class Event {
    constructor() {
      this.deviceId = "x";
      this.sequence = 1;
      this.kind = "snapshot";
      this.state = { a: 1 };
    }
  }
  assert.deepEqual(
    foldDeviceEvents([new Event()]),
    [{ deviceId: "x", sequence: 1, state: { a: 1 } }]
  );
});

const result = {
  schema_version: "capability-terrain-d4-plain-object-grade-v0",
  checks,
  passed: checks.every((row) => row.passed)
};
process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
if (!result.passed) process.exitCode = 1;
