#!/usr/bin/node
/*
 * Star wars Wedge Antilles
 */
const process = require('process');
const args = process.argv[2];

const request = require('request');

const MAIN_URL = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(
  MAIN_URL,
  function (error, response, body) {
    if (error && !args) {
      console.error(error);
    }
    console.log(JSON.parse(body).films.length);
  }
);
