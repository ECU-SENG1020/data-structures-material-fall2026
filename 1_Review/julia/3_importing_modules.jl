# 3) Importing modules
# Run: julia 3_importing_modules.jl

# Import a standard library module
using Random

items = ["A", "B", "C", "D", "E"]
println("***available choices to choose from***")
println(items)
println("***first random choice***")
println(rand(items))
println("***second random choice***")
println(rand(items))
println()

println("***before shuffle***")
println(items)
shuffle!(items)
println("***after shuffle***")
println(items)
println()

# Import a specific function from a module
using Statistics: mean

nums = [1, 2, 3, 4]
println("mean of ", nums, " is: ", mean(nums))

# Another example: using Base's built-in power operator
println("2 to the power of 2 is: ", 2^2)
