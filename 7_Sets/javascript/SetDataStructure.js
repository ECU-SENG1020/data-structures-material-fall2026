export class MySet {
  constructor(...args) {
    this.data = [];
    for (const a of args) this.add(a);
  }

  get size() {
    return this.data.length;
  }

  add(value) {
    if (!this.data.includes(value)) this.data.push(value);
  }

  remove(value) {
    const idx = this.data.indexOf(value);
    if (idx !== -1) this.data.splice(idx, 1);
  }

  contains(value) {
    return this.data.includes(value);
  }

  [Symbol.iterator]() {
    return this.data[Symbol.iterator]();
  }

  union(other) {
    const out = new MySet();
    for (const x of this) out.add(x);
    for (const x of other) out.add(x);
    return out;
  }

  intersection(other) {
    const out = new MySet();
    for (const x of this) if (other.contains(x)) out.add(x);
    return out;
  }

  difference(other) {
    const out = new MySet();
    for (const x of this) if (!other.contains(x)) out.add(x);
    return out;
  }

  toString() {
    if (this.data.length === 0) return "set()";
    return `{${this.data.map(String).join(", ")}}`;
  }
}
