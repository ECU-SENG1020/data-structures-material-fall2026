# 0, 1, 1, 2, 3, 5, 8, 13, ...

# Recursive example
def fib1(n):
    
    if n <= 1:
        return n
    
    return fib1(n-1) + fib1(n-2)


# Memoization example
def fib2(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib2(n-1, memo) + fib2(n-2, memo)
    # print(memo)
    return memo[n]


# Dynamic example
def fib3(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
        # print(dp)
    return dp[n]




print(fib1(6))
print(fib2(6))
print(fib3(6))