import { MySetDict } from "./SetByDictionary.js";

const s = new MySetDict(1, 2, 3);
console.log(s.constructor.name);
console.log(String(s));

s.add(4);
console.log(String(s));
