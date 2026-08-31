#!/usr/bin/node

let x = parseInt(process.argv[2], 10);

if (!(Number.isNaN(x))) {
  while (x) {
    console.log('C is fun');
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
