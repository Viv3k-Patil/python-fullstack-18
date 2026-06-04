let nums = [3, 1, 4, 1, 5, 9, 2, 6];

let mynums=nums.map((item)=>item>1)
               .reduce((accu,curr)=>accu+curr,0);
console.log(mynums)

// Sort (careful — sorts as strings by default!)
let num=nums.sort((a, b) => a - b);  // [1, 1, 2, 3, 4, 5, 6, 9] ascending
console.log(num)
nums.sort((a, b) => b - a);  // [9, 6, 5, 4, 3, 2, 1, 1] descending

// Find
nums.find(n => n > 4);       // 5 — returns first match
nums.findIndex(n => n > 4);  // returns index of first match

// Check if any/all pass a test
nums.some(n => n > 8);       // true — at least one is > 8
nums.every(n => n > 0);      // true — all are > 0