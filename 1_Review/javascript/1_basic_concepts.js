// 1) Basic JavaScript concepts (Node.js)
// Run: node 1_basic_concepts.js

console.log("It's me");

function greet() {
  console.log('Hello, World!');
  console.log('Hello again');
  // No return statement => returns undefined
}

function add(num1, num2) {
  return num1 + num2;
}

greet();

console.log(add(1, 2));

// Prints undefined because greet() returns undefined
console.log(greet());

const items = [1, 2, 3];

// In Python you can do: items * 2 (repeat the list)
// In JS, you can repeat/duplicate arrays like this:
const repeated = [...items, ...items];
console.log(repeated);

// Or multiply each value by 2:
const multiplied = items.map((x) => x * 2);
console.log(multiplied);
