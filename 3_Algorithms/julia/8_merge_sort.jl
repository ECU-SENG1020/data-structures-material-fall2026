# 8) Merge sort
# Run: julia 8_merge_sort.jl

"""Merge two sorted ranges in `numbers`: i..j and (j+1)..k (inclusive)."""
function merge!(numbers, i::Int, j::Int, k::Int)
    merged_size = k - i + 1
    merged_numbers = Vector{eltype(numbers)}(undef, merged_size)

    merge_pos = 1
    left_pos = i
    right_pos = j + 1

    while left_pos <= j && right_pos <= k
        if numbers[left_pos] <= numbers[right_pos]
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        end
        merge_pos += 1
    end

    while left_pos <= j
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1
    end

    while right_pos <= k
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1
    end

    for pos in 1:merged_size
        numbers[i + pos - 1] = merged_numbers[pos]
    end

    return numbers
end

"""Merge that also returns (comparisons, copies) for teaching."""
function merge_with_counts!(numbers, i::Int, j::Int, k::Int)
    merged_size = k - i + 1
    merged_numbers = Vector{eltype(numbers)}(undef, merged_size)

    merge_pos = 1
    left_pos = i
    right_pos = j + 1
    comparisons = 0
    copies = 0

    while left_pos <= j && right_pos <= k
        comparisons += 1
        if numbers[left_pos] <= numbers[right_pos]
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        end
        merge_pos += 1
        copies += 1
    end

    while left_pos <= j
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1
        copies += 1
    end

    while right_pos <= k
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1
        copies += 1
    end

    for pos in 1:merged_size
        numbers[i + pos - 1] = merged_numbers[pos]
        copies += 1
    end

    return comparisons, copies
end

"""Sort `numbers` between indices i and k (inclusive) using merge sort."""
function merge_sort!(numbers, i::Int, k::Int)
    if i < k
        j = (i + k) ÷ 2
        merge_sort!(numbers, i, j)
        merge_sort!(numbers, j + 1, k)
        merge!(numbers, i, j, k)
    end
    return numbers
end

"""Merge sort wrapper that returns (sorted_copy, comparisons, copies)."""
function merge_sort_with_counts(numbers)
    nums = copy(numbers)

    # Use Refs so the inner function can update counters (beginner-friendly)
    total_comps_local = Ref(0)
    total_copies_local = Ref(0)

    function _merge_sort!(a, left::Int, right::Int)
        if left < right
            mid = (left + right) ÷ 2
            _merge_sort!(a, left, mid)
            _merge_sort!(a, mid + 1, right)
            comps, copies = merge_with_counts!(a, left, mid, right)
            total_comps_local[] += comps
            total_copies_local[] += copies
        end
    end

    _merge_sort!(nums, firstindex(nums), lastindex(nums))

    return nums, total_comps_local[], total_copies_local[]
end

function main()
    numbers = [10, 2, 78, 4, 45, 32, 7, 11]
    println("UNSORTED:")
    println(join(string.(numbers), " "))

    merge_sort!(numbers, firstindex(numbers), lastindex(numbers))

    println("SORTED:")
    println(join(string.(numbers), " "))

    _, comps, copies = merge_sort_with_counts(numbers)
    println("(demo) comparisons=$(comps), copies=$(copies)")
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
