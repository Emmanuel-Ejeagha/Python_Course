'use strict';

// variable declaration
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnShowModal = document.querySelectorAll('.show-modal');

// This function hides the modal class
const closelModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

// This function displays the modal class
const showModal = function () {
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

for (let i = 0; i < btnShowModal.length; i++)
  btnShowModal[i].addEventListener('click', showModal);

// Hides th modal class by clicking on the window
btnCloseModal.addEventListener('click', closelModal);
overlay.addEventListener('click', closelModal);

// closes the window when ESC is pressed
document.addEventListener('keydown', function (e) {
  // console.log(e.key);

  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    closelModal();
  }
});
