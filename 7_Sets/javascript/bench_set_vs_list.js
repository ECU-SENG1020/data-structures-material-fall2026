// Mirrors 6_Sets/python/bench_set_vs_list.py

import { performance } from "node:perf_hooks";

const PARAMS = [10_000, 100_000, 500_000];
const M = 10_000;

function makeQueries(n, m) {
  // Deterministic-ish without extra deps
  let state = 0x12345678;
  const out = new Array(m);
  for (let i = 0; i < m; i++) {
    state = (1103515245 * state + 12345) >>> 0;
    out[i] = state % n;
  }
  return out;
}

console.log(`Node: ${process.version}`);
console.log(`Membership queries per test: ${M}\n`);

for (const n of PARAMS) {
  const data = Array.from({ length: n }, (_, i) => i);
  const queries = makeQueries(n, M);

  const t0 = performance.now();
  const s = new Set(data);
  const t1 = performance.now();
  const setBuild = (t1 - t0) / 1000;

  let hitsList = 0;
  let start = performance.now();
  for (const q of queries) if (data.includes(q)) hitsList++;
  let end = performance.now();
  const listMembership = (end - start) / 1000;

  let hitsSet = 0;
  start = performance.now();
  for (const q of queries) if (s.has(q)) hitsSet++;
  end = performance.now();
  const setMembership = (end - start) / 1000;

  if (hitsList !== M || hitsSet !== M) throw new Error("Unexpected membership count");

  console.log(`n=${n}`);
  console.log(`  set build time:           ${setBuild.toFixed(6)} s`);
  console.log(`  list membership (m=${M}): ${listMembership.toFixed(6)} s`);
  console.log(`  set  membership (m=${M}): ${setMembership.toFixed(6)} s`);
  if (setMembership > 0) {
    console.log(
      `  membership speedup (list / set): ${(listMembership / setMembership).toFixed(1)}x`
    );
  }
  console.log("");
}

console.log("Note: speedups vary by CPU/cache and data sizes.");
console.log(
  "Interpretation: building the set is O(n) but gives ~O(1) membership; repeated array membership is O(n) per query."
);
