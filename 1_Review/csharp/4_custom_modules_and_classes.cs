using System;

var p1 = new Person("Alice", 30);
p1.Greet();

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

    public override string ToString()
    {
        return $"Person(name={Name}, age={Age})";
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
