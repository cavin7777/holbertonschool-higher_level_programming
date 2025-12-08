// Select the element with id 'character'
const characterDiv = document.querySelector('#character');

// Fetch the character data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // parse JSON
  .then(data => {
    // Update the HTML with the character name
    characterDiv.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
