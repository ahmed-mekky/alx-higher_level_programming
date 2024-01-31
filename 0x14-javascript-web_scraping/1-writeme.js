#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], 'utf-8', process.argv[3], (err)=>{
  if( err ) {
      throw err;
  }
});
