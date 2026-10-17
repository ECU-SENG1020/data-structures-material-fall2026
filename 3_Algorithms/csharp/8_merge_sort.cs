using System;
using System.Collections.Generic;

static void Merge(List<int> numbers, int i, int j, int k)
{
    var mergedSize = k - i + 1;
    var mergedNumbers = new List<int>(new int[mergedSize]);
    var mergePos = 0;
    var leftPos = i;
    var rightPos = j + 1;

    while (leftPos <= j && rightPos <= k)
    {
        if (numbers[leftPos] <= numbers[rightPos])
        {
            mergedNumbers[mergePos] = numbers[leftPos];
            leftPos++;
        }
        else
        {
            mergedNumbers[mergePos] = numbers[rightPos];
            rightPos++;
        }

        mergePos++;
    }

    while (leftPos <= j)
    {
        mergedNumbers[mergePos] = numbers[leftPos];
        leftPos++;
        mergePos++;
    }

    while (rightPos <= k)
    {
        mergedNumbers[mergePos] = numbers[rightPos];
        rightPos++;
        mergePos++;
    }

    for (var pos = 0; pos < mergedSize; pos++)
    {
        numbers[i + pos] = mergedNumbers[pos];
    }
}

static (List<int> numbers, int comparisons, int copies) MergeWithCounts(List<int> numbers, int i, int j, int k)
{
    var mergedSize = k - i + 1;
    var mergedNumbers = new List<int>(new int[mergedSize]);
    var mergePos = 0;
    var leftPos = i;
    var rightPos = j + 1;
    var comparisons = 0;
    var copies = 0;

    while (leftPos <= j && rightPos <= k)
    {
        comparisons++;
        if (numbers[leftPos] <= numbers[rightPos])
        {
            mergedNumbers[mergePos] = numbers[leftPos];
            leftPos++;
        }
        else
        {
            mergedNumbers[mergePos] = numbers[rightPos];
            rightPos++;
        }

        mergePos++;
        copies++;
    }

    while (leftPos <= j)
    {
        mergedNumbers[mergePos] = numbers[leftPos];
        leftPos++;
        mergePos++;
        copies++;
    }

    while (rightPos <= k)
    {
        mergedNumbers[mergePos] = numbers[rightPos];
        rightPos++;
        mergePos++;
        copies++;
    }

    for (var pos = 0; pos < mergedSize; pos++)
    {
        numbers[i + pos] = mergedNumbers[pos];
        copies++;
    }

    return (numbers, comparisons, copies);
}

static void MergeSort(List<int> numbers, int i, int k)
{
    if (i < k)
    {
        var j = (i + k) / 2;
        MergeSort(numbers, i, j);
        MergeSort(numbers, j + 1, k);
        Merge(numbers, i, j, k);
    }
}

static (List<int> numbers, int comparisons, int copies) MergeSortWithCounts(List<int> numbers, int i, int k)
{
    var nums = new List<int>(numbers);
    var totalComparisons = 0;
    var totalCopies = 0;

    void Sort(List<int> arr, int left, int right)
    {
        if (left < right)
        {
            var mid = (left + right) / 2;
            Sort(arr, left, mid);
            Sort(arr, mid + 1, right);
            (var _, int comparisons, int copies) = MergeWithCounts(arr, left, mid, right);
            totalComparisons += comparisons;
            totalCopies += copies;
        }
    }

    Sort(nums, i, k);
    return (nums, totalComparisons, totalCopies);
}

static void Main()
{
    var numbers = new List<int> { 10, 2, 78, 4, 45, 32, 7, 11 };
    Console.WriteLine("UNSORTED:");
    Console.WriteLine(string.Join(" ", numbers));

    MergeSort(numbers, 0, numbers.Count - 1);

    Console.WriteLine("SORTED:");
    Console.WriteLine(string.Join(" ", numbers));

    var (_, comps, copies) = MergeSortWithCounts(numbers, 0, numbers.Count - 1);
    Console.WriteLine($"(demo) comparisons={comps}, copies={copies}");
}

Main();
