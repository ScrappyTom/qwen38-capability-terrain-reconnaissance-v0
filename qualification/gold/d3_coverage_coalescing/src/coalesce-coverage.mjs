export function coalesceCoverage(windows) {
  if (!Array.isArray(windows)) {
    throw new TypeError("windows must be an array");
  }

  // Validate entries and attach original index for stable sort
  const entries = windows.map((entry, index) => {
    if (entry === null || typeof entry !== "object") {
      throw new TypeError("each entry must be an object");
    }
    const { start, end, label } = entry;
    if (typeof start !== "number" || !Number.isInteger(start)) {
      throw new RangeError("start must be an integer");
    }
    if (typeof end !== "number" || !Number.isInteger(end)) {
      throw new RangeError("end must be an integer");
    }
    if (start >= end) {
      throw new RangeError("start must be less than end");
    }
    if (typeof label !== "string" || label.length === 0) {
      throw new TypeError("label must be a non-empty string");
    }
    return { start, end, label, index };
  });

  // Stable sort by ascending start, then ascending end, then original position
  entries.sort((a, b) => {
    if (a.start !== b.start) return a.start - b.start;
    if (a.end !== b.end) return a.end - b.end;
    return a.index - b.index;
  });

  // Merge overlapping or touching windows
  const result = [];
  for (const { start, end, label } of entries) {
    const last = result[result.length - 1];
    if (last && start <= last.end) {
      // Merge: extend the end if needed
      if (end > last.end) {
        last.end = end;
      }
      // Add label if not already present
      if (!last.labels.includes(label)) {
        last.labels.push(label);
      }
    } else {
      // New disjoint group
      result.push({ start, end, labels: [label] });
    }
  }

  return result;
}
