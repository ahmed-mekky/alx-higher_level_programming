#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0; i < list / 2; i++) {
    let temp = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = temp;
  }
}