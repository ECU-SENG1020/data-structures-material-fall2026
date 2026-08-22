import DsTuple from './TupleModule.js';

const myTuple = new DsTuple('a', 'b', 'c');
console.log('myTuple =', String(myTuple));
console.log('length =', myTuple.length);
console.log('item[1] =', myTuple.get(1));
console.log("contains 'b'?", myTuple.contains('b'));

const other = new DsTuple('x', 'y');
console.log('combined =', String(myTuple.add(other)));
console.log("count('b') =", new DsTuple('a', 'b', 'c', 'b').count('b'));
console.log("index('b') =", myTuple.index('b'));
