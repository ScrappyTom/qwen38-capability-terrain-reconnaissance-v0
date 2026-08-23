import assert from "node:assert/strict";
import test from "node:test";

import { foldDeviceEvents } from "../src/fold-device-events.mjs";

test("one snapshot creates one active device", () => {
  assert.deepEqual(
    foldDeviceEvents([{ deviceId: "sensor-a", sequence: 1, kind: "snapshot", state: { online: true } }]),
    [{ deviceId: "sensor-a", sequence: 1, state: { online: true } }]
  );
});

test("per-device sequence rather than input order controls patches", () => {
  const events = [
    { deviceId: "sensor-a", sequence: 3, kind: "patch", changes: { zone: null, online: false } },
    { deviceId: "sensor-b", sequence: 1, kind: "snapshot", state: { online: true } },
    { deviceId: "sensor-a", sequence: 1, kind: "snapshot", state: { zone: "west", online: true } },
    { deviceId: "sensor-a", sequence: 2, kind: "patch", changes: { zone: "east" } }
  ];
  assert.deepEqual(foldDeviceEvents(events), [
    { deviceId: "sensor-a", sequence: 3, state: { online: false } },
    { deviceId: "sensor-b", sequence: 1, state: { online: true } }
  ]);
});

test("gaps and events after delete are rejected without mutation", () => {
  const gap = [{ deviceId: "x", sequence: 1, kind: "snapshot", state: {} }, { deviceId: "x", sequence: 3, kind: "patch", changes: {} }];
  const afterDelete = [
    { deviceId: "x", sequence: 1, kind: "snapshot", state: {} },
    { deviceId: "x", sequence: 2, kind: "delete" },
    { deviceId: "x", sequence: 3, kind: "patch", changes: { active: true } }
  ];
  const before = structuredClone(afterDelete);
  assert.throws(() => foldDeviceEvents(gap), RangeError);
  assert.throws(() => foldDeviceEvents(afterDelete), RangeError);
  assert.deepEqual(afterDelete, before);
});
