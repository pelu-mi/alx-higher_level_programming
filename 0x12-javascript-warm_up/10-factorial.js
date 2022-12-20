#!/usr/bin/node
function factorial (a) {
  return a <= 1 ? 1 : a * factorial(a - 1);
}

const num = process.argv[2] / 1;
isNaN(num) ? console.log('1') : console.log(factorial(num));
