#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Not a number');
} else if (isNaN(args[0]) ===false) {
  console.log('My number: ' + args[0]);
} else {
  console.log('Not a number');
}
