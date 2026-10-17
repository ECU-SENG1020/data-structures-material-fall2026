using System;

static int LinearSearch(int[] arr, int target)
{
    for (var index = 0; index < arr.Length; index++)
    {
        if (arr[index] == target)
        {
            return index;
        }
    }

    return -1;
}

static void Main()
{
    var numbers = new[] { 4, 2, 7, 1, 9, 3 };
    var target = 9;

    var result = LinearSearch(numbers, target);

    if (result != -1)
    {
        Console.WriteLine($"Element {target} found at index {result}");
    }
    else
    {
        Console.WriteLine($"Element {target} not found in the list");
    }
}

Main();
