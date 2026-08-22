import { DsDictionary } from "./DsDictionaryModule.js";

const d = new DsDictionary([
  ["name", "Ada"],
  ["role", "Engineer"],
]);

console.log(d.constructor.name);
console.log(String(d));

d.set("language", "Python");
console.log(String(d));

console.log("keys:", [...d.keys()]);
console.log("values:", [...d.values()]);
console.log("items:", [...d.items()]);
