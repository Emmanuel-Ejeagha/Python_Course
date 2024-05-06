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


// test
function annualGrandRent(annualRent, numOfMonth) {
    annualRent = Number(prompt('Enter your annual rent and I will tell \
    you its cost per month'))
    numOfMonth = Number(prompt('Enter the number of months you want to pay'))
    const total = annualRent / numOfMonth
    console.log(`Your annual rent is ${annualRent} for ${numOfMonth} months.\
     Your rent is $${total} per month.`)
}

rent = annualGrandRent()
// console.log(`${rent}`)

const student1 = {
    firstName: 'James',
    midddleName: 'Ikenna',
    lastName: 'Christian',
    age: 2024 - 1990,
    class: '200 Level',
    dept: 'Computer Science',
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

console.log(`${student1.firstName} has ${student1.friends.length} friends, and \
his best friend is ${student1.friends[1]}`)
console.log(student1)


const mark = {
    fullName: 'Mark Miller',
    mass: 78,
    height: 1.69,
    calcBMI: function() {
        this.bmi = this.mass / this.height ** 2;
        return this.bmi
    }
};

const john = {
    fullName: 'John Smith',
    mass: 92,
    height: 1.95,
    calcBMI: function() {
        this.bmi = this.mass / this.height ** 2;
        return this.bmi
    }
};

mark.calcBMI();
john.calcBMI();

console.log(mark.bmi, john.bmi);

// 
if (mark.bmi > john.bmi) {
console.log(`${mark.fullName}'s BMI (${mark.bmi}) is higher than ${john.fullName}'s BMI (${john.bmi})`)
} else if (john.bmi > mark.bmi) {
console.log(`${john.fullName}'s BMI (${john.bmi}) is higher than ${mark.fullName}'s BMI (${mark.bmi})`)
}

for(let rep = 1; rep <= 10; rep++) {
    console.log(`${rep}. for loop repetitions!`)
}


const student1 = [
    'James',
    'Ikenna',
    'Christian',
     2024 - 1990,
    '200 Level',
    'Computer Science',
    'School of Science',
    ['Praise', 'Cyril', 'Mercy'],
    'Student',
    true
]
const types = []


for (let i = 0; i < student1.length; i++) {
    console.log(student1[i], (typeof student1[i]))
    // inserting into an empty array 
    types[i] = typeof student1[i];

    // another method of filling an empty array
    types.push(typeof student1[i]);
}

console.log(types);

const years = [1992, 1994, 1984, 1960, 2015, 2004, 2006];
const ages = [];

for (let i = 0; i < years.length; i++) {
    ages.push(2024 - years[i]);
}
console.log(ages);

console.log('Prints only non strigs to the)
for (let i = 0; i < student1.length; i++) {
    if (typeof student1[i] === 'string') continue;

    console.log(student1[i], typeof student1[i]);
}
*/

const mark = [
    'Jonas',
    'Kennedy',
    2024 - 1992,
    'teacher',
    ['Mike', 'Kingsley', 'Ben', 'Mitchell'],
    true
];

for (let i = mark.length -1; i >= 0; i--) {
    console.log(mark[i])
}

for (let i = 0; i <= 7; i++) {
    console.log(`-------Daily Routines-------week ${i}`)
    for (let rep = 1; rep <=3; rep++) {
        console.log(`Read documentations, coding, programming ${rep}`)
    }
}

let counter = 1
while (counter < 5){
    // console.log(`Fill this jar 5 times. Filled ${counter} time(s) `)
    counter++
}

let dice = Math.trunc(Math.random() * 6) + 1;

while (dice !== 6) {
    console.log(`You rolled a ${dice}`);
    dice = Math.trunc(Math.random() * 6) + 1;
    if (dice === 6) {
        console.log('You are a winner!🏆')
    }
}