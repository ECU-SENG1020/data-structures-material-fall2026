# Set Data Structure Study Guide

## Learning goals

After studying this guide, you should be able to:

- Explain what makes a set different from a list or dictionary.
- Add, remove, and test for values in a Python set.
- Find the union, intersection, difference, and symmetric difference of sets using both named methods and operators.
- Test subset and superset relationships and compare sets for equality.
- Name the special (dunder) methods behind `len`, `in`, `bool`, `repr`, iteration, `==`, and the set operators.
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

### Core members at a glance

| Member | What it does | Missing-value behavior |
|---|---|---|
| `add(value)` | Inserts the value; a duplicate is silently ignored and the set is unchanged | — |
| `remove(value)` | Deletes the value | Raises `KeyError` |
| `discard(value)` | Deletes the value | Silently does nothing |
| `clear()` | Empties the set so `len` is `0` and iteration yields nothing | — |
| `copy()` | Returns a new, independent set with the same members | — |

### Copying sets

`copy()` performs a **shallow copy**: the result is a distinct object (`clone is original` is `False`) that compares equal (`clone == original` is `True`). Changing the copy afterward does not change the original:

```python
treasure = {"gold coin", "ruby"}
clone = treasure.copy()
clone.add("map")
print("map" in clone)     # True
print("map" in treasure)  # False
```

### Truthiness

A set participates in boolean contexts: an empty set is falsy and a non-empty set is truthy.

```python
print(bool(set()))       # False
print(bool({"ruby"}))    # True
if treasure:
    print("the chest is not empty")
```

## Set algebra

Let:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
```

| Operation | Named method | Operator | Meaning | Example result |
|---|---|---|---|---|
| Union | `a.union(b)` | `a \| b` | Values in either set | `{1, 2, 3, 4, 5}` |
| Intersection | `a.intersection(b)` | `a & b` | Values in both sets | `{3, 4}` |
| Difference | `a.difference(b)` | `a - b` | Values in `a`, but not `b` | `{1, 2}` |
| Symmetric difference | `a.symmetric_difference(b)` | `a ^ b` | Values in exactly one set | `{1, 2, 5}` |

Each named method and its operator produce the same result. These operations create new sets and leave `a` and `b` unchanged. Difference is directional: `a - b` is not generally the same as `b - a`.

```python
print(a | b == {1, 2, 3, 4, 5})  # True
print(a & b == {3, 4})          # True
print(a - b == {1, 2})          # True
print(a ^ b == {1, 2, 5})       # True

a.update(b)  # in-place union: a now contains {1, 2, 3, 4, 5}
```

Set results have no guaranteed display order. The examples compare sets for equality rather than relying on how Python prints their elements.

### Subset and superset tests

`issubset` asks "is every one of my values in the other set?" `issuperset` asks the reverse. Both return a `bool`, and both are directional:

```python
mine = {"ruby", "gold coin"}
chest = {"gold coin", "ruby", "pearl"}

