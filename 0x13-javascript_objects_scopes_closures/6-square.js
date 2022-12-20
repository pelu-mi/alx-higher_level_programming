#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let h = this.height;
    while (h > 0) {
      let w = this.width;
      let output = '';
      while (w > 0) {
        output = output + c;
        w--;
      }
      console.log(output);
      h--;
    }
  }
}

module.exports = Square;
