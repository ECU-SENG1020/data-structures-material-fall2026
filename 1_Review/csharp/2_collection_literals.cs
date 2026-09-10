using System;
using System.Collections.Generic;

var fruitList = new List<string> { "apple", "banana", "cherry" };
var fruitTuple = ("apple", "banana", "cherry");
var fruitDictionary = new Dictionary<string, string>
{
    ["a"] = "apple",
    ["b"] = "banana"
};
var fruitSet = new HashSet<string> { "apple", "banana", "cherry", "cherry" };

Console.WriteLine("***** List *****");
foreach (var fruit in fruitList)
{
    Console.WriteLine(fruit);
}

Console.WriteLine("***** tuple *****");
Console.WriteLine(fruitTuple.Item1);
Console.WriteLine(fruitTuple.Item2);
Console.WriteLine(fruitTuple.Item3);

Console.WriteLine("***** set *****");
foreach (var fruit in fruitSet)
{
    Console.WriteLine(fruit);
}

Console.WriteLine("***** dictionary *****");
foreach (var item in fruitDictionary)
{
    Console.WriteLine($"{item.Key}: {item.Value}");
}

foreach (var item in fruitDictionary)
{
    Console.WriteLine($"Key from tuple: {item.Key} - value from tuple: {item.Value}");
}

foreach (var key in fruitDictionary.Keys)
{
    Console.WriteLine(key);
}

foreach (var value in fruitDictionary.Values)
{
    Console.WriteLine(value);
}
