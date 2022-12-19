#!/usr/bin/node
let num = process.argv[2] / 1;
if (!(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
