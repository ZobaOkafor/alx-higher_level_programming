#!/usr/bin/node

const initialList = require('./100-data.js');

const newList = initialList.map((value, index) => value * index);

console.log('Initial List:', initialList);
console.log('New List:', newList);
