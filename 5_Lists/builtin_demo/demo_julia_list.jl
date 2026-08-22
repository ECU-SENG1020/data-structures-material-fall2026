#=
Julia vector (List) Demonstration
A comprehensive guide to Julia's built-in vector data structure
In Julia, what Python calls "lists" are called "Vectors"
=#

# ============================================================================
# 1. CREATING VECTORS
# ============================================================================

# Empty vector - need to specify the type
empty_vector = []  # Empty vector of any
empty_int_vector = Int[]  # Empty vector of integers
println("Empty vector: ", empty_vector)
println("Empty integer vector: ", empty_int_vector)

# vector with initial values
fruits = ["apple", "banana", "cherry"]
println("Fruits: ", fruits)

# vector with numbers
numbers = [1, 2, 3, 4, 5]
println("Numbers: ", numbers)

# Mixed types - Julia can infer common type (Any)
mixed = [1, "hello", 3.14, true, nothing]
println("Mixed types: ", mixed)

# Creating vector with repeated values
zeros_vector = zeros(Int, 5)  # [0, 0, 0, 0, 0]
println("Five zeros: ", zeros_vector)

ones_vector = ones(Int, 5)  # [1, 1, 1, 1, 1]
println("Five ones: ", ones_vector)

# Fill with specific value
fives = fill(5, 4)  # [5, 5, 5, 5]
println("Four fives: ", fives)

# Using collect() to convert ranges to Vectors
from_range = collect(1:5)  # [1, 2, 3, 4, 5]
println("From range: ", from_range)

# Convert string to vector of characters
from_string = collect("hello")
println("From string: ", from_string)

println("\n", "="^70, "\n")

# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================

colors = ["red", "green", "blue", "yellow", "purple"]

# Access by index - Julia Vectors start at index 1 (not 0!)
first = colors[1]  # First element
println("First color: ", first)

third = colors[3]  # Third element
println("Third color: ", third)

# end keyword - refers to the last index
last = colors[end]  # Last element
println("Last color: ", last)

second_last = colors[end-1]  # Second from the end
println("Second to last: ", second_last)

println("\n", "="^70, "\n")

# ============================================================================
# 3. MODIFYING ELEMENTS
# ============================================================================

pets = ["dog", "cat", "bird"]
println("Original pets: ", pets)

# Change a single element
pets[2] = "hamster"  # Replace "cat" with "hamster"
println("After replacing cat: ", pets)

# Change multiple elements with range
pets[1:2] = ["fish", "turtle"]  # Replace first two elements
println("After replacing first two: ", pets)

println("\n", "="^70, "\n")

# ============================================================================
# 4. ADDING ELEMENTS
# ============================================================================

shopping = ["milk", "eggs"]
println("Shopping list: ", shopping)

# push!() - adds ONE element to the END
# Note: ! at the end means it modifies the vector
push!(shopping, "bread")
println("After push!: ", shopping)

# pushfirst!() - adds element to the BEGINNING
pushfirst!(shopping, "butter")
println("After pushfirst!: ", shopping)

# insert!() - adds element at specific position
# Syntax: insert!(vector, index, value)
insert!(shopping, 3, "cheese")  # Insert at index 3
println("After insert! at index 3: ", shopping)

# append!() - adds MULTIPLE elements from another vector
more_items = ["yogurt", "apples"]
append!(shopping, more_items)
println("After append!: ", shopping)

# Using vcat() - concatenate vertically (creates NEW vector)
combined = vcat(shopping, ["oranges", "grapes"])
println("Using vcat(): ", combined)
println("Original shopping still: ", shopping)

println("\n", "="^70, "\n")

# ============================================================================
# 5. REMOVING ELEMENTS
# ============================================================================

tasks = ["email", "coding", "meeting", "lunch", "coding", "review"]
println("Tasks: ", tasks)

# pop!() - removes and RETURNS last element
last_task = pop!(tasks)
println("Popped task: ", last_task)
println("Tasks after pop!(): ", tasks)

# popfirst!() - removes and returns first element
first_task = popfirst!(tasks)
println("Popped first task: ", first_task)
println("Tasks after popfirst!(): ", tasks)

# deleteat!() - removes element at specific index
deleteat!(tasks, 2)  # Delete at index 2
println("After deleteat!(tasks, 2): ", tasks)

# deleteat!() with range - remove multiple elements
tasks = ["a", "b", "c", "d", "e", "f"]
deleteat!(tasks, 2:4)  # Remove indices 2, 3, 4
println("After deleteat!(tasks, 2:4): ", tasks)

# empty!() - removes ALL elements
empty!(tasks)
println("After empty!(): ", tasks)

println("\n", "="^70, "\n")

# ============================================================================
# 6. SLICING - Getting portions of an vector
# ============================================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
println("Days: ", days)

# Syntax: vector[start:end]  (both start and end ARE included!)
weekdays = days[1:5]  # From index 1 to 5 (inclusive)
println("Weekdays (1:5): ", weekdays)

# Using end keyword
weekend = days[6:end]  # From index 6 to the end
println("Weekend (6:end): ", weekend)

