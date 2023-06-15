#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occured = 0;
  list.forEach(element => {
    if (element === searchElement) occured++;
  });

  return occured;
};
