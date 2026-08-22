import fs from 'node:fs';
import crypto from 'node:crypto';
import DsTuple from './TupleModule.js';

const failures = [];
let successCount = 0;

function ok() {
  successCount += 1;
}

function testCreate() {
  try {
    const t = new DsTuple('a', 'b', 'c');
    if (t.length !== 3) throw new Error('length mismatch');
    ok();
  } catch (e) {
    failures.push(['testCreate', String(e)]);
  }
}

function testGetItem() {
  try {
    const t = new DsTuple('a', 'b', 'c');
    if (t.get(1) !== 'b') throw new Error('getitem mismatch');
    ok();
  } catch (e) {
    failures.push(['testGetItem', String(e)]);
  }
}

function testIter() {
  try {
    const t = new DsTuple('a', 'b', 'c');
    let c = 0;
    for (const _ of t) c += 1;
    if (c !== 3) throw new Error('iter count mismatch');
    ok();
  } catch (e) {
    failures.push(['testIter', String(e)]);
  }
}

function testAdd() {
  try {
    const t1 = new DsTuple('a', 'b', 'c');
    const t2 = new DsTuple('e', 'f', 'g');
    const t3 = t1.add(t2);
    const normalized = String(t3).replace(/\s+/g, '');
    if (normalized !== '(a,b,c,e,f,g)') throw new Error('add mismatch');
    ok();
  } catch (e) {
    failures.push(['testAdd', String(e)]);
  }
}

function testInTrue() {
  try {
    const t = new DsTuple('a', 'b', 'c');
    const result = t.contains('b');
    if (!(t.length === 3 && result === true)) throw new Error('contains true mismatch');
    ok();
  } catch (e) {
    failures.push(['testInTrue', String(e)]);
  }
}

function testInFalse() {
  try {
    const t = new DsTuple('a', 'b', 'c');
    const result = t.contains('z');
    if (result !== false) throw new Error('contains false mismatch');
    if (!(t.length === 3 && result === false)) throw new Error('contains false mismatch');
    ok();
  } catch (e) {
    failures.push(['testInFalse', String(e)]);
  }
}

function testIndex() {
  try {
    const t = new DsTuple('a', 'b', 'c');
    if (t.index('b') !== 1) throw new Error('index mismatch');
    ok();
  } catch (e) {
    failures.push(['testIndex', String(e)]);
  }
}

function testCount() {
  try {
    const t = new DsTuple('a', 'b', 'c', 'b');
    if (t.count('b') !== 2) throw new Error('count mismatch');
    ok();
  } catch (e) {
    failures.push(['testCount', String(e)]);
  }
}

function sha256Normalized(path) {
  const text = fs.readFileSync(path, 'utf8');
  const normalized = text.replace(/\s+/g, '');
  return crypto.createHash('sha256').update(normalized, 'utf8').digest('hex');
}

function testFileHashes() {
  try {
    if (!fs.existsSync('file_hashes.json')) {
      throw new Error('file_hashes.json not found');
    }
    const expected = JSON.parse(fs.readFileSync('file_hashes.json', 'utf8'));
    for (const [fname, expHash] of Object.entries(expected)) {
      if (!fs.existsSync(fname)) throw new Error(`Expected file ${fname} is missing`);
      const actual = sha256Normalized(fname);
      if (expHash !== actual) throw new Error(`Hash mismatch for ${fname}`);
    }
    ok();
  } catch (e) {
    failures.push(['testFileHashes', String(e)]);
  }
}

function main() {
  testCreate();
  testGetItem();
  testIter();
  testAdd();
  testInTrue();
  testInFalse();
  testIndex();
  testCount();
  testFileHashes();

  console.log('');
  if (failures.length) {
    for (const [name, msg] of failures) {
      console.log(`ERROR: ${name} -> ${msg}`);
    }
    console.log(`\n${failures.length} tests failed`);
    console.log(`\n${successCount} tests passed`);
    console.log('');
    process.exit(1);
  }

  console.log(`All ${successCount} tests passed`);
  console.log('');
}

main();
