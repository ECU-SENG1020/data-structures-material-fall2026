export class MyHashedSet {
  constructor() {
    this.hashSet = new Map();
  }

  // Note: this is intentionally simplistic for teaching.
  // For objects, JSON.stringify can be unstable if key ordering differs.
  hash(value) {
    const t = typeof value;
    if (value === null) return "null";
    if (t === "string") return `s:${value}`;
    if (t === "number") return `n:${Object.is(value, -0) ? "-0" : String(value)}`;
    if (t === "boolean") return `b:${value}`;
    return `j:${JSON.stringify(value)}`;
  }

  add(value) {
    this.hashSet.set(this.hash(value), value);
  }

  remove(value) {
    this.hashSet.delete(this.hash(value));
  }

  contains(value) {
    return this.hashSet.has(this.hash(value));
  }

  [Symbol.iterator]() {
    return this.hashSet.values();
  }

  toString() {
    const items = [...this.hashSet.values()];
    if (items.length === 0) return "set()";
    return `{${items.map(String).join(", ")}}`;
  }
}
