// 6) Selection sort
// Run: node 6_selection_sort.js

function selectionSort(numbers) {
  // Sorts the array in place.
  for (let i = 0; i < numbers.length - 1; i += 1) {
    let indexSmallest = i;

    for (let j = i + 1; j < numbers.length; j += 1) {
      if (numbers[j] < numbers[indexSmallest]) {
        indexSmallest = j;
      }
    }

    [numbers[i], numbers[indexSmallest]] = [numbers[indexSmallest], numbers[i]];
  }
}

function selectionSortWithCounts(numbers) {
  let comparisons = 0;
  let swaps = 0;
  const nums = [...numbers];

  for (let i = 0; i < nums.length - 1; i += 1) {
    let indexSmallest = i;

    for (let j = i + 1; j < nums.length; j += 1) {
      comparisons += 1;
      if (nums[j] < nums[indexSmallest]) {
        indexSmallest = j;
      }
    }

    [nums[i], nums[indexSmallest]] = [nums[indexSmallest], nums[i]];
    swaps += 1;
  }

  return { sorted: nums, comparisons, swaps };
}

function main() {
  const numbers = [10, 2, 78, 4, 45, 32, 7, 11];
  const numbers2 = [10, 2, 78, 4, 45, 32, 7, 11];

  console.log('UNSORTED:');
  console.log(numbers);
  console.log('');

  selectionSort(numbers);

  const demo = selectionSortWithCounts(numbers2);
  console.log(`(demo) comparisons=${demo.comparisons}, swaps=${demo.swaps}`);

  console.log('SORTED:');
  console.log(numbers);
}

main();
