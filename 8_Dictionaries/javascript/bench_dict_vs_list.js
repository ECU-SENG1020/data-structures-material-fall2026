// Benchmark: compare dictionary key lookup vs array scan.
// Mirrors the spirit of 7_Sets/javascript/bench_set_vs_list.js.

import { performance } from "node:perf_hooks";

const PARAMS = [10_000, 100_000, 500_000];
const M = 10_000;

function makeQueries(n, m) {
  let state = 0x12345678;
  const out = new Array(m);
  for (let i = 0; i < m; i++) {
    state = (1103515245 * state + 12345) >>> 0;
    out[i] = `k_${state % n}`;
  }
  return out;
}

console.log(`Node: ${process.version}`);
console.log(`Key lookup queries per test: ${M}\n`);

for (const n of PARAMS) {
  const entries = Array.from({ length: n }, (_, i) => [`k_${i}`, i]);
  const queries = makeQueries(n, M);

  const t0 = performance.now();
  const dict = new Map(entries);
  const t1 = performance.now();
  const dictBuild = (t1 - t0) / 1000;

  let hitsArray = 0;
  let start = performance.now();
  for (const q of queries) {
    const found = entries.find(([k]) => k === q);
    if (found) hitsArray++;
  }
  let end = performance.now();
  const arrayScan = (end - start) / 1000;

  let hitsDict = 0;
  start = performance.now();
  for (const q of queries) {
    if (dict.has(q)) hitsDict++;
  }
  end = performance.now();
  const dictLookup = (end - start) / 1000;

  if (hitsArray !== M || hitsDict !== M) {
    throw new Error("Unexpected hit count");
  }

  console.log(`n=${n}`);
  console.log(`  dict build time:           ${dictBuild.toFixed(6)} s`);
  console.log(`  array scan lookup (m=${M}): ${arrayScan.toFixed(6)} s`);
  console.log(`  dict key lookup (m=${M}):   ${dictLookup.toFixed(6)} s`);
  if (dictLookup > 0) {
    console.log(`  lookup speedup (array / dict): ${(arrayScan / dictLookup).toFixed(1)}x`);
  }
  console.log("");
}

console.log("Note: speedups vary by CPU/cache and data sizes.");
console.log("Interpretation: building the dictionary is O(n), repeated key lookups are typically O(1).");
