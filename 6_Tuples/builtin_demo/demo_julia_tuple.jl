#=
Julia Tuple Demonstration
A concise guide to Julia's immutable `Tuple` type
=#

using Printf

println("1. CREATING TUPLES")

# Empty tuple - use ()
empty = ()
println("Empty tuple:", empty)

# Literal tuple
point = (10, 20)
println("Point:", point)

# Single-element tuple - trailing comma required
single = (42,)
println("Single-element:", single)

println("\n", "="^60, "\n")

println("2. IMMUTABILITY")
tpl = (1, 2, 3)
println("Original:", tpl)
try
    tpl[1] = 99  # will error - tuples are immutable
catch e
    println("Cannot modify tuple (error): ", e)
end

println("\n", "="^60, "\n")

println("3. DESTRUCTURING / PACKING")
packed = 1, 2, 3  # packing
println("Packed:", packed)
x, y, z = packed
println("Unpacked:", x, y, z)

println("\n", "="^60, "\n")

println("4. SLICING / ITERATING")
nums = (10, 20, 30, 40, 30)
println("Slice 2:4 (note: tuples index from 1, use range):", nums[2:4])
println("Iterate:")
for n in nums
    println("  ", n)
end
println("Count of 30:", count(==(30), nums))
println("First index of 30:", findfirst(==(30), nums))
println("Is 100 in tuple?", 100 in nums)

println("\n", "="^60, "\n")

println("5. CONCATENATION & CONVERSION")
t1 = (1, 2)
t2 = (3, 4)
println("Concat:", (t1..., t2...))  # splat into new tuple
mutable = collect(t1)  # convert to vector to modify
push!(mutable, 99)
println("Modified via conversion:", Tuple(mutable))

println("\nTuple demo complete (Julia).")
