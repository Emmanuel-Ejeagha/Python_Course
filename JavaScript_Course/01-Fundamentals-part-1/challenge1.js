let markWeight = 78;
let markHeight = 1.69
let johnWeight = 92
let johnHeight = 1.95


let markBMI = markWeight / (markHeight ** 2);
let johnBMI = johnWeight / (johnHeight ** 2);
let markHigherBMI = markBMI > johnBMI;

console.log("TEST DATA 1, is mark's BMI > John's BMI?")
console.log(markBMI, johnBMI, markHigherBMI);

markWeight = 78;
markHeight = 1.69;
johnWeight = 95;
johnHeight = 1.76;

markBMI = markWeight / (markHeight ** 2);
johnBMI = johnWeight / (johnHeight ** 2);
markHigherBMI = markBMI > johnBMI;


console.log("TEST DATA 2, is mark's BMI > John's BMI?")
console.log(markBMI, johnBMI, markHigherBMI);
