using System;

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

