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
      console.error(error);
    }
    const outcome = JSON.parse(body).results;
    const character_url = 'https://swapi-api.alx-tools.com/api/people/14/';
    const mapped = outcome.map((episode) => episode.characters);
    const joined = mapped.flat(1);
    const filtered = joined.filter((character) => character === character_url);
    console.log(filtered.length);
  }
)
