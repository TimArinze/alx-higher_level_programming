#!/usr/bin/node
/*
 * status code
 */
const process = require('process');
const args = process.argv[2];
const request = require('request');

request.get(
  args,
  function (error, response, body) {
    if (error) {
      return console.error(error);
    }
    console.log('code: ' + response.statusCode);
  }
);
