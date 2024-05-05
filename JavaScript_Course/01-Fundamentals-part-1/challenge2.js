'use strip'

/*
const calcTip = function(bill) {
    return bill >= 50 && bill <= 300 ? bill * 0.15 : 
    bill * 0.2;
}

//const calTip = bill => bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;

const bills = [125, 555, 44];
const tips = [calcTip(bills[0]),  calcTip(bills[0]),  calcTip(bills[0])];
const totals = [bills[0] + tips[0], bills[1] + tips[1], bills[2] + tips[2]]
console.log(`Your bill is ${bills}, your tips are ${tips} the total is ${totals}`);
*/

// test
function annualGrandRent(annualRent, numOfMonth) {
    annualRent = Number(prompt('Enter your annual rent and I will tell you its cost per month'))
    numOfMonth = Number(prompt('Enter the number of months you want to pay'))
    const total = annualRent / numOfMonth
    console.log(`Your annual rent is ${annualRent} for ${numOfMonth} months. Your rent is ${total} payment per month.`)
}

rent = annualGrandRent()
// console.log(`${rent}`)

const student1 = {
    firstName: 'James',
    midddleName: 'Ikenna',
    lastName: 'Christian',
    age: 2024 - 1990,
    class: '200 Level',
    dept: 'Somputer Science',
    faculty: 'School of Science',
    friends: ['Praise', 'Cyril', 'Mercy']
}

console.log(student1.firstName)
const message = prompt('What do you know about student1? choose between \
firstName, lastName, middleName, age, class, dept, faculty, friends')
if (student1[message]){
    console.log(student1[message]);
} else {
    console.log('Wrong request! Choose between firstName, lastName, \
    middleName, age, class, dept, faculty, friends')
}

console.log(`${student1.firstName} has ${student1.friends.length}, and \
his best friend is ${student1.friends[1]}`)