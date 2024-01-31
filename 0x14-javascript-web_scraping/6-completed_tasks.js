#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const content = JSON.parse(body);
  const list = {};
  let count = 0;
  let id = content[0].userId;
  content.forEach(element => {
    if (element.userId !== id) {
      list[id] = count;
      id = element.userId;
      count = 0;
    }
    if (element.completed === true) {
      count += 1;
    }
  });
  list[id] = count;
  console.log(list);
});
