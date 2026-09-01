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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
