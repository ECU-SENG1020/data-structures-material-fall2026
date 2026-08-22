# Common Dunder Attributes and Methods for Python Data Structures

## 🔹 list

- `__getitem__(self, index)`  
  Retrieves an item at a specific index using `list[index]`.

- `__setitem__(self, index, value)`  
  Sets the value at a specific index using `list[index] = value`.

- `__delitem__(self, index)`  
  Deletes an item at a specific index using `del list[index]`.

- `__len__(self)`  
  Returns the number of items using `len(list)`.

- `__iter__(self)`  
  Returns an iterator for looping with `for item in list`.

- `__contains__(self, item)`  
  Checks membership using `item in list`.

- `__reversed__(self)`  
  Returns a reversed iterator using `reversed(list)`.

- `__add__(self, other)`  
  Concatenates two lists using `list1 + list2`.

- `__mul__(self, n)`  
  Repeats the list `n` times using `list * n`.

- `__eq__(self, other)`  
  Compares two lists for equality using `==`.

## 🔹 tuple

- `__getitem__(self, index)`  
  Accesses an element by index.

- `__len__(self)`  
  Returns the number of elements.

- `__iter__(self)`  
  Enables iteration.

- `__contains__(self, item)`  
  Checks if an item exists in the tuple.

- `__add__(self, other)`  
  Concatenates two tuples.

- `__mul__(self, n)`  
  Repeats the tuple `n` times.

- `__eq__(self, other)`  
  Compares two tuples for equality.

- `__hash__(self)`  
  Returns a hash value (tuples are hashable if all elements are hashable).

## 🔹 set

- `__contains__(self, item)`  
  Checks if an item is in the set.

- `__len__(self)`  
  Returns the number of elements.

- `__iter__(self)`  
  Enables iteration.

- `__eq__(self, other)`  
  Checks if two sets are equal.

- `__or__(self, other)`  
  Union of two sets using `set1 | set2`.

- `__and__(self, other)`  
  Intersection using `set1 & set2`.

- `__sub__(self, other)`  
  Difference using `set1 - set2`.

- `__xor__(self, other)`  
  Symmetric difference using `set1 ^ set2`.

- `__le__(self, other)`  
  Subset check using `<=`.

- `__ge__(self, other)`  
  Superset check using `>=`.

## 🔹 dict

- `__getitem__(self, key)`  
  Retrieves a value by key using `dict[key]`.

- `__setitem__(self, key, value)`  
  Sets a key-value pair using `dict[key] = value`.

- `__delitem__(self, key)`  
  Deletes a key-value pair using `del dict[key]`.

- `__len__(self)`  
  Returns the number of key-value pairs.

- `__iter__(self)`  
  Iterates over keys.

- `__contains__(self, key)`  
  Checks if a key exists using `key in dict`.

- `__eq__(self, other)`  
  Compares two dictionaries for equality.

- `__repr__(self)`  
  Returns the string representation of the dictionary.

- `__or__(self, other)`  
  Merges two dictionaries (Python 3.9+).