print(mine.issubset(chest))    # True: every item of mine is in the chest
print(chest.issubset(mine))    # False: the chest has an extra pearl
print(chest.issuperset(mine))  # True
print(mine.issuperset(chest))  # False
```

Python's built-in set also supports the comparison operators `<=` (subset) and `>=` (superset). Every set is a subset and a superset of itself.

### Set equality

Two sets are equal (`==`) when they contain the same members, regardless of the order in which the values were added. `!=` is the negation:

```python
left = {"ruby", "gold coin"}
right = {"gold coin", "ruby"}
print(left == right)             # True: same members, order ignored
print(left != {"ruby", "map"})   # True: different members
```

### Operand type rules

The operators and the named methods differ in what they accept:

- **Operators (`|`, `&`, `-`, `^`) require another set.** Mixing a set with a non-set like a list raises `TypeError`: `{"ruby"} | ["ruby"]` fails.
- **Built-in set named methods accept any iterable:** `{"ruby"}.union(["map"])` works because Python converts the iterable.
- **A custom set class chooses its own rules.** The course `PirateSet` raises `TypeError` from its named methods when the argument is not a `PirateSet`, and its operators reject non-`PirateSet` operands as unsupported.

When you implement an operator in your own class and the other operand's type is unsupported, return the special constant `NotImplemented` (or raise `TypeError`). Returning `NotImplemented` lets Python try the other operand's implementation before raising `TypeError` itself.

## Special methods behind the syntax

Every piece of set syntax is powered by a special ("dunder") method. A custom set-like class, such as the course `PirateSet`, implements these to behave like a set:

| Expression | Special method | Expected behavior |
|---|---|---|
| `PirateSet("a", "b", "a")` | `__init__(self, *items)` | Stores each distinct value once; a list-backed set keeps insertion order |
| `len(s)` | `__len__` | Number of distinct values |
| `for v in s` / `list(s)` | `__iter__` | Yields each value once; a list-backed set yields in insertion order |
| `value in s` | `__contains__` | `True` if a stored value is the same object (`is`) or equal (`==`) |
| `bool(s)` / `if s:` | `__bool__` | `False` when empty, `True` otherwise |
| `repr(s)` | `__repr__` | Readable text such as `PirateSet('gold coin', 'ruby')` |
| `s == t` / `s != t` | `__eq__` | Same members, order ignored |
| `s \| t` | `__or__` | Union |
| `s & t` | `__and__` | Intersection |
| `s - t` | `__sub__` | Difference |
| `s ^ t` | `__xor__` | Symmetric difference |

Two behaviors differ between the built-in set and a list-backed custom set:

- **Order:** the built-in set guarantees no order, while a list-backed set naturally preserves insertion order (the unit tests rely on that order). Union keeps the left set's values first, then the right set's new values; intersection and difference keep the left set's order.
- **Membership:** the built-in set requires hashable values, so a list cannot be an element. A list-backed set that checks `is` or `==` directly can store unhashable values such as lists, and `["ruby"] in pirate_set` is `True` when an equal list was stored.

```python
value = ["ruby"]                 # unhashable: rejected by the built-in set
treasure = PirateSet(value)
print(value in treasure)         # True: same object (is)
print(["ruby"] in treasure)      # True: equal value (==)
```


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
- **Mixing operand types with operators:** `my_set | some_list` raises `TypeError`. Use the named method with an iterable, or convert the other operand to a set first.
- **Mutating a copy and expecting the original to change:** `copy()` returns an independent set; additions and removals on the copy do not affect the original.
- **Reversing a subset test:** `a.issubset(b)` and `b.issubset(a)` ask different questions. Only one may be true when the sets differ in size.
- **Assuming every set is hash-based:** the set abstraction guarantees uniqueness, not a particular implementation or complexity.

## Self-check

1. What does `set([2, 2, 5])` contain, and how many values does it have?
2. Given `x = {1, 2, 3}` and `y = {3, 4}`, what are `x & y` and `x - y`?
3. Why should a program avoid relying on the order of `for value in my_set`?
4. Which structure fits better: a list of steps where order and repeated steps matter, or a collection of unique course codes that will be checked for membership often?
5. What is the difference between `remove` and `discard` for a missing value in a Python built-in set?
6. Which special methods make `len(s)`, `value in s`, `bool(s)`, and `s ^ t` work?
7. After `clone = treasure.copy()` and `clone.add("map")`, is `"map"` in `treasure`? Are `clone` and `treasure` the same object?
8. Given `mine = {"ruby"}` and `chest = {"ruby", "pearl"}`, what do `mine.issubset(chest)` and `mine.issuperset(chest)` return?
9. Do `{"a", "b"}` and `{"b", "a"}` compare equal? Why?
10. What happens when you evaluate `{"ruby"} | ["ruby"]`, and what should a custom class's operator method do with an unsupported operand type?

### Answers

1. `{2, 5}`; it has 2 values.
2. `x & y` is `{3}`; `x - y` is `{1, 2}`.
3. A set does not guarantee positional or insertion order.
4. Use a list for the ordered steps and a set for the unique course codes.
5. `remove` raises `KeyError`; `discard` leaves the set unchanged without raising an error.
6. `__len__`, `__contains__`, `__bool__`, and `__xor__`.
7. `"map"` is not in `treasure`; `clone` is a distinct object (`clone is treasure` is `False`) even though it compared equal before the `add`.
8. `mine.issubset(chest)` is `True`; `mine.issuperset(chest)` is `False`.
9. Yes. Set equality compares members only and ignores the order values were added.
10. `TypeError` is raised because the `|` operator requires another set. A custom operator method should return `NotImplemented` (or raise `TypeError`) for an unsupported operand type.
