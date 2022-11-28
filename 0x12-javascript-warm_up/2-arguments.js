#!/usr/bin/node
/* A script that prints a message depending on the number of arguments passed
 */
// Importing the process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

if (args.length < 3) {
  console.log('No Argument');
} else if (args.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
