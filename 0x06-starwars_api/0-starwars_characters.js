#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.log('Error:', err);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.log('Error:', err);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
