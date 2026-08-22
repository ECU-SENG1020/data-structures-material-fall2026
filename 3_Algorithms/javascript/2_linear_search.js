// 2) Linear search
// Run: node 2_linear_search.js

function linearSearch(arr, target) {
  for (let index = 0; index < arr.length; index += 1) {
    if (arr[index] === target) {
      return index; // Target found
    }
  }
  return -1; // Target not found
}

function main() {
  const numbers = [4, 2, 7, 1, 9, 3];
  const target = 9;

  const result = linearSearch(numbers, target);

  if (result !== -1) {
    console.log(`Element ${target} found at index ${result}`);
  } else {
    console.log(`Element ${target} not found in the list`);
  }
}

main();
