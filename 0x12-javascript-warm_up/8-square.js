#!/usr/bin/node
const size = process.argv[2] / 1;
let num = size;
if (!(num)) {
  console.log('Missing size');
} else {
  while (num > 0) {
    let count = size;
    let output = '';
    while (count > 0) {
      output = output + 'X';
      count--;
    }
    console.log(output);
    num--;
  }
}
