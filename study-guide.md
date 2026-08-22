# Data Structures Study Guide
### Topics: Arrays · Nodes · Singly Linked Lists · List Data Structures · Tuples · Sets · Dictionaries

---

## Part 1: Key Terminology

Before diving into specific structures, understand these foundational classification terms:

| Term | Description |
|---|---|
| **Linear** | Elements are arranged sequentially, one after another. |
| **Non-Linear** | Elements are arranged hierarchically or in a network. |
| **Homogeneous** | All elements must be the same data type. |
| **Heterogeneous** | Elements can be of different data types. |
| **Indexed** | Each element can be accessed directly using an index. |
| **Unindexed** | Elements are not directly accessible by position. |
| **Ordered** | Elements maintain a specific, predictable sequence. |
| **Unordered** | No guaranteed order of elements. |
| **Mutable** | Elements can be changed after creation. |
| **Immutable** | Elements cannot be changed after creation. |
| **Static** | Size is fixed at creation and cannot change. |
| **Dynamic** | Size can grow or shrink as needed. |
| **Unique** | No duplicate elements allowed. |
| **Duplicates** | Duplicate elements are permitted. |

---

## Part 2: Arrays

### What Is an Array?

An **array** is a **linear**, **homogeneous**, **static** data structure that stores elements in a **contiguous block of memory**. Each element is accessed using a zero-based **index**, which allows for **constant-time (O(1)) random access**.

### Characteristics at a Glance

| Characteristic | Value |
|---|---|
| Linear / Non-Linear | **Linear** |
| Homogeneous / Heterogeneous | **Homogeneous** |
| Indexed / Unindexed | **Indexed** |
| Ordered / Unordered | **Ordered** |
| Mutable / Immutable | **Mutable** |
| Dynamic / Static | **Static** |
| Unique / Duplicates | **Duplicates allowed** |

### Memory Layout & Address Calculation

Array elements are stored in consecutive memory locations. Because the size of each element is known, you can calculate the exact memory address of any element directly:

```
Address of element[i] = BaseAddress + (i × SizeOfElement)
```

**Example:** An array of `doubles` (8 bytes each) with base address `1000`:
- `array[0]` → address `1000`
- `array[1]` → address `1000 + (1 × 8) = 1008`
- `array[2]` → address `1000 + (2 × 8) = 1016`
- `array[n]` → address `1000 + (n × 8)`

This direct computation is why **random access is O(1)** — no traversal is needed.

> **Note on storage:** For primitive types (e.g., `int`, `double`), the value is stored directly in the array. For objects, the array stores a **reference (memory address)** to the object in the heap. In dynamically-typed languages like Python, *everything* — including primitives — is stored as an object reference.

### Key Properties

- **Fixed size**: The length of an array must be declared when it is created and cannot change.
- **Zero-based indexing**: The first element is at index `0`, the last at index `length - 1`.
- **Cache-friendly**: Contiguous memory layout means the CPU can prefetch nearby elements, making iteration fast.
- **Building block**: Arrays are the foundation for building many other data structures (stacks, queues, hash tables, etc.).

### Time & Space Complexity

| Operation | Time Complexity |
|---|---|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Insert at end (if space) | O(1) |
| Insert at index | O(n) — must shift elements |
| Delete at index | O(n) — must shift elements |
| **Space** | O(n) |

### When to Use an Array

- You need fast, direct access by index.
- The number of elements is known in advance and won't change.
- You want cache-efficient sequential processing.
- You are building another data structure (e.g., a stack or hash table).

---

## Part 3: Nodes

### What Is a Node?

A **node** is the fundamental building block of linked data structures. Unlike arrays, which store data in contiguous memory, nodes can be scattered anywhere in memory. Each node holds two things:

1. **Data** — the value being stored.
2. **Next pointer / reference** — the memory address of the *next* node in the sequence.

### Node Structure (Conceptual)

