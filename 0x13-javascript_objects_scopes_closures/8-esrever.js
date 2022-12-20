#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  let len = list.length - 1;
  let i = 0;
  while (len >= 0) {
    rev[i] = list[len];
    i++;
    len--;
  }
  return rev;
};
