def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
    return -1  # Target not found

# [1, 3, 4, 7, 9, 11, 15]



def binary_search_using_recursion(numbers, low, high, key): 
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] < key: 
        return binary_search_using_recursion(numbers, mid + 1, high, key)

    elif numbers[mid] > key:
        return binary_search_using_recursion(numbers, low, mid - 1, key)

    return mid


def main():
    # Example usage
    numbers = [1, 3, 4, 7, 9, 11, 15]
    target = 9

    result = binary_search(numbers, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the list")

    print("***********")
    print(binary_search_using_recursion(numbers,0,6,9))



if __name__ == "__main__":
    main()


