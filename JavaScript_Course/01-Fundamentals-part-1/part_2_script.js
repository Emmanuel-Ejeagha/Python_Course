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


// Arrow function
const yearUntilRetirement = (birthYear, firstName) => {
    const age = 2037 - birthYear;
    const retirement = 65 - age;
    return `${firstName} will retire in ${retirement} year(s) time.`
}
let retire1 = yearUntilRetirement(1991, 'James')
console.log(retire1)
console.log(yearUntilRetirement(1980, 'Bob'))
const calcAge  = function (birthYear) {
    return 2024 - birthYear;
}
const year = [1990, 1997, 2002, 1994];
const age1 = calcAge(year[0]);
const age2 = calcAge(year[1]);
const age3 = calcAge(year[year.length - 1]);
console.log(age1, age2, age3);

const years = new Array(1991, 1992, 1993, 1994, 1995)
console.log(years[0])
const ages = [calcAge(year[0]), calcAge(year[1]),
calcAge(year[year.length - 1])];
console.log(ages);
*/

// Arrays
const friends = ['Ken', 'steven', 'Miracle', 'Sharom']
console.log(friends)


console.log(friends.length)
console.log(friends[friends.length - 1]);

// Add elements
friends.push = ('Seyi'); // add elements at the end of the array
console.log(friends);

friends.unshift('John') // add elements at the beginning of the array
console.log(friends);

// Remove elements
let popped = friends.pop()
console.log(friends);
console.log(popped);

friends.shift()
console.log(friends);

console.log(friends.indexOf('steven')); // displays the index num of an element
console.log(friends.includes('Bob'));
console.log(friends.includes('Miracle'))
console.log(friends.indexOf('Miracle'))

if (friends.includes('Miracle')) {
    console.log(`You have a friend called ${friends[2]}.`)
}