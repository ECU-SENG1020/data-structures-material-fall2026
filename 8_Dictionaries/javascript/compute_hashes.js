import crypto from "node:crypto";
import fs from "node:fs";

const FILES = ["test.js"];

function sha256FileNoWhitespace(path) {
  const text = fs.readFileSync(path, "utf-8");
  const normalized = text.replace(/\s+/g, "");
  return crypto.createHash("sha256").update(normalized, "utf-8").digest("hex");
}

function buildHashes() {
  const out = {};
  for (const fname of FILES) {
    if (fs.existsSync(fname)) out[fname] = sha256FileNoWhitespace(fname);
    else out[fname] = null;
  }
  return out;
}

function writeHashes(path = "file_hashes.json") {
  fs.writeFileSync(path, JSON.stringify(buildHashes(), null, 2));
}

if (import.meta.url === `file://${process.argv[1].replace(/\\/g, "/")}`) {
  writeHashes();
  console.log("Wrote file_hashes.json");
}
