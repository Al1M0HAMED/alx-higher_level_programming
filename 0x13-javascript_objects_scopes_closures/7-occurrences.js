#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = list.length;
  let number = 0;

  while (i) {
    i--;
    if (list[i] === searchElement) {
      number++;
    }
  }
  return (number);
};
