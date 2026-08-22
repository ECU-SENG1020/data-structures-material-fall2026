# 1) Basic Julia concepts
# Run: julia 1_basic_concepts.jl

println("It's me")

# In Julia you can define functions before or after you call them
# (as long as the code is executed in order). In scripts, define first.

function greet()
    println("Hello, World!")
    println("Hello again")
    # If you don't return anything, Julia returns `nothing`
end

function greet2()
    print("Hello, World!: ")
end

function add(num1, num2)
    return num1 + num2
end

greet()
greet()

greet2()
greet2()

println(add(1, 2))

# Prints `nothing` because greet() returns nothing
println(greet())

items = [1, 2, 3]
items2 = repeat(items, 2)  # duplicate each element
println(items2)


items3 = [item * 2 for item in items]
println(items3)


items4 = items .* 2  # element-wise multiplication
println(items4)

items5 = map(x -> x * 2, items)
println(items5)

items6 = [2 * item for item in items if item % 2 == 1]  # only odd items
println(items6)

items7 = filter(x -> x % 2 == 1, items)  # only odd items
println(items7)

items8 = map(x -> x * 2, filter(x -> x % 2 == 1, items))  # only odd items
println(items8)

items9 = items |> 
    x -> filter(y -> y % 2 == 1, x) |> 
    x -> map(y -> y * 2, x)
println(items9)