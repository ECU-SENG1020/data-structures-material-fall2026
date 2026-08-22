# Big-O Study Guide

This guide explains Big-O notation with clear examples, code walkthroughs, and simple drawn charts to visualize growth rates.

**Contents**
- What is Big-O?
- Common complexity classes
- Visual charts (ASCII)
- Code examples and walkthroughs
- Recap and quick reference

---

## What is Big-O?

Big-O notation describes how the runtime (or memory) of an algorithm grows as the input size $n$ increases. It gives an upper bound on growth, ignoring constant factors and lower-order terms.

- Formal: $f(n) = O(g(n))$ means there exist constants $C > 0$ and $n_0$ such that for all $n \ge n_0$, $f(n) \le C\cdot g(n)$.

Key idea: focus on the fastest-growing term.

## Common Complexity Classes

- O(1) — constant time (e.g., array access)
- O(log n) — logarithmic (e.g., binary search)
- O(n) — linear (e.g., single pass through array)
- O(n log n) — linearithmic (e.g., efficient sorts: merge sort, heapsort)
- O(n^2) — quadratic (e.g., simple nested loops, selection sort)
- O(2^n), O(n!) — exponential / factorial (e.g., brute-force combinatorics)

## Visual Charts (Mermaid XY-style)

Below are Mermaid flowcharts used as XY-style line charts. The horizontal axis (left→right) is input size `n` at sample points [1,2,4,8,16,32,64]. Each node shows `n` and the approximate operation count `y`. Nodes are connected to indicate the line trend.

### O(1)

```mermaid
xychart
    title "Big O of O(1)"
    x-axis [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y-axis "f(n)"
    line  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

```

### O(log n) (base 2)

Values: log2(1)=0, log2(2)=1, log2(4)=2, log2(8)=3, log2(16)=4, log2(32)=5, log2(64)=6

```mermaid
xychart
    title "Big O of O(logn)"
    x-axis [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y-axis "f(n)"
    line  [0, 1, 1.585, 2, 2.322, 2.585, 2.807, 3, 3.170, 3.322]
```

### O(n)

Values equal to n at the sample points.

```mermaid
xychart
    title "Big O of O(n)"
    x-axis [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y-axis "f(n)"
    line  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

### O(n log n)

```mermaid
xychart
    title "Big O of O(nlogn)"
    x-axis [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y-axis "f(n)"
    line  [0, 2, 4.755, 8, 11.609, 15.510, 19.649, 24.00, 28.530, 33.220]
```

### O(n^2)

Values: 1, 4, 16, 64, 256, 1024, 4096

```mermaid
xychart
    title "Big O of O(n)"
    x-axis [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y-axis "f(n)"
    line  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

These charts use node labels to show `x=n` and `y=` operation counts; connecting edges indicate the trend across sample points. For precise plotted charts (true XY axes) I can generate PNGs from measured runtime data and include them in the guide.

---

## Code Examples and Walkthroughs

We'll walk through a few canonical algorithms and count operations to reason about Big-O.

### 1) Linear Search — O(n)

JavaScript:

```javascript
function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) return i; // constant-time check
  }
  return -1;
}
```

Walkthrough:
- Loop runs up to `n = arr.length` times.
- Each iteration does O(1) work (compare, maybe return).
- Worst-case: target not present -> loop executes n times -> O(n).
- Best-case: target at index 0 -> O(1).

Practical note: average-case (random target) is O(n) as well (roughly n/2 checks).

### 2) Binary Search — O(log n)

JavaScript (iterative):

```javascript
function binarySearch(arr, target) {
  let lo = 0, hi = arr.length - 1;
  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}
```

Why O(log n): each loop iteration halves the search range. Starting from n, after k iterations range ≈ n / 2^k. Stop when range ≤ 1 -> k ≈ log2 n.

Edge cases: requires sorted input.

### 3) Selection Sort — O(n^2)

JavaScript:

```javascript
function selectionSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let minIdx = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx]) minIdx = j;
    }
    [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
  }
  return arr;
}
```

Walkthrough:
- Outer loop runs ≈ n times.
- Inner loop runs ≈ n, n-1, n-2, ... → total comparisons ≈ n(n-1)/2 = O(n^2).

### 4) Merge Sort — O(n log n)

JavaScript (recursive):

```javascript
function merge(left, right) {
  const res = [];
  let i = 0, j = 0;
  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) res.push(left[i++]);
    else res.push(right[j++]);
  }
  return res.concat(left.slice(i)).concat(right.slice(j));
}

function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));
  return merge(left, right);
}
```

Analysis:
- Recurrence: T(n) = 2T(n/2) + O(n) (the merge step is linear)
- By Master Theorem, T(n) = O(n log n).

### 5) Counting Operations Example (walk-through)

Take a simple loop:

```javascript
let sum = 0;
for (let i = 0; i < n; i++) {
  sum += i; // O(1)
}
```

Operation count ≈ n additions -> O(n).

If nested:

```javascript
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    // O(1) body
  }
}
```

Total ≈ n * n = n^2 -> O(n^2).

---

## Big-O Tips and Common Pitfalls

- Drop constants: O(2n) -> O(n).
- Drop lower-order terms: O(n + n^2) -> O(n^2).
- Distinguish worst/average/best-case where relevant.
- Remember space complexity: count extra memory allocation.

## Quick Reference Table

```
Operation           Typical Example           Time
O(1)                Array access              Constant
O(log n)            Binary search             Very slow growth
O(n)                Linear scan               Proportional to n
O(n log n)          Efficient sorts           n log n
O(n^2)              Double nested loops       Quadratic explosion
O(2^n)              Brute-force subsets       Exponential (avoid for n>30)
```

---

## Where to go next

- Try timing these algorithms for increasing `n` and plot results in a spreadsheet or quick Python script.
- Convert the examples to the language you use most; measure actual runtime vs theoretical growth.

---

File placed at: 3_Algorithms/big-o/big-o-study-guide.md

If you want, I can also add PNG charts generated from actual runtime data or include runnable timing scripts.
