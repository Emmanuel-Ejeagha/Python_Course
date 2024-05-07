'use strip';

/*
 1) Understanding the problem
- Array transformed to string, separated by ...
- What is the X days? Answer: index + 1


2) Breaking up into sub-problems
- Create a function that contains one parameter
- declare a variable 
- Use a forn loop to iterate through the array
- Transform array into string
- Transform each element to string with °C
- Add ... between elements and start end of string
- Log string to the screen
*/
const data1 = [17, 21, 23];
const data2 = [12, 5, -5, 0, 4];
// const data3 = data1.concat(data2)

function printTemp(arr) {
  let str = '';
  for (let i = 0; i < arr.length; i++) {
    str += `${arr[i]}°C in ${i + 1} days... `;
  }
  console.log('... ' + str);
}

printTemp(data1);
