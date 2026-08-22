# 2) Linear search
# Run: julia 2_linear_search.jl

"""Return the index of target in arr, or -1 if not found.

Note: Julia uses 1-based indexing.
"""
function linear_search(arr, target)
    for index in eachindex(arr)
        if arr[index] == target
            return index
        end
    end
    return -1
end

function main()
    numbers = [4, 2, 7, 1, 9, 3]
    target = 9

    result = linear_search(numbers, target)

    if result != -1
        println("Element $(target) found at index $(result)")
    else
        println("Element $(target) not found in the list")
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
