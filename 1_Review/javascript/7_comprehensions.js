// 7) Comprehensions (JS uses map/filter instead of Python comprehensions)
// Run: node 7_comprehensions.js

// Numbers 0 through 9
const numbers = Array.from({ length: 10 }, (_, i) => i);
console.log('List of numbers:');
console.log(numbers);

const evenNumbers = numbers.filter((x) => x % 2 === 0);
console.log('Even numbers:');
console.log(evenNumbers);

const oddNumbers = numbers.filter((x) => x % 2 !== 0);
console.log('Odd numbers:');
console.log(oddNumbers);

const squaredNumbers = numbers.map((x) => x ** 2);
console.log('Squared numbers:');
console.log(squaredNumbers);

function doubleNum(num) {
  return num * 2;
}

const numbersList = numbers.map(doubleNum);
console.log(numbersList);

const numbersSet = new Set(numbers);
console.log('Set of numbers:');
console.log(numbersSet);

// "Dictionary" of squared numbers (object)
const dictionarySquaredNumbers = Object.fromEntries(numbers.map((x) => [String(x), x ** 2]));
console.log('Dictionary of squared numbers:');
console.log(dictionarySquaredNumbers);
