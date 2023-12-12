#!/usr/bin/node
const argv = process.argv;

if (!Number.isInteger(argv[2])) {
  console.log('Missing size');
}

let x = '';
for (let i = 0; i < argv[2]; i++) {
  for (let j = 0; j < argv[2]; j++) {
    x += 'X';
  }
  console.log(x);
  x = '';
}
