# 7) Insertion sort
# Run: julia 7_insertion_sort.jl

"""Sort `numbers` in-place using insertion sort."""
function insertion_sort!(numbers)
    n = length(numbers)

    # The left side (1..i) is the sorted portion.
    for i in 1:n
        j = i
        while j > 1 && numbers[j] < numbers[j - 1]
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
        end
    end

    return numbers
end

"""Insertion sort that returns (sorted_copy, comparisons, shifts)."""
function insertion_sort_with_counts(numbers)
    comps = 0
    shifts = 0
    nums = copy(numbers)
    n = length(nums)

    for i in 1:n
        j = i
        while j > 1
            comps += 1
            if nums[j] < nums[j - 1]
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                shifts += 1
                j -= 1
            else
                break
            end
        end
    end

    return nums, comps, shifts
end

function main()
    numbers = [10, 2, 78, 4, 45, 32, 7, 11]

    println("UNSORTED:")
    println(numbers)
    println()

    insertion_sort!(numbers)

    println("SORTED:")
    println(numbers)
    println()

    _, comps, shifts = insertion_sort_with_counts([10, 2, 78, 4, 45, 32, 7, 11])
    println("(demo) comparisons=$(comps), shifts=$(shifts)")
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
