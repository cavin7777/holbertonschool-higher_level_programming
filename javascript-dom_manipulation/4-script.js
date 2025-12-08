// Select the div with id 'add_item'
const addItemDiv = document.querySelector('#add_item');

// Add a click event listener
addItemDiv.addEventListener('click', function () {
  // Select the ul element with class 'my_list'
  const ul = document.querySelector('.my_list');

  // Create a new li element
  const li = document.createElement('li');
  li.textContent = 'Item';

  // Append the new li to the ul
  ul.appendChild(li);
});
