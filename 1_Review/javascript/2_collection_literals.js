// 2) Collection literals
// Run: node 2_collection_literals.js

// Array (like a Python list)
const fruitArray = ['apple', 'banana', 'cherry'];

// Object (key/value pairs, like a dictionary)
const fruitObject = { a: 'apple', b: 'banana' };

// Map (also key/value pairs, but supports any key type)
const fruitMap = new Map([
  ['a', 'apple'],
  ['b', 'banana'],
]);

// Set (unique values)
const fruitSet = new Set(['apple', 'banana', 'cherry', 'cherry']);

console.log('***** Array *****');
for (const fruit of fruitArray) {
  console.log(fruit);
}

console.log('***** Set *****');
for (const fruit of fruitSet) {
  console.log(fruit);
}

console.log('***** Object *****');
for (const [key, value] of Object.entries(fruitObject)) {
  console.log(key, value);
}

console.log('***** Map *****');
for (const [key, value] of fruitMap) {
  console.log(key, value);
}

console.log('Keys (Object):');
for (const key of Object.keys(fruitObject)) {
  console.log(key);
}

console.log('Values (Object):');
for (const value of Object.values(fruitObject)) {
  console.log(value);
}
