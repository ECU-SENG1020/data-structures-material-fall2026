include("DsDictionaryModule.jl")

using .DsDictionaryModule: DsDictionary, keys, values, items

my_dict2 = DsDictionary((("a", 1), ("b", 2)))
println(my_dict2)

my_dict = DsDictionary()
println(names(typeof(my_dict)))

my_dict["name"] = "Alice"
my_dict["age"] = 25

keys_view = keys(my_dict)
values_view = values(my_dict)
items_view = items(my_dict)

println(keys_view)
println(values_view)
println(items_view)

my_dict["city"] = "New York"

println(keys_view)
println(values_view)
println(items_view)
