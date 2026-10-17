using System;
using System.Collections.Generic;

public class Node<T>
{
    public T Data { get; set; }
    public Node<T>? Next { get; set; }

    public Node(T data)
    {
        Data = data;
        Next = null;
    }

    public override string ToString()
    {
        return Data?.ToString() ?? string.Empty;
    }
}

public class DsList<T> : IEnumerable<T>
{
    private Node<T>? head;

    public int Count { get; private set; }

    public void Append(T data)
    {
        if (head is null)
        {
            head = new Node<T>(data);
            Count++;
            return;
        }

        var current = head;
        while (current.Next is not null)
        {
            current = current.Next;
        }

        current.Next = new Node<T>(data);
        Count++;
    }

    public T this[int index]
    {
        get
        {
            if (index < 0 || index >= Count)
            {
                throw new IndexOutOfRangeException();
            }

            var current = head;
            var currentIndex = 0;
            while (current is not null && currentIndex < index)
            {
                current = current.Next;
                currentIndex++;
            }

            return current!.Data;
        }
        set
        {
            if (index < 0 || index >= Count)
            {
                throw new IndexOutOfRangeException();
            }

            var current = head;
            var currentIndex = 0;
            while (current is not null && currentIndex < index)
            {
                current = current.Next;
                currentIndex++;
            }

            current!.Data = value;
        }
    }

    public bool Contains(T value)
    {
        foreach (var item in this)
        {
            if (EqualityComparer<T>.Default.Equals(item, value))
            {
                return true;
            }
        }

        return false;
    }

    public IEnumerator<T> GetEnumerator()
    {
        var current = head;
        while (current is not null)
        {
            yield return current.Data;
            current = current.Next;
        }
    }

    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => GetEnumerator();

    public override string ToString()
    {
        if (head is null)
        {
            return "[]";
        }

        var values = new List<string>();
        var current = head;
        while (current is not null)
        {
            values.Add(current.Data is string s ? $"'{s}'" : current.Data?.ToString() ?? string.Empty);
            current = current.Next;
        }

        return $"[{string.Join(", ", values)}]";
    }
}

var myList = new DsList<int>();
myList.Append(1);
myList.Append(2);
myList.Append(3);
myList.Append(1);
myList.Append(2);
myList.Append(3);

Console.WriteLine(myList.Count);
Console.WriteLine(myList);

var customStringList = new DsList<string>();
customStringList.Append("a");
customStringList.Append("b");
Console.WriteLine(customStringList);

Console.WriteLine(myList[0]);

foreach (var item in myList)
{
    Console.WriteLine(item);
}

Console.WriteLine(myList.Contains(3));
