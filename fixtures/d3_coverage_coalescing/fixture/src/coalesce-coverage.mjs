export function coalesceCoverage(windows) {
  return windows.map(({ start, end, label }) => ({
    start,
    end,
    labels: [label]
  }));
}
