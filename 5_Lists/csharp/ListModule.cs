using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

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
            var node = GetNodeAt(index);
            return node.Data;
        }
        set
        {
            var node = GetNodeAt(index);
            node.Data = value;
        }
    }

    public void Insert(int index, T value)
    {
        if (index < 0 || index > Count)
        {
            throw new ArgumentOutOfRangeException(nameof(index));
        }

        if (index == 0)
        {
            var newHead = new Node<T>(value)
            {
                Next = head
            };
            head = newHead;
            Count++;
            return;
        }

        var previous = GetNodeAt(index - 1);
        var next = previous.Next;
        previous.Next = new Node<T>(value)
        {
            Next = next
        };
        Count++;
    }

    public void RemoveAt(int index)
    {
        if (index < 0 || index >= Count)
        {
            throw new ArgumentOutOfRangeException(nameof(index));
        }

        if (index == 0)
        {
            head = head?.Next;
            Count--;
            return;
        }

        var previous = GetNodeAt(index - 1);
        previous.Next = previous.Next?.Next;
        Count--;
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

    public void Clear()
    {
        head = null;
        Count = 0;
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

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();

    public static DsList<T> operator +(DsList<T> left, DsList<T> right)
    {
        var combined = new DsList<T>();

        foreach (var item in left)
        {
            combined.Append(item);
        }

        foreach (var item in right)
        {
            combined.Append(item);
        }

        return combined;
    }

    public override string ToString()
    {
        if (head is null)
        {
            return "[]";
        }

        var builder = new StringBuilder();
        builder.Append('[');

        var current = head;
        while (current is not null)
        {
            var value = current.Data is string s ? $"'{s}'" : current.Data?.ToString() ?? string.Empty;
            builder.Append(value);

            if (current.Next is not null)
            {
                builder.Append(", ");
            }

            current = current.Next;
        }

        builder.Append(']');
        return builder.ToString();
    }

    private Node<T> GetNodeAt(int index)
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

        return current!;
    }
}

