import Node from './NodeModule.js';

// Singly linked list implementation
class DsList {
  constructor() {
    this.head = null;
  }

  formatValue(value) {
    if (typeof value === 'string') {
      return `'${value}'`;
    }
    return String(value);
  }

  // Append data to the end of the list
  append(data) {
    if (this.head === null) {
      this.head = new Node(data);
      return;
    }

    let currentNode = this.head;
    while (currentNode.next) {
      currentNode = currentNode.next;
    }

    currentNode.next = new Node(data);
  }

  // format print output
  toString() {
    if (this.head === null) {
      return '[]';
    }

    let printString = '[';
    let node = this.head;
    printString += this.formatValue(node.data);

    while (node.next) {
      node = node.next;
      printString += `, ${this.formatValue(node.data)}`;
    }

    printString += ']';
    return printString;
  }

  // count of nodes
  get length() {
    let count = 0;
    let node = this.head;

    while (node) {
      count += 1;
      node = node.next;
    }

    return count;
  }

  // retrieve value of specific element
  getItem(index) {
    let node = this.head;
    let count = 0;

    while (node) {
      if (count === index) {
        return node.data;
      }
      node = node.next;
      count += 1;
    }

    return undefined;
  }

  // set data of specific element
  setItem(index, value) {
    let node = this.head;
    let count = 0;

    while (node) {
      if (count === index) {
        node.data = value;
        return;
      }
      node = node.next;
      count += 1;
    }
  }

  // insert element at a specific index
  insert(index, value) {
    let node = this.head;
    let count = 0;

    if (index === 0) {
      this.head = new Node(value);
      this.head.next = node;
      return;
    }

    while (node) {
      if (count === index - 1) {
        const nodeNext = node.next;
        node.next = new Node(value);
        node.next.next = nodeNext;
        return;
      }
      node = node.next;
      count += 1;
    }
  }

  // remove element at a specific index
  remove(index) {
    let node = this.head;
    let count = 0;

    if (node === null) {
      return;
    }

    if (index === 0) {
      if (node.next) {
        this.head = node.next;
        return;
      }
      this.head = null;
      return;
    }

    if (index === this.length - 1) {
      while (node) {
        if (count + 1 === index) {
          node.next = null;
          return;
        }
        node = node.next;
        count += 1;
      }
      return;
    }

    while (node) {
      if (count === index - 1) {
        if (!node.next) {
          return;
        }
        node.next = node.next.next;
        return;
      }
      node = node.next;
      count += 1;
    }
  }

  // provide ability to use DsList in a loop
  *[Symbol.iterator]() {
    let node = this.head;
    while (node) {
      yield node.data;
      node = node.next;
    }
  }

  // provide ability to add two DsLists together
  // dsList3 = dsList1.add(dsList2)
  add(other) {
    const newDsList = new DsList();
    for (const item of this) {
      newDsList.append(item);
    }
    for (const item of other) {
      newDsList.append(item);
    }
    return newDsList;
  }

  // provide ability to check if a value exists in the list
  contains(value) {
    let node = this.head;
    while (node) {
      if (node.data === value) {
        return true;
      }
      node = node.next;
    }

    return false;
  }

  // delete all elements
  clear() {
    this.head = null;
  }
}

export default DsList;
