// 6) "Dunder" equivalents in JavaScript: special methods + introspection
// Run: node 6_special_methods_and_introspection.js

// JavaScript does NOT have Python-style dunder methods.
// But it *does* have special method names and Symbols that customize behavior.

class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  // Similar idea to Python __str__ / __repr__
  toString() {
    return `Person(name=${this.name}, age=${this.age})`;
  }

  // Used when JS tries to turn the object into a number.
  valueOf() {
    return this.age;
  }

  // More control over how it becomes a string/number.
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return this.age;
    return this.toString();
  }
}

const p1 = new Person('Alice', 35);
const p2 = new Person('Bob', 30);

console.log(String(p1));
console.log(String(p2));

// JS has no operator overloading (you cannot redefine + for your class).
// But comparisons like >= will use numeric conversion if you provide valueOf/toPrimitive.
console.log('Alice is older than Bob:', p1 >= p2);

console.log('\nIntrospection:');
console.log('typeof p1:', typeof p1);
console.log('p1 instanceof Person:', p1 instanceof Person);
console.log('Object keys:', Object.keys(p1));
console.log('All property names:', Object.getOwnPropertyNames(p1));

console.log('\nPrototype methods:');
console.log(Object.getOwnPropertyNames(Person.prototype));
