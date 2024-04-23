#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    const count = filmsData.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(count);
  } else {
    console.error(error || `Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
