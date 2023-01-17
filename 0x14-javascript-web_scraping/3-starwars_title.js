#!/usr/bin/node
/*
 * Star wars movie title
 */
const process = require('process');
const args = process.argv[2];

const request = require('request');

const main_url = "https://swapi-api.alx-tools.com/api/films/"
request.get(
	main_url + args,
	function (error, response, body) {
		if (error) {
			return console.error(error);
		}
		console.log(body["title"]);
	};
);
