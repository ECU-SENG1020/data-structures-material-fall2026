// JavaScript Dictionary Demonstration
// Uses Map for dictionary-like key/value storage.

// 1. Creating dictionaries
const empty = new Map();
console.log("Empty Map:", empty);

const profile = new Map([
  ["name", "Ada"],
  ["role", "Engineer"],
]);
console.log("Profile:", profile);

// 2. Adding, updating, removing
const scores = new Map([
  ["alice", 90],
  ["bob", 82],
]);
console.log("Original:", scores);

scores.set("carol", 95);
console.log("After add carol:", scores);

scores.set("alice", 93);
console.log("After update alice:", scores);

const removed = scores.get("bob");
scores.delete("bob");
console.log("Deleted bob (value was):", removed, "Remaining:", scores);

console.log("Delete missing key returns:", scores.delete("missing"));

// 3. Membership, lookup, iteration
const inventory = new Map([
  ["pen", 10],
  ["notebook", 5],
  ["eraser", 2],
]);
console.log("Has 'pen'?", inventory.has("pen"));
console.log("Safe get marker:", inventory.has("marker") ? inventory.get("marker") : 0);

console.log("Keys:");
for (const key of inventory.keys()) {
  console.log(" ", key);
}

console.log("Values:");
for (const value of inventory.values()) {
  console.log(" ", value);
}

console.log("Entries:");
for (const [key, value] of inventory.entries()) {
  console.log(" ", key, "->", value);
}

// 4. Merge / copy / build from transforms
const a = new Map([
  ["x", 1],
  ["y", 2],
]);
const b = new Map([
  ["y", 20],
  ["z", 3],
]);
const merged = new Map([...a, ...b]);
console.log("Merged:", merged);

const squares = new Map(Array.from({ length: 6 }, (_, n) => [n, n * n]));
console.log("Squares:", squares);

// 5. Key type notes
const objectKeys = new Map();
const keyObj = { id: 1 };
objectKeys.set(keyObj, "record-1");
console.log("Object key lookup works:", objectKeys.get(keyObj));

console.log("JS dictionary demo complete");
