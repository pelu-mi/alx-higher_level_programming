#!/usr/bin/node
const list = require('./100-data.js').list;

let i = -1;
const func = function (x) {
  i++;
  return x * i;
};

const indexList = list.map(func);

console.log(list);
console.log(indexList);
