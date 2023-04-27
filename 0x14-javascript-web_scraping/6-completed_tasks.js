#!/usr/bin/node
/*
 * How many completed
 */
const process = require('process');
const args = process.argv[2];

const request = require('request');


request.get(
  args,
  function (error, response, body) {
    if (error) {
    console.error(error);
    }
    const outcome = JSON.parse(body);
    const users = outcome
      .filter(complete => complete.completed == true);
    
    console.log(users);
  }
);
