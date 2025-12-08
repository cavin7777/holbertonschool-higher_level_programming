#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(args[0]) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    let square = '';
    for (let j = 0; j < args[0]; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
