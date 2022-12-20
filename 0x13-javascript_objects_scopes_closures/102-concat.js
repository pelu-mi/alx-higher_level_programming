#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(fileC, dataA, err => {
    if (err) {
      console.error(err);
    }
  });
});

fs.readFile(fileB, 'utf8', (err, dataB) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.appendFile(fileC, dataB, err => {
    if (err) {
      console.error(err);
    }
  });
});
