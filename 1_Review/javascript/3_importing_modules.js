// 3) Importing modules
// Run: node 3_importing_modules.js

import { randomInt } from 'node:crypto';

const items = ['A', 'B', 'C', 'D', 'E'];

function choice(array) {
  return array[randomInt(0, array.length)];
}

function shuffleInPlace(array) {
  // Fisher-Yates shuffle
  for (let i = array.length - 1; i > 0; i -= 1) {
    const j = randomInt(0, i + 1);
    [array[i], array[j]] = [array[j], array[i]];
  }
}

console.log('***available choices to choose from***');
console.log(items);
console.log('***first random choice***');
console.log(choice(items));
console.log('***second random choice***');
console.log(choice(items));
console.log('');

const items2 = ['A', 'B', 'C', 'D', 'E'];
console.log('***before shuffle***');
console.log(items2);
shuffleInPlace(items2);
console.log('***after shuffle***');
console.log(items2);
console.log('');

// Importing specific things isn't always needed in JS (Math is global)
console.log(`2 to the power of 2 is: ${2 ** 2}`);
