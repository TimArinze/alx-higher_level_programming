#!/usr/bin/node
/*
 * Star wars Wedge Antilles
 */
const process = require('process');
const args = process.argv[2];

const request = require('request');

const MAIN_URL = args;
const CHARACTER_URL = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request.get(
  MAIN_URL,
  function (error, response, body) {
    if (error) {
      console.error(error);
    }
    const outcome = JSON.parse(body).results;
    for (let a = 0; a < outcome.length; a++) {
      for (const [key, value] of Object.entries(outcome[a])) {
        if (key === 'characters') {
          for (let b = 0; b < value.length; b++) {
            if (value[b] === CHARACTER_URL) {
              count += 1;
            }
          }
        }
      }
    }
    console.log(count);
  }
);
