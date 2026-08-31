#!/usr/bin/node

const len = process.argv.length;
let biggest = NaN;
let secBig = NaN;

if (!(len <= 3)) {
  let i = len - 1;

  while (i > 1) {
    const n = parseInt(process.argv[i], 10);
    if (Number.isNaN(secBig) || (n > secBig && n !== biggest)) { secBig = n; }
    if (n > biggest || Number.isNaN(biggest)) { secBig = biggest; biggest = n; }
    i--;
  }
  console.log(secBig);
} else {
  console.log(0);
}
