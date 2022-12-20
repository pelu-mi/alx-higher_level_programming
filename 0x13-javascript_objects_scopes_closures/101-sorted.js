#!/usr/bin/node
const dict = require('./101-data.js').dict;

const keys = Object.keys(dict);
const values = Object.values(dict);
const result = {};

for (const v of values) {
  const arr = [];
  for (const k of keys) {
    if (dict[k] === v) {
      arr.push(k);
    }
  }
  result[v] = arr;
}

console.log(result);
