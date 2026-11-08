# Study Guide: Tuple Data Structure

## What is a tuple?
A tuple is an ordered, immutable collection of Python objects. Tuples store a fixed sequence of elements and, because they're immutable, their contents cannot be changed after creation.

Key properties:
- Ordered — elements have a defined position and can be indexed.
- Immutable — once created, elements cannot be added, removed, or modified.
- Can contain mixed types (e.g., numbers, strings, other tuples).
- Tuples are hashable if and only if every element inside the tuple is hashable. This makes tuples useful as dictionary keys when appropriate.

## When to use a tuple
- Group related values that belong together and should not change (e.g., coordinates (x, y)).
- Use as lightweight records when you only need ordering and immutability.
- Use as dictionary keys when the composite key must be hashable.
- Return multiple values from a function (packing/unpacking).

## Complexity overview (average-case)
- Indexing (`t[i]`): O(1)
- Length (`len(t)`): O(1)
- Iteration: O(n)
- Membership test (`x in t`): O(n) — linear scan
- Concatenation (`t + u`): O(len(t) + len(u))
- Slicing (`t[a:b]`): O(k) where k is slice length (creates a new tuple)

Note: Tuples are typically cheaper than lists in memory and slightly faster for fixed-size sequences because immutability allows certain optimizations.

## Python API (common idioms and functions)
- Creation: `t = (1, 2, 3)` or `t = 1, 2, 3` or `tuple(iterable)`
- Single-element tuple: `t = (42,)` (notice the trailing comma)
- Unpacking / packing:
	- `a, b = (1, 2)` — unpacking
	- `a, *rest = (1, 2, 3)` — starred assignment
- Methods: tuples have only two built-in methods:
	- `t.count(x)` — number of times `x` appears
	- `t.index(x)` — index of first occurrence (raises `ValueError` if missing)
- Conversion: `list(t)` -> convert to list; `tuple(list_obj)` -> convert to tuple

## Indexing rules

Indexing is stricter than it first appears. Each rule below applies to the built-in tuple and to a tuple-like custom class such as the course `PirateCharter`:

- **Positive indexes** count from the front: `t[0]` is the first element, `t[2]` the third.
- **Negative indexes** count from the back: `t[-1]` is the last element and `t[-len(t)]` is the first.
- **Booleans work as indexes** because `bool` is a subclass of `int`: `t[False]` is `t[0]` and `t[True]` is `t[1]`.
- **Out-of-range indexes raise `IndexError`** — including every index on an empty tuple.
- **Non-integer indexes raise `TypeError`**: `t["0"]`, `t[1.0]`, and `t[None]` all fail. The built-in tuple accepts a `slice` (`t[a:b]`), but a custom class that supports only integer indexes raises `TypeError` for a slice too.

```py
t = ("gold", "ruby", "pearl")
t[2]        # 'pearl'
t[-1]       # 'pearl'
t[-3]       # 'gold'
t[True]     # 'ruby'  (True == 1)
t[3]        # IndexError
t[1.0]      # TypeError: indexes must be integers
```

## Immutability in practice

A tuple rejects every mutation attempt with `TypeError`:

```py
t = ("gold", "ruby")
t[0] = "silver"   # TypeError: no item assignment
del t[0]          # TypeError: no item deletion
```

Tuples also have **no mutator methods** — there is no `append`, `extend`, `insert`, `pop`, `remove`, `clear`, `sort`, or `reverse`. A well-built tuple-like class likewise omits all of them (and `__setitem__`/`__delitem__`), so the mutations above fail.

Immutability is **shallow**: the tuple stores references to its elements, and it never copies them. If an element is a mutable object, that object can still change, and the tuple will show the change:

```py
cargo = ["ruby"]
t = (cargo,)
cargo.append("pearl")
t[0]            # ['ruby', 'pearl'] — same object, now mutated
t[0] is cargo   # True
```

## Operators: concatenation and repetition

`+` and `*` never modify their operands; they always build and return a **new** tuple (even `t * 1` and `t + ()` return a new object in a custom class):

- **Concatenation (`t + u`)** joins two tuples in order. Both operands must be tuples (or the same custom class): `t + ["x"]`, `t + "x"`, and `t + 3` raise `TypeError`.
- **Repetition (`t * n` and `n * t`)** repeats the elements `n` times. Repetition works on either side (`__mul__` and `__rmul__`).
	- `n` must be an integer; `t * 2.0`, `t * "2"`, and `t * None` raise `TypeError`.
	- Zero or negative `n` produces an empty tuple.
	- Booleans count as integers: `t * True` equals `t * 1` and `False * t` is empty.
- Both operators copy **references**, not elements: after `pair = (cargo,) * 2`, `pair[0] is pair[1] is cargo`.

