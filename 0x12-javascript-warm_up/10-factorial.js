#!/usr/bin/node
const argv = process.argv;
console.log(fact(argv[2]));

function fact (x) {
  if (x === 0 || x === 1 || !x) return 1;
  else return x * fact(x - 1);
}
