#!/usr/bin/node

const num = parseInt(process.argv[2]) ? parseInt(process.argv[2]) : 0;

function fact (num) {
  if (num <= 0) return 1;
  return (num * fact(num - 1));
}

console.log(fact(num));