```py
first = ("gold", "ruby")
second = ("pearl",)
first + second       # ('gold', 'ruby', 'pearl'); first and second unchanged
first * 3            # ('gold', 'ruby', 'gold', 'ruby', 'gold', 'ruby')
2 * first            # ('gold', 'ruby', 'gold', 'ruby')
first * 0            # ()
first * -5           # ()
first + ["pearl"]    # TypeError
first * 2.0          # TypeError
```

## Membership, count, and index semantics

`in`, `count`, and `index` all match by **identity or equality**: a stored element matches when it `is` the searched value or compares `==` to it. This has two useful consequences:

- **Unhashable values work.** A tuple can contain a list, and `["ruby"] in (["ruby"],)` is `True` because the lists compare equal.
- **Identity rescues values that are not equal to themselves.** `float("nan") != float("nan")`, yet `nan in (nan,)` is `True` for the *same* `nan` object because identity is checked first. `count` and `index` find it the same way.

Behavior summary:

| Member | Found | Missing | No argument |
|---|---|---|---|
| `value in t` | `True` | `False` | — |
| `t.count(value)` | Number of matches (duplicates included) | `0` | `TypeError` |
| `t.index(value)` | Index of the **first** match | `ValueError` | `TypeError` |

```py
t = ("gold", "ruby", "gold", None)
"ruby" in t          # True
"emerald" not in t   # True
t.count("gold")      # 2
t.count(None)        # 1
t.count("emerald")   # 0
t.index("gold")      # 0 — first match only
t.index("emerald")   # ValueError
```

## Iteration behavior

Iterating a tuple yields every element — duplicates included — in stored order. Iteration is **repeatable**: you can loop over the same tuple any number of times. Each call to `iter(t)` returns a **fresh, independent iterator**, so two loops (or `next` calls on two iterators) do not interfere:

```py
t = (1, 2, 3)
first = iter(t)
second = iter(t)
next(first)      # 1
next(first)      # 2
next(second)     # 1 — unaffected by first
list(first)      # [3]
list(second)     # [2, 3]
```

## Display and repr

Python displays a tuple with parentheses, and a **single-element tuple keeps its trailing comma** so the text is unambiguous: `str((42,))` is `'(42,)'`, not `'(42)'`. A custom class follows the same convention in its `__str__`/`__repr__`:

```py
str(PirateCharter())                     # "PirateCharter()"
str(PirateCharter("ruby"))               # "PirateCharter('ruby',)"
str(PirateCharter("gold coin", 2, None)) # "PirateCharter('gold coin', 2, None)"
```

Note that elements are shown with their `repr` (strings get quotes, `None` is bare), and a constructor call like `PirateCharter(["a", "b"])` stores the list as **one element** — a single argument is never unpacked.

## Special methods behind the syntax

Each tuple behavior maps to a special ("dunder") method that a custom tuple-like class implements:

| Expression | Special method | Expected behavior |
|---|---|---|
| `PirateCharter(1, 2, 3)` | `__init__(self, *items)` | Stores all arguments in order, duplicates kept; a single argument stays one element |
| `len(t)` | `__len__` | Number of elements (0 for empty) |
| `t[i]` | `__getitem__` | Positive, negative, and boolean integer indexes; `IndexError` out of range; `TypeError` for non-integers |
| `t[i] = x` / `del t[i]` | `__setitem__` / `__delitem__` **absent** | `TypeError`: immutable |
| `for v in t` / `iter(t)` | `__iter__` | Fresh independent iterator each call; order and duplicates preserved |
| `value in t` | `__contains__` | `True` when an element `is` or `==` the value |
| `print(t)` / `str(t)` | `__str__` / `__repr__` | `PirateCharter('ruby',)` style, trailing comma for one element |
| `t + u` | `__add__` | New object; `TypeError` for non-tuple operands |
| `t * n` | `__mul__` | New object; integer counts only; `<= 0` gives empty |
| `n * t` | `__rmul__` | Same as `t * n` with the integer on the left |



## Examples (Python)
```py
# creation
t = (1, 'a', 3.14)
t2 = tuple([4,5,6])

# single element
single = (42,)

# unpacking
point = (10, 20)
x, y = point

# functions returning tuples
def min_max(seq):
		return (min(seq), max(seq))

low, high = min_max([3, 1, 7])

# tuples as dict keys
coords = {}
coords[(0,0)] = 'origin'

# immutability example (this will raise)
# t[0] = 99  -> TypeError
```

## Tuple vs List — quick comparison
- Mutability: lists are mutable, tuples are immutable.
- Use lists when you need to modify, append, or reorder elements frequently.
- Use tuples when the sequence is fixed, for hashability, or when conveying "this data shouldn't change".
- Performance: tuples generally use slightly less memory and can be marginally faster for iteration and attribute access since they're fixed-size.

