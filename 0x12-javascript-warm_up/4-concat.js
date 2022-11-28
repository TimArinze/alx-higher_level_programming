#!/usr/bin/node
/* A script that prints two arguments passed to it, with is in between
 */

const process = require('process');

const args = process.argv;

if (args.length < 2) {
  console.log('undefined ' + 'is undefined');
} else if (args.length === 2) {
  console.log(args[2] + ' is undefined');
} else {
  console.log(args[2] + ' is ' + args[3]);
}
