#!/usr/bin/node
exports.converter = function (base) {
  const convert = function (num) {
    return num.toString(base);
  };
  return convert;
};
