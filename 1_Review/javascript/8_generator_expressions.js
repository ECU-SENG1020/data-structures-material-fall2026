// 8) Generators (JS has generator functions)
// Run: node 8_generator_expressions.js

// Generator function using `yield`
function* generatorFunction() {
  yield 'START';
  yield 'PROCESSING';
  yield 'DONE';
}

let genFunc = generatorFunction();

console.log('Print using generator function and next()');
console.log(genFunc.next().value);
console.log(genFunc.next().value);
console.log(genFunc.next().value);
console.log(genFunc.next().value ?? 'No more states');

console.log('\nPrint using generator function in for..of loop');
genFunc = generatorFunction();
for (const state of genFunc) {
  console.log(state);
}

// List of numbers 0 through 9
const numbers = Array.from({ length: 10 }, (_, i) => i);

// Generator "expression" style: create a generator that yields squares
function* squares(items) {
  for (const x of items) {
    yield x ** 2;
  }
}

const genExp = squares(numbers);

console.log('\nPrint using generator and next()');
console.log(genExp.next().value);
console.log(genExp.next().value);
console.log(genExp.next().value);

console.log('\nPrint remaining squares using for..of loop');
for (const item of genExp) {
  console.log(item);
}
