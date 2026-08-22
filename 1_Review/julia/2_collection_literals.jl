# 2) Collection literals
# Run: julia 2_collection_literals.jl

# Vector (like a Python list)
# - mutable
# - can hold different types (but it's best to keep them the same)
fruit_vector = ["apple", "banana", "cherry"]

# Tuple
# - immutable (can't change its size)
fruit_tuple = ("apple", "banana", "cherry")

# Dict (like a Python dictionary)
fruit_dict = Dict("a" => "apple", "b" => "banana")

# Set (unique values)
fruit_set = Set(["apple", "banana", "cherry", "cherry"])

# Converting a tuple to a vector
fruits2 = collect(fruit_tuple)

println("***** Vector *****")
for fruit in fruit_vector
    println(fruit)
end

println("***** Tuple *****")
for fruit in fruit_tuple
    println(fruit)
end

println("***** Set *****")
for fruit in fruit_set
    println(fruit)
end

println("***** Dict *****")
# Dict iteration yields pairs: (key => value)
for (key, value) in fruit_dict
    println(key, " ", value)
end

println("Keys:")
for key in keys(fruit_dict)
    println(key)
end

println("Values:")
for value in values(fruit_dict)
    println(value)
end
