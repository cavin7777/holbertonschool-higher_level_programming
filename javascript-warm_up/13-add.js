#!/usr/bin/node

function add(a, b) {
  return a + b;
}

// Make the function visible outside
exports.add = add;
