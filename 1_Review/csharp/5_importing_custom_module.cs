using System;

// In a multi-file project, this example would use a shared model file such as person.cs.
// This repository uses the single-file convention, so the shared model stays in this script.
var p0 = new Person("Alice", 30);
p0.Greet();

var d1 = new Dog("Cinna", 2);
d1.Greet();

var d2 = new Dog("Joey", 13);
d2.Greet();

var c1 = new Cat("Cat1", 100);
c1.Greet();

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
}

public class Dog
{
    public string Name { get; }
    public int Age { get; }

    public Dog(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public void Greet()
    {
        Console.WriteLine("Wuf");
    }
}

public class Cat
{
    public string Name { get; }
    public int Age { get; }

    public Cat(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public void Greet()
    {
        Console.WriteLine("Meow");
    }
}
