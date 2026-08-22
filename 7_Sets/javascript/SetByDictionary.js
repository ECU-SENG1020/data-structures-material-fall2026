export class MySetDict {
  constructor(...args) {
    this.data = new Map();
    for (const a of args) this.add(a);
  }

  get size() {
    return this.data.size;
  }

  add(value) {
    this.data.set(value, true);
  }

  remove(value) {
    this.data.delete(value);
  }

  contains(value) {
    return this.data.has(value);
  }

  copy() {
    const out = new MySetDict();
    for (const k of this.data.keys()) out.add(k);
    return out;
  }

  [Symbol.iterator]() {
    return this.data.keys();
  }

  union(other) {
    const out = new MySetDict();
    for (const x of this) out.add(x);
    for (const x of other) out.add(x);
    return out;
  }

  intersection(other) {
    const out = new MySetDict();
    for (const x of this) if (other.contains(x)) out.add(x);
    return out;
  }

  difference(other) {
    const out = new MySetDict();
    for (const x of this) if (!other.contains(x)) out.add(x);
    return out;
  }

  toString() {
    const items = [...this.data.keys()];
    if (items.length === 0) return "set()";
    return `{${items.map(String).join(", ")}}`;
  }
}
