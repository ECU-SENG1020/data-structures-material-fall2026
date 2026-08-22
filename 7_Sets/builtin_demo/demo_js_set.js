// JavaScript Set Demonstration
// Simple examples showing common Set operations in JS

// 1. Creating sets
const empty = new Set();
console.log('Empty set:', empty);

const nums = new Set([1,2,2,3]);
console.log('Nums (duplicates removed):', nums);

// 2. Adding and deleting
nums.add(4);
console.log('After add(4):', nums);
nums.delete(2);
console.log('After delete(2):', nums);

// 3. Membership and size
console.log('Has 3?', nums.has(3));
console.log('Size:', nums.size);

// 4. Iteration
for (const v of nums) {
  console.log('  ', v);
}

// 5. Convert between Array and Set (remove duplicates)
const withDups = [1,2,2,3,3,4];
const unique = [...new Set(withDups)];
console.log('Unique array via Set:', unique);

// 6. Union / Intersection / Difference (helpers)
function union(a,b){ return new Set([...a, ...b]); }
function intersection(a,b){ return new Set([...a].filter(x => b.has(x))); }
function difference(a,b){ return new Set([...a].filter(x => !b.has(x))); }

const a = new Set([1,2,3]);
const b = new Set([3,4,5]);
console.log('Union:', union(a,b));
console.log('Intersection:', intersection(a,b));
console.log('Difference (A\B):', difference(a,b));

// 7. WeakSet note: holds only objects and is not iterable
console.log('JS Set demo complete');
