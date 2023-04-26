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
		console.log(outcome);
		for (let a = 0; a < outcome.length; a++) {
			for (const [key, value] of Object.entries(outcome[a])) {
				if (key === "completed" && "completed" === true) {
					console.log(key + ": " + value);
				}
			}
		}
	}
);
