// 7) Insertion sort
// Run: node 7_insertion_sort.js

function insertionSort(numbers) {
  // Sorts the array in place.
  for (let i = 0; i < numbers.length; i += 1) {
    let j = i;

    while (j > 0 && numbers[j] < numbers[j - 1]) {
      [numbers[j], numbers[j - 1]] = [numbers[j - 1], numbers[j]];
      j -= 1;
    }
  }
}

function insertionSortWithCounts(numbers) {
  let comparisons = 0;
  let shifts = 0;
  const nums = [...numbers];

  for (let i = 0; i < nums.length; i += 1) {
    let j = i;

    while (j > 0) {
      comparisons += 1;
      if (nums[j] < nums[j - 1]) {
        [nums[j], nums[j - 1]] = [nums[j - 1], nums[j]];
        shifts += 1;
        j -= 1;
      } else {
        break;
      }
    }
  }

  return { sorted: nums, comparisons, shifts };
}

function main() {
  const numbers = [10, 2, 78, 4, 45, 32, 7, 11];

  console.log('UNSORTED:');
  console.log(numbers);
  console.log('');

  insertionSort(numbers);

  console.log('SORTED:');
  console.log(numbers);
  console.log('');

  const demo = insertionSortWithCounts([10, 2, 78, 4, 45, 32, 7, 11]);
  console.log(`(demo) comparisons=${demo.comparisons}, shifts=${demo.shifts}`);
}

main();
