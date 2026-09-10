using System;
using System.Collections.Generic;
using System.Linq;

var numbers = Enumerable.Range(0, 10).ToList();
Console.WriteLine("List of numbers:");
Console.WriteLine(string.Join(", ", numbers));

var evenNumbers = numbers.Where(x => x % 2 == 0).ToList();
Console.WriteLine("Even numbers:");
Console.WriteLine(string.Join(", ", evenNumbers));

var oddNumbers = numbers.Where(x => x % 2 != 0).ToList();
Console.WriteLine("Odd numbers:");
Console.WriteLine(string.Join(", ", oddNumbers));

var squaredNumbers = numbers.Select(x => x * x).ToList();
Console.WriteLine("Squared numbers:");
Console.WriteLine(string.Join(", ", squaredNumbers));

static int DoubleNum(int value) => value * 2;

var numbersList = numbers.Select(DoubleNum).ToList();
Console.WriteLine(string.Join(", ", numbersList));

var numbers2 = new[] { 1, 1, 2, 3, 4, 4, 5, 6, 7, 7 };
var numbersSet = numbers2.Distinct().ToHashSet();
Console.WriteLine("Set of numbers:");
Console.WriteLine(string.Join(", ", numbersSet.OrderBy(x => x)));

var dictionarySquaredNumbers = numbers.ToDictionary(x => x.ToString(), x => x * x);
Console.WriteLine("Dictionary of squared numbers:");
foreach (var item in dictionarySquaredNumbers)
{
    Console.WriteLine($"{item.Key}: {item.Value}");
}
