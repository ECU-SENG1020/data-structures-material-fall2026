import crypto from 'node:crypto';
import fs from 'node:fs';

const FILES = ['test.js'];

function sha256Normalized(path) {
  const text = fs.readFileSync(path, 'utf8');
  const normalized = text.replace(/\s+/g, '');
  return crypto.createHash('sha256').update(normalized, 'utf8').digest('hex');
}

function buildHashes() {
  const out = {};
  for (const fname of FILES) {
    out[fname] = fs.existsSync(fname) ? sha256Normalized(fname) : null;
  }
  return out;
}

function writeHashes(path = 'file_hashes.json') {
  fs.writeFileSync(path, JSON.stringify(buildHashes(), null, 2));
}

if (import.meta.url === new URL(`file://${process.argv[1]}`).href) {
  writeHashes();
  console.log('Wrote file_hashes.json');
}
