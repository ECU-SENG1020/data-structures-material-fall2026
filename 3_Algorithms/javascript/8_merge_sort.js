// 8) Merge sort
// Run: node 8_merge_sort.js

function merge(numbers, i, j, k) {
  const merged = [];
  let leftPos = i;
  let rightPos = j + 1;

  while (leftPos <= j && rightPos <= k) {
    if (numbers[leftPos] <= numbers[rightPos]) {
      merged.push(numbers[leftPos]);
      leftPos += 1;
    } else {
      merged.push(numbers[rightPos]);
      rightPos += 1;
    }
  }

  while (leftPos <= j) {
    merged.push(numbers[leftPos]);
    leftPos += 1;
  }

  while (rightPos <= k) {
    merged.push(numbers[rightPos]);
    rightPos += 1;
  }

  for (let m = 0; m < merged.length; m += 1) {
    numbers[i + m] = merged[m];
  }
}

function mergeSort(numbers, i, k) {
  if (i < k) {
    const j = Math.floor((i + k) / 2);
    mergeSort(numbers, i, j);
    mergeSort(numbers, j + 1, k);
    merge(numbers, i, j, k);
  }
}

function mergeWithCounts(numbers, i, j, k) {
  const merged = [];
  let leftPos = i;
  let rightPos = j + 1;
  let comparisons = 0;
  let copies = 0;

  while (leftPos <= j && rightPos <= k) {
    comparisons += 1;
    if (numbers[leftPos] <= numbers[rightPos]) {
      merged.push(numbers[leftPos]);
      leftPos += 1;
    } else {
      merged.push(numbers[rightPos]);
      rightPos += 1;
    }
    copies += 1;
  }

  while (leftPos <= j) {
    merged.push(numbers[leftPos]);
    leftPos += 1;
    copies += 1;
  }

  while (rightPos <= k) {
    merged.push(numbers[rightPos]);
    rightPos += 1;
    copies += 1;
  }

  for (let m = 0; m < merged.length; m += 1) {
    numbers[i + m] = merged[m];
    copies += 1;
  }

  return { comparisons, copies };
}

function mergeSortWithCounts(numbers) {
  const nums = [...numbers];
  let totalComparisons = 0;
  let totalCopies = 0;

  function inner(a, left, right) {
    if (left < right) {
      const mid = Math.floor((left + right) / 2);
      inner(a, left, mid);
      inner(a, mid + 1, right);
      const { comparisons, copies } = mergeWithCounts(a, left, mid, right);
      totalComparisons += comparisons;
      totalCopies += copies;
    }
  }

  inner(nums, 0, nums.length - 1);
  return { sorted: nums, comparisons: totalComparisons, copies: totalCopies };
}

function main() {
  const numbers = [10, 2, 78, 4, 45, 32, 7, 11];
  console.log('UNSORTED:');
  console.log(numbers.join(' '));

  mergeSort(numbers, 0, numbers.length - 1);

  console.log('SORTED:');
  console.log(numbers.join(' '));

  const demo = mergeSortWithCounts(numbers);
  console.log(`(demo) comparisons=${demo.comparisons}, copies=${demo.copies}`);
}

main();
