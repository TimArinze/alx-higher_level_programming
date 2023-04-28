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
      .filter(task => task.completed === true);
    const reduced = users.reduce((accumulator, user) => {
      if (user.userId in accumulator) {
        accumulator[user.userId] += 1;
      } else {
        accumulator[user.userId] = 1;
      }
      return accumulator;
    }, {});
    console.log(reduced);
  }
);
