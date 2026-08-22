"""
Python List Demonstration
A comprehensive guide to Python's built-in list data structure
"""

# ============================================================================
# 1. CREATING LISTS
# ============================================================================

# Empty list - a list with no elements
empty_list = []
print("Empty list:", empty_list)

# List with initial values - can contain any type of data
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# List with numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)

# Mixed types - Python allows different types in the same list
mixed = [1, "hello", 3.14, True, None]
print("Mixed types:", mixed)

# Creating a list with repeated values using multiplication
zeros = [0] * 5  # Creates [0, 0, 0, 0, 0]
print("Five zeros:", zeros)

# Using list() constructor
from_string = list("hello")  # Converts string to list of characters
print("From string:", from_string)

print("\n" + "="*70 + "\n")

# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================

colors = ["red", "green", "blue", "yellow", "purple"]

# Access by index - lists start at index 0
first = colors[0]      # First element
print("First color:", first)

third = colors[2]      # Third element (index 2)
print("Third color:", third)

# Negative indexing - count from the end
last = colors[-1]      # Last element
print("Last color:", last)

second_last = colors[-2]  # Second from the end
print("Second to last:", second_last)

print("\n" + "="*70 + "\n")

# ============================================================================
# 3. MODIFYING ELEMENTS
# ============================================================================

pets = ["dog", "cat", "bird"]
print("Original pets:", pets)

# Change a single element
pets[1] = "hamster"  # Replace "cat" with "hamster"
print("After replacing cat:", pets)

# Change multiple elements with slicing
pets[0:2] = ["fish", "turtle"]  # Replace first two elements
print("After replacing first two:", pets)

print("\n" + "="*70 + "\n")

# ============================================================================
# 4. ADDING ELEMENTS
# ============================================================================

shopping = ["milk", "eggs"]
print("Shopping list:", shopping)

# append() - adds ONE element to the END
shopping.append("bread")
print("After append:", shopping)

# insert() - adds element at specific position
# Syntax: list.insert(index, value)
shopping.insert(1, "butter")  # Insert at index 1
print("After insert at index 1:", shopping)

# extend() - adds MULTIPLE elements from another list
more_items = ["cheese", "yogurt"]
shopping.extend(more_items)
print("After extend:", shopping)

# Using + operator - creates NEW list (doesn't modify original)
combined = shopping + ["apples", "oranges"]
print("Using + operator:", combined)
print("Original shopping still:", shopping)

print("\n" + "="*70 + "\n")

# ============================================================================
# 5. REMOVING ELEMENTS
# ============================================================================

tasks = ["email", "coding", "meeting", "lunch", "coding", "review"]
print("Tasks:", tasks)

# remove() - removes FIRST occurrence of a value
tasks.remove("coding")  # Removes first "coding"
print("After remove('coding'):", tasks)

# pop() - removes and RETURNS element at index (or last if no index)
last_task = tasks.pop()  # Removes and returns last element
print("Popped task:", last_task)
print("Tasks after pop():", tasks)

second = tasks.pop(1)  # Remove at index 1
print("Popped second task:", second)
print("Tasks after pop(1):", tasks)

# del - removes element(s) by index
del tasks[0]  # Delete first element
print("After del tasks[0]:", tasks)

# clear() - removes ALL elements
tasks.clear()
print("After clear():", tasks)

print("\n" + "="*70 + "\n")

# ============================================================================
# 6. SLICING - Getting portions of a list
# ============================================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("Days:", days)

# Syntax: list[start:end]  (end is NOT included)
weekdays = days[0:5]  # From index 0 to 4
print("Weekdays (0:5):", weekdays)

# Omit start - goes from beginning
first_three = days[:3]  # Same as days[0:3]
print("First three (:3):", first_three)

# Omit end - goes to the end
weekend = days[5:]  # From index 5 to end
print("Weekend (5:):", weekend)

# With step - every nth element
# Syntax: list[start:end:step]
every_other = days[::2]  # Every 2nd element
print("Every other (::2):", every_other)

# Negative step - reverse the list
reversed_days = days[::-1]
print("Reversed ([::-1]):", reversed_days)

print("\n" + "="*70 + "\n")

# ============================================================================
# 7. ITERATING - Looping through lists
# ============================================================================

animals = ["dog", "cat", "bird", "fish"]

# Basic for loop - iterate over values
print("Loop through values:")
for animal in animals:
    print(f"  Animal: {animal}")

# Loop with index using enumerate()
print("\nLoop with index:")
for index, animal in enumerate(animals):
    print(f"  {index}: {animal}")

# Loop with custom starting index
print("\nLoop starting at 1:")
for index, animal in enumerate(animals, start=1):
    print(f"  {index}. {animal}")

# While loop with index
print("\nUsing while loop:")
i = 0
while i < len(animals):
    print(f"  Position {i}: {animals[i]}")
    i += 1

print("\n" + "="*70 + "\n")

# ============================================================================
# 8. SEARCHING AND CHECKING
# ============================================================================

numbers = [10, 20, 30, 40, 50, 30]

# in operator - check if value exists
has_30 = 30 in numbers
print("Is 30 in the list?", has_30)

has_100 = 100 in numbers
print("Is 100 in the list?", has_100)

# index() - find position of FIRST occurrence
position = numbers.index(30)
print("First position of 30:", position)

# index() with start parameter
position_after = numbers.index(30, 3)  # Search starting from index 3
print("Position of 30 after index 3:", position_after)

