#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const data_A;
const data_B;

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(dataA);
  data_A = dataA;
});
fs.readFile(fileB, 'utf8', (err, dataB) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(dataB);
  data_B = dataB;
});

fs.writeFile(fileC, data_A, err => {
  if (err) {
    console.error(err);
  }
});

fs.appendFile(fileC, data_B, err => {
  if (err) {
    console.error(err);
  }
});
