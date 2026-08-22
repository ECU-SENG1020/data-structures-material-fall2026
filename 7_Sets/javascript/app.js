import { MySet } from "./SetDataStructure.js";
import { MyHashedSet } from "./HashedSetDataStructure.js";

const mySetA = new MySet();
const mySetB = new MySet();

for (const x of [1, 2, 3, 4, 5]) mySetA.add(x);
for (const x of [4, 5, 6, 7, 8]) mySetB.add(x);

console.log(`Union: A | B = ${mySetA.union(mySetB)}`);
console.log(`Union: B | A = ${mySetB.union(mySetA)}`);
console.log(`Intersection: A & B = ${mySetA.intersection(mySetB)}`);
console.log(`Intersection: B & A = ${mySetB.intersection(mySetA)}`);
console.log(`Difference: A - B = ${mySetA.difference(mySetB)}`);
console.log(`Difference: B - A = ${mySetB.difference(mySetA)}`);

console.log("");

const hs = new MyHashedSet();
console.log(`Hashed set initially: ${hs}`);
hs.add("Hello");
hs.add("World");
console.log(`Hashed set after add: ${hs}`);
console.log(`contains('Hello')? ${hs.contains("Hello")}`);
