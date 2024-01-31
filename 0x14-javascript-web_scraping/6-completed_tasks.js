#!/usr/bin/node
const request = require('request');

request.get('https://jsonplaceholder.typicode.com/todos', (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  let content = JSON.parse(body)
  let list = {}
  let count = 0
  let id = content[0].userId
  content.forEach(element => {
    if ( element.userId != id) {
      list[id] = count
      id = element.userId
      count = 0
    }
    if( element.completed === true ) {
      count += 1
    }
  });
  console.log(list)
});
