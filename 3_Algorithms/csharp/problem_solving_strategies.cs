using System;

static int Fib1(int n)
{
    if (n <= 1)
    {
        return n;
    }

    return Fib1(n - 1) + Fib1(n - 2);
}

static int Fib2(int n, Dictionary<int, int>? memo = null)
{
    memo ??= new Dictionary<int, int>();

    if (memo.ContainsKey(n))
    {
        return memo[n];
    }

    if (n <= 1)
    {
        return n;
    }

    memo[n] = Fib2(n - 1, memo) + Fib2(n - 2, memo);
    return memo[n];
}

static int Fib3(int n)
{
    var dp = new int[n + 1];
    dp[0] = 0;
    if (n >= 1)
    {
        dp[1] = 1;
    }

    for (var i = 2; i <= n; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

Console.WriteLine(Fib1(6));
Console.WriteLine(Fib2(6));
Console.WriteLine(Fib3(6));