```
┌────────────┬──────────────┐
│   data     │  next (ptr)  │
└────────────┴──────────────┘
```

The last node in a chain has its `next` set to `null` (or `None`/`nothing`), signaling the end of the sequence.

### Node Implementation

```python
# Python
class Node:
    def __init__(self, data):
        self.data = data   # the stored value
        self.next = None   # pointer to next node (null by default)

    def __str__(self):
        return str(self.data)
```

```javascript
// JavaScript
class Node {
    constructor(data) {
        this.data = data;   // the stored value
        this.next = null;   // pointer to next node (null by default)
    }
}
```

### Why Nodes Matter

- Nodes allow data structures to **grow and shrink dynamically** without pre-allocating a block of memory.
- Because nodes are connected by pointers, they do **not** need to be stored in contiguous memory.
- The trade-off is **extra memory overhead** — each node requires space for both its data and its pointer.

---

## Part 4: Singly Linked Lists

### What Is a Singly Linked List?

A **singly linked list (SLL)** is a linear, dynamic data structure made up of a chain of **nodes**. Each node points to the *next* node, forming a one-directional sequence from **head** (first node) to **tail** (last node).

```
head
 ↓
[10 | •]──→[25 | •]──→[47 | •]──→[8 | null]
                                        ↑
                                       tail
```

- **Head**: the entry point of the list; the reference the list object holds.
- **Tail**: the last node; its `next` is `null`.
- **Traversal**: always starts at the head and follows `next` pointers — you **cannot** go backwards.

### Characteristics at a Glance

| Characteristic | Value |
|---|---|
| Linear / Non-Linear | **Linear** |
| Homogeneous / Heterogeneous | **Heterogeneous** (by design, though often used homogeneously) |
| Indexed / Unindexed | **Unindexed** (no direct access; must traverse) |
| Ordered / Unordered | **Ordered** (insertion order is preserved) |
| Mutable / Immutable | **Mutable** |
| Dynamic / Static | **Dynamic** |
| Unique / Duplicates | **Duplicates allowed** |

### How a Singly Linked List Works (From Scratch)

A custom singly linked list wraps a chain of `Node` objects and tracks only the **head**.

```python
class DsList:
    def __init__(self):
        self.head = None   # empty list starts with no head
```

#### Core Operations

**Append (add to end) — O(n)**
Traverse to the last node, then link a new node:
```python
def append(self, data):
    if self.head is None:
        self.head = Node(data)
        return
    current = self.head
    while current.next:          # walk to the last node
        current = current.next
    current.next = Node(data)    # attach new node at the end
```

**Prepend (add to front) — O(1)**
Create a new node and make it point to the current head:
```python
def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head    # new node points to old head
    self.head = new_node         # update head
```

**Access by Index — O(n)**
Walk from the head, counting steps:
```python
def __getitem__(self, index):
    current = self.head
    count = 0
    while current:
        if count == index:
            return current.data
        current = current.next
        count += 1
```

**Delete by Index — O(n)**
Walk to the node *before* the target, then re-link around it:
```python
def remove(self, index):
    if index == 0:
        self.head = self.head.next
        return
    current = self.head
    count = 0
    while current:
        if count == index - 1:       # stop one before target
            current.next = current.next.next  # skip target node
            return
        current = current.next
        count += 1
```

**Length — O(n)**
No size field is stored; must count by traversal:
```python
def __len__(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count
```

**Membership (`in`) — O(n)**
Traverse until the value is found or the list ends:
```python
def __contains__(self, value):
    current = self.head
    while current:
        if current.data == value:
            return True
        current = current.next
    return False
```

### Time & Space Complexity

| Operation | Time Complexity |
|---|---|
| Prepend (insert at head) | **O(1)** |
| Append (insert at tail) | O(n) — must walk to end |
| Access by index | O(n) — must traverse |
| Search by value | O(n) |
| Delete at head | **O(1)** |
| Delete at index | O(n) |
| Length | O(n) — unless a `size` field is maintained |
| **Space** | O(n) |

