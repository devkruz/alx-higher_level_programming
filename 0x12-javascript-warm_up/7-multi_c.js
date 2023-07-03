#!/usr/bin/node
let index = 0;

if (process.argv[2] === undefined) console.log('Missing number of occurrences');

while (index < process.argv[2]) {
  console.log('C is fun');
  index++;
}
