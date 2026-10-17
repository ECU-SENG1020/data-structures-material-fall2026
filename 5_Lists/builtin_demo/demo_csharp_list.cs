using System;
using System.Collections.Generic;

// Creating lists
var emptyList = new List<int>();
Console.WriteLine($"Empty list: [{string.Join(", ", emptyList)}]");

var fruits = new List<string> { "apple", "banana", "cherry" };
Console.WriteLine($"Fruits: [{string.Join(", ", fruits)}]");

var numbers = new List<int> { 1, 2, 3, 4, 5 };
Console.WriteLine($"Numbers: [{string.Join(", ", numbers)}]");

var mixed = new List<object> { 1, "hello", 3.14, true, null };
Console.WriteLine($"Mixed types: [{string.Join(", ", mixed.Select(x => x ?? "null"))}]");

var zeros = new List<int>(new int[5]);
Console.WriteLine($"Five zeros: [{string.Join(", ", zeros)}]");

var fromString = "hello".ToCharArray();
Console.WriteLine($"From string: [{string.Join(", ", fromString)}]");

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Accessing elements
var colors = new List<string> { "red", "green", "blue", "yellow", "purple" };
Console.WriteLine($"First color: {colors[0]}");
Console.WriteLine($"Third color: {colors[2]}");
Console.WriteLine($"Last color: {colors[^1]}");
Console.WriteLine($"Second to last: {colors[^2]}");

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Modifying elements
var pets = new List<string> { "dog", "cat", "bird" };
Console.WriteLine($"Original pets: [{string.Join(", ", pets)}]");
pets[1] = "hamster";
Console.WriteLine($"After replacing cat: [{string.Join(", ", pets)}]");
pets.RemoveRange(0, 2);
pets.Insert(0, "fish");
pets.Insert(1, "turtle");
Console.WriteLine($"After replacing first two: [{string.Join(", ", pets)}]");

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Adding elements
var shopping = new List<string> { "milk", "eggs" };
shopping.Add("bread");
Console.WriteLine($"After append: [{string.Join(", ", shopping)}]");
shopping.Insert(1, "butter");
Console.WriteLine($"After insert at index 1: [{string.Join(", ", shopping)}]");

var moreItems = new List<string> { "cheese", "yogurt" };
shopping.AddRange(moreItems);
Console.WriteLine($"After add range: [{string.Join(", ", shopping)}]");

var combined = new List<string>(shopping);
combined.AddRange(new[] { "apples", "oranges" });
Console.WriteLine($"Using + style: [{string.Join(", ", combined)}]");

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Removing elements
var tasks = new List<string> { "email", "coding", "meeting", "lunch", "coding", "review" };
Console.WriteLine($"Tasks: [{string.Join(", ", tasks)}]");

tasks.Remove("coding");
Console.WriteLine($"After Remove('coding'): [{string.Join(", ", tasks)}]");

var lastTask = tasks[^1];
tasks.RemoveAt(tasks.Count - 1);
Console.WriteLine($"Popped task: {lastTask}");
Console.WriteLine($"Tasks after pop: [{string.Join(", ", tasks)}]");

tasks.RemoveAt(1);
Console.WriteLine($"Tasks after RemoveAt(1): [{string.Join(", ", tasks)}]");

tasks.RemoveAt(0);
Console.WriteLine($"After RemoveAt(0): [{string.Join(", ", tasks)}]");

tasks.Clear();
Console.WriteLine($"After Clear(): [{string.Join(", ", tasks)}]");

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Slicing
var days = new List<string> { "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" };
Console.WriteLine($"Days: [{string.Join(", ", days)}]");
Console.WriteLine($"Weekdays: [{string.Join(", ", days.GetRange(0, 5))}]");
Console.WriteLine($"First three: [{string.Join(", ", days.GetRange(0, 3))}]");
Console.WriteLine($"Weekend: [{string.Join(", ", days.GetRange(5, 2))}]");
Console.WriteLine($"Every other: [{string.Join(", ", days.Where((_, i) => i % 2 == 0))}]");
var reversed = new List<string>(days);
reversed.Reverse();
Console.WriteLine($"Reversed: [{string.Join(", ", reversed)}]");

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Iteration
var animals = new List<string> { "dog", "cat", "bird", "fish" };
Console.WriteLine("Loop through values:");
foreach (var animal in animals)
{
    Console.WriteLine($"  Animal: {animal}");
}

Console.WriteLine();
Console.WriteLine("Loop with index:");
for (var index = 0; index < animals.Count; index++)
{
    Console.WriteLine($"  {index}: {animals[index]}");
}

Console.WriteLine();
Console.WriteLine("Using while loop:");
var i = 0;
while (i < animals.Count)
{
    Console.WriteLine($"  Position {i}: {animals[i]}");
    i++;
}

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Searching and checking
var numbersForSearch = new List<int> { 10, 20, 30, 40, 50, 30 };
Console.WriteLine($"Is 30 in the list? {numbersForSearch.Contains(30)}");
Console.WriteLine($"Is 100 in the list? {numbersForSearch.Contains(100)}");
Console.WriteLine($"First position of 30: {numbersForSearch.IndexOf(30)}");
Console.WriteLine($"Position of 30 after index 3: {numbersForSearch.FindIndex(3, value => value == 30)}");
Console.WriteLine($"How many times 30 appears: {numbersForSearch.Count(value => value == 30)}");

Console.WriteLine();
Console.WriteLine("=".PadRight(70, '='));

// Sorting
var unsorted = new List<int> { 64, 34, 25, 12, 22, 11, 90 };
Console.WriteLine($"Original: [{string.Join(", ", unsorted)}]");
unsorted.Sort();
Console.WriteLine($"After Sort(): [{string.Join(", ", unsorted)}]");

unsorted.Sort();
unsorted.Reverse();
Console.WriteLine($"After reverse sort: [{string.Join(", ", unsorted)}]");

var original = new List<int> { 64, 34, 25, 12, 22, 11, 90 };
var sortedCopy = new List<int>(original);
sortedCopy.Sort();
Console.WriteLine($"Original list: [{string.Join(", ", original)}]");
Console.WriteLine($"New sorted list: [{string.Join(", ", sortedCopy)}]");

var words = new List<string> { "zebra", "apple", "mango", "banana" };
words.Sort();
Console.WriteLine($"Sorted words: [{string.Join(", ", words)}]");
