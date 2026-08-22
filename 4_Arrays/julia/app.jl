include("ArrayModule.jl")
include("IntegerArrayModule.jl")

using .ArrayModule: DsArray
using .IntegerArrayModule: IntArray

#############################
# Example using IntArray
#############################

myIntArray = IntArray(3)

myIntArray[1] = 42
myIntArray[2] = 7
myIntArray[3] = 13

println(size(myIntArray))

println("myIntArray[1] = $(myIntArray[1])")

foreach(println, myIntArray)
foreach(x -> println("Value: $x"), myIntArray)

show(myIntArray)
println()
println(myIntArray)


#############################
# Example using DsArray with a Float64 type
#############################

myDsArray = DsArray{Float64}(4)

myDsArray[1] = 3.14
myDsArray[2] = 2.71
myDsArray[3] = 1.41
myDsArray[4] = 1.73

println(size(myDsArray))

println("myDsArray[1] = $(myDsArray[1])")

foreach(println, myDsArray)
foreach(x -> println("Value: $x"), myDsArray)

show(myDsArray)
println()
println(myDsArray)


#############################
# Example using DsArray with Boolean type
#############################

myBooleanArray = DsArray{Bool}(3)

myBooleanArray[1] = true
myBooleanArray[2] = false
myBooleanArray[3] = true

println(size(myBooleanArray))

println("myBooleanArray[1] = $(myBooleanArray[1])")

foreach(println, myBooleanArray)
foreach(x -> println("Value: $x"), myBooleanArray)

show(myBooleanArray)
println()
println(myBooleanArray)


#############################
# Example using DsArray with Char type
#############################

myCharArray = DsArray{Char}(3)

myCharArray[1] = 'A'
myCharArray[2] = 'B'
myCharArray[3] = 'C'

println(size(myCharArray))

println("myCharArray[1] = $(myCharArray[1])")

foreach(println, myCharArray)
foreach(x -> println("Value: $x"), myCharArray)

show(myCharArray)
println()
println(myCharArray)


#############################
# Example using DsArray with String type
#############################


# myStringArray = DsArray{String}(3)

# myStringArray[1] = "Hello"
# myStringArray[2] = "World"
# myStringArray[3] = "Julia"

# println(size(myStringArray))

# println("myStringArray[1] = $(myStringArray[1])")

# foreach(println, myStringArray)
# foreach(x -> println("Value: $x"), myStringArray)

# show(myStringArray)
# println()
# println(myStringArray)

