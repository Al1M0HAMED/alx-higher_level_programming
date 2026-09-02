#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length;
  let j = 0;

  while (i > j) {
    i--;
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j++;
  }
  return (list);
};
