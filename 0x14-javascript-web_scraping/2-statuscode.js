#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log('code:', res.statusCode);
});