# Every nth element using range with step
# Syntax: vector[start:step:end]
every_other = days[1:2:end]  # Every 2nd element
println("Every other (1:2:end): ", every_other)

# Reverse using range
reversed_days = days[end:-1:1]  # From end to start, step -1
println("Reversed (end:-1:1): ", reversed_days)

println("\n", "="^70, "\n")

# ============================================================================
# 7. ITERATING - Looping through Vectors
# ============================================================================

animals = ["dog", "cat", "bird", "fish"]

# Basic for loop - iterate over values
println("Loop through values:")
for animal in animals
    println("  Animal: ", animal)
end

# Loop with index using enumerate()
println("\nLoop with index:")
for (index, animal) in enumerate(animals)
    println("  ", index, ": ", animal)
end

# Loop with just indices
println("\nLoop with indices only:")
for i in eachindex(animals)
    println("  Position ", i, ": ", animals[i])
end

# While loop with index
println("\nUsing while loop:")
i = 1
while i <= length(animals)
    println("  Position ", i, ": ", animals[i])
    i += 1
end

println("\n", "="^70, "\n")

# ============================================================================
# 8. SEARCHING AND CHECKING
# ============================================================================

numbers = [10, 20, 30, 40, 50, 30]

# in operator - check if value exists
has_30 = 30 in numbers
println("Is 30 in the vector? ", has_30)

has_100 = 100 in numbers
println("Is 100 in the vector? ", has_100)

# findfirst() - find position of FIRST occurrence
position = findfirst(==(30), numbers)
println("First position of 30: ", position)

# findall() - find ALL positions
positions = findall(==(30), numbers)
println("All positions of 30: ", positions)

# findlast() - find position of LAST occurrence
last_position = findlast(==(30), numbers)
println("Last position of 30: ", last_position)

# count() - how many times value appears
count_30 = count(==(30), numbers)
println("How many times 30 appears: ", count_30)

println("\n", "="^70, "\n")

# ============================================================================
# 9. SORTING
# ============================================================================

unsorted = [64, 34, 25, 12, 22, 11, 90]
println("Original: ", unsorted)

# sort!() - sorts the vector IN PLACE (modifies original)
sort!(unsorted)
println("After sort!(): ", unsorted)

# sort!() with reverse=true - descending order
unsorted = [64, 34, 25, 12, 22, 11, 90]
sort!(unsorted, rev=true)
println("After sort!(rev=true): ", unsorted)

# sort() - returns NEW sorted vector (original unchanged)
original = [64, 34, 25, 12, 22, 11, 90]
new_sorted = sort(original)
println("Original vector: ", original)
println("New sorted vector: ", new_sorted)

# Sorting strings
words = ["zebra", "apple", "mango", "banana"]
sort!(words)
println("Sorted words: ", words)

println("\n", "="^70, "\n")

# ============================================================================
# 10. REVERSING
# ============================================================================

letters = ["a", "b", "c", "d", "e"]
println("Original: ", letters)

# reverse!() - reverses IN PLACE (modifies original)
reverse!(letters)
println("After reverse!(): ", letters)

# reverse() - returns NEW reversed vector (original unchanged)
letters = ["a", "b", "c", "d", "e"]
rev_vector = reverse(letters)
println("Using reverse(): ", rev_vector)
println("Original unchanged: ", letters)

# Using range slicing
letters = ["a", "b", "c", "d", "e"]
rev_slice = letters[end:-1:1]
println("Using [end:-1:1]: ", rev_slice)

println("\n", "="^70, "\n")

# ============================================================================
# 11. LENGTH AND OTHER INFO
# ============================================================================

items = [5, 10, 15, 20, 25]

# length() - number of elements
len = length(items)
println("vector: ", items)
println("Length: ", len)

# minimum() and maximum() - smallest and largest values
min_val = minimum(items)
max_val = maximum(items)
println("Minimum: ", min_val)
println("Maximum: ", max_val)

# sum() - total of all numbers
total = sum(items)
println("Sum: ", total)

# mean() - average (need Statistics package)
using Statistics
average = mean(items)
println("Average: ", average)

# size() - returns tuple of dimensions
dimensions = size(items)
println("Size (dimensions): ", dimensions)

println("\n", "="^70, "\n")

# ============================================================================
# 12. COPYING Vectors
# ============================================================================

original = [1, 2, 3]

# WRONG way - just creates another reference to same vector
not_a_copy = original
push!(not_a_copy, 4)
println("Original: ", original)  # Both changed!
println("'Copy': ", not_a_copy)

# RIGHT way 1 - using copy()
original = [1, 2, 3]
real_copy = copy(original)
push!(real_copy, 4)
println("\nOriginal: ", original)  # Original unchanged
println("Real copy: ", real_copy)

# RIGHT way 2 - using vector constructor
original = [1, 2, 3]
constructor_copy = [original...]  # ... is splat operator
push!(constructor_copy, 4)
println("\nOriginal: ", original)
println("Constructor copy: ", constructor_copy)

println("\n", "="^70, "\n")

