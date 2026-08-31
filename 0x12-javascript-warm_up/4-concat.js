#!/usr/bin/node

let first = null;
let third = null;
const seccond = 'is';

if (process.argv[2] === undefined) {
  first = 'undefined';
} else {
  first = process.argv[2];
}

if (process.argv[3] === undefined) {
  third = 'undefined';
} else {
  third = process.argv[3];
}

console.log(first, seccond, third);
