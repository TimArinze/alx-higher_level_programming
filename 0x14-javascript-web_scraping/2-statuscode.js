#!/usr/bin/node
/*
 * status code
 */
const process = require('process');
const args = process.argv[2];
const request = require('request');

request.get(
	args, function (error, response, body) {
		res = response.statusCode;
		console.log("code: " + res);
	}
);
