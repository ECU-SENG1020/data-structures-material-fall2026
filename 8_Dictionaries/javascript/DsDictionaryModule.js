export class KeyError extends Error {
  constructor(key) {
    super(`KeyError: ${String(key)}`);
    this.name = "KeyError";
    this.key = key;
  }
}

function reprPy(value) {
  if (typeof value === "string") {
    const escaped = value.replace(/\\/g, "\\\\").replace(/'/g, "\\'");
    return `'${escaped}'`;
  }
  if (Array.isArray(value) && value.length === 2) {
    return `(${reprPy(value[0])}, ${reprPy(value[1])})`;
  }
  return String(value);
}

function listStr(values) {
  return `[${values.map(reprPy).join(", ")}]`;
}

export class DsDictionaryView {
  constructor(store, viewType) {
    this._store = store; // reference to underlying store (live view)
    this._viewType = viewType;
  }

  toString() {
    if (this._viewType === "keys") {
      const keys = this._store.map(([k]) => k);
      return `DsDictionaryView_Keys(${listStr(keys)})`;
    }
    if (this._viewType === "values") {
      const values = this._store.map(([, v]) => v);
      return `DsDictionaryView_Values(${listStr(values)})`;
    }
    if (this._viewType === "items") {
      const items = this._store.map(([k, v]) => [k, v]);
      return `DsDictionaryView_Items(${listStr(items)})`;
    }
    throw new Error("Invalid view type");
  }

  *[Symbol.iterator]() {
    if (this._viewType === "keys") {
      for (const [k] of this._store) yield k;
      return;
    }
    if (this._viewType === "values") {
      for (const [, v] of this._store) yield v;
      return;
    }
    if (this._viewType === "items") {
      for (const [k, v] of this._store) yield [k, v];
      return;
    }
    throw new Error("Invalid view type");
  }
}

export class DsDictionary {
  constructor(items = null) {
    this._store = [];
    if (items != null) {
      for (const [k, v] of items) {
        this._store.push([k, v]);
      }
    }
  }

  toString() {
    const parts = this._store.map(([k, v]) => `${reprPy(k)}: ${reprPy(v)}`);
    return `{${parts.join(", ")}}`;
  }

  set(key, value) {
    for (let i = 0; i < this._store.length; i++) {
      const [k] = this._store[i];
      if (k === key) {
        this._store[i] = [key, value];
        return;
      }
    }
    this._store.push([key, value]);
  }

  get(key) {
    for (const [k, v] of this._store) {
      if (k === key) return v;
    }
    throw new KeyError(key);
  }

  delete(key) {
    for (let i = 0; i < this._store.length; i++) {
      const [k] = this._store[i];
      if (k === key) {
        this._store.splice(i, 1);
        return;
      }
    }
    throw new KeyError(key);
  }

  get length() {
    return this._store.length;
  }

  *[Symbol.iterator]() {
    for (const [k] of this._store) yield k;
  }

  keys() {
    return new DsDictionaryView(this._store, "keys");
  }

  values() {
    return new DsDictionaryView(this._store, "values");
  }

  items() {
    return new DsDictionaryView(this._store, "items");
  }
}
