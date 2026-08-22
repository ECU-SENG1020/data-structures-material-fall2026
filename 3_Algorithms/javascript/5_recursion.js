// 5) Recursion
// Run: node 5_recursion.js

// Many problems can be solved by using divide-and-conquer techniques.

function myRecursiveFunction(numLevels) {
  if (numLevels === 0) {
    console.log('Base Case');
    return;
  }

  console.log(`Start Level ${numLevels}`);

  myRecursiveFunction(numLevels - 1);

  console.log(`Level ${numLevels} completed`);
}

function main() {
  myRecursiveFunction(3);
}

main();
