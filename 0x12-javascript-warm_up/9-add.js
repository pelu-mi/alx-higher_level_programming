#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const num1 = process.argv[2] / 1;
const num2 = process.argv[3] / 1;
if (!num1 || !num2) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
