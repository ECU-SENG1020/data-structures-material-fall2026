// 3) Binary search
// Run: node 3_binary_search.js

function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);

    if (arr[mid] === target) {
      return mid;
    }

    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return -1;
}

function binarySearchUsingRecursion(numbers, low, high, key) {
  if (low > high) {
    return -1;
  }

  const mid = Math.floor((low + high) / 2);

  if (numbers[mid] < key) {
    return binarySearchUsingRecursion(numbers, mid + 1, high, key);
  }

  if (numbers[mid] > key) {
    return binarySearchUsingRecursion(numbers, low, mid - 1, key);
  }

  return mid;
}

function main() {
  const numbers = [1, 3, 4, 7, 9, 11, 15];
  const target = 9;

  const result = binarySearch(numbers, target);

  if (result !== -1) {
    console.log(`Element ${target} found at index ${result}`);
  } else {
    console.log(`Element ${target} not found in the list`);
  }

  console.log('***********');
  console.log(binarySearchUsingRecursion(numbers, 0, numbers.length - 1, 9));
}

main();
