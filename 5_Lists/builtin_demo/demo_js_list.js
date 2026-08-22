/**
 * JavaScript Array Demonstration
 * A comprehensive guide to JavaScript's built-in Array data structure
 * 
 * In JavaScript, what Python calls "lists" are called "Arrays". 
 * They are ordered collections of values that can hold any type of data, 
 * including numbers, strings, objects, and even other arrays. JavaScript 
 * arrays are dynamic and can grow or shrink in size as needed. They come 
 * with a rich set of built-in methods for manipulation, searching, sorting, 
 * and more.
 */

// ============================================================================
// 1. CREATING ARRAYS
// ============================================================================

// Empty array
const emptyArray = [];
console.log("Empty array:", emptyArray);

// Array with initial values
const fruits = ["apple", "banana", "cherry"];
console.log("Fruits:", fruits);

// Array with numbers
const numbers = [1, 2, 3, 4, 5];
console.log("Numbers:", numbers);

// Mixed types - JavaScript allows different types in the same array
const mixed = [1, "hello", 3.14, true, null, undefined];
console.log("Mixed types:", mixed);

// Creating array with repeated values using Array() and fill()
const zeros = new Array(5).fill(0);  // [0, 0, 0, 0, 0]
console.log("Five zeros:", zeros);

// Using Array.from() to create arrays
const fromString = Array.from("hello");  // Converts string to array
console.log("From string:", fromString);

const range = Array.from({length: 5}, (_, i) => i + 1);  // [1, 2, 3, 4, 5]
console.log("Range 1-5:", range);

// Using spread operator with arrays
const copy = [...fruits];
console.log("Copy of fruits:", copy);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 2. ACCESSING ELEMENTS
// ============================================================================

const colors = ["red", "green", "blue", "yellow", "purple"];

// Access by index - arrays start at index 0
const first = colors[0];      // First element
console.log("First color:", first);

const third = colors[2];      // Third element (index 2)
console.log("Third color:", third);

// Negative indexing is NOT supported in JavaScript (unlike Python)
// Instead, use array.length or at() method

// at() method - supports negative indices (newer JavaScript)
const last = colors.at(-1);      // Last element
console.log("Last color:", last);

const secondLast = colors.at(-2);  // Second from the end
console.log("Second to last:", secondLast);

// Traditional way to get last element
const lastTraditional = colors[colors.length - 1];
console.log("Last (traditional way):", lastTraditional);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 3. MODIFYING ELEMENTS
// ============================================================================

const pets = ["dog", "cat", "bird"];
console.log("Original pets:", pets);

// Change a single element
pets[1] = "hamster";  // Replace "cat" with "hamster"
console.log("After replacing cat:", pets);

// Change multiple elements with splice()
// splice(start, deleteCount, ...items)
pets.splice(0, 2, "fish", "turtle");  // Replace first two elements
console.log("After replacing first two:", pets);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 4. ADDING ELEMENTS
// ============================================================================

const shopping = ["milk", "eggs"];
console.log("Shopping list:", shopping);

// push() - adds ONE or MORE elements to the END
shopping.push("bread");
console.log("After push:", shopping);

// Can push multiple items at once
shopping.push("butter", "cheese");
console.log("After pushing multiple:", shopping);

// unshift() - adds element(s) to the BEGINNING
shopping.unshift("yogurt");
console.log("After unshift:", shopping);

// splice() - adds element at specific position
// splice(index, 0, item) - 0 means don't delete anything
shopping.splice(2, 0, "apples");  // Insert at index 2
console.log("After splice at index 2:", shopping);

// concat() - joins arrays (creates NEW array, doesn't modify original)
const moreItems = ["oranges", "grapes"];
const combined = shopping.concat(moreItems);
console.log("Using concat:", combined);
console.log("Original shopping still:", shopping);

// Spread operator - modern way to combine arrays
const combinedSpread = [...shopping, ...moreItems];
console.log("Using spread:", combinedSpread);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 5. REMOVING ELEMENTS
// ============================================================================

const tasks = ["email", "coding", "meeting", "lunch", "coding", "review"];
console.log("Tasks:", tasks);

// pop() - removes and RETURNS last element
const lastTask = tasks.pop();
console.log("Popped task:", lastTask);
console.log("Tasks after pop():", tasks);

