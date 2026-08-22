# 6) Selection sort
# Run: julia 6_selection_sort.jl

"""Sort the vector `numbers` in-place using selection sort."""
function selection_sort!(numbers)
    # We go from the first element to the second-to-last element.
    for i in firstindex(numbers):(lastindex(numbers) - 1)
        index_smallest = i

        for j in (i + 1):lastindex(numbers)
            if numbers[j] < numbers[index_smallest]
                index_smallest = j
            end
        end

        numbers[i], numbers[index_smallest] = numbers[index_smallest], numbers[i]
    end

    return numbers
end

"""Selection sort demo that returns (sorted_copy, comparisons, swaps)."""
function selection_sort_with_counts(numbers)
    comparisons = 0
    swaps = 0
    nums = copy(numbers)

    for i in firstindex(nums):(lastindex(nums) - 1)
        index_smallest = i

        for j in (i + 1):lastindex(nums)
            comparisons += 1
            if nums[j] < nums[index_smallest]
                index_smallest = j
            end
        end

        nums[i], nums[index_smallest] = nums[index_smallest], nums[i]
        swaps += 1
    end

    return nums, comparisons, swaps
end

function main()
    numbers = [10, 2, 78, 4, 45, 32, 7, 11]
    numbers2 = [10, 2, 78, 4, 45, 32, 7, 11]

    println("UNSORTED:")
    println(numbers)
    println()

    selection_sort!(numbers)

    _, comps, swaps = selection_sort_with_counts(numbers2)
    println("(demo) comparisons=$(comps), swaps=$(swaps)")

    println("SORTED:")
    println(numbers)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
