import assert from "node:assert/strict";
import test from "node:test";

import { describeWave, listServiceIds, planDeploymentWaves } from "../src/deployment-waves.mjs";

test("preserved helpers retain their behavior", () => {
  assert.deepEqual(listServiceIds([{ id: "api" }, { id: "web" }]), ["api", "web"]);
  assert.equal(describeWave(["api", "web"]), "api+web");
});

test("dependency closure creates strictly later dependent waves", () => {
  const result = planDeploymentWaves([" web "], [
    { id: "db", priority: 1 },
    { id: "api", dependsOn: ["db"], priority: 5 },
    { id: "web", dependsOn: ["api"], priority: 9 }
  ], { maxParallel: 3 });
  assert.deepEqual(result, {
    requestedIds: ["web"],
    includedIds: ["db", "api", "web"],
    alreadySatisfiedIds: [],
    waves: [["db"], ["api"], ["web"]]
  });
});

test("parallel limit and exclusive groups shape ready work", () => {
  const result = planDeploymentWaves(["a", "b", "c"], [
    { id: "a", priority: 9, exclusiveGroup: "zone" },
    { id: "b", priority: 8, exclusiveGroup: "zone" },
    { id: "c", priority: 7 }
  ], { maxParallel: 2 });
  assert.deepEqual(result.waves, [["a", "c"], ["b"]]);
});

