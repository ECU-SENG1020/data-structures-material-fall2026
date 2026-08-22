# Common "Special Methods" in JavaScript (Python dunder equivalents)

JavaScript doesn't have Python-style dunder methods like `__len__` or `__iter__`.
Instead, JavaScript uses:
- **method names** like `toString()`
- **Symbols** like `Symbol.iterator`

## Examples

### Printing / string conversion
- Implement `toString()`
- Or implement `[Symbol.toPrimitive](hint)` for more control

### Iteration
- Implement `[Symbol.iterator]()` to make `for..of` work:

```js
class MyThing {
  *[Symbol.iterator]() {
    yield 1;
    yield 2;
  }
}
```

### Membership ("in")
- Arrays: `array.includes(x)`
- Sets: `set.has(x)`
- Objects: `key in obj` checks keys, not values

### Length
- Arrays use `.length`
- Strings use `.length`
- For your own classes, you can create a `length` getter, but it won't integrate with a global `len()` like Python.

## Big difference
JavaScript **does not support operator overloading** (you cannot redefine `+`, `>=`, etc. for custom classes).
