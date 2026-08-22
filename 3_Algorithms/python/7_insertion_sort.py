
def insertion_sort(numbers, numbersSize):
    """Sort `numbers` in place using insertion sort.

    Insertion sort builds a sorted section on the left. For each new
    element, it "inserts" it into the correct position among the
    elements that are already sorted.
    """

    # Loop over each position in the list. The sublist numbers[0:i]
    # is considered sorted before each iteration.
    for i in range(numbersSize):
        j = i

        # Move numbers[j] left until it is in the right spot
        # compared with the already-sorted portion.
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap the element with the previous one to move it left
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j -= 1


def insertion_sort_with_counts(numbers):
    """Insertion sort that returns (sorted_list, comparisons, shifts).

    `comparisons` counts element comparisons; `shifts` counts the number
    of times elements are moved (swapped) which shows the work done.
    """
    comps = 0
    shifts = 0
    nums = list(numbers)
    n = len(nums)

    for i in range(n):
        j = i
        while j > 0:
            comps += 1
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                shifts += 1
                j -= 1
            else:
                break

    return nums, comps, shifts


def main():
    # Example list for students to try
    numbers = [10, 2, 78, 4, 45, 32, 7, 11]
    NUMBERS_SIZE = len(numbers)

    print("UNSORTED:")
    print(numbers)
    print()

    insertion_sort(numbers, NUMBERS_SIZE)

    print("SORTED:")
    print(numbers)
    print()

    # Demo counts
    _, comps, shifts = insertion_sort_with_counts(numbers)
    print(f"(demo) comparisons={comps}, shifts={shifts}")


if __name__ == '__main__':
    main()
