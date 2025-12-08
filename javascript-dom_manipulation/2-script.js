// Select the div with id 'red_header'
const redHeader = document.querySelector('#red_header');

// Add a click event listener
redHeader.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');

  // Add the 'red' class
  header.classList.add('red');
});