> **Key insight:** Singly linked lists are efficient for **front insertions/deletions** but slow for **random access**, because there is no index — every access requires traversal from the head.

### Singly vs. Other List Types

| Feature | Singly Linked | Doubly Linked | Circular |
|---|---|---|---|
| Direction of traversal | Forward only | Forward & backward | Forward (loops) |
| Memory per node | data + 1 pointer | data + 2 pointers | data + 1 pointer |
| Tail deletion | O(n) | O(1) | O(n) |
| Use cases | Stacks, queues | Deques, browser history | Round-robin scheduling |

---

## Part 5: List Data Structures (Custom Implementation)

### What Is a Custom List?

In this course, a **custom list** (`DsList`) is a singly linked list built from scratch — **without using Python's built-in `list` or any other built-in collection type**. It mimics the behavior of a built-in list while exposing how the underlying linked structure actually works.

### Characteristics at a Glance

| Characteristic | Value |
|---|---|
| Linear / Non-Linear | **Linear** |
| Homogeneous / Heterogeneous | **Heterogeneous** |
| Indexed / Unindexed | **Indexed** (0-based, via traversal) |
| Ordered / Unordered | **Ordered** |
| Mutable / Immutable | **Mutable** |
| Dynamic / Static | **Dynamic** |
| Unique / Duplicates | **Duplicates allowed** |

### Operations Implemented (Full List)

| # | Operation | Description | Complexity |
|---|---|---|---|
| 1 | `__init__` / Create | Construct an empty list | O(1) |
| 2 | `append` | Add to the end | O(n) |
| 3 | `__str__` / Print | Human-readable output | O(n) |
| 4 | `__len__` / Length | Count of elements | O(n) |
| 5 | `__getitem__` | Retrieve by index | O(n) |
| 6 | `__setitem__` | Update value at index | O(n) |
| 7 | `remove` (by index) | Delete node at index | O(n) |
| 8 | `__iter__` | Make list iterable (for-loops) | O(n) per iteration |
| 9 | `__add__` | Concatenate two lists | O(n + m) |
| 10 | `extend` | Add elements from another iterable | O(k) |
| 11 | `__contains__` | Membership test (`in`) | O(n) |
| 12 | `clear` | Remove all elements | O(1) |
| 13 | Remove by value | Remove first occurrence of value | O(n) |
| 14 | Insert after | Insert after a target value or node | O(n) |
| 15 | `prepend` | Add to the front | O(1) |
| 16 | `sort` | Sort elements in-place | O(n²) or better |

### Under the Hood: How `clear` Works

```python
def clear(self):
    self.head = None   # drop the reference; all nodes become unreachable
```

Setting `head = None` is O(1) — the garbage collector handles memory cleanup.

### Under the Hood: How concatenation (`+`) works

```python
def __add__(self, other):
    new_list = DsList()
    for item in self:          # copy all items from self
        new_list.append(item)
    for item in other:         # then append all items from other
        new_list.append(item)
    return new_list            # returns a brand new list
```

The `+` operator always produces a **new list** — neither original list is modified.

---

## Part 6: Tuples

### What Is a Tuple?

A **tuple** is a **linear**, **ordered**, **indexed**, **immutable** sequence. In Python, tuples can hold mixed data types and have a fixed length after creation.

### Characteristics at a Glance

| Characteristic | Value |
|---|---|
| Linear / Non-Linear | **Linear** |
| Homogeneous / Heterogeneous | **Heterogeneous** (can also be homogeneous) |
| Indexed / Unindexed | **Indexed** |
| Ordered / Unordered | **Ordered** |
| Mutable / Immutable | **Immutable** |
| Dynamic / Static | **Static** (fixed length once created) |
| Unique / Duplicates | **Duplicates allowed** |

### Key Properties

