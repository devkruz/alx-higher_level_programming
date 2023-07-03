#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const size = process.argv[2];
  for (let i = 0; i < size; i++) {
    for (let i = 0; i < size; i++) process.stdout.write('X');
    console.log('');
  }
} else {
  console.log('Missing size');
}
