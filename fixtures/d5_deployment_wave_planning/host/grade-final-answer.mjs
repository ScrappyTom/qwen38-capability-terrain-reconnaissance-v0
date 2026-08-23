#!/usr/bin/env node
import { readFile } from "node:fs/promises";

const file = process.argv[2];
if (!file) throw new Error("usage: node grade-final-answer.mjs <final-answer-text-file>");
const answer = await readFile(file, "utf8");
const labels = ["Root cause", "Files changed", "Verification", "Remaining limitations"];
const sections = [];
let previous = -1;
for (let index = 0; index < labels.length; index += 1) {
  const label = labels[index];
  const start = answer.indexOf(`${label}:`);
  const next = index + 1 < labels.length ? answer.indexOf(`${labels[index + 1]}:`, start + label.length + 1) : answer.length;
  const content = start === -1 || next === -1 ? "" : answer.slice(start + label.length + 1, next).trim();
  sections.push({ label, present: start !== -1, ordered: start > previous, substantive: content.length >= 20, characters: content.length });
  previous = start;
}
const result = { schema_version: 1, grader: "experiment-107-final-answer-contract", exact_declared_labels: labels, minimum_section_characters: 20, minimum_total_characters: 180, sections, total_characters: answer.trim().length, passed: sections.every((section) => section.present && section.ordered && section.substantive) && answer.trim().length >= 180 };
process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
if (!result.passed) process.exitCode = 1;

