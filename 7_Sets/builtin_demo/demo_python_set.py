"""
Python Set Demonstration
A concise guide to Python's built-in set data structure
"""

# ============================================================================
# 1. CREATING SETS
# ============================================================================
# fruits = {"apple", "banana", "cherry"}
empty_list = []
empty_tuple = ()
empty_dictionary = {}
empty_set = set()

# Empty set - use set() ({} creates a dict)
empty = set()
print("Empty set:", empty)

# Literal set (note: order is arbitrary)
fruits = {"apple", "banana", "apple", "cherry"}
print("Fruits (duplicates removed):", fruits)

# From iterable - useful to remove duplicates from a list
nums = set([1, 2, 2, 3, 4])
print("Nums from list:", nums)

my_list = [1, 2, 2, 3, 4]
my_list = list(set(my_list))

my_set = set(my_list)
my_list = list(my_set)  

print('\n' + '='*60 + '\n')

# ============================================================================
# 2. ADDING AND REMOVING
# ============================================================================

s = {1, 2, 3}
print("Original:", s)

# add() - adds an element
s.add(4)
print("After add(4):", s)

# discard() - removes element if present, no error if missing
s.discard(99)
print("After discard(99) (no error):", s)

# remove() - removes element, raises KeyError if missing
try:
    s.remove(2)
    print("After remove(2):", s)
except KeyError as e:
    print("remove raised:", e)

# pop() - removes and returns an arbitrary element
val = s.pop()
print("Popped arbitrary element:", val, "Remaining:", s)

# clear() - removes all elements
s.clear()
print("After clear():", s)

print('\n' + '='*60 + '\n')

# ============================================================================
# 3. MEMBERSHIP AND ITERATION
# ============================================================================

letters = set("abracadabra")  # set of unique chars
print("Letters:", letters)
print("Is 'a' in letters?", 'a' in letters)

print("Iterate:")
for ch in letters:
    print(' ', ch)

print('\n' + '='*60 + '\n')

# ============================================================================
# 4. SET OPERATIONS (ALGEBRA)
# ============================================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("A:", a)
print("B:", b)

print("Union (A | B):", a | b)
print("Intersection (A & B):", a & b)
print("Difference (A - B):", a - b)
print("Symmetric difference (A ^ B):", a ^ b)

# In-place variants
c = set(a)
c.update(b)  # union into c
print("After c.update(b):", c)

print('\n' + '='*60 + '\n')

# ============================================================================
# 5. SUBSETS / SUPERSETS / DISJOINT
# ============================================================================

small = {1, 2}
print("small <= a?", small.issubset(a))
print("a >= small?", a.issuperset(small))
print("Are a and b disjoint?", a.isdisjoint(b))

print('\n' + '='*60 + '\n')

# ============================================================================
# 6. IMMUTABLE SETS
# ============================================================================

f = frozenset([1, 2, 3])
print("Frozen set (immutable, hashable):", f)

try:
    f.add(4)
except AttributeError as e:
    print("Cannot modify frozenset:", e)

print('\n' + '='*60 + '\n')

# ============================================================================
# 7. CONVERSIONS AND COMPREHENSIONS
# ============================================================================

lst = [1, 2, 2, 3, 3, 3]
unique = set(lst)  # remove duplicates
print("Unique from list:", unique)

# Set comprehension
squares = {x*x for x in range(6)}
print("Squares set:", squares)

# Convert back to list (ordering not guaranteed)
as_list = list(squares)
print("As list:", as_list)

print('\nSet demo complete (Python).')
