#!/usr/bin/node

exports.converter = function (base) {
  function conver (n) {
    return (n.toString(base));
  }

  return (conver);
};
