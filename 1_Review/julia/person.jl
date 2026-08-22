module PersonModule

    export Person, Dog, Cat, greet

    # In Julia, custom types are usually structs.
    # "mutable" means we can change fields after creation.
    mutable struct Person
        name::String
        age::Int
    end

    mutable struct Dog
        name::String
        age::Int
    end

    mutable struct Cat
        name::String
        age::Int
    end

    # Functions live outside structs; multiple dispatch picks the right one.
    function greet(p::Person)
        println("Hello, my name is $(p.name) and I am $(p.age) years old.")
    end

    # greet(p::Person) = println("Hello, my name is $(p.name) and I am $(p.age) years old.")

    greet(d::Dog) = println("Wuf")
    greet(c::Cat) = println("Meow")

end
