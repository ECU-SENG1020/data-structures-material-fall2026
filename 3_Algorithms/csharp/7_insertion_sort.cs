using System;
using System.Collections.Generic;

static void InsertionSort(List<int> numbers, int numbersSize)
{
    for (var i = 0; i < numbersSize; i++)
    {
        var j = i;

        while (j > 0 && numbers[j] < numbers[j - 1])
        {
            var temp = numbers[j];
            numbers[j] = numbers[j - 1];
            numbers[j - 1] = temp;
            j--;
        }
    }
}

static (List<int> numbers, int comparisons, int shifts) InsertionSortWithCounts(List<int> numbers)
{
    var comps = 0;
    var shifts = 0;
    var nums = new List<int>(numbers);
    var n = nums.Count;

    for (var i = 0; i < n; i++)
    {
        var j = i;

        while (j > 0)
        {
            comps++;
            if (nums[j] < nums[j - 1])
            {
                var temp = nums[j];
                nums[j] = nums[j - 1];
                nums[j - 1] = temp;
                shifts++;
                j--;
            }
            else
            {
                break;
            }
        }
    }

    return (nums, comps, shifts);
}

static void Main()
{
    var numbers = new List<int> { 10, 2, 78, 4, 45, 32, 7, 11 };
    var numbersSize = numbers.Count;

    Console.WriteLine("UNSORTED:");
    Console.WriteLine(string.Join(" ", numbers));
    Console.WriteLine();

    InsertionSort(numbers, numbersSize);

    Console.WriteLine("SORTED:");
    Console.WriteLine(string.Join(" ", numbers));
    Console.WriteLine();

    var (_, comps, shifts) = InsertionSortWithCounts(numbers);
    Console.WriteLine($"(demo) comparisons={comps}, shifts={shifts}");
}

Main();
