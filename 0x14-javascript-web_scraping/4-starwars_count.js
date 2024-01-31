#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  let x = 0
  let dict = JSON.parse(body).results
  Object.keys(dict).forEach(element => {
    dict[element].characters.forEach(character => {
      if ( character == "https://swapi-api.alx-tools.com/api/people/18/" ) {
        x += 1
      }
    });
  });
  console.log(x)
});
