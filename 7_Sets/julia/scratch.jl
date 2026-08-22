include("SetByDictionary.jl")
using .SetByDictionary: MySetDict, add!

s = MySetDict(1, 2, 3)
println(typeof(s))
println(s)
add!(s, 4)
println(s)
