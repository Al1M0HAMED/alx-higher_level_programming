#!/usr/bin/node

const value = process.argv[2];
const num = parseInt(value, 10);

if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
