include("DsDictionaryModule.jl")
using .DsDictionaryModule: DsDictionary, keys, values, items

d = DsDictionary((("name", "Ada"), ("role", "Engineer")))
println(typeof(d))
println(d)

d["language"] = "Julia"
println(d)

println("keys: ", collect(keys(d)))
println("values: ", collect(values(d)))
println("items: ", collect(items(d)))
