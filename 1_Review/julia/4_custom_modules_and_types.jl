# 4) Creating custom modules and types
# Run: julia 4_custom_modules_and_types.jl

include("person.jl")
using .PersonModule: Person, Dog, Cat, greet

p1 = Person("Alice", 30)
greet(p1)

p2 = Person("Bob", 25)
greet(p2)

d1 = Dog("Cinna", 2)
greet(d1)

c1 = Cat("Cat1", 100)
greet(c1)
