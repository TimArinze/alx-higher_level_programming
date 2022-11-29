#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments
 */
const process = require('process');

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (!isNaN(num)) {
      arr.push(num);
    }
  }
  arr.sort();
  arr.reverse();
  console.log(arr[1]);
}
