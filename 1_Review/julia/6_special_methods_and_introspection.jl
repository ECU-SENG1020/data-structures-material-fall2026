# 6) "Dunder" equivalents in Julia: special methods + introspection
# Run: julia 6_special_methods_and_introspection.jl

using Random

mutable struct Person
    name::String
    age::Int
end

# Pretty printing (similar idea to Python __str__)
Base.show(io::IO, p::Person) = print(io, "Person(name=$(p.name), age=$(p.age))")

# Comparison (like Python __ge__)
Base.:>=(a::Person, b::Person) = a.age >= b.age

# Operator overloading (like Python __add__)
function Base.:+(a::Person, b::Person)
    sex = rand(["boy", "girl"])
    return Person("Baby $(sex)", 0)
end

fruits = ["apple", "banana", "cherry"]
println(fruits)

p1 = Person("Alice", 35)
println(p1)

p2 = Person("Bob", 30)
println(p2)

println("Alice is older than Bob: ", p1 >= p2)

p3 = p1 + p2
println(p3)

# Introspection helpers
println("\nType info:")
println(typeof(p1))
println(fieldnames(Person))

println("\nMethods for + (showing a few):")
println(first(methods(+), 5))
