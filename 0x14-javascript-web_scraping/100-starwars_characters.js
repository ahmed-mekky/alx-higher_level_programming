#!/usr/bin/node
const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, res, body) => {
  const dict = JSON.parse(body);
    dict['characters'].forEach(character => {
      request.get(character, (err, res, body) => {
        console.log(JSON.parse(body).name)
      });
    });
});
