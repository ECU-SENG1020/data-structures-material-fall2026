// 5) Importing a custom module
// Run: node 5_importing_custom_module.js

import { Person, Dog, Cat } from './person.js';

const p0 = new Person('Alice', 30);
p0.greet();

const d1 = new Dog('Cinna', 2);
d1.greet();

const d2 = new Dog('Joey', 13);
d2.greet();

const c1 = new Cat('Cat1', 100);
c1.greet();
