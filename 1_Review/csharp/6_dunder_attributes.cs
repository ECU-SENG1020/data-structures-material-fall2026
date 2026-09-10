using System;

var p1 = new Person("Alice", 35);
Console.WriteLine(p1);

var p2 = new Person("Bob", 30);
Console.WriteLine(p2);

Console.WriteLine($"Alice is older than Bob: {p1 >= p2}");

var p3 = p1 + p2;
Console.WriteLine(p3);

var p4 = p2 + p1;
Console.WriteLine(p4);

var p5 = p1 + p2;
Console.WriteLine(p5);

public class Person
{
    public string Name { get; }
    public int Age { get; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public void Greet()
    {
        Console.WriteLine($"Hello, my name is {Name} and I am {Age} years old.");
    }

    public override string ToString()
    {
        return $"Person(name={Name}, age={Age})";
    }

    public static bool operator >=(Person left, Person right)
    {
        return left is not null && right is not null && left.Age >= right.Age;
    }

    public static bool operator <=(Person left, Person right)
    {
        return left is not null && right is not null && left.Age <= right.Age;
    }

    public static Person operator +(Person left, Person right)
    {
        var sex = new Random().Next(2) == 0 ? "boy" : "girl";
        return new Person($"Baby {sex}", 0);
    }
}
