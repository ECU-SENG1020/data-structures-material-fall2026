import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import DsList from './ListModule.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const failures = [];
let successCount = 0;

function assert(condition, message) {
  if (!condition) {
    throw new Error(message || 'Assertion failed');
  }
}

function testAppend() {
  const dsList = new DsList();
  dsList.append('a');
  dsList.append('b');
  dsList.append('c');
  assert(dsList.length === 3, 'Expected length 3 after append');
}

function testGetItem() {
  const dsList = new DsList();
  dsList.append('a');
  dsList.append('b');
  dsList.append('c');
  assert(dsList.getItem(1) === 'b', 'Expected index 1 to be b');
}

function testSetItem() {
  const dsList = new DsList();
  dsList.append('a');
  dsList.append('b');
  dsList.append('c');
  dsList.setItem(1, 'd');
  assert(dsList.getItem(1) === 'd', 'Expected index 1 to be updated to d');
}

function testIter() {
  const dsList = new DsList();
  dsList.append('a');
  dsList.append('b');

  let count = 0;
  for (const _item of dsList) {
    count += 1;
  }

  assert(count === 2, 'Expected iteration to visit 2 items');
}

function testAdd() {
  const dsList1 = new DsList();
  dsList1.append('e');
  dsList1.append('b');

  const dsList2 = new DsList();
  dsList2.append('f');
  dsList2.append('f');

  const newDsList = dsList1.add(dsList2);
  assert(newDsList.toString() === "['e', 'b', 'f', 'f']", 'Expected concatenated list output');
}

function testInTrue() {
  const dsList = new DsList();
  dsList.append('e');
  dsList.append('b');
  dsList.append('f');
  dsList.append('f');

  const result = dsList.contains('b');
  assert(result === true, 'Expected contains to return true');
}

function testInFalse() {
  const dsList = new DsList();
  dsList.append('e');
  dsList.append('b');
  dsList.append('f');
  dsList.append('f');

  const result = dsList.contains('z');
  assert(dsList.length === 4 && result === false, 'Expected contains to return false');
}

function testClear() {
  const dsList = new DsList();
  dsList.append('e');
  dsList.append('b');
  dsList.append('f');
  dsList.append('f');

  dsList.clear();
  assert(dsList.length === 0, 'Expected length 0 after clear');
}

function checkFileForArrayUsage() {
  const filename = 'ListModule.js';
  const filepath = path.join(__dirname, filename);
  const content = fs.readFileSync(filepath, 'utf8');

  // Heuristic checks that avoid false positives for [Symbol.iterator]
  const bannedPatterns = [
    /\bnew\s+Array\b/, // new Array(...)
    /\bArray\.from\b/, // Array.from(...)
    /\bArray\s*\(/, // Array(...)
    /\.push\s*\(/,
    /\.pop\s*\(/,
    /\.shift\s*\(/,
    /\.unshift\s*\(/,
    /\.splice\s*\(/,
  ];

  for (const pattern of bannedPatterns) {
    if (pattern.test(content)) {
      return true;
    }
  }

  return false;
}

function testBuiltinListUsed() {
  const result = checkFileForArrayUsage();
  assert(result === false, 'Detected Array usage in ListModule.js');
}

function runTest(name, fn) {
  try {
    fn();
    successCount += 1;
  } catch (e) {
    failures.push([name, e && e.message ? e.message : String(e)]);
  }
}

function main() {
  runTest('testAppend', testAppend);
  runTest('testGetItem', testGetItem);
  runTest('testSetItem', testSetItem);
  runTest('testIter', testIter);
  runTest('testAdd', testAdd);
  runTest('testInTrue', testInTrue);
  runTest('testInFalse', testInFalse);
  runTest('testClear', testClear);
  runTest('testBuiltinListUsed', testBuiltinListUsed);

  console.log('');

  if (failures.length) {
    for (const [testName, message] of failures) {
      console.log(`ERROR: ${testName} -> ${message}`);
    }
    console.log(`\n${failures.length} tests failed`);
    console.log(`\n${successCount} tests passed`);
    console.log('');
    process.exitCode = 1;
    return;
  }

  console.log(`All ${successCount} tests passed`);
  console.log('');
}

main();