## Common pitfalls and notes
- Single-element tuple requires a trailing comma: `(1,)` not `(1)`. The same comma appears when Python prints a one-element tuple.
- Tuples are hashable only if all elements inside are hashable. E.g., `(1, 2, (3, 4))` is hashable; `(1, [2, 3])` is not.
- Don’t mistake immutability of the tuple for immutability of its contents: a tuple can contain a mutable object (e.g., a list) which can still be modified:
	- `t = (1, [2,3]); t[1].append(4)` is allowed.
- Membership (`x in t`) is O(n); for large collections where you need frequent membership tests, use a `set` instead.
- `t.index(x)` raises `ValueError` when `x` is missing; `t.count(x)` just returns `0`. Both require an argument — calling them with none raises `TypeError`.
- `index` reports only the **first** match even when the value appears more than once.
- Mixing types with the operators fails: `t + [1]` and `t * 2.0` raise `TypeError`. Convert first (`t + tuple([1])`) if that is what you mean.
- `t * 0` and `t * -5` quietly produce an empty tuple — negative counts are not an error.
- `t[True]` is legal and means `t[1]`, because booleans are integers. This can hide bugs when a boolean reaches an indexing expression.
- Wrapping a single iterable does not unpack it: `PirateCharter(["a", "b"])` has length 1, while `tuple(["a", "b"])` has length 2 — the built-in `tuple(iterable)` constructor is the special case.

## Practical use-cases
- Fixed-size records (coordinates, RGB colors, database row keys).
- Function returns for multiple values without creating a custom class.
- Lightweight immutable keys for dictionaries and sets (when elements are hashable).

## Practice Examples
1) Write a function that swaps the first and last elements of a 3-tuple and returns a new tuple.
2) Given a list of tuples (pairs), write a function to unzip them into two lists.
3) Demonstrate when a tuple is hashable and when it is not with code examples.
4) Predict the result of each expression for `t = ("gold", "ruby")`: `t[-2]`, `t[True]`, `t[2]`, `t["0"]`.
5) What do `t * 0`, `t * -3`, and `2 * t` evaluate to, and which exception does `t * "2"` raise?
6) For `t = ("gold", "ruby", "gold")`, what are `t.count("gold")`, `t.index("gold")`, and `t.index("pearl")`?
7) After `cargo = ["ruby"]; t = (cargo,); cargo.append("pearl")`, what is `t[0]`? Did the tuple change?
8) Which special methods make `len(t)`, `t[i]`, `value in t`, `t + u`, and `2 * t` work?

### Answers (brief)
1)
```py
def swap_first_last(t):
		a, b, c = t
		return (c, b, a)
```
2)
```py
def unzip(pairs):
		return [a for a, _ in pairs], [b for _, b in pairs]

# or using zip
# a_list, b_list = map(list, zip(*pairs))
```
3)
```py
# hashable
ht = (1, 2, (3, 4))
hash(ht)  # works

# unhashable because inner list
ut = (1, [2, 3])
try:
		hash(ut)
except TypeError:
		print('not hashable')
```
4) `t[-2]` is `'gold'`; `t[True]` is `'ruby'` (True == 1); `t[2]` raises `IndexError`; `t["0"]` raises `TypeError`.
5) `t * 0` and `t * -3` are `()`; `2 * t` is `('gold', 'ruby', 'gold', 'ruby')`; `t * "2"` raises `TypeError`.
6) `t.count("gold")` is `2`; `t.index("gold")` is `0` (first match only); `t.index("pearl")` raises `ValueError`.
7) `t[0]` is `['ruby', 'pearl']`. The tuple did not change — it still holds the same reference; the list it refers to mutated (shallow immutability).
8) `__len__`, `__getitem__`, `__contains__`, `__add__`, and `__rmul__` (with `__mul__` handling `t * 2`).

## One-page cheat-sheet
- Create: `t = (1, 2)` or `t = tuple(iterable)`
- Single element: `t = (x,)` — and it prints with the trailing comma: `('x',)`
- Length: `len(t)`
- Indexing: `t[i]`, `t[-1]`; out of range → `IndexError`; non-integer index → `TypeError`
- Immutable: `t[i] = x` and `del t[i]` → `TypeError`; no `append`/`pop`/`sort`; contents are shared references (shallow)
- Operators: `t + u` (tuples only), `t * n` / `n * t` (integers only; `n <= 0` → empty); both return new tuples
- Membership: `value in t` — matches by identity (`is`) or equality (`==`); works with unhashable elements
- Iterate: `for v in t` — ordered, duplicates kept, repeatable; `iter(t)` gives independent iterators
- Unpack: `a, b = t`
- Methods: `t.count(x)` (missing → `0`), `t.index(x)` (first match; missing → `ValueError`)
- Convert: `list(t)` / `tuple(list_obj)`
- Hashable if all elements are hashable: usable as dict keys


