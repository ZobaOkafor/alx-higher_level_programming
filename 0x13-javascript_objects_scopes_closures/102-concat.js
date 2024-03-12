#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

const concatenatedContent = contentA + '\n' + contentB;

fs.writeFileSync(fileC, concatenatedContent);

console.log(`Concatenated ${fileA} and ${fileB} into ${fileC}`);
