// Printing to the console.
Console.WriteLine("It's me");

// Custom methods must be declared before they are called.
static void Greet()
{
    Console.WriteLine("Hello, World!");
    Console.WriteLine("Hello again");
}

static void Greet2()
{
    Console.Write("Hello, World!: ");
}

static int Add(int number1, int number2)
{
    return number1 + number2;
}

// A method does not execute until it is called.
Greet();
Greet();

Greet2();
Greet2();
Console.WriteLine();

// Prints 3 to the console.
Console.WriteLine(Add(1, 2));

// A void method has no return value.
Greet();

var items = new List<int> { 1, 2, 3 };
var items2 = items.Concat(items).ToList();
Console.WriteLine(string.Join(", ", items2));

var items3 = items.Select(item => item * 2).ToList();
Console.WriteLine(string.Join(", ", items3));

var items4 = items.Select(item => item * 2);
// The following line will print the type of items4, not its individual elements
Console.WriteLine(items4);

var items5 = items4.ToList();
Console.WriteLine(string.Join(", ", items5));