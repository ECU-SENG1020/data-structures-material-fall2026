"""
Julia Set Demonstration
A brief look at Julia's Set collection and common operations
"""

# 1. Creating sets
empty = Set()
println("Empty set:", empty)

fruits = Set(["apple", "banana", "apple", "cherry"])
println("Fruits (duplicates removed): ", fruits)

# 2. Adding and removing
s = Set([1,2,3])
push!(s, 4)
println("After push!: ", s)
delete!(s, 2)
println("After delete!: ", s)

# 3. Membership and iteration
println("Is 3 in s?", 3 in s)
for x in s
    println("  ", x)
end

# 4. Set algebra
a = Set([1,2,3,4])
b = Set([3,4,5,6])
println("Union: ", union(a,b))
println("Intersect: ", intersect(a,b))
println("Difference (a \\ b): ", setdiff(a,b))

# 5. Subset / superset
println("issubset([1,2], a):", issubset(Set([1,2]), a))

# 6. Conversion
arr = collect(a)
println("Array from set:", arr)

println("Julia Set demo complete")
