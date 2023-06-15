#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) process.stdout.write('X');
      console.log('');
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  charPrint (c) {
    const cha = c || 'X';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) process.stdout.write(cha);
      console.log('');
    }
  }
};
