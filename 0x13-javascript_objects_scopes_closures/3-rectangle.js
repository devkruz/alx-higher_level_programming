#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) process.stdout.write('X');
      console.log('');
    }
  }
};
