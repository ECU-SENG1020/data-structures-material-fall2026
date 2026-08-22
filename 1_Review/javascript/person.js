// Custom module that exports multiple classes

export class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

export class Dog {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log('Wuf');
  }
}

export class Cat {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log('Meow');
  }
}
