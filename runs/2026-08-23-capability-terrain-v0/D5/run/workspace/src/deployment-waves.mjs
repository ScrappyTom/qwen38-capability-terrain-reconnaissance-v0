export function listServiceIds(services) {
  if (!Array.isArray(services)) throw new TypeError("services must be an array");
  return services.map((service) => service.id);
}

function isPlainObject(value) {
  if (typeof value !== "object" || value === null || Array.isArray(value)) return false;
  const proto = Object.getPrototypeOf(value);
  return proto === null || proto === Object.prototype;
}

function canonicalId(value, label) {
  if (typeof value !== "string") throw new TypeError(`${label} must be a string`);
  const trimmed = value.trim();
  if (trimmed.length === 0) throw new TypeError(`${label} must be non-empty after trimming`);
  return trimmed;
}

function validateServices(services, options) {
  if (!Array.isArray(requestedIds)) throw new TypeError("requestedIds must be an array");
  if (!Array.isArray(services)) throw new TypeError("services must be an array");
  if (options !== undefined && !isPlainObject(options)) throw new TypeError("options must be a non-array object");

  const maxParallel = options?.maxParallel;
  if (typeof maxParallel !== "number" || !Number.isSafeInteger(maxParallel) || maxParallel <= 0) {
    throw new TypeError("options.maxParallel is required and must be a positive safe integer");
  }

  const requestedSet = new Set();
  for (const id of requestedIds) {
    const canonical = canonicalId(id, "requested ID");
    if (requestedSet.has(canonical)) throw new TypeError("requested IDs must be unique after trimming");
    requestedSet.add(canonical);
  }

  const serviceMap = new Map();
  for (const [index, raw] of services.entries()) {
    if (!isPlainObject(raw)) throw new TypeError(`service at index ${index} must be a non-array object`);

    const id = canonicalId(raw.id, "service id");
    if (serviceMap.has(id)) throw new TypeError("service ids must be unique after trimming");

    let dependsOn = [];
    if (raw.dependsOn !== undefined) {
      if (!Array.isArray(raw.dependsOn)) throw new TypeError(`dependsOn for ${id} must be an array`);
      const seen = new Set();
      dependsOn = raw.dependsOn.map((dep) => {
        const depId = canonicalId(dep, "dependency id");
        if (seen.has(depId)) throw new TypeError(`dependsOn for ${id} must be unique after trimming`);
        seen.add(depId);
        return depId;
      });
    }

    let enabled = true;
    if (raw.enabled !== undefined) {
      if (typeof raw.enabled !== "boolean") throw new TypeError(`enabled for ${id} must be a boolean`);
      enabled = raw.enabled;
    }

    let alreadyDeployed = false;
    if (raw.alreadyDeployed !== undefined) {
      if (typeof raw.alreadyDeployed !== "boolean") throw new TypeError(`alreadyDeployed for ${id} must be a boolean`);
      alreadyDeployed = raw.alreadyDeployed;
    }

    let exclusiveGroup = null;
    if (raw.exclusiveGroup !== undefined) {
      if (raw.exclusiveGroup === null) exclusiveGroup = null;
      else exclusiveGroup = canonicalId(raw.exclusiveGroup, `exclusiveGroup for ${id}`);
    }

    let priority = 0;
    if (raw.priority !== undefined) {
      if (!Number.isInteger(raw.priority) || raw.priority < 0 || raw.priority > 100) {
        throw new TypeError(`priority for ${id} must be an integer from 0 through 100`);
      }
      priority = raw.priority;
    }

    serviceMap.set(id, {
      id,
      dependsOn,
      enabled,
      alreadyDeployed,
      exclusiveGroup,
      priority,
      index
    });
  }

  for (const { id, dependsOn } of serviceMap.values()) {
    if (dependsOn.includes(id)) throw new TypeError(`service ${id} cannot depend on itself`);
    for (const dep of dependsOn) {
      if (!serviceMap.has(dep)) throw new TypeError(`dependency ${dep} must name a service`);
    }
  }

  for (const id of requestedSet) {
    if (!serviceMap.has(id)) throw new TypeError(`requested ID ${id} must name a service`);
  }

  return { serviceMap, requestedIds: [...requestedSet] };
}

