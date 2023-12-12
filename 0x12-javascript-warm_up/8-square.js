#!/usr/bin/node
const argv = process.argv;

if (typeof(argv[2]) != Number) {
  console.log('Missing size')
}

for (let i = 0; i < argv[2]; i++) {
  for (let j = 0; j < argv[2]; j++) {
    process.stdout.write('X');
  }
  console.log();
}
