# Deployment-wave contract

`planDeploymentWaves(requestedIds, services, options)` builds dependency-safe waves for a requested deployment. It must not mutate any input.

## Validation and canonicalization

- A canonical string is a string trimmed at both ends and non-empty.
- `requestedIds` and `services` must be arrays. Requested IDs are canonicalized and must be unique after trimming.
- `options` must be a non-array object when supplied. `maxParallel` is required and must be a positive safe integer.
- Every service is validated before requested-membership or dependency-closure filtering. A service is a non-array object with:
  - canonical unique `id`;
  - `dependsOn`, omitted as `[]` or otherwise an array of canonical IDs unique after trimming;
  - optional boolean `enabled` (default `true`);
  - optional boolean `alreadyDeployed` (default `false`);
  - optional `exclusiveGroup`, either `null`/omitted or a canonical non-empty string;
  - optional integer `priority` from `0` through `100` (default `0`).
- Every dependency must name a service, and a service cannot depend on itself. Every requested ID must name a service. Invalid data throws `TypeError`, including invalid unrequested services.

## Required closure

The required closure begins with requested services and recursively includes their dependencies. An `alreadyDeployed` service satisfies its dependency and appears in `alreadySatisfiedIds`; traversal stops at that service, so its own dependencies are not added. Already-deployed services never appear in waves.

An enabled service may depend on a disabled service only when the disabled service is already deployed. Otherwise a disabled member of the required closure makes the request unschedulable and throws `Error`.

A dependency cycle among required, non-deployed services throws `Error`.

## Wave construction

A service is ready only when every dependency is already deployed or appeared in an earlier wave. Dependencies cannot share a wave with their dependents.

For each wave, sort ready services by descending `priority`, breaking ties by original service-array position. Greedily scan that order and select at most `maxParallel` services. At most one selected service may use any non-null `exclusiveGroup`; skipped ready services remain eligible for the next wave. Null groups do not conflict.

## Result

Return a fresh object with properties in exactly this order:

1. `requestedIds` — canonical requested IDs in request order
2. `includedIds` — all scheduled IDs in wave order
3. `alreadySatisfiedIds` — required already-deployed IDs in original service-array order
4. `waves` — fresh arrays of canonical service IDs

No returned array may alias an input.

