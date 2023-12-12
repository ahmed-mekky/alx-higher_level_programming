#!/usr/bin/node
const argv = process.argv;

if (argv.length < 4) {
  console.log(0);
} else {
  const x = [];
  for (let i = 2; i < argv.length; i++) {
    x[i - 2] = Number.parseInt(argv[i]);
  }

  const min = Math.min(...x);
  const max = Math.max(...x);

  let y = min;
  for (let i = 0; i < x.length; i++) {
    if (x[i] > y && x[i] !== max) {
      y = x[i];
    }
  }
  console.log(y);
}
