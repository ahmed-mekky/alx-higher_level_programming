#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

fs.readFile(argv[2], 'utf8', function (err, data1) {
  if (err) {
    return console.log(err);
  }

  fs.readFile(argv[3], 'utf8', function (err, data2) {
    if (err) {
      return console.log(err);
    }

    const data = data1 + data2;

    fs.writeFile(argv[4], data, 'utf8', function (err) {
      if (err) {
        return console.log(err);
      }
    });
  });
});
