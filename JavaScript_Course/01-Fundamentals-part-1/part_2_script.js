#!/usr/bin/node
'use strict'

/*
let hasDriversLicense = false;
const passTest = true;

if (passTest) hasDriversLicense = true
console.log('Hello world')


function greeter(name) {
    name = prompt('What is your name? ')
    return `Hello ${name}, Welcome to JavaScript Language.`
}

let myName = greeter('Emma')
console.log(myName)

function fruitJuice( oranges, apples) {
    console.log("Welcome to juice shop.")
    const juice = `Your Juice with ${apples} apples and ${oranges} oranges is ready!.`
    return juice
}

console.log(fruitJuice(2, 3))

// function declration
function calcAge1(birthYear) {
    return 2040 - birthYear;
}

const age1 = calcAge1(1994);
console.log(age1)

// function expression
const calcAge2 = function (birthYear) {
    return 2024 - birthYear;
}

const age2 = calcAge2(1994)
console.log(age2)


const calcAge3 = birthYear => 2024 - birthYear;
const age3 = calcAge3(1996)
console.log(age3)
*/

// Arrow function
const yearUntilRetirement = (birthYear, firstName) => {
    const age = 2037 - birthYear;
    const retirement = 65 - age;
    return `${firstName} will retire in ${retirement} year(s) time.`
}
let retire1 = yearUntilRetirement(1991, 'James')
console.log(retire1)
console.log(yearUntilRetirement(1980, 'Bob'))
