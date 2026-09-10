using System;
using System.Collections.Generic;
using System.Linq;

static IEnumerable<string> GeneratorFunction()
{
    yield return "START";
    yield return "PROCESSING";
    yield return "DONE";
}

var genFunc = GeneratorFunction();

Console.WriteLine("Print using generator function and next()");
Console.WriteLine(genFunc.First());
Console.WriteLine(genFunc.Skip(1).First());
Console.WriteLine(genFunc.Skip(2).First());
Console.WriteLine(genFunc.Skip(3).FirstOrDefault() ?? "No more states");

var nextGenFunc = GeneratorFunction();
foreach (var state in nextGenFunc)
{
    Console.WriteLine(state);
}

var numbers = Enumerable.Range(0, 10).ToList();
var genExp = numbers.Select(x => x * x);

Console.WriteLine("Print using generator expression and next()");
Console.WriteLine(genExp.First());
Console.WriteLine(genExp.Skip(1).First());
Console.WriteLine(genExp.Skip(2).First());
Console.WriteLine(genExp.Skip(3).First());
Console.WriteLine(genExp.Skip(4).First());
Console.WriteLine(genExp.Skip(5).First());
Console.WriteLine(genExp.Skip(6).First());
Console.WriteLine(genExp.Skip(7).First());
Console.WriteLine(genExp.Skip(8).First());
Console.WriteLine(genExp.Skip(9).First());

Console.WriteLine("Print using generator expression in for loop");
foreach (var item in numbers.Select(x => x * x))
{
    Console.WriteLine(item);
}
