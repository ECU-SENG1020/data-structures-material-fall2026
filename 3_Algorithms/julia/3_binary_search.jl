# 3) Binary search
# Run: julia 3_binary_search.jl

"""Binary search on a sorted array.
Returns the index of target, or -1 if not found.

Note: Julia uses 1-based indexing.
"""
function binary_search(arr, target)
    low = firstindex(arr)
    high = lastindex(arr)

    while low <= high
        mid = (low + high) ÷ 2

        if arr[mid] == target
            return mid
        elseif arr[mid] < target
            low = mid + 1
        else
            high = mid - 1
        end
    end

    return -1
end

function binary_search_using_recursion(numbers, low::Int, high::Int, key)
    if low > high
        return -1
    end

    mid = (low + high) ÷ 2

    if numbers[mid] < key
        return binary_search_using_recursion(numbers, mid + 1, high, key)
    elseif numbers[mid] > key
        return binary_search_using_recursion(numbers, low, mid - 1, key)
    end

    return mid
end

function main()
    numbers = [1, 3, 4, 7, 9, 11, 15]
    target = 9

    result = binary_search(numbers, target)

    if result != -1
        println("Element $(target) found at index $(result)")
    else
        println("Element $(target) not found in the list")
    end

    println("***********")
    println(binary_search_using_recursion(numbers, firstindex(numbers), lastindex(numbers), 9))
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