// shift() - removes and returns first element
const firstTask = tasks.shift();
console.log("Shifted task:", firstTask);
console.log("Tasks after shift():", tasks);

// splice() - removes element(s) at specific position
// splice(start, deleteCount)
const removed = tasks.splice(1, 1);  // Remove 1 element at index 1
console.log("Removed with splice:", removed);
console.log("Tasks after splice:", tasks);

// Remove multiple elements
tasks.splice(1, 2);  // Remove 2 elements starting at index 1
console.log("After removing 2 elements:", tasks);

// Setting length to 0 - removes all elements
const toEmpty = [1, 2, 3, 4, 5];
toEmpty.length = 0;
console.log("After setting length to 0:", toEmpty);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 6. SLICING - Getting portions of an array
// ============================================================================

const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
console.log("Days:", days);

// slice(start, end) - end is NOT included
const weekdays = days.slice(0, 5);  // From index 0 to 4
console.log("Weekdays (0, 5):", weekdays);

// Omit end - goes to the end
const weekend = days.slice(5);  // From index 5 to end
console.log("Weekend (5):", weekend);

// Negative indices - count from end
const lastThree = days.slice(-3);  // Last 3 elements
console.log("Last three (-3):", lastThree);

// Slice with negative start and end
const middleSlice = days.slice(2, -2);  // From index 2 to second-to-last
console.log("Middle (2, -2):", middleSlice);

// Copy entire array with slice()
const daysCopy = days.slice();
console.log("Copy of days:", daysCopy);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 7. ITERATING - Looping through arrays
// ============================================================================

const animals = ["dog", "cat", "bird", "fish"];

// for...of loop - iterate over values (modern JavaScript)
console.log("Loop through values with for...of:");
for (const animal of animals) {
    console.log(`  Animal: ${animal}`);
}

// forEach() method - functional approach
console.log("\nUsing forEach():");
animals.forEach((animal, index) => {
    console.log(`  ${index}: ${animal}`);
});

// Traditional for loop with index
console.log("\nTraditional for loop:");
for (let i = 0; i < animals.length; i++) {
    console.log(`  ${i}: ${animals[i]}`);
}

// for...in loop - iterates over indices (not recommended for arrays)
console.log("\nUsing for...in (indices):");
for (const index in animals) {
    console.log(`  ${index}: ${animals[index]}`);
}

// While loop
console.log("\nUsing while loop:");
let i = 0;
while (i < animals.length) {
    console.log(`  Position ${i}: ${animals[i]}`);
    i++;
}

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 8. SEARCHING AND CHECKING
// ============================================================================

const numbersArray = [10, 20, 30, 40, 50, 30];

// includes() - check if value exists (returns true/false)
const has30 = numbersArray.includes(30);
console.log("Is 30 in the array?", has30);

const has100 = numbersArray.includes(100);
console.log("Is 100 in the array?", has100);

// indexOf() - find position of FIRST occurrence (-1 if not found)
const position = numbersArray.indexOf(30);
console.log("First position of 30:", position);

// indexOf() with start position
const positionAfter = numbersArray.indexOf(30, 3);  // Search from index 3
console.log("Position of 30 after index 3:", positionAfter);

// lastIndexOf() - find position of LAST occurrence
const lastPosition = numbersArray.lastIndexOf(30);
console.log("Last position of 30:", lastPosition);

// find() - returns first element that satisfies condition
const found = numbersArray.find(num => num > 25);
console.log("First number > 25:", found);

// findIndex() - returns index of first element that satisfies condition
const foundIndex = numbersArray.findIndex(num => num > 25);
console.log("Index of first number > 25:", foundIndex);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 9. SORTING
// ============================================================================

let unsorted = [64, 34, 25, 12, 22, 11, 90];
console.log("Original:", unsorted);

// sort() - sorts the array IN PLACE (modifies original)
// WARNING: Sorts as strings by default!
unsorted.sort();
console.log("After sort() [WRONG - sorts as strings]:", unsorted);

// Correct way - provide compare function for numbers
unsorted = [64, 34, 25, 12, 22, 11, 90];
unsorted.sort((a, b) => a - b);  // Ascending order
console.log("After sort with compare function:", unsorted);

