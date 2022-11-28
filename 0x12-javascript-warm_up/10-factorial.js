#!/usr/bin/node
/* A script that computes and prints a factorial
 */
const process = require('process');

const args = process.argv;

const num = parseInt(args[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}

function factorial (n) {
  let result = 0;
  if (n === 0) {
    result = 1;
  } else {
    result = n * factorial(n - 1);
  }
  return result;
}
