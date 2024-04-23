#!/usr/bin/node

const request = require('request');

// Function to fetch character data and print the name
function fetchAndPrintCharacterName (characterUrls, index) {
  // Base case: if index is greater than or equal to the length of characterUrls, stop recursion
  if (index >= characterUrls.length) {
    return;
  }

  const characterUrl = characterUrls[index];

  request(characterUrl, (error, response, body) => {
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

    // Recursive call: fetch and print the next character's name
    fetchAndPrintCharacterName(characterUrls, index + 1);
  });
}

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

  // Start the recursive process with the initial index 0
  fetchAndPrintCharacterName(charactersUrls, 0);
});