// Descending order
unsorted.sort((a, b) => b - a);
console.log("After sort descending:", unsorted);

// Sorting strings (default sort works fine)
const words = ["zebra", "apple", "mango", "banana"];
words.sort();
console.log("Sorted words:", words);

// toSorted() - returns NEW sorted array (original unchanged) [newer JS]
const original = [64, 34, 25, 12, 22, 11, 90];
const newSorted = [...original].sort((a, b) => a - b);  // Using spread to copy first
console.log("Original array:", original);
console.log("New sorted array:", newSorted);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 10. REVERSING
// ============================================================================

let letters = ["a", "b", "c", "d", "e"];
console.log("Original:", letters);

// reverse() - reverses IN PLACE (modifies original)
letters.reverse();
console.log("After reverse():", letters);

// toReversed() - returns NEW reversed array (newer JS)
letters = ["a", "b", "c", "d", "e"];
const revArray = [...letters].reverse();  // Using spread to copy first
console.log("Using spread + reverse():", revArray);
console.log("Original unchanged:", letters);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 11. LENGTH AND OTHER INFO
// ============================================================================

const items = [5, 10, 15, 20, 25];

// length property - number of elements
const length = items.length;
console.log("Array:", items);
console.log("Length:", length);

// Math.min() and Math.max() with spread operator
const minimum = Math.min(...items);
const maximum = Math.max(...items);
console.log("Minimum:", minimum);
console.log("Maximum:", maximum);

// reduce() to calculate sum
const total = items.reduce((sum, num) => sum + num, 0);
console.log("Sum:", total);

// Average (mean) - sum divided by length
const average = total / length;
console.log("Average:", average);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 12. COPYING ARRAYS
// ============================================================================

let originalArray = [1, 2, 3];

// WRONG way - just creates another reference to same array
const notACopy = originalArray;
notACopy.push(4);
console.log("Original:", originalArray);  // Both changed!
console.log("'Copy':", notACopy);

// RIGHT way 1 - using slice()
originalArray = [1, 2, 3];
const realCopy = originalArray.slice();
realCopy.push(4);
console.log("\nOriginal:", originalArray);  // Original unchanged
console.log("Real copy:", realCopy);

// RIGHT way 2 - using spread operator
originalArray = [1, 2, 3];
const spreadCopy = [...originalArray];
spreadCopy.push(4);
console.log("\nOriginal:", originalArray);
console.log("Spread copy:", spreadCopy);

// RIGHT way 3 - using Array.from()
originalArray = [1, 2, 3];
const fromCopy = Array.from(originalArray);
fromCopy.push(4);
console.log("\nOriginal:", originalArray);
console.log("Array.from copy:", fromCopy);

// Note: These are SHALLOW copies - nested arrays/objects are still referenced
const nested = [[1, 2], [3, 4]];
const shallowCopy = [...nested];
shallowCopy[0].push(99);  // This modifies BOTH!
console.log("\nOriginal nested:", nested);
console.log("Shallow copy:", shallowCopy);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 13. MAP, FILTER, REDUCE - Functional Programming Methods
// ============================================================================

// map() - transforms each element (creates new array)
const mapNumbers = [1, 2, 3, 4, 5];
const squares = mapNumbers.map(x => x ** 2);
console.log("Original:", mapNumbers);
console.log("Squares with map():", squares);

// map() with index
const indexed = mapNumbers.map((x, i) => `${i}: ${x}`);
console.log("With index:", indexed);

// filter() - keeps elements that match condition
const filterNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evens = filterNumbers.filter(x => x % 2 === 0);
console.log("\nFiltered evens:", evens);

// reduce() - reduces array to single value
const reduceNumbers = [1, 2, 3, 4, 5];
const sum = reduceNumbers.reduce((accumulator, current) => accumulator + current, 0);
console.log("\nSum with reduce():", sum);

// reduce() to find max
const max = reduceNumbers.reduce((max, current) => current > max ? current : max);
console.log("Max with reduce():", max);

// Chaining methods
const result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    .filter(x => x % 2 === 0)      // Get evens: [2, 4, 6, 8, 10]
    .map(x => x ** 2)               // Square them: [4, 16, 36, 64, 100]
    .reduce((sum, x) => sum + x);   // Sum them: 220
