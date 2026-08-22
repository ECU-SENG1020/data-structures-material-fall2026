"""
Julia Dictionary Demonstration
A brief look at Julia's Dict collection and common operations
"""

# 1. Creating dictionaries
empty = Dict()
println("Empty Dict: ", empty)

profile = Dict("name" => "Ada", "role" => "Engineer")
println("Profile: ", profile)

from_pairs = Dict(["a" => 1, "b" => 2, "c" => 3])
println("From pairs: ", from_pairs)

println("\n", "="^60, "\n")

# 2. Adding, updating, removing
scores = Dict("alice" => 90, "bob" => 82)
println("Original: ", scores)

scores["carol"] = 95
println("After add carol: ", scores)

scores["alice"] = 93
println("After update alice: ", scores)

removed = pop!(scores, "bob")
println("Popped bob: ", removed, " Remaining: ", scores)

missing = get(scores, "missing", "n/a")
println("Safe get missing: ", missing)

delete!(scores, "carol")
println("After delete! carol: ", scores)

empty!(scores)
println("After empty!: ", scores)

println("\n", "="^60, "\n")

# 3. Membership, lookup, iteration
inventory = Dict("pen" => 10, "notebook" => 5, "eraser" => 2)
println("Inventory: ", inventory)
println("Has key 'pen'? ", haskey(inventory, "pen"))
println("Safe get marker: ", get(inventory, "marker", 0))

println("Keys:")
for k in keys(inventory)
    println("  ", k)
end

println("Values:")
for v in values(inventory)
    println("  ", v)
end

println("Pairs:")
for (k, v) in inventory
    println("  ", k, " -> ", v)
end

println("\n", "="^60, "\n")

# 4. Merge / copy / comprehensions
a = Dict("x" => 1, "y" => 2)
b = Dict("y" => 20, "z" => 3)
merged = merge(a, b)
println("Merged: ", merged)

copied = copy(merged)
copied["w"] = 0
println("Copy then update: ", copied)

squares = Dict(n => n^2 for n in 0:5)
println("Squares: ", squares)

println("\n", "="^60, "\n")

# 5. Key type notes
coords = Dict((0, 0) => "origin", (1, 2) => "point")
println("Tuple keys are valid: ", coords)

println("Julia Dictionary demo complete")
