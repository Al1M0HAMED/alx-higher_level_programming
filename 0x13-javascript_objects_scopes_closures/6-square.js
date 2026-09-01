#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!(c === undefined)) {
      let height = this.height;
      while (height) {
        let width = this.width;
        while (width) {
          process.stdout.write('C');
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
