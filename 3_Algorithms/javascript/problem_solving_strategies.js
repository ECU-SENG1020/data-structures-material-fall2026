// Problem solving strategies: Fibonacci examples
// Run: node problem_solving_strategies.js

// 0, 1, 1, 2, 3, 5, 8, 13, ...

// Recursive example
function fib1(n) {
  if (n <= 1) {
    return n;
  }
  return fib1(n - 1) + fib1(n - 2);
}

// Memoization example
function fib2(n, memo = {}) {
  if (memo[n] !== undefined) {
    return memo[n];
  }
  if (n <= 1) {
    return n;
  }
  memo[n] = fib2(n - 1, memo) + fib2(n - 2, memo);
  return memo[n];
}

// Dynamic programming example
function fib3(n) {
  const dp = [0, 1];
  for (let i = 2; i <= n; i += 1) {
    dp.push(dp[i - 1] + dp[i - 2]);
  }
  return dp[n];
}

console.log(fib1(6));
console.log(fib2(6));
console.log(fib3(6));
