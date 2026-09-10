using System;

var items = new[] { "A", "B", "C", "D", "E" };
var random = new Random();

Console.WriteLine("***available choices to choose from***");
Console.WriteLine(string.Join(", ", items));
Console.WriteLine("***first random choice***");
Console.WriteLine(items[random.Next(items.Length)]);
Console.WriteLine("***second random choice***");
Console.WriteLine(items[random.Next(items.Length)]);
Console.WriteLine();

Console.WriteLine($"2 to the power of 2 is: {Math.Pow(2, 2)}");
