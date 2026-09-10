using System;

var person = new Person("Alice", 30);
person.Greet();

var dog = new Dog("Cinna", 2);
dog.Greet();

var cat = new Cat("Cat1", 100);
cat.Greet();

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
