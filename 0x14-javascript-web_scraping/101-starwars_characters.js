#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  // Function to fetch character data and print the name
  const fetchAndPrintCharacterName = (url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  };

  // Iterate through each character URL and fetch/print the name
  charactersUrls.forEach(fetchAndPrintCharacterName);
});
