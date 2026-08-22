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
- Single-element tuple requires a trailing comma: `(1,)` not `(1)`.
- Tuples are hashable only if all elements inside are hashable. E.g., `(1, 2, (3, 4))` is hashable; `(1, [2, 3])` is not.
- Don’t mistake immutability of the tuple for immutability of its contents: a tuple can contain a mutable object (e.g., a list) which can still be modified:
	- `t = (1, [2,3]); t[1].append(4)` is allowed.
- Membership (`x in t`) is O(n); for large collections where you need frequent membership tests, use a `set` instead.

## Practical use-cases
- Fixed-size records (coordinates, RGB colors, database row keys).
- Function returns for multiple values without creating a custom class.
- Lightweight immutable keys for dictionaries and sets (when elements are hashable).

## Practice Examples
1) Write a function that swaps the first and last elements of a 3-tuple and returns a new tuple.
2) Given a list of tuples (pairs), write a function to unzip them into two lists.
3) Demonstrate when a tuple is hashable and when it is not with code examples.

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

## One-page cheat-sheet
- Create: `t = (1, 2)` or `t = tuple(iterable)`
- Single element: `t = (x,)`
- Length: `len(t)`
- Indexing: `t[i]`
- Unpack: `a, b = t`
- Methods: `t.count(x)`, `t.index(x)`
- Convert: `list(t)` / `tuple(list_obj)`
- Hashable if all elements are hashable: usable as dict keys