# ============================================================================
# 13. vector COMPREHENSIONS - Concise way to create Vectors
# ============================================================================

# Basic comprehension - create vector of squares
squares = [x^2 for x in 1:5]
println("Squares: ", squares)

# With condition - only even numbers
evens = [x for x in 1:10 if x % 2 == 0]
println("Even numbers: ", evens)

# Transform existing vector
words = ["hello", "world", "julia"]
uppercase = [uppercase(word) for word in words]
println("Uppercase: ", uppercase)

# With if-else (ternary operator)
numbers = [1, 2, 3, 4, 5]
labels = [x % 2 == 0 ? "even" : "odd" for x in numbers]
println("Labels: ", labels)

println("\n", "="^70, "\n")

# ============================================================================
# 14. CONCATENATION AND REPETITION
# ============================================================================

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# Concatenation with vcat() or [a; b]
combined1 = vcat(arr1, arr2)
println("vcat(arr1, arr2): ", combined1)

combined2 = [arr1; arr2]
println("[arr1; arr2]: ", combined2)

# Repetition with repeat()
repeated = repeat(arr1, 3)
println("repeat(arr1, 3): ", repeated)

println("\n", "="^70, "\n")

# ============================================================================
# 15. NESTED Vectors - Vectors inside Vectors (2D Vectors)
# ============================================================================

# Matrix - vector of Vectors
# Better way in Julia: use actual 2D vector syntax
matrix = [1 2 3; 4 5 6; 7 8 9]  # Space separates columns, ; separates rows

println("Matrix:")
println(matrix)

# Access element in matrix
# matrix[row, column]
element = matrix[2, 3]  # Row 2, Column 3 = 6
println("\nElement at [2, 3]: ", element)

# Modify element
matrix[1, 1] = 99
println("\nAfter changing [1, 1] to 99:")
println(matrix)

# vector of Vectors (jagged vector)
jagged = [[1, 2], [3, 4, 5], [6]]
println("\nJagged vector: ", jagged)
println("First sub-vector: ", jagged[1])
println("Element [2][3]: ", jagged[2][3])

println("\n", "="^70, "\n")

# ============================================================================
# 16. CHECKING IF vector IS EMPTY
# ============================================================================

empty_arr = Int[]
full_arr = [1, 2, 3]

# Using isempty()
if isempty(empty_arr)
    println("The vector is empty")
end

if !isempty(full_arr)
    println("The vector has items")
end

# Check length
if length(empty_arr) == 0
    println("Empty vector has length 0")
end

println("\n", "="^70, "\n")

# ============================================================================
# 17. COMMON PATTERNS AND TIPS
# ============================================================================

# Creating ranges (don't need to collect unless you want an vector)
numbers = 1:5  # This is a range, not an vector
println("Range 1:5: ", numbers)
println("Type: ", typeof(numbers))

numbers_vector = collect(1:5)  # Convert to vector
println("As vector: ", numbers_vector)

# Range with step
numbers = 0:2:10  # 0, 2, 4, 6, 8, 10
println("Range 0:2:10: ", collect(numbers))

# Filter with filter() function
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(x -> x % 2 == 0, original)
println("\nFiltered evens: ", evens)

# Transform with map() function
numbers = [1, 2, 3, 4, 5]
doubled = map(x -> x * 2, numbers)
println("Doubled: ", doubled)

# Broadcasting with . operator (powerful Julia feature!)
numbers = [1, 2, 3, 4, 5]
doubled_broadcast = numbers .* 2  # Apply * 2 to each element
println("Doubled with broadcast: ", doubled_broadcast)

# Zip - combine two Vectors
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = collect(zip(names, ages))
println("\nZipped: ", combined)

# Unpacking
for (name, age) in zip(names, ages)
    println("$name is $age years old")
end

println("\n", "="^70, "\n")

# ============================================================================
# 18. UNIQUE JULIA FEATURES
# ============================================================================

# Broadcasting - apply operations element-wise
arr = [1, 2, 3, 4, 5]
result = arr .^ 2  # Square each element
println("arr .^ 2: ", result)

# Function broadcasting
words = ["hello", "world", "julia"]
upper = uppercase.(words)  # Apply uppercase to each element
println("uppercase.(words): ", upper)

# any() and all() - check conditions
numbers = [2, 4, 6, 8, 10]
all_even = all(x -> x % 2 == 0, numbers)
println("\nAll even? ", all_even)

numbers = [1, 2, 3, 4, 5]
has_even = any(x -> x % 2 == 0, numbers)
println("Has any even? ", has_even)

# unique() - remove duplicates
with_dupes = [1, 2, 2, 3, 4, 4, 5]
no_dupes = unique(with_dupes)
println("\nRemove duplicates: ", no_dupes)

# reshape() - change dimensions
flat = [1, 2, 3, 4, 5, 6]
matrix_form = reshape(flat, 2, 3)  # 2 rows, 3 columns
println("\nReshape to 2x3:")
println(matrix_form)

println("\n", "="^70, "\n")

println("🎉 vector demonstration complete!")
println("Julia Vectors are powerful, fast, and support advanced mathematical operations!")
