#!/usr/bin/node
/* A script that prints My number: <1st arg converted to int>
 */
const process = require('process');

const args = process.argv;

const num = parseInt(args[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
