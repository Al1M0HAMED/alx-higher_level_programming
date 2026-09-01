#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((!(Number.isNaN(w)) && w > 0) && (!(Number.isNaN(h)) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
