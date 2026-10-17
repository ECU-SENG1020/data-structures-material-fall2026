using System;

var node = new Node<string>("a");
Console.WriteLine(node.Data);
Console.WriteLine(node);

var node2 = new Node<string>("b");
Console.WriteLine(node2);

var third = new Node<string>("c");
Console.WriteLine(third);

node.Next = node2;
Console.WriteLine(node.Next);

Console.WriteLine(node.Next?.Next);
node.Next!.Next = third;
Console.WriteLine(node.Next!.Next!.Data);

var current = node;
var count = 0;
while (current is not null)
{
    Console.WriteLine(current.Data);
    count++;
    current = current.Next;
}

Console.WriteLine($"Count: {count}");
