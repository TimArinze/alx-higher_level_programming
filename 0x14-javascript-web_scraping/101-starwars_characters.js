#!/usr/bin/node
/*
 * with movie id gets the list of character
 */
const process = require('process');
const argv = process.argv[2];

const request = require('request');

const movieId = argv;
const MAIN_URL = 'https://swapi-api.alx-tools.com/api/';

request.get(
  MAIN_URL + 'films/' + movieId,
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const results = JSON.parse(body).characters;
    results.forEach(people => {
      request.get(people,
        function (error, response, body) {
          if (!error) {
            console.log(JSON.parse(body).name);
          }
        });
    });
  }
);
