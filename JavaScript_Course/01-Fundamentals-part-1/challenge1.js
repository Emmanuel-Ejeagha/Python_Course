/*
let markWeight = 78;
let markHeight = 1.69
let johnWeight = 92
let johnHeight = 1.95


let markBMI = markWeight / (markHeight ** 2);
let johnBMI = johnWeight / (johnHeight ** 2);
let markHigherBMI = markBMI > johnBMI;

console.log("TEST DATA 1, is mark's BMI > John's BMI?")
console.log(markBMI, johnBMI, markHigherBMI);
console.log('Who has the higher BMI?');
if (markBMI > johnBMI) {
    console.log(`Marks BMI is ${markBMI}, it is greater than ${johnBMI} John's BMI `)
} else {
    console.log(`John's BMI is ${johnBMI}, it is greater than ${markBMI} Mark's BMI`)
}

markWeight = 78;
markHeight = 1.69;
johnWeight = 95;
johnHeight = 1.76;

markBMI = markWeight / (markHeight ** 2);
johnBMI = johnWeight / (johnHeight ** 2);
markHigherBMI = markBMI > johnBMI;


console.log("TEST DATA 2, is mark's BMI > John's BMI?")
if (markBMI > johnBMI) {
    console.log(`Marks BMI is ${markBMI}, it is greater than ${johnBMI} John's BMI `)
} else {
    console.log(`John's BMI is ${johnBMI}, it is greater than ${markBMI} Mark's BMI`)
}


// const teamDolphinesAvg = Number((96 + 108 + 89) / 3);
// const teamKoalasAvg = Number((88 + 91 + 110) / 3)
const scoresDolphine = Number(96 + 108 + 89);
const scoresKoalas = Number(88 + 91 + 110);
const numTimes = 3;
const averageDolphine = scoresDolphine / numTimes;
const averagekoalas = scoresKoalas / numTimes;
const minScore = 100

console.log(`The Average score of Dolphine and Koalas is ${averageDolphine}, ${averagekoalas} respectively.`)
if (averageDolphine > averagekoalas) {
    console.log('Dolpines is the winner!');
} else if (averageDolphine < averagekoalas) {
    console.log("Koalas is the winner!")
} else {
    console.log('The game ended with draw!')
}


// method 1
let tip = Number(prompt('Enter your bill: '))

tip >= 50 && tip <= 300 ? console.log(`Your tip is ${tip * 0.15}`) : 
console.log(`Your tip is ${tip * 0.2}.`)

// method 2
let bill = Number(prompt('Enter your bill: '))

let tip = bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2
console.log(`The bill was ${bill}, the tip was ${tip}, 
and the total value ${bill + tip}`)
*/

// #3 challenge
const calAverage = (x, y, z) => (x + y + z) / 3;
console.log(calAverage(55, 56, 57))

const scoreDolphins = calAverage(44, 23, 71);
const scoreKoalas = calAverage(65, 54, 49)

function checkWinner(avgDolphins, avgKoalas) {
    if (avgDolphins >= avgKoalas * 2) {
        console.log(`Dolphines win 🏆 (${avgDolphins} vs. ${avgKoalas})`)
    } else if (avgKoalas >= avgDolphins * 2) {
        console.log(`Koalas win 🏆 (${avgKoalas} vs. ${avgDolphins})`)
    } else {
        console.log('No team wins...')
    }
}
checkWinner(scoreDolphins, scoreKoalas);

checkWinner(40, 111)