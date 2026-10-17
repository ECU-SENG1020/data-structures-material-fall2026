using System;

static int BinarySearch(int[] arr, int target)
{
    var low = 0;
    var high = arr.Length - 1;

    while (low <= high)
    {
        var mid = (low + high) / 2;

        if (arr[mid] == target)
        {
            return mid;
        }
        else if (arr[mid] < target)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return -1;
}

static int BinarySearchUsingRecursion(int[] numbers, int low, int high, int key)
{
    if (low > high)
    {
        return -1;
    }

    var mid = (low + high) / 2;

    if (numbers[mid] < key)
    {
        return BinarySearchUsingRecursion(numbers, mid + 1, high, key);
    }
    else if (numbers[mid] > key)
    {
        return BinarySearchUsingRecursion(numbers, low, mid - 1, key);
    }

    return mid;
}

static void Main()
{
    var numbers = new[] { 1, 3, 4, 7, 9, 11, 15 };
    var target = 9;

    var result = BinarySearch(numbers, target);

    if (result != -1)
    {
        Console.WriteLine($"Element {target} found at index {result}");
    }
    else
    {
        Console.WriteLine($"Element {target} not found in the list");
    }

    Console.WriteLine("***********");
    Console.WriteLine(BinarySearchUsingRecursion(numbers, 0, numbers.Length - 1, 9));
}

Main();
