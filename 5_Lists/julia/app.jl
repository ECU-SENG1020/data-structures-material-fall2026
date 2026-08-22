include("ListModule.jl")
using .ListModule: DsList, append!

my_list = DsList()

append!(my_list, 1)
append!(my_list, 2)
append!(my_list, 3)
append!(my_list, 1)
append!(my_list, 2)
append!(my_list, 3)

println(length(my_list))
println(my_list)

custom_string_list = DsList()
append!(custom_string_list, "a")
append!(custom_string_list, "b")
println(custom_string_list)

println(my_list[1])  # Julia is 1-based indexing

# Example iteration:
for item in my_list
    println(item)
end

# Example contains:
println(3 in my_list)