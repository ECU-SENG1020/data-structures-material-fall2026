/**
 * JavaScript "Tuple" Demonstration (tuple-like patterns)
 *
 * JavaScript does not have a built-in immutable tuple type in plain ES. Arrays
 * are commonly used as tuple-like containers. To emulate immutability, use
 * `Object.freeze()` or prefer language-level tuples in TypeScript. This demo
 * shows tuple-like patterns using arrays and freezing.
 */

// ============================================================================
// 1. CREATING TUPLE-LIKE STRUCTURES
// ============================================================================

// Using an array as a tuple
const point = [10, 20]; // (x, y)
console.log("Point (array as tuple):", point);

// Freezing to emulate immutability
const frozenPoint = Object.freeze([1, 2]);
console.log("Frozen point:", frozenPoint);

// Note: Object.freeze prevents top-level mutation but doesn't deeply freeze
const nested = Object.freeze([ [1, 2], {a: 3} ]);

console.log("\n" + "=".repeat(60) + "\n");

// ============================================================================
// 2. ACCESSING ELEMENTS
// ============================================================================

const colors = ["red", "green", "blue"];
console.log("First:", colors[0]);
console.log("Last (at()):", colors.at(-1));

console.log("\n" + "=".repeat(60) + "\n");

// ============================================================================
// 3. IMMUTABILITY (EMULATION)
// ============================================================================

const t = Object.freeze(["a", "b"]);
try {
    t[0] = "z"; // silently fails in non-strict mode, throws in strict
    console.log("After assign attempt:", t);
} catch (e) {
    console.log("Error assigning to frozen tuple-like:", e.message);
}

// To "modify": create a new array
const newT = [...t.slice(0, 1), "z", ...t.slice(1)];
console.log("New tuple (copy with change):", newT);

console.log("\n" + "=".repeat(60) + "\n");

// ============================================================================
// 4. DESTRUCTURING / PACKING
// ============================================================================

const coords = [3, 4, 5];
const [x, y, z] = coords; // destructuring
console.log("Destructured:", x, y, z);

// Rest element
const [head, ...tail] = [1, 2, 3, 4];
console.log("Head:", head, "Tail:", tail);

console.log("\n" + "=".repeat(60) + "\n");

// ============================================================================
// 5. CONVERSION BETWEEN MUTABLE/IMMUTABLE
// ============================================================================

const list = [1, 2, 3];
const asTuple = Object.freeze([...list]);
console.log("As frozen tuple-like:", asTuple);

const backToList = [...asTuple]; // copy to a mutable list
backToList.push(4);
console.log("Back to list (mutable):", backToList);

console.log("\n" + "=".repeat(60) + "\n");

// ============================================================================
// 6. COMMON OPERATIONS (readonly style)
// ============================================================================

const a = Object.freeze([1, 2]);
const b = Object.freeze([3, 4]);
// Concatenate (returns new array)
const concatenated = [...a, ...b];
console.log("Concatenated:", concatenated);

// Slicing and indexing work as usual
console.log("Slice:", concatenated.slice(1, 3));

// Searching
console.log("Includes 3:", concatenated.includes(3));
console.log("Index of 4:", concatenated.indexOf(4));

console.log("\nTuple-like demo complete (JS).\n");
