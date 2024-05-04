#!/usr/bin/node
'use strict'

/*
let hasDriversLicense = false;
const passTest = true;

if (passTest) hasDriversLicense = true
console.log('Hello world')
*/

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


function calcAge(birthYear) {
    return 2040 - birthYear;
}

const age1 = calcAge(1994);
console.log(age1)

const age2 = function (birthYear) {
    return 2023 - birthYear;
}

