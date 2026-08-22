// 4) Custom classes (defined in this file)
// Run: node 4_custom_modules_and_classes.js

// Classes are usually abstractions of real-world objects and processes.
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  // Instance methods use `this`
  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

const p1 = new Person('Alice', 30);
p1.greet();

const p2 = new Person('Bob', 25);
p2.greet();