console.log("\nChained filter->map->reduce:", result);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 14. OTHER USEFUL METHODS
// ============================================================================

// every() - checks if ALL elements satisfy condition
const allNumbers = [2, 4, 6, 8, 10];
const allEven = allNumbers.every(x => x % 2 === 0);
console.log("Are all even?", allEven);

// some() - checks if ANY element satisfies condition
const someNumbers = [1, 2, 3, 4, 5];
const hasEven = someNumbers.some(x => x % 2 === 0);
console.log("Has any even?", hasEven);

// fill() - fills all or some elements with a value
const fillArray = [1, 2, 3, 4, 5];
fillArray.fill(0);  // Fill all with 0
console.log("After fill(0):", fillArray);

const fillArray2 = [1, 2, 3, 4, 5];
fillArray2.fill(0, 2, 4);  // Fill indices 2-3 with 0
console.log("After fill(0, 2, 4):", fillArray2);

// flat() - flattens nested arrays
const nestedFlat = [1, [2, 3], [4, [5, 6]]];
const flattened1 = nestedFlat.flat();  // One level
console.log("\nFlat one level:", flattened1);

const flattened2 = nestedFlat.flat(2);  // Two levels
console.log("Flat two levels:", flattened2);

// flatMap() - map then flatten
const flatMapArray = [1, 2, 3];
const flatMapped = flatMapArray.flatMap(x => [x, x * 2]);
console.log("\nFlatMap result:", flatMapped);

// join() - converts array to string
const joinArray = ["Hello", "World", "JavaScript"];
const joined = joinArray.join(" ");  // Join with space
console.log("\nJoined:", joined);

const csv = joinArray.join(", ");  // Join with comma
console.log("CSV format:", csv);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 15. ARRAY DESTRUCTURING - Modern JavaScript Feature
// ============================================================================

// Basic destructuring
const [firstFruit, secondFruit, thirdFruit] = ["apple", "banana", "cherry"];
console.log("First:", firstFruit);
console.log("Second:", secondFruit);
console.log("Third:", thirdFruit);

// Skip elements
const [first2, , third2] = [1, 2, 3, 4, 5];
console.log("First and third:", first2, third2);

// Rest operator
const [head, ...tail] = [1, 2, 3, 4, 5];
console.log("Head:", head);
console.log("Tail:", tail);

// Default values
const [a, b, c = 99] = [1, 2];
console.log("With default:", a, b, c);

// Swapping variables
let x = 1, y = 2;
[x, y] = [y, x];
console.log("After swap: x =", x, "y =", y);

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 16. MULTIDIMENSIONAL ARRAYS
// ============================================================================

// 2D array (array of arrays)
const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log("Matrix:");
matrix.forEach(row => console.log(row));

// Access element
const element = matrix[1][2];  // Row 1, Column 2 = 6
console.log("\nElement at [1][2]:", element);

// Modify element
matrix[0][0] = 99;
console.log("\nAfter changing [0][0] to 99:");
matrix.forEach(row => console.log(row));

// Iterate through 2D array
console.log("\nIterating through matrix:");
for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[row].length; col++) {
        console.log(`  [${row}][${col}] = ${matrix[row][col]}`);
    }
}

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 17. CHECKING IF ARRAY IS EMPTY
// ============================================================================

const emptyCheck = [];
const fullCheck = [1, 2, 3];

// Check length
if (emptyCheck.length === 0) {
    console.log("Array is empty");
}

if (fullCheck.length > 0) {
    console.log("Array has items");
}

// Using Boolean conversion (falsy length)
if (!emptyCheck.length) {
    console.log("Empty array has falsy length");
}

console.log("\n" + "=".repeat(70) + "\n");

// ============================================================================
// 18. ARRAY.isArray() - Check if something is an array
// ============================================================================

console.log("Is [1,2,3] an array?", Array.isArray([1, 2, 3]));
console.log("Is 'hello' an array?", Array.isArray("hello"));
console.log("Is {a:1} an array?", Array.isArray({a: 1}));
console.log("Is null an array?", Array.isArray(null));

console.log("\n" + "=".repeat(70) + "\n");

console.log("🎉 Array demonstration complete!");
console.log("JavaScript arrays are flexible and packed with powerful methods!");
