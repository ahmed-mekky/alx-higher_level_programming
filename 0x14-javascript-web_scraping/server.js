#!/usr/bin/node
const http = require('http');
const fs = require('fs');
const parser = require('url');

http.createServer(function (req, res) {
  const pathname = parser.parse(req.url, true).pathname;
  res.writeHead(200, {'Content-Type': 'application/json'});
  if (pathname === '/route_1') {
    fs.readFile('file_1', 'utf8', function (err, contents) {
      res.end(contents);
    });
  } else if (pathname === '/route_2') {
    fs.readFile('file_2', 'utf8', function (err, contents) {
      res.end(contents);
    });
  } else {
    res.end("OK");  
  }
}).listen(5050);
