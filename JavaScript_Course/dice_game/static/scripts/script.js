#!/usr/bin/node
'use strict';

// Selecting elements
const player0Element = document.querySelector('.player--0');
const player1Element = document.querySelector('.player--1');
const score0Element = document.querySelector('#score--0');
const score1Element = document.getElementById('score--1');
const current0Element = document.getElementById('current--0');
const current1Element = document.getElementById('current--1');

const diceElement = document.querySelector('.dice');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');
// Starting condition

// restarts the game
const init = function () {
    
    const scores = [0, 0];
    let currentScore = 0;
    let activePlayer = 0;
    let playing = true;

    score0Element.textContent = 0;
    score1Element.textContent = 0;
    current0Element.textContent = 0;
    current1Element.textContent = 0;
    
    diceElement.classList.add('hidden');
    player0Element.classList.remove('player--winner');
    player1Element.classList.remove('player--winner');
    player0Element.classList.add('player--active');
    player0Element.classList.remove('player--active');
}

// This function switches the players
const switchPlayer = function () {
  document.getElementById(`current--${activePlayer}`).textContent = 0;
  activePlayer = activePlayer === 0 ? 1 : 0;
  currentScore = 0;
  player0Element.classList.toggle('player--active');
  player1Element.classList.toggle('player--active');
};

// Rolling dice functionality
btnRoll.addEventListener('click', function () {
  if (playing) {
    // 1. Generating a random dice roll
    const dice = Math.trunc(Math.random() * 6) + 1;

    // 2. Display dice
    diceElement.classList.remove('hidden');
    diceElement.src = `/static/images/dice-${dice}.png`;

    // 3. Check for rolled 1: if true, switch to next player
    if (dice !== 1) {
      // Add dice to the current score
      currentScore += dice;
      document.getElementById(`current--${activePlayer}`).textContent =
        currentScore;
      // current0Element.textContent = currentScore;
    } else {
      // Switch to next player
      switchPlayer();
    }
  }
});

// btnRoll.addEventListner('click');
btnHold.addEventListener('click', function () {
  if (player) {
    // 1. Add current score to active player's score
    score[activePlayer] += currentScore;
    document.getElementById(`current--${activePlayer}`).textContent =
      score[activePlayer];

    // Checks if the player's score is >= 100
    if (scores[activePlayer] >= 100) {
      // Finish the game
      playing = false;
      diceElement.classList.add('hidden');

      document
        .querySelector(`.player--${activePlayer}`)
        .classList.add('.player--winner');
      document
        .querySelector(`.player--${activePlayer}`)
        .classList.remove('.player--winner');
    } else {
      switchPlayer();
    }
  }
});

// Restarts the game
btnNew.addEventListener('click', 


});
