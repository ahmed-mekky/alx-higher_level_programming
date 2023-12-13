#!/usr/bin/node
const list = require('./100-data').list;

function x (num, idx) {
  return num * idx;
}
console.log(list);
console.log(list.map(x));
