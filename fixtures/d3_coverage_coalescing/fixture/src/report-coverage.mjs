import { coalesceCoverage } from "./coalesce-coverage.mjs";

export function reportCoverage(windows) {
  return coalesceCoverage(windows).map((window) => `${window.start}-${window.end}:${window.labels.join(",")}`);
}
