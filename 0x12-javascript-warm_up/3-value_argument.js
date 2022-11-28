#!/usr/bin/node
/* A script that prints the first argument passed to it
 */
// importing the process module
const process = require('process');

const args = process.argv;

if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
