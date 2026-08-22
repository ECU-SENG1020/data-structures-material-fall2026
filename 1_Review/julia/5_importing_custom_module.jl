# 5) Importing a custom module
# Run: julia 5_importing_custom_module.jl

include("person.jl")

# `using .PersonModule` brings exported names into scope
using .PersonModule

p0 = Person("Alice", 30)
greet(p0)

d1 = Dog("Cinna", 2)
greet(d1)

d2 = Dog("Joey", 13)
greet(d2)

c1 = Cat("Cat1", 100)
greet(c1)
