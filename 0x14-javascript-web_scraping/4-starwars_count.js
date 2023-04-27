#!/usr/bin/node
/*
 * Star wars Wedge Antilles
 */
const process = require('process');
const args = process.argv[2];

const request = require('request');

const MAIN_URL = args;
let count = 0;

request.get(
  MAIN_URL,
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const results = JSON.parse(body).results;
    const num_c = results.reduce((num, movie) => {
      return movie.characters.find(character => character.endsWith("18/"))
      ? num + 1 : num;}, 0);
    console.log(num_c);
  }
);
