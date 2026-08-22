include("SetDataStructure.jl")
include("HashedSetDataStructure.jl")

using .SetDataStructure: MySet, add!
using .HashedSetDataStructure: MyHashedSet, contains

my_setA = MySet()
my_setB = MySet()

for x in (1, 2, 3, 4, 5)
    add!(my_setA, x)
end
for x in (4, 5, 6, 7, 8)
    add!(my_setB, x)
end

println("Union: A | B = ", my_setA | my_setB)
println("Union: B | A = ", my_setB | my_setA)
println("Intersection: A & B = ", my_setA & my_setB)
println("Intersection: B & A = ", my_setB & my_setA)
println("Difference: A - B = ", my_setA - my_setB)
println("Difference: B - A = ", my_setB - my_setA)

println()

hs = MyHashedSet()
println("Hashed set initially: ", hs)
HashedSetDataStructure.add!(hs, "Hello")
HashedSetDataStructure.add!(hs, "World")
println("Hashed set after add: ", hs)
println("contains('Hello')? ", contains(hs, "Hello"))
