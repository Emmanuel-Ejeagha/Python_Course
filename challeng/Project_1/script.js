"use strict";

let secretNumber = Math.trunc(Math.random() * 20) + 1;
let score = 20
// console.log(secretNumber);

document.querySelector(".check").addEventListener("click", function () {
  const guess = Number(document.querySelector(".guess").value);

  if (!guess) {
    document.querySelector(".message").textContent = "🚫 No number!";
  } else if (guess === secretNumber) {
    document.querySelector(".number").textContent = secretNumber;
    document.querySelector(".message").textContent = "🎉 Correct Number!";
    document.querySelector('body').style.backgroundColor = '#60b347';
    document.querySelector('.number').style.width = '30rem'
  } else if {
    
  }
});
