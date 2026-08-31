#!/usr/bin/node

const len = process.argv.length;
let biggest = NaN;
let secBig = NaN;

if (!(len <= 3)) {
  let i = len - 1;

  while (i > 1) {
    const n = parseInt(process.argv[i], 10);
    if (n > biggest || Number.isNaN(biggest)) { biggest = n; }
    if ((n > secBig && n < biggest) || (Number.isNaN(secBig) && n != biggest)) { secBig = n; }
    i--;
  }
  console.log(secBig);
} else {
  console.log(0);
}
