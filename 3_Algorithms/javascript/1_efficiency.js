// 1) Efficiency (compare two algorithms)
// Run: node 1_efficiency.js

function getEvenNumbersVersionOne({ fromNum = 2, toNum = 1000 } = {}) {
  let number = fromNum;
  const evenNumbers = [];

  while (number <= toNum) {
    if (number % 2 === 0) {
      evenNumbers.push(number);
    }
    number += 1;
  }

  return evenNumbers;
}

function getEvenNumbersVersionTwo({ fromNum = 2, toNum = 1000 } = {}) {
  let number = fromNum;
  const evenNumbers = [];

  while (number <= toNum) {
    if (number % 2 === 0) {
      evenNumbers.push(number);
    }
    number += 2;
  }

  return evenNumbers;
}

const result1 = getEvenNumbersVersionOne({ fromNum: 2, toNum: 100000 });
 console.log(result1);

const result2 = getEvenNumbersVersionTwo({ fromNum: 2, toNum: 100000 });
// console.log(result2);

let startTime = process.hrtime.bigint();
getEvenNumbersVersionOne();
let elapsed = process.hrtime.bigint() - startTime;
console.log(`Algorithm 1 took ${elapsed} nanoseconds.`);

startTime = process.hrtime.bigint();
getEvenNumbersVersionTwo();
elapsed = process.hrtime.bigint() - startTime;
console.log(`Algorithm 2 took ${elapsed} nanoseconds.`);
