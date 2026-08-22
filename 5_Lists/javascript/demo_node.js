import Node from './NodeModule.js';

const node = new Node('a');

node.next = new Node('b');
node.next.next = new Node('c');

let currentNode = node;
let count = 0;
while (currentNode) {
  console.log(currentNode.data);
  count += 1;
  currentNode = currentNode.next;
}

console.log(count);
