#!/usr/bin/node
const num = process.argv[2] / 1;
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(num));
}
