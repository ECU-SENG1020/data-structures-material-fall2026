# 8) Generators and iterators
# Run: julia 8_generators.jl

# Generator "function" style (Julia uses Channels for yield-like behavior)
function generator_function()
    Channel() do ch
        put!(ch, "START")
        put!(ch, "PROCESSING")
        put!(ch, "DONE")
    end
end

gen = generator_function()

println("Print using generator (Channel) and iterate/for")
for state in gen
    println(state)
end

# List of numbers 0 through 9
numbers = [x for x in 0:9]

# Generator expression (lazy iterator)
# This does not build an array until you collect it.
gen_exp = (x^2 for x in numbers)

println("\nFirst five squares using a generator expression:")
for (i, x) in enumerate(gen_exp)
    println(x)
    if i == 5
        break
    end
end

println("\nCollecting squares into a vector:")
println(collect(x^2 for x in numbers))
