using System;
using System.Collections.Generic;

static void SelectionSort(List<int> numbers)
{
    for (var i = 0; i < numbers.Count - 1; i++)
    {
        var indexSmallest = i;

        for (var j = i + 1; j < numbers.Count; j++)
        {
            if (numbers[j] < numbers[indexSmallest])
            {
                indexSmallest = j;
            }
        }

        var temp = numbers[i];
        numbers[i] = numbers[indexSmallest];
        numbers[indexSmallest] = temp;
    }
}

static (List<int> numbers, int comparisons, int swaps) SelectionSortWithCounts(List<int> numbers)
{
    var comparisons = 0;
    var swaps = 0;
    var nums = new List<int>(numbers);

    for (var i = 0; i < nums.Count - 1; i++)
    {
        var indexSmallest = i;

        for (var j = i + 1; j < nums.Count; j++)
        {
            comparisons++;
            if (nums[j] < nums[indexSmallest])
            {
                indexSmallest = j;
            }
        }

        var temp = nums[i];
        nums[i] = nums[indexSmallest];
        nums[indexSmallest] = temp;
        swaps++;
    }

    return (nums, comparisons, swaps);
}

static void Main()
{
    var numbers = new List<int> { 10, 2, 78, 4, 45, 32, 7, 11 };
    var numbers2 = new List<int> { 10, 2, 78, 4, 45, 32, 7, 11 };

    Console.WriteLine("UNSORTED:");
    Console.WriteLine(string.Join(" ", numbers));
    Console.WriteLine();

    SelectionSort(numbers);

    var (_, comps, swaps) = SelectionSortWithCounts(numbers2);
    Console.WriteLine($"(demo) comparisons={comps}, swaps={swaps}");

    Console.WriteLine("SORTED:");
    Console.WriteLine(string.Join(" ", numbers));
}

Main();
