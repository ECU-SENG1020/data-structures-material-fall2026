def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Target found, return its index
    return -1  # Target not found


def main():
    # Example usage
    numbers = [4, 2, 7, 1, 9, 3]
    target = 9

    result = linear_search(numbers, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the list")


if __name__ == "__main__":
    main()