// Select the div with id 'update_header'
const updateDiv = document.querySelector('#update_header');

// Add a click event listener
updateDiv.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');

  // Update the header text
  header.textContent = 'New Header!!!';
});
