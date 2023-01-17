#!/usr/bin/node
/*
 * Star wars movie title
 */
const process = require('process');
const args = process.argv[2];

const request = require('request');

const MAIN_URL = 'https://swapi-api.alx-tools.com/api/films/';

request.get(
  MAIN_URL + args,
  function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).title);
  }
);
