export function listServiceIds(services) {
  if (!Array.isArray(services)) throw new TypeError("services must be an array");
  return services.map((service) => service.id);
}

export function planDeploymentWaves(requestedIds, services, options) {
  return {
    requestedIds: [...requestedIds],
    includedIds: [...requestedIds],
    alreadySatisfiedIds: [],
    waves: [[...requestedIds]]
  };
}

export function describeWave(wave) {
  if (!Array.isArray(wave)) throw new TypeError("wave must be an array");
  return wave.join("+");
}

