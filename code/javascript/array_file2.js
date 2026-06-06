let numbers = [1, 2, 3, 4, 5];

let total = numbers.reduce((accumulator, current) => {
  return accumulator - current;
}, 0); // 0 is the starting value

console.log(total); // 15