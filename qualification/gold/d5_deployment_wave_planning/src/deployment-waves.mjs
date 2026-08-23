export function listServiceIds(services) {
  if (!Array.isArray(services)) throw new TypeError("services must be an array");
  return services.map((service) => service.id);
}

export function describeWave(wave) {
  if (!Array.isArray(wave)) throw new TypeError("wave must be an array");
  return wave.join("+");
}

function canonicalize(str) {
  if (typeof str !== "string") throw new TypeError("expected string");
  const trimmed = str.trim();
  if (trimmed.length === 0) throw new TypeError("empty after trimming");
  return trimmed;
}

export function planDeploymentWaves(requestedIds, services, options) {
  // ── Validate inputs ──────────────────────────────────────────────
  if (!Array.isArray(requestedIds))
    throw new TypeError("requestedIds must be an array");
  if (!Array.isArray(services))
    throw new TypeError("services must be an array");
  if (options == null || typeof options !== "object" || Array.isArray(options))
    throw new TypeError("options must be a non-array object");
  if (
    typeof options.maxParallel !== "number" ||
    !Number.isSafeInteger(options.maxParallel) ||
    options.maxParallel < 1
  )
    throw new TypeError("maxParallel must be a positive safe integer");

  // ── Canonicalize requested IDs ───────────────────────────────────
  const canonicalRequestedIds = [];
  const seenRequested = new Set();
  for (const raw of requestedIds) {
    const c = canonicalize(raw);
    if (seenRequested.has(c))
      throw new TypeError("duplicate requested ID: " + c);
    seenRequested.add(c);
    canonicalRequestedIds.push(c);
  }

  // ── Validate and canonicalize services ───────────────────────────
  const serviceMap = new Map();
  for (let idx = 0; idx < services.length; idx++) {
    const svc = services[idx];
    if (typeof svc !== "object" || svc === null || Array.isArray(svc))
      throw new TypeError("each service must be a non-array object");

    const id = canonicalize(svc.id);
    if (serviceMap.has(id))
      throw new TypeError("duplicate service ID: " + id);

    // dependsOn
    let dependsOn = [];
    if (svc.dependsOn !== undefined) {
      if (!Array.isArray(svc.dependsOn))
        throw new TypeError("dependsOn must be an array");
      const seenDeps = new Set();
      for (const dep of svc.dependsOn) {
        const c = canonicalize(dep);
        if (seenDeps.has(c))
          throw new TypeError("duplicate dependency: " + c);
        seenDeps.add(c);
        dependsOn.push(c);
      }
    }

    // enabled
    const enabled =
      svc.enabled === undefined ? true : svc.enabled;
    if (typeof enabled !== "boolean")
      throw new TypeError("enabled must be boolean");

    // alreadyDeployed
    const alreadyDeployed =
      svc.alreadyDeployed === undefined ? false : svc.alreadyDeployed;
    if (typeof alreadyDeployed !== "boolean")
      throw new TypeError("alreadyDeployed must be boolean");

    // exclusiveGroup
    let exclusiveGroup = null;
    if (svc.exclusiveGroup !== undefined && svc.exclusiveGroup !== null) {
      exclusiveGroup = canonicalize(svc.exclusiveGroup);
    }

    // priority
    let priority = 0;
    if (svc.priority !== undefined) {
      priority = svc.priority;
      if (
        typeof priority !== "number" ||
        !Number.isSafeInteger(priority) ||
        priority < 0 ||
        priority > 100
      )
        throw new TypeError("priority must be an integer 0-100");
    }

    serviceMap.set(id, {
      id,
      dependsOn,
      enabled,
      alreadyDeployed,
      exclusiveGroup,
      priority,
      position: idx,
    });
  }

  // ── Validate every dependency references a known service ─────────
  for (const [id, svc] of serviceMap) {
    for (const dep of svc.dependsOn) {
      if (!serviceMap.has(dep))
        throw new TypeError("service " + id + " depends on unknown service " + dep);
      if (dep === id)
        throw new TypeError("service " + id + " depends on itself");
    }
  }

  // ── Validate every requested ID references a known service ───────
  for (const rid of canonicalRequestedIds) {
    if (!serviceMap.has(rid))
      throw new TypeError("requested ID " + rid + " does not name a service");
  }

  // ── Compute required closure ─────────────────────────────────────
  const required = new Set();       // non-deployed services in closure
  const alreadySatisfied = new Set(); // already-deployed services in closure

  function addClosure(id) {
    if (required.has(id) || alreadySatisfied.has(id)) return;
    const svc = serviceMap.get(id);
    if (svc.alreadyDeployed) {
      alreadySatisfied.add(id);
      return; // traversal stops
    }
    required.add(id);
    for (const dep of svc.dependsOn) {
      addClosure(dep);
    }
  }

  for (const rid of canonicalRequestedIds) {
    addClosure(rid);
  }

  // ── Check enabled status ─────────────────────────────────────────
  // An enabled service may depend on a disabled service only if that
  // disabled service is already deployed. Otherwise throw.
  for (const id of required) {
    const svc = serviceMap.get(id);
    if (!svc.enabled) {
      throw new Error("required service " + id + " is disabled");
    }
  }

  // ── Detect cycles among required (non-deployed) services ─────────
  const WHT = 0, GRAY = 1, BLK = 2;
  const color = new Map();
  for (const id of required) color.set(id, WHT);

  let cycleFound = false;
  function dfsCycle(id) {
    if (cycleFound) return;
    color.set(id, GRAY);
    const svc = serviceMap.get(id);
    for (const dep of svc.dependsOn) {
      if (alreadySatisfied.has(dep)) continue;
      if (color.get(dep) === GRAY) {
        cycleFound = true;
        return;
      }
      if (color.get(dep) === WHT) dfsCycle(dep);
    }
    color.set(id, BLK);
  }
  for (const id of required) {
    if (color.get(id) === WHT) dfsCycle(id);
  }
  if (cycleFound) throw new Error("dependency cycle detected");

  // ── Build waves ──────────────────────────────────────────────────
  const waves = [];
  const deployed = new Set(); // IDs already placed in a wave (or alreadyDeployed)
  for (const id of alreadySatisfied) deployed.add(id);

  const remaining = new Set(required);

  while (remaining.size > 0) {
    // Find ready services: all deps are in `deployed`
    const ready = [];
    for (const id of remaining) {
      const svc = serviceMap.get(id);
      let allDepsMet = true;
      for (const dep of svc.dependsOn) {
        if (!deployed.has(dep)) {
          allDepsMet = false;
          break;
        }
      }
      if (allDepsMet) ready.push(id);
    }

    if (ready.length === 0) {
      // Should not happen if cycle detection is correct
      throw new Error("no ready services but remaining exist");
    }

    // Sort by descending priority, then ascending original position
    ready.sort((a, b) => {
      const pa = serviceMap.get(a).priority;
      const pb = serviceMap.get(b).priority;
      if (pb !== pa) return pb - pa;
      return serviceMap.get(a).position - serviceMap.get(b).position;
    });

    // Greedy selection respecting maxParallel and exclusiveGroup
    const wave = [];
    const usedGroups = new Set();
    for (const id of ready) {
      if (wave.length >= options.maxParallel) break;
      const svc = serviceMap.get(id);
      if (svc.exclusiveGroup !== null) {
        if (usedGroups.has(svc.exclusiveGroup)) continue;
      }
      wave.push(id);
      if (svc.exclusiveGroup !== null) {
        usedGroups.add(svc.exclusiveGroup);
      }
    }

    waves.push(wave);
    for (const id of wave) {
      deployed.add(id);
      remaining.delete(id);
    }
  }

  // ── Build includedIds in wave order ──────────────────────────────
  const includedIds = [];
  for (const wave of waves) {
    for (const id of wave) {
      includedIds.push(id);
    }
  }

  // ── Build alreadySatisfiedIds in original service-array order ────
  const alreadySatisfiedIds = [];
  for (const [id, svc] of serviceMap) {
    if (alreadySatisfied.has(id)) alreadySatisfiedIds.push(id);
  }

  // ── Return ───────────────────────────────────────────────────────
  return {
    requestedIds: [...canonicalRequestedIds],
    includedIds,
    alreadySatisfiedIds,
    waves,
  };
}
