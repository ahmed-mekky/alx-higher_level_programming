#!/usr/bin/node
const argv = process.argv;

if (argv.length < 4) {
  console.log(0);
}

const x = [];
for (let i = 2; i < argv.length; i++) {
  x[i - 2] = argv[i];
}

const min = Math.min(...x);
const max = Math.max(...x);

let y = min;
for (let i = 2; i < argv.length; i++) {
  if (argv[i] > y && Number.parseInt(argv[i]) !== max) {
    y = argv[i];
  }
}
console.log(y);