function buildWaves(requestedCanonical, services, options) {
  const maxParallel = options.maxParallel;
  const byId = new Map();
  for (const [index, raw] of services.entries()) {
    if (!isPlainObject(raw)) throw new TypeError(`service at index ${index} must be a non-array object`);

    const id = canonicalId(raw.id, "service id");
    if (byId.has(id)) throw new TypeError("service ids must be unique after trimming");

    let dependsOn = [];
    if (raw.dependsOn !== undefined) {
      if (!Array.isArray(raw.dependsOn)) throw new TypeError(`dependsOn for ${id} must be an array`);
      const seen = new Set();
      dependsOn = raw.dependsOn.map((dep) => {
        const depId = canonicalId(dep, "dependency id");
        if (seen.has(depId)) throw new TypeError(`dependsOn for ${id} must be unique after trimming`);
        seen.add(depId);
        return depId;
      });
    }

    let enabled = true;
    if (raw.enabled !== undefined) {
      if (typeof raw.enabled !== "boolean") throw new TypeError(`enabled for ${id} must be a boolean`);
      enabled = raw.enabled;
    }

    let alreadyDeployed = false;
    if (raw.alreadyDeployed !== undefined) {
      if (typeof raw.alreadyDeployed !== "boolean") throw new TypeError(`alreadyDeployed for ${id} must be a boolean`);
      alreadyDeployed = raw.alreadyDeployed;
    }

    let exclusiveGroup = null;
    if (raw.exclusiveGroup !== undefined) {
      if (raw.exclusiveGroup === null) exclusiveGroup = null;
      else exclusiveGroup = canonicalId(raw.exclusiveGroup, `exclusiveGroup for ${id}`);
    }

    let priority = 0;
    if (raw.priority !== undefined) {
      if (!Number.isInteger(raw.priority) || raw.priority < 0 || raw.priority > 100) {
        throw new TypeError(`priority for ${id} must be an integer from 0 through 100`);
      }
      priority = raw.priority;
    }

    byId.set(id, { id, dependsOn, enabled, alreadyDeployed, exclusiveGroup, priority, index });
  }

  for (const [id, svc] of byId) {
    if (svc.dependsOn.includes(id)) throw new TypeError(`service ${id} cannot depend on itself`);
    for (const dep of svc.dependsOn) {
      if (!byId.has(dep)) throw new TypeError(`dependency ${dep} must name a service`);
    }
  }

  for (const id of requestedCanonical) {
    if (!byId.has(id)) throw new TypeError(`requested ID ${id} must name a service`);
  }

  const required = new Set();
  const stack = [...requestedCanonical];
  while (stack.length > 0) {
    const id = stack.pop();
    if (required.has(id)) continue;
    required.add(id);
    const svc = byId.get(id);
    if (!svc.alreadyDeployed) {
      for (const dep of svc.dependsOn) {
        if (!required.has(dep)) stack.push(dep);
      }
    }
  }

  const alreadySatisfied = [];
  for (const [id, svc] of byId) {
    if (svc.alreadyDeployed && required.has(id)) alreadySatisfied.push(id);
  }
  alreadySatisfied.sort((a, b) => byId.get(a).index - byId.get(b).index);

  const inWave = new Set();
  for (const id of requestedCanonical) {
    if (!byId.has(id)) throw new TypeError(`requested ID ${id} must name a service`);
  }

  // Detect cycles among required non-deployed services using DFS colors.
  const color = new Map(); // 0/absent unvisited, 1 visiting, 2 done
  const visit = (id) => {
    if (color.get(id) === 2) return;
    if (color.get(id) === 1) throw new Error("dependency cycle detected");
    color.set(id, 1);
    const svc = byId.get(id);
    for (const dep of svc.dependsOn) {
      if (!svc.alreadyDeployed && !byId.get(dep).alreadyDeployed && required.has(dep)) visit(dep);
    }
    color.set(id, 2);
  };
  for (const id of requestedCanonical) visit(id);

  // Build dependency-safe waves greedily.
  const waves = [];
  const placed = new Set();
  while (true) {
    const ready = [];
    for (const [id, svc] of byId) {
      if (placed.has(id)) continue;
      if (!required.has(id)) continue;
      if (svc.alreadyDeployed) continue;
      let ok = true;
      for (const dep of svc.dependsOn) {
        const depSvc = byId.get(dep);
        if (depSvc.alreadyDeployed || placed.has(dep)) continue;
        ok = false;
        break;
      }
      if (ok) ready.push(id);
    }

    if (ready.length === 0) {
      // If there are still required non-deployed services not placed, it's a cycle (should have been caught above).
      const remaining = [...required].some((id) => !placed.has(id) && !byId.get(id).alreadyDeployed);
      if (remaining) throw new Error("dependency cycle detected");
      break;
    }

    ready.sort((a, b) => {
      const pa = byId.get(a).priority;
      const pb = byId.get(b).priority;
      if (pa !== pb) return pb - pa;
      return byId.get(a).index - byId.get(b).index;
    });

    const selected = [];
    const usedGroups = new Set();
    for (const id of ready) {
      if (selected.length >= maxParallel) break;
      const group = byId.get(id).exclusiveGroup;
      if (group !== null && usedGroups.has(group)) continue;
      selected.push(id);
      if (group !== null) usedGroups.add(group);
    }

    waves.push(selected);
    for (const id of selected) placed.add(id);
  }

  const includedIds = [];
  for (const wave of waves) {
    for (const id of wave) includedIds.push(id);
  }

  return {
    requestedIds: [...requestedCanonical],
    includedIds,
    alreadySatisfiedIds: alreadySatisfied,
    waves
  };
}

export function planDeploymentWaves(requestedIds, services, options) {
  if (!Array.isArray(requestedIds)) throw new TypeError("requestedIds must be an array");
  if (!Array.isArray(services)) throw new TypeError("services must be an array");
  if (options !== undefined && !isPlainObject(options)) throw new TypeError("options must be a non-array object");

  const maxParallel = options?.maxParallel;
  if (typeof maxParallel !== "number" || !Number.isSafeInteger(maxParallel) || maxParallel <= 0) {
    throw new TypeError("options.maxParallel is required and must be a positive safe integer");
  }

  const requestedCanonical = [];
  for (const id of requestedIds) {
    const canonical = canonicalId(id, "requested ID");
    if (requestedCanonical.includes(canonical)) throw new TypeError("requested IDs must be unique after trimming");
    requestedCanonical.push(canonical);
  }

  return buildWaves(requestedCanonical, services, options);
}

export function describeWave(wave) {
  if (!Array.isArray(wave)) throw new TypeError("wave must be an array");
  return wave.join("+");
}
