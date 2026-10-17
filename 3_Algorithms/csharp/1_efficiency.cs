using System;
using System.Collections.Generic;
using System.Diagnostics;

static List<int> GetEvenNumbersVersionOne(int fromNum, int toNum)
{
    var number = fromNum;
    var evenNumbers = new List<int>();

    while (number <= toNum)
    {
        if (number % 2 == 0)
        {
            evenNumbers.Add(number);
        }

        number += 1;
    }

    return evenNumbers;
}

static List<int> GetEvenNumbersVersionTwo(int fromNum, int toNum)
{
    var number = fromNum;
    var evenNumbers = new List<int>();

    while (number <= toNum)
    {
        if (number % 2 == 0)
        {
            evenNumbers.Add(number);
        }

        number += 2;
    }

    return evenNumbers;
}

static void Main()
{
    var startTime = Stopwatch.GetTimestamp();
    _ = GetEvenNumbersVersionOne(2, 1000);
    var endTime = Stopwatch.GetTimestamp();
    var elapsedTime = (long)((endTime - startTime) * 1_000_000_000.0 / Stopwatch.Frequency);
    Console.WriteLine($"Algorithm 1 took {elapsedTime} nanoseconds.");

    startTime = Stopwatch.GetTimestamp();
    _ = GetEvenNumbersVersionTwo(2, 1000);
    endTime = Stopwatch.GetTimestamp();
    elapsedTime = (long)((endTime - startTime) * 1_000_000_000.0 / Stopwatch.Frequency);
    Console.WriteLine($"Algorithm 2 took {elapsedTime} nanoseconds.");
}

Main();
