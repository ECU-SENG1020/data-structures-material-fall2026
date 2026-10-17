using System;

static void MyRecursiveFunction(int numLevels)
{
    if (numLevels == 0)
    {
        Console.WriteLine("Base Case");
        return;
    }

    Console.WriteLine($"Start Level {numLevels}");

    MyRecursiveFunction(numLevels - 1);

    Console.WriteLine($"Level {numLevels} completed");
}

static void Main()
{
    MyRecursiveFunction(3);
}

Main();
