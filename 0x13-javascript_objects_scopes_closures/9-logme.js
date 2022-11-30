#!/usr/bin/node
/* function that prints the number of arguments already printed and the new argument value
 */

let callCount = -1;
exports.logMe = function (item) {
	callCount += 1;
	console.log(callCount + ': ' + item);
}
