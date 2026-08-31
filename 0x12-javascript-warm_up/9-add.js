#!/usr/bin/node

function add (a, b) {
  const first = parseInt(a, 10);
  const seccond = parseInt(b, 10);

  if (!(Number.isNaN(first) || (Number.isNaN(seccond)))) {
    const sum = (first + seccond);
    console.log(sum);
  } else {
    console.log('NaN');
  }
}
add(process.argv[2], process.argv[3]);
