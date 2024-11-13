#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/3/';

async function getData() {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error('Could not fetch the resource');
    }

    const data = await response.json();
    for (const characterUrl of data.characters) {
      const charResponse = await fetch(characterUrl);

      if (!charResponse.ok) {
        throw new Error('Could not fetch character data');
      }

      const charData = await charResponse.json();
      console.log(charData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getData();
