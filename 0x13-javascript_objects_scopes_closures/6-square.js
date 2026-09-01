#!/usr/bin/node

const SquareA = require('./5-square');

class Square extends SquareA {
  charPrint (c) {
    if (!(c === undefined)) {
      let height = this.height;
      while (height) {
        let width = this.width;
        while (width) {
          process.stdout.write(c);
          width--;
        }
        console.log('');
        height--;
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