# count() - how many times value appears
count_30 = numbers.count(30)
print("How many times 30 appears:", count_30)

print("\n" + "="*70 + "\n")

# ============================================================================
# 9. SORTING
# ============================================================================

unsorted = [64, 34, 25, 12, 22, 11, 90]
print("Original:", unsorted)

# sort() - sorts the list IN PLACE (modifies original)
unsorted.sort()
print("After sort():", unsorted)

# sort(reverse=True) - descending order
unsorted.sort(reverse=True)
print("After sort(reverse=True):", unsorted)

# sorted() - returns NEW sorted list (original unchanged)
original = [64, 34, 25, 12, 22, 11, 90]
new_sorted = sorted(original)
print("Original list:", original)
print("New sorted list:", new_sorted)

# Sorting strings
words = ["zebra", "apple", "mango", "banana"]
words.sort()
print("Sorted words:", words)

print("\n" + "="*70 + "\n")

# ============================================================================
# 10. REVERSING
# ============================================================================

letters = ["a", "b", "c", "d", "e"]
print("Original:", letters)

# reverse() - reverses IN PLACE (modifies original)
letters.reverse()
print("After reverse():", letters)

# reversed() - returns iterator (need to convert to list)
letters = ["a", "b", "c", "d", "e"]
rev_list = list(reversed(letters))
print("Using reversed():", rev_list)
print("Original unchanged:", letters)

# Slicing trick - creates new reversed list
letters = ["a", "b", "c", "d", "e"]
rev_slice = letters[::-1]
print("Using [::-1]:", rev_slice)

print("\n" + "="*70 + "\n")

# ============================================================================
# 11. LENGTH AND OTHER INFO
# ============================================================================

items = [5, 10, 15, 20, 25]

# len() - number of elements
length = len(items)
print("List:", items)
print("Length:", length)

# min() and max() - smallest and largest values
minimum = min(items)
maximum = max(items)
print("Minimum:", minimum)
print("Maximum:", maximum)

# sum() - total of all numbers
total = sum(items)
print("Sum:", total)

# Average (mean) - sum divided by length
average = sum(items) / len(items)
print("Average:", average)

print("\n" + "="*70 + "\n")

# ============================================================================
# 12. COPYING LISTS
# ============================================================================

original = [1, 2, 3]

# WRONG way - just creates another reference to same list
not_a_copy = original
not_a_copy.append(4)
print("Original:", original)  # Both changed!
print("'Copy':", not_a_copy)

# RIGHT way 1 - using copy() method
original = [1, 2, 3]
real_copy = original.copy()
real_copy.append(4)
print("\nOriginal:", original)  # Original unchanged
print("Real copy:", real_copy)

# RIGHT way 2 - using slicing
original = [1, 2, 3]
slice_copy = original[:]
slice_copy.append(4)
print("\nOriginal:", original)
print("Slice copy:", slice_copy)

# RIGHT way 3 - using list() constructor
original = [1, 2, 3]
constructor_copy = list(original)
constructor_copy.append(4)
print("\nOriginal:", original)
print("Constructor copy:", constructor_copy)

print("\n" + "="*70 + "\n")

# ============================================================================
# 13. LIST COMPREHENSIONS - Concise way to create lists
# ============================================================================

# Basic comprehension - create list of squares
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# With condition - only even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)

# Transform existing list
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print("Uppercase:", uppercase)

# With if-else
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print("Labels:", labels)

print("\n" + "="*70 + "\n")

# ============================================================================
# 14. CONCATENATION AND REPETITION
# ============================================================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation with +
combined = list1 + list2
print("list1 + list2:", combined)

# Repetition with *
repeated = list1 * 3
print("list1 * 3:", repeated)

print("\n" + "="*70 + "\n")

# ============================================================================
# 15. NESTED LISTS - Lists inside lists (2D arrays)
# ============================================================================

# Matrix - list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Access element in nested list
# matrix[row][column]
element = matrix[1][2]  # Row 1, Column 2 = 6
print("\nElement at [1][2]:", element)

# Modify nested element
matrix[0][0] = 99
print("\nAfter changing [0][0] to 99:")
for row in matrix:
    print(row)

print("\n" + "="*70 + "\n")

# ============================================================================
# 16. CHECKING IF LIST IS EMPTY
# ============================================================================

empty = []
full = [1, 2, 3]

# Pythonic way - empty list is "falsy"
if not empty:
    print("The list is empty")

if full:
    print("The list has items")

# Explicit way - check length
if len(empty) == 0:
    print("Empty list has length 0")

print("\n" + "="*70 + "\n")

# ============================================================================
# 17. COMMON PATTERNS AND TIPS
# ============================================================================

# Creating a range of numbers
numbers = list(range(5))  # [0, 1, 2, 3, 4]
print("Range 0-4:", numbers)

numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
print("Range 1-5:", numbers)

numbers = list(range(0, 10, 2))  # [0, 2, 4, 6, 8] - step of 2
print("Range 0-10 step 2:", numbers)

# Filter with filter() function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("\nFiltered evens:", evens)

# Transform with map() function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# Zip - combine two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print("\nZipped:", combined)

# Unpacking
for name, age in combined:
    print(f"{name} is {age} years old")

print("\n" + "="*70 + "\n")

print("🎉 List demonstration complete!")
print("Lists are one of Python's most powerful and versatile data structures.")
