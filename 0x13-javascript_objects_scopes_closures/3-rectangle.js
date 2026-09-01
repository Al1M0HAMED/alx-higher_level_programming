#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((!(Number.isNaN(w)) && w > 0) && (!(Number.isNaN(h)) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let height = this.height;
    while (height) {
      let width = this.width;
      while (width) {
        process.stdout.write('X');
        width--;
      }
      console.log('');
      height--;
    }
  }
}
module.exports = Rectangle;
