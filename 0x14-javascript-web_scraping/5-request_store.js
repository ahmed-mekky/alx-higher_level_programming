#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const { encode } = require('punycode');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(process.argv[3], body, encode, (err) => {
    if (err) {
      throw err;
    }
  });
  
});
