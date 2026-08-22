# 5) Recursion
# Run: julia 5_recursion.jl

# Many problems can be solved with divide-and-conquer techniques.

function my_recursive_function(num_levels::Int)
    if num_levels == 0
        println("Base Case")
        return
    end

    println("Start Level $(num_levels)")

    my_recursive_function(num_levels - 1)

    println("Level $(num_levels) completed")
end

function main()
    my_recursive_function(3)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
