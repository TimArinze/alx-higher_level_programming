#!/usr/bin/node
/*
 * A script that writes a string to a file
 */
const process = require('process');
const filename = process.argv[2];
const string = process.argv[3];
const fs = require('fs');
fs.writeFile(
  filename,
  string,
  function (err) {
    if (err) {
      return console.error(err);
    }
  }
);
