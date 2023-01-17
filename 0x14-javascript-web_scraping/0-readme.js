#!/usr/bin/node
/* A script that reads and prints the content of a file
 */

const process = require('process');
const fs = require('fs');

const args = process.argv[2];

const filename = args;
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
