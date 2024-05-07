"use strip";

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


*/

// Challenge

calcTip = function (bill) {
  return bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
};

const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
const tips = [];
const totals = [];

for (let i = 0; i < bills.length; i++) {
  const tip = calcTip(bills[i]);
  tips.push(tip);
  totals.push(tip + bills[i]);
}
console.log(bills, tips, totals);

const calcAverage = function (arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum / arr.length;
};
calcAverage([2, 3, 6]);
calcAverage(totals);
calcAverage(tips);

const x = 23;
