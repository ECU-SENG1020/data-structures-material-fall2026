# Problem solving strategies: Fibonacci examples
# Run: julia problem_solving_strategies.jl

# 0, 1, 1, 2, 3, 5, 8, 13, ...

# Recursive example
function fib1(n::Int)
    if n <= 1
        return n
    end
    return fib1(n - 1) + fib1(n - 2)
end

# Memoization example
function fib2(n::Int, memo::Dict{Int,Int}=Dict{Int,Int}())
    if haskey(memo, n)
        return memo[n]
    end
    if n <= 1
        return n
    end
    memo[n] = fib2(n - 1, memo) + fib2(n - 2, memo)
    return memo[n]
end

# Dynamic programming example
function fib3(n::Int)
    if n <= 1
        return n
    end

    dp = [0, 1]
    for i in 2:n
        push!(dp, dp[i] + dp[i - 1])
    end

    return dp[n + 1]  # dp is 1-based, so fib(n) stored at dp[n+1]
end

println(fib1(6))
println(fib2(6))
println(fib3(6))
