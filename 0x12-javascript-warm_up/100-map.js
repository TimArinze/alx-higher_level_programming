#!/usr/bin/node
// A script that imports an array and computes a new array
const arr = require('./100-data').list;
console.log(arr);
const map1 = arr.map((num, index) => num * index);
console.log(map1);
