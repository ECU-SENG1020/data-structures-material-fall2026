import { DsDictionary } from "./DsDictionaryModule.js";

const myDict2 = new DsDictionary([
  ["a", 1],
  ["b", 2],
]);
console.log(String(myDict2));

const myDict = new DsDictionary();
console.log(Object.getOwnPropertyNames(Object.getPrototypeOf(myDict)));

myDict.set("name", "Alice");
myDict.set("age", 25);

const keysView = myDict.keys();
const valuesView = myDict.values();
const itemsView = myDict.items();

console.log(String(keysView));
console.log(String(valuesView));
console.log(String(itemsView));

myDict.set("city", "New York");

console.log(String(keysView));
console.log(String(valuesView));
console.log(String(itemsView));
