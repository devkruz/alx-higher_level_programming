#!/usr/bin/node
const data = require('./101-data.js').dict;
function feq (item) {
  const sortFeq = {};
  for (const keyOn in item) {
    const setOn = [];
    for (const [key, feq] of Object.entries(item)) {
      if (item[keyOn] === feq) setOn.unshift(key);
    }
    sortFeq[item[keyOn]] = setOn;
  }

  console.log(sortFeq);
}

feq(data);
