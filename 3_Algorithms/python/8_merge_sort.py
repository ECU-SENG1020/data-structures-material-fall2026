def merge(numbers, i, j, k):
    """Merge two sorted sublists of `numbers`.

    The sublists are numbers[i..j] and numbers[j+1..k]. This function
    creates a temporary list to hold the merged result in sorted order,
    then copies it back into the original list.
    """

    merged_size = k - i + 1
    merged_numbers = [0] * merged_size  # temporary storage for merged values
    merge_pos = 0
    left_pos = i
    right_pos = j + 1

    # Merge elements from the left and right partitions in order
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos += 1

    # If there are remaining items in the left partition, copy them
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1

    # If there are remaining items in the right partition, copy them
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1

    # Copy the merged, sorted values back into the original list slice
    for merge_pos in range(merged_size):
        numbers[i + merge_pos] = merged_numbers[merge_pos]


def merge_with_counts(numbers, i, j, k):
    """Merge that also returns comparison and copy counts for teaching.

    Returns a tuple (merged_list, comparisons, copies).
    """
    merged_size = k - i + 1
    merged_numbers = [0] * merged_size
    merge_pos = 0
    left_pos = i
    right_pos = j + 1
    comparisons = 0
    copies = 0

    while left_pos <= j and right_pos <= k:
        comparisons += 1
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos += 1
        copies += 1

    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1
        copies += 1

    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1
        copies += 1

    for merge_pos in range(merged_size):
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        # copying back counts as a copy operation
        copies += 1

    return numbers, comparisons, copies


def merge_sort(numbers, i, k):
    """Sort the list `numbers` between indexes i and k using merge sort.

    Merge sort is a divide-and-conquer algorithm: split the list into
    halves, sort each half recursively, then merge the sorted halves.
    """

    # Only continue if the slice has more than one element
    if i < k:
        # Find the midpoint to split into two halves
        j = (i + k) // 2
        # Recursively sort the left half
        merge_sort(numbers, i, j)
        # Recursively sort the right half
        merge_sort(numbers, j + 1, k)
        # Merge the two sorted halves
        merge(numbers, i, j, k)


def merge_sort_with_counts(numbers, i, k):
    """Merge sort wrapper that returns (sorted_list, comparisons, copies)."""
    nums = list(numbers)
    total_comps = 0
    total_copies = 0

    def _merge_sort(a, left, right):
        nonlocal total_comps, total_copies
        if left < right:
            mid = (left + right) // 2
            _merge_sort(a, left, mid)
            _merge_sort(a, mid + 1, right)
            _, comps, copies = merge_with_counts(a, left, mid, right)
            total_comps += comps
            total_copies += copies

    _merge_sort(nums, i, k)
    return nums, total_comps, total_copies


def main():
    # Example list for students to try
    numbers = [10, 2, 78, 4, 45, 32, 7, 11]
    print("UNSORTED:")
    print(" ".join(str(num) for num in numbers))

    # Sort the entire list (0 .. len(numbers)-1)
    merge_sort(numbers, 0, len(numbers) - 1)

    print("SORTED:")
    print(" ".join(str(num) for num in numbers))

    # Demo counts for teaching
    _, comps, copies = merge_sort_with_counts(numbers, 0, len(numbers) - 1)
    print(f"(demo) comparisons={comps}, copies={copies}")


if __name__ == "__main__":
    main()
