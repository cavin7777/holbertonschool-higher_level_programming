// Select the div with id 'red_header'
const redHeader = document.querySelector('#red_header');

// Add a click event listener
redHeader.addEventListener('click', function () {
  // Select the header element and change its color
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
