#!/usr/bin/node
/*
 * Star wars movie title
 */
const process = require('process');
const MAIN_URL = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request.get(
	MAIN_URL,
	function (error, response, body) {
		if (error) {
			console.error(error);
		}
		fs.writeFile(
			filename,
			body,
			function (err) {
				if (err) {
					return console.error(err);
				}
			}
		);
	}
);
