# 7) Comprehensions (vector, set, dict)
# Run: julia 7_comprehensions.jl

numbers = [x for x in 0:9]
println("List of numbers:")
println(numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
println("Even numbers:")
println(even_numbers)

odd_numbers = [x for x in numbers if x % 2 != 0]
println("Odd numbers:")
println(odd_numbers)

squared_numbers = [x^2 for x in numbers]
println("Squared numbers:")
println(squared_numbers)

double_num(x) = x * 2
numbers_list = [double_num(x) for x in numbers]
println(numbers_list)

numbers_set = Set([x for x in numbers])
println("Set of numbers:")
println(numbers_set)

dictionary_squared_numbers = Dict(string(x) => x^2 for x in numbers)
println("Dictionary of squared numbers:")
println(dictionary_squared_numbers)