- **Fixed-size grouping**: useful for storing related values like `(x, y)` coordinates.
- **Immutability**: prevents accidental modification and makes intent clear.
- **Hashability (conditional)**: a tuple can be used as a dictionary key only when all its elements are hashable.
- **Packing/unpacking**: tuples naturally support returning and assigning multiple values.

### Tuple Basics (Python)

```python
# creation
t = (1, "a", 3.14)
t2 = 1, 2, 3

# single-element tuple (comma required)
single = (42,)

# unpacking
x, y = (10, 20)

# tuple methods
count_of_1 = t2.count(1)
index_of_2 = t2.index(2)
```

### Time & Space Complexity

| Operation | Time Complexity |
|---|---|
| Access by index | **O(1)** |
| Length (`len`) | **O(1)** |
| Iteration | O(n) |
| Membership (`in`) | O(n) |
| Concatenation (`t + u`) | O(n + m) |
| Slicing (`t[a:b]`) | O(k), where `k` is slice length |
| **Space** | O(n) |

### Common Pitfalls

- A single-element tuple needs a trailing comma: `(5,)`.
- Tuple immutability does not freeze nested mutable elements.
    - Example: `(1, [2, 3])` is a tuple, but the inner list can still change.
- `tuple.index(x)` raises `ValueError` when `x` is not present.

---

## Part 7: Arrays vs. Tuples vs. Linked Lists — Head-to-Head Comparison

| Feature | Array | Tuple | Singly Linked List |
|---|---|---|---|
| Memory layout | Contiguous | Contiguous | Non-contiguous (scattered) |
| Access by index | **O(1)** — direct calculation | **O(1)** | O(n) — must traverse |
| Insert / Delete at front | O(n) — must shift elements | Not supported (immutable) | **O(1)** |
| Insert / Delete at end | O(1) if space; O(n) if resize | Not supported (immutable) | O(n) — walk to tail |
| Memory overhead | Low (only data) | Low (fixed sequence) | Higher (data + pointer per node) |
| Size flexibility | Fixed (static) | Fixed (static) | **Dynamic** |
| Cache performance | Excellent (contiguous) | Excellent (contiguous) | Poor (scattered memory) |
| Data type requirement | Homogeneous | Heterogeneous | Heterogeneous |
| Mutability | Mutable | **Immutable** | Mutable |

### Which to Choose?

- **Array** → you know the size upfront, need fast random access, or want cache efficiency.
- **Tuple** → you need fixed, ordered data that should not change after creation.
- **Linked List** → you need frequent insertions/deletions at the front, or the size is unpredictable.

---

## Part 8: Sets

### What Is a Set?

A **set** is a collection of **unique** elements. In most high-level languages, sets are implemented using a **hash table**, which gives very fast average-case membership checks, insertions, and deletions.

### Characteristics at a Glance

| Characteristic | Value |
|---|---|
| Linear / Non-Linear | **Non-linear** (hash-based buckets) |
| Homogeneous / Heterogeneous | **Heterogeneous** (language-dependent constraints) |
| Indexed / Unindexed | **Unindexed** |
| Ordered / Unordered | **Unordered** (do not rely on iteration order) |
| Mutable / Immutable | **Mutable** (`set`) |
| Dynamic / Static | **Dynamic** |
| Unique / Duplicates | **Unique only** |

### Key Properties

- Duplicate insertions have no effect (the value already exists).
- Ideal for membership testing: `x in my_set`.
- Typical operations are based on hashing.
- Supports mathematical set operations: union, intersection, difference, symmetric difference.

### Core Operations (Python examples)

```python
numbers = {1, 2, 3}
numbers.add(4)                 # {1, 2, 3, 4}
numbers.remove(2)              # {1, 3, 4}
exists = 3 in numbers          # True

evens = {2, 4, 6}
odds = {1, 3, 5}
all_nums = evens | odds        # union
shared = evens & {4, 8}        # intersection => {4}
```

### Time & Space Complexity

| Operation | Average | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Membership test | O(1) | O(n) |
| Union / Intersection / Difference | O(n + m) | O(n * m) in degenerate cases |
| **Space** | O(n) | O(n) |

> Worst-case behavior happens when many keys collide into the same hash bucket.

### When to Use a Set

- You need to remove duplicates.
- You need very fast membership checks.
- You need mathematical set operations.

---

## Part 9: Dictionaries (Maps / Hash Maps)

### What Is a Dictionary?

A **dictionary** stores **key-value pairs** where each key is unique and maps to a value. Like sets, dictionaries are usually hash-table based, so lookup by key is very fast on average.

### Characteristics at a Glance

| Characteristic | Value |
|---|---|
| Linear / Non-Linear | **Non-linear** (hash-based buckets) |
| Homogeneous / Heterogeneous | **Heterogeneous** (keys/values can vary) |
| Indexed / Unindexed | **Indexed by key** (not by numeric position) |
| Ordered / Unordered | **Ordered by insertion** in modern Python; conceptually key-based |
| Mutable / Immutable | **Mutable** |
| Dynamic / Static | **Dynamic** |
| Unique / Duplicates | **Keys are unique**, values may duplicate |

### Key Properties

- Keys must be hashable (immutable in Python: `str`, `int`, `tuple`, etc.).
- Access is by key, not by positional index.
- Updating an existing key overwrites the old value.
- Very common for counters, lookups, configuration, and caching.

### Core Operations (Python examples)

```python
student = {"id": 101, "name": "Ava", "gpa": 3.8}

student["major"] = "Computer Science"   # insert
student["gpa"] = 3.9                      # update
name = student["name"]                    # lookup
exists = "id" in student                  # membership by key
removed = student.pop("major")            # delete and return value
```

### Time & Space Complexity

| Operation | Average | Worst Case |
|---|---|---|
| Insert / Update by key | O(1) | O(n) |
| Lookup by key | O(1) | O(n) |
| Delete by key | O(1) | O(n) |
| Iterate keys/values/items | O(n) | O(n) |
| **Space** | O(n) | O(n) |

### When to Use a Dictionary

- You need fast lookup by an identifier/key.
- You need to associate related pieces of data (`key -> value`).
- You need frequency counts or grouping.

---

## Part 10: Choosing the Right Structure

| Need | Best Fit | Why |
|---|---|---|
| Fast random access by position | **Array** | Direct index math gives O(1) access |
| Fixed read-only grouped values | **Tuple** | Immutable, compact, and still indexable |
| Frequent inserts/deletes at front | **Singly Linked List** | Head operations are O(1) |
| Remove duplicates + membership checks | **Set** | Unique elements and O(1) average membership |
| Fast lookup by key | **Dictionary** | O(1) average key-based access |

---

## Part 11: Quick-Reference Summary Table

| Data Structure | Linear | Homogeneous | Indexed | Ordered | Mutable | Dynamic | Duplicates |
|---|---|---|---|---|---|---|---|
| **Array** | ✅ | ✅ | ✅ (numeric index) | ✅ | ✅ | ❌ | ✅ |
| **Tuple** | ✅ | ❌* | ✅ (numeric index) | ✅ | ❌ | ❌ | ✅ |
| **Singly Linked List** | ✅ | ❌ | ❌† | ✅ | ✅ | ✅ | ✅ |
| **List** | ✅ | ❌ | ✅† | ✅ | ✅ | ✅ | ✅ |
| **Set** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| **Dictionary** | ❌ | ❌ | ✅ (by key) | ✅** | ✅ | ✅ | Keys: ❌ / Values: ✅ |

> \* Tuples can be homogeneous or heterogeneous.

> † Indexed *logically* (via traversal), but not via direct memory calculation like arrays.

> \** In Python 3.7+, dictionaries preserve insertion order.

---