function isPlainObject(value) {
  if (value === null || typeof value !== "object") return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

function isNonArrayObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function clone(value) {
  return structuredClone(value);
}

export function foldDeviceEvents(events) {
  if (!Array.isArray(events)) throw new TypeError("events must be an array");

  const groups = new Map();
  for (const event of events) {
    if (!isNonArrayObject(event)) throw new TypeError("each event must be an object");
    const { deviceId, sequence, kind } = event;
    if (typeof deviceId !== "string" || deviceId.length === 0 || deviceId !== deviceId.trim()) {
      throw new TypeError("deviceId must be a non-empty canonical string");
    }
    if (!Number.isInteger(sequence) || sequence <= 0) {
      throw new RangeError("sequence must be a positive integer");
    }
    if (!new Set(["snapshot", "patch", "delete"]).has(kind)) {
      throw new TypeError("kind must be snapshot, patch, or delete");
    }
    if (kind === "snapshot" && !isPlainObject(event.state)) {
      throw new TypeError("snapshot state must be a plain object");
    }
    if (kind === "patch" && !isPlainObject(event.changes)) {
      throw new TypeError("patch changes must be a plain object");
    }
    if (!groups.has(deviceId)) groups.set(deviceId, []);
    groups.get(deviceId).push(event);
  }

  const result = [];
  for (const [deviceId, original] of groups) {
    const ordered = [...original].sort((left, right) => left.sequence - right.sequence);
    for (let index = 0; index < ordered.length; index += 1) {
      const event = ordered[index];
      if (event.sequence !== index + 1) {
        throw new RangeError("device sequence must start at 1 and remain contiguous");
      }
      if (index === 0 && event.kind !== "snapshot") {
        throw new RangeError("first device event must be a snapshot");
      }
      if (index > 0 && event.kind === "snapshot") {
        throw new RangeError("later device events cannot be snapshots");
      }
      if (event.kind === "delete" && index !== ordered.length - 1) {
        throw new RangeError("delete must be the final device event");
      }
    }

    let state = clone(ordered[0].state);
    let active = true;
    for (const event of ordered.slice(1)) {
      if (event.kind === "patch") {
        for (const [key, value] of Object.entries(event.changes)) {
          if (value === null) delete state[key];
          else state[key] = clone(value);
        }
      } else if (event.kind === "delete") {
        active = false;
      }
    }
    if (active) {
      result.push({
        deviceId,
        sequence: ordered.at(-1).sequence,
        state: clone(state)
      });
    }
  }
  return result;
}
