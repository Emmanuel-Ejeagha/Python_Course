/*
let js = 'amazing';
console.log(40 + 8 + 23 - 10);

console.log('Jonah');
console.log(23);

firstName = 'Mercy';
let $name = 'Kyrian';
console.log(firstName)
console.log($name)
// This is a single single line comment
 
This is a
Multi
Line
comment


// Boolean
let javascriptIsFun = true;
console.log(javascriptIsFun)
console.log(typeof true)

// chang the value of a variable
javascriptIsFun = 10;
console.log(javascriptIsFun)

// const
const birthYear = 1991;

// operators
const ageMary = 2040 - 1999;
const ageBen = 2040 - 1991;

console.log(ageMary, ageBen)


const firstName = 'James'
const job = 'teacher';
const birthYear = 1999
let year = 2024;
const james = "I'm " + firstName + ', a ' + (year - birthYear) + ' Years old ' + job + '!';
console.log(james)

let jamesNew = `I'm ${firstName}, a ${year - birthYear} years old ${job}!`;
console.log(jamesNew);


const age = 15;

if (age >= 18){
    console.log('Henry can start driving license 🚗');
} else {
    const yearLeft = 18 - age; 
    console.log(`Henry is too young. Wait another ${yearLeft} years :)`)
}

const birthYear = 2002;

let century;
if (birthYear <= 2000) {
    century = 20;
} else {
    century = 21
}
console.log(century);


// 5 falsy values: 0, '', undefined, null,
console.log(Boolean(0))
console.log(Boolean(''))
console.log(Boolean(NaN))
console.log(Boolean(null))
console.log(Boolean(undefined))
console.log(Boolean('Emma'))
console.log(Boolean({}))

let money = 0;
if (money) {
    console.log('Spend wisely! 💰');
} else {
    console.log("You're broke! 😢");
}

let food;
if (food) {
    console.log('Food is ready!')
 } else {
    console.log('The food has finished! 🍲')
 }

 


 // equality operators
 const age = '18';

 if (age === 18) console.log('You just became an adult! (strict)')  // strict equality
 if (age == 18) console.log('You just became an adult! (loose)') //loose equality

 const favourite = Number(prompt(" What's your favourite number? "))

 if (favourite === 23) {
    console.log('Cool! 23 is an amazing number!')
 } else if (favourite === 7) {
    console.log('7 is also cool number')
 } else if (favourite === 9) {
    console.log('9 is an even number!')
 } else {
    console.log('Number is not 23, 7 or 9')
 }

 if (favourite !== 23) console.log("It is not 23")


const hasDriversLisence = true;
const hasGoodVision = true;

if (hasDriversLisence && hasGoodVision) {
    console.log('Emman is qualified to drive!')
} else {
    console.log('Someone else should drive.....')
}

const isTired = true;
console.log(hasDriversLisence || hasGoodVision || isTired)
console.log(hasDriversLisence && hasGoodVision && !isTired)


// Switch statement
const day = prompt("Enter a day of the week. ")

switch (day) {
    case 'monday':
        console.log('It is Monday, Plan course structure');
        break;` `
    case 'tuesday':
        console.log('Prepare theory videos.');
        break
    case 'wednesday':
        console.log('Write a poem');
        break;
    case 'thursday':
        console.log('Read for my exams');
        break;
    case 'friday':
        console.log('Thank God it\'s friday');
        break;
    case 'saturday':
    case 'sunday':
        console.log('Enjoy the weekend 🙋')
    default:
        console.log('Not a valid day!')
}
*/


let day = prompt("Enter the day of the week ")

if (day === 'monday') {
    console.log("It's monday, Happy new week!");
} else if (day === 'tuesday') {
    console.log('Read some documentation');
} else if (day === 'wednesday') {
    console.log("Write code and debug");
} else if (day === 'thursday') {
    console.log(" read more books");
} else if (day === 'friday') {
    console.log("Thank God it's friday!");
} else if (day === 'saturday' || day === 'sunday') {
    console.log("Enjoy your weekend!");
} else {
    console.log('Not a valid day!')
}


// Conditional (Ternary Operators)
const age = 17;
age >= 18 ? console.log('I like to drink wine!🍷') : console.log('I like to drink water 💧')

let bill = Number(prompt('Enter your bill: '))

let tip = bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2
console.log(`The bill was ${bill}, the tip was ${tip}, 
and the total value ${bill + tip}`)