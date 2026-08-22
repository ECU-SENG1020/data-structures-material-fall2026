import fs from "node:fs";
import crypto from "node:crypto";
import { DsDictionary, KeyError } from "./DsDictionaryModule.js";

const failures = [];
let successCount = 0;

function ok(name, fn) {
  try {
    fn();
    successCount++;
  } catch (e) {
    failures.push([name, String(e)]);
  }
}

ok("test_create_empty", () => {
  const d = new DsDictionary();
  if (d.length !== 0) throw new Error("Expected empty dictionary");
});

ok("test_create_non_empty", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
  ]);
  if (d.length !== 2) throw new Error("Expected length 2");
});

ok("test_set", () => {
  const d = new DsDictionary();
  d.set("a", 1);
  if (d.length !== 1) throw new Error("Expected length 1");
});

ok("test_get", () => {
  const d = new DsDictionary([["a", 1]]);
  if (d.get("a") !== 1) throw new Error("Expected value 1");
});

ok("test_overwrite_value", () => {
  const d = new DsDictionary();
  d.set("x", 5);
  d.set("x", 10);
  if (d.get("x") !== 10 || d.length !== 1) throw new Error("Overwrite failed");
});

ok("test_delitem", () => {
  const d = new DsDictionary();
  d.set("k", "v");
  d.delete("k");
  if (d.length !== 0) throw new Error("Expected empty after delete");
});

ok("test_keyerror", () => {
  const d = new DsDictionary();
  let threw = false;
  try {
    d.get("missing");
  } catch (e) {
    if (!(e instanceof KeyError)) throw e;
    threw = true;
  }
  if (!threw) throw new Error("KeyError not thrown");
});

ok("test_len", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
    ["c", 3],
  ]);
  if (d.length !== 3) throw new Error("Expected length 3");
});

ok("test_iter", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
    ["c", 3],
  ]);
  const keys = [...d];
  const expected = ["a", "b", "c"];
  if (JSON.stringify(keys) !== JSON.stringify(expected)) throw new Error("Iter mismatch");
});

ok("test_print_dsdictionary", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
  ]);
  const normalized = String(d).replace(/\s+/g, "");
  if (normalized !== "{'a':1,'b':2}") throw new Error(`Got ${normalized}`);
});

ok("test_print_keys", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
  ]);
  const normalized = String(d.keys()).replace(/\s+/g, "");
  if (normalized !== "DsDictionaryView_Keys(['a','b'])") throw new Error(`Got ${normalized}`);
});

ok("test_print_values", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
  ]);
  const normalized = String(d.values()).replace(/\s+/g, "");
  if (normalized !== "DsDictionaryView_Values([1,2])") throw new Error(`Got ${normalized}`);
});

ok("test_print_items", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
  ]);
  const normalized = String(d.items()).replace(/\s+/g, "");
  if (normalized !== "DsDictionaryView_Items([('a',1),('b',2)])") throw new Error(`Got ${normalized}`);
});

ok("test_values", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
  ]);
  const values = [...d.values()];
  if (JSON.stringify(values) !== JSON.stringify([1, 2])) throw new Error("Values mismatch");
});

ok("test_items", () => {
  const d = new DsDictionary([
    ["a", 1],
    ["b", 2],
  ]);
  const items = [...d.items()];
  if (JSON.stringify(items) !== JSON.stringify([
    ["a", 1],
    ["b", 2],
  ])) throw new Error("Items mismatch");
});

ok("test_view_reflects_changes", () => {
  const d = new DsDictionary([["a", 1]]);
  const keysView = d.keys();
  if (JSON.stringify([...keysView]) !== JSON.stringify(["a"])) throw new Error("Initial view mismatch");
  d.set("b", 2);
  if (JSON.stringify([...keysView]) !== JSON.stringify(["a", "b"])) throw new Error("View did not reflect changes");
});

function sha256NoWs(path) {
  const text = fs.readFileSync(path, "utf-8");
  const normalized = text.replace(/\s+/g, "");
  return crypto.createHash("sha256").update(normalized, "utf-8").digest("hex");
}

ok("test_file_hashes", () => {
  if (!fs.existsSync("file_hashes.json")) throw new Error("file_hashes.json not found");
  const expected = JSON.parse(fs.readFileSync("file_hashes.json", "utf-8"));
  for (const [fname, expHash] of Object.entries(expected)) {
    if (!fs.existsSync(fname)) throw new Error(`Missing file ${fname}`);
    const actual = sha256NoWs(fname);
    if (expHash !== actual) throw new Error(`Hash mismatch for ${fname}`);
  }
});

ok("test_builtin_dictionary_used", () => {
  const text = fs.readFileSync("DsDictionaryModule.js", "utf-8");
  if (/\bnew\s+Map\b/.test(text) || /\bMap\s*\(/.test(text)) {
    throw new Error("Built-in Map used in DsDictionaryModule.js");
  }
});

console.log("");
if (failures.length) {
  for (const [name, msg] of failures) console.log(`ERROR: ${name} -> ${msg}`);
  console.log(`\n${failures.length} tests failed`);
  console.log(`\n${successCount} tests passed\n`);
  process.exit(1);
}
console.log(`\nAll ${successCount} tests passed\n`);
