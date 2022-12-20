#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h = this.height;
    while (h > 0) {
      let w = this.width;
      let output = '';
      while (w > 0) {
        output = output + 'X';
        w--;
      }
      console.log(output);
      h--;
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
