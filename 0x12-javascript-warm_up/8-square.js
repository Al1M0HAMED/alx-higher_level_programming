#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

if (!(Number.isNaN(x))) {
  let i = x;
  while (i > 0) {
    let j = x;
    while (j) {
      process.stdout.write('X');
      j--;
    }
    console.log('');
    i--;
  }
} else {
  console.log('Missing size');
}
