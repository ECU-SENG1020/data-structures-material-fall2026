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