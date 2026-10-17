
#load "Models/Cat.csx"
#load "Models/Dog.csx"
#load "Models/Person.csx"

var p1 = new Person("Alice", 30);
p1.Greet();

var d1 = new Dog("Cinna", 2);
d1.Greet();

var d2 = new Dog("Joey", 13);
d2.Greet();

var c1 = new Cat("Cat1", 100);
c1.Greet();


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
