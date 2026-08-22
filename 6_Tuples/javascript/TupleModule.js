export default class DsTuple {
  constructor(...args) {
    if (args.length === 0) {
      throw new Error('DsTuple requires at least one item');
    }
    this.items = [...args];
  }

  get length() {
    return this.items.length;
  }

  toString() {
    if (this.items.length === 1) {
      return `(${String(this.items[0])},)`;
    }
    return `(${this.items.map((x) => String(x)).join(', ')})`;
  }

  *[Symbol.iterator]() {
    for (let i = 0; i < this.items.length; i += 1) {
      yield this.items[i];
    }
  }

  contains(value) {
    for (const item of this.items) {
      if (item === value) return true;
    }
    return false;
  }

  get(index) {
    return this.items[index];
  }

  add(other) {
    if (!(other instanceof DsTuple)) return null;
    return new DsTuple(...this.items, ...other.items);
  }

  mul(n) {
    const newItems = [];
    for (let i = 0; i < n; i += 1) {
      newItems.push(...this.items);
    }
    return new DsTuple(...newItems);
  }

  count(value = null) {
    if (value === null) return 0;
    let total = 0;
    for (const item of this.items) {
      if (item === value) total += 1;
    }
    return total;
  }

  index(value) {
    if (value === null) return -1;
    for (let i = 0; i < this.items.length; i += 1) {
      if (this.items[i] === value) return i;
    }
    return -1;
  }
}
