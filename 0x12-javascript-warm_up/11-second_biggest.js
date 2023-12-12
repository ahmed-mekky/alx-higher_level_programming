#!/usr/bin/node
const argv = process.argv;

if (argv.length < 4) {
  console.log(0);
}
let sec; let first = argv[2];
for (let i = 3; i < argv.length; i++) {
  if (argv[i] > first) {
    sec = first;
    first = argv[i];
  }
}
console.log(sec);
