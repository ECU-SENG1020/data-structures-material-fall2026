# Set Data Structure Study Guide

## Learning goals

After studying this guide, you should be able to:

- Explain what makes a set different from a list or dictionary.
- Add, remove, and test for values in a Python set.
- Find the union, intersection, difference, and symmetric difference of sets.
- Describe the typical performance and limitations of a hash-based set.
- Choose a set when uniqueness or fast membership testing matters.

## What is a set?

A **set** is a collection of distinct values. If a value is added more than once, it is still stored only once. Sets are useful when you care whether a value is present, rather than where it occurs.

Python's built-in `set` is mutable and hash-based. It does not provide positional indexing, and its iteration order is not guaranteed. A set's elements must be **hashable**: numbers, strings, and many immutable values can be elements, but a list cannot. A tuple is hashable only when all of its elements are hashable.

The set is an abstract data type: uniqueness and set-algebra behavior are the defining ideas, while the implementation determines performance. Python's built-in set uses hashing. A simple custom set backed by a list, such as the course implementation, must scan values to check for membership.

## Creating and using sets

```python
colors = {"blue", "green", "blue"}
print(len(colors))  # 2: repeated values collapse into one

empty = set()       # {} creates an empty dictionary, not an empty set
from_list = set([1, 2, 2, 3])
print(from_list == {1, 2, 3})  # True

colors.add("red")
has_green = "green" in colors  # True

colors.remove("blue")  # removes the value; raises KeyError if it is absent
colors.discard("purple")  # does nothing if the value is absent
```

Use `clear()` to remove every element. Use `len(my_set)` to count the distinct values. You can iterate over a set with `for value in my_set`, but do not depend on the order in which values appear. `pop()` removes and returns an arbitrary element; it is not a way to request a particular value.

## Set algebra

Let:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
```

| Operation | Symbol | Meaning | Example result |
|---|---|---|---|
| Union | `a \| b` | Values in either set | `{1, 2, 3, 4, 5}` |
| Intersection | `a & b` | Values in both sets | `{3, 4}` |
| Difference | `a - b` | Values in `a`, but not `b` | `{1, 2}` |
| Symmetric difference | `a ^ b` | Values in exactly one set | `{1, 2, 5}` |

These operations create new sets and leave `a` and `b` unchanged. Difference is directional: `a - b` is not generally the same as `b - a`.

```python
print(a | b == {1, 2, 3, 4, 5})  # True
print(a & b == {3, 4})          # True
print(a - b == {1, 2})          # True
print(a ^ b == {1, 2, 5})       # True

a.update(b)  # in-place union: a now contains {1, 2, 3, 4, 5}
```

Set results have no guaranteed display order. The examples compare sets for equality rather than relying on how Python prints their elements.

## Hashing and performance

A hash-based set uses each value's hash to locate a place to store or find it. This is why membership tests and updates are usually fast. Hashes can collide, so the common performance is an average-case expectation, not a guarantee for every input.

For Python's built-in set, where `n` and `m` are the sizes of the operands:

| Operation | Typical/average time | Worst case |
|---|---:|---:|
| Membership, add, remove | `O(1)` | `O(n)` |
| Union | `O(n + m)` | Can degrade with many collisions |
| Intersection | `O(min(n, m))` expected | Can degrade with many collisions |
| Difference (`a - b`) | `O(n)` expected | Can degrade with many collisions |
| Storage for `n` values | `O(n)` | `O(n)` |

These are typical hash-table bounds, not rules for every possible set implementation. For example, a list-backed custom set needs `O(n)` time to check membership, so adding `n` distinct values one by one can take `O(n²)` total time. Choose complexity claims based on the implementation being discussed.

## When should you use a set?

Use a set when you need to:

- Remove duplicates from a collection.
- Repeatedly ask whether a value has been seen or is allowed.
- Compare groups of values using union, intersection, or difference.

| Structure | Best fit | Key difference |
|---|---|---|
| List | Keep sequence order, duplicates, or positional access | `value in items` requires a linear scan |
| Set | Keep unique values and test membership | No positional indexing or guaranteed iteration order |
| Dictionary | Associate each unique key with a value | Stores key-value pairs rather than values alone |

## Common pitfalls

- **Using `{}` for an empty set:** `{}` is an empty dictionary. Use `set()`.
- **Expecting duplicates to be retained:** adding an existing value does not change the set.
- **Depending on iteration order:** sort values for display only when the values can be compared and a sorted presentation is useful.
- **Adding mutable values:** lists and ordinary dictionaries are unhashable and cannot be set elements. A `frozenset` is immutable and can itself be a set element when its contents are hashable.
- **Confusing removal behavior:** Python's built-in `set.remove(value)` raises `KeyError` when the value is absent; `discard(value)` does not. A custom set implementation may define different behavior.
- **Assuming every set is hash-based:** the set abstraction guarantees uniqueness, not a particular implementation or complexity.

## Self-check

1. What does `set([2, 2, 5])` contain, and how many values does it have?
2. Given `x = {1, 2, 3}` and `y = {3, 4}`, what are `x & y` and `x - y`?
3. Why should a program avoid relying on the order of `for value in my_set`?
4. Which structure fits better: a list of steps where order and repeated steps matter, or a collection of unique course codes that will be checked for membership often?
5. What is the difference between `remove` and `discard` for a missing value in a Python built-in set?

### Answers

1. `{2, 5}`; it has 2 values.
2. `x & y` is `{3}`; `x - y` is `{1, 2}`.
3. A set does not guarantee positional or insertion order.
4. Use a list for the ordered steps and a set for the unique course codes.
5. `remove` raises `KeyError`; `discard` leaves the set unchanged without raising an error.
