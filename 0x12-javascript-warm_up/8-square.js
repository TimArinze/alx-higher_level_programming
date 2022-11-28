#!/usr/bin/node
/* A script that prints a square
 */
const process = require('process');

const args = process.argv;

const num = parseInt(args[2]);

const string = 'X';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log(string.repeat(num));
  }
}
