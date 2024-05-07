'use strip';

const temperatures = [3, -2, 'error', 9, 13, 17, 15, 14, 9, 5];
function calcTempAmplitude(temps) {
  let max = temps[0];
  let min = temps[0];

  for (let i = 0; i < temps.length; i++) {
    if (typeof temps[i] !== 'number') continue;

    if (temps[i] > max) max = temps[i];
    if (temps[i] < min) min = temps[i];
  }

  console.log(max, min);
  return max - min;
}

// calcTempAmplitude([3, 4, 10, -3, 30, 1, 9]);
// const aptitude = calcTempAmplitude(temperatures);
// console.log(aptitude);

// Using two parameters, concatinate two arrays
function calcTempAmplitudeNew(arr1, arr2) {
  const temps = arr1.concat(arr2);
  let max = temps[0];
  let min = temps[0];

  for (let i = 0; i < temps.length; i++) {
    if (typeof temps[i] !== 'number') continue;
    // debugger;
    if (temps[i] > max) max = temps[i];
    if (temps[i] < min) min = temps[i];
  }

  console.log(max, min);
  return max - min;
}

apptitude = calcTempAmplitudeNew(
  [3, 4, 10, 30, 1, 9],
  ['error', 'merit', 7, 11, 13]
);
console.log(apptitude);
