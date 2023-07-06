#!/usr/bin/node
let num = process.argv.slice(2);
num = num.map((x) => parseInt(x));
num = num.sort((a, b) => b - a);
if (num <= 1) {
  console.log('0');
} else {
  console.log(num[1]);
}
