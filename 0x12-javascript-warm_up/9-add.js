#!/usr/bin/node
/* A script that prints the addition of 2 integers
 */
const process = require('process');

const args = process.argv;

console.log(add(parseInt(args[2]), parseInt(args[3])));

function add (a, b) {
  // addition function
  return a + b;
}
