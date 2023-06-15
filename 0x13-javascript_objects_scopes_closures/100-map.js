#!/usr/bin/node
const data = require('./100-data.js').list;
function mapped (item) {
  const newItem =
  item.map(function (num, index) {
    return num * index;
  });

  console.log(item);
  console.log(newItem);
}

mapped(data);
