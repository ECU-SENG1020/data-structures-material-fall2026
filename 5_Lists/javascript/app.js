import DsList from './ListModule.js';


const myList = new DsList();

myList.append(1);
myList.append(2);
myList.append(3);
myList.append(1);
myList.append(2);
myList.append(3);

console.log(myList.length);
console.log(myList.toString());

const customStringList = new DsList();
customStringList.append('a');
customStringList.append('b');
console.log(customStringList.toString());

console.log(myList.getItem(0));

// Example iteration:
for (const item of myList) {
  console.log(item);
}

// Example contains:
console.log(myList.contains(3));