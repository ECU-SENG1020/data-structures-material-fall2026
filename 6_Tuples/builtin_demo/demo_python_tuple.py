"""
Python Tuple Demonstration
A concise guide to Python's built-in tuple data structure
"""

# ============================================================================
# 1. CREATING TUPLES
# ============================================================================

# Empty tuple
empty = ()
print("Empty tuple:", empty)

# Literal tuple
point = (10, 20)
print("Point:", point)

# Single-element tuple - comma is required
single = (42,)
print("Single-element tuple:", single)

# Tuple constructor
chars = tuple('abc')
print("From string:", chars)

print('\n' + '='*60 + '\n')

# ============================================================================
# 2. IMMUTABILITY
# ============================================================================

tpl = (1, 2, 3)
print("Original:", tpl)
try:
    tpl[0] = 99  # Raises TypeError
except TypeError as e:
    print("Cannot modify tuple (TypeError):", e)

# To "modify", convert to list and back
lst = list(tpl)
lst[0] = 99
tpl2 = tuple(lst)
print("Modified copy via list -> tuple:", tpl2)

print('\n' + '='*60 + '\n')

# ============================================================================
# 3. PACKING AND UNPACKING
# ============================================================================

packed = 1, 2, 3  # packing without parentheses
print("Packed:", packed)

# Unpacking
a, b, c = packed
print("Unpacked:", a, b, c)

# Starred unpacking
head, *middle, tail = (1, 2, 3, 4, 5)
print("Head:", head, "Middle:", middle, "Tail:", tail)

print('\n' + '='*60 + '\n')

# ============================================================================
# 4. SLICING, ITERATION, SEARCH
# ============================================================================

nums = (10, 20, 30, 40, 30)
print("Slice (1:4):", nums[1:4])
print("Iterate:")
for n in nums:
    print(' ', n)
print("Count of 30:", nums.count(30))
print("Index of 30:", nums.index(30))
print("Is 100 in tuple?", 100 in nums)

print('\n' + '='*60 + '\n')

# ============================================================================
# 5. CONCATENATION, REPETITION, LENGTH
# ============================================================================

t1 = (1, 2)
t2 = (3, 4)
print("Concat:", t1 + t2)
print("Repeat:", t1 * 3)
print("Length:", len(t1))

print('\n' + '='*60 + '\n')

# ============================================================================
# 6. NESTED, CONVERSION, STATS
# ============================================================================

nested = ((1, 2), (3, 4))
print("Nested:", nested)
nums = (5, 10, 15)
print("Min, Max, Sum:", min(nums), max(nums), sum(nums))

# Convert to list to modify
mutable = list(nums)
mutable.append(20)
nums2 = tuple(mutable)
print("Converted, modified, reconverted:", nums2)

print('\nTuple demo complete (Python).')
