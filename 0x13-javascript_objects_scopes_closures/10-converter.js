#!/usr/bin/node
exports.converter = function (item) {
  return function (num) {
    return (num.toString(item));
  };
};
