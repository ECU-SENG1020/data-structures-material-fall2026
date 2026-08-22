def merge(numbers, start_index, mid_index, end_index, reverse=False):
    """Merge two sorted sublists of `numbers`.

    The sublists are numbers[start_index..mid_index] and numbers[mid_index+1..end_index]. This function
    creates a temporary list to hold the merged result in sorted order,
    then copies it back into the original list.
    """

    merged_size = end_index - start_index + 1
    merged_numbers = [0] * merged_size  # temporary storage for merged values
    merge_pos = 0
    left_pos = start_index
    right_pos = mid_index + 1

    # Merge elements from the left and right partitions in order
    while left_pos <= mid_index and right_pos <= end_index:
        if (numbers[left_pos] <= numbers[right_pos]) ^ reverse:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos += 1

    # If there are remaining items in the left partition, copy them
    while left_pos <= mid_index:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1

    # If there are remaining items in the right partition, copy them
    while right_pos <= end_index:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1

    # Copy the merged, sorted values back into the original list slice
    for merge_pos in range(merged_size):

        numbers[start_index + merge_pos] = merged_numbers[merge_pos]


def merge_sort(numbers, start_index, end_index, reverse = False):

    # Only continue if the slice has more than one element
    if start_index == end_index:
        # Base case: a slice of length 0 or 1 is already sorted
        return
    else:
        # Find the midpoint to split into two halves
        mid_index = (start_index + end_index) // 2

        # Recursively sort the left half
        merge_sort(numbers, start_index, mid_index, reverse)
        # Recursively sort the right half
        merge_sort(numbers, mid_index + 1, end_index, reverse)
        
        # Merge the two sorted halves
        merge(numbers, start_index, mid_index, end_index,reverse)




