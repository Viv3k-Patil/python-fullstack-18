// operators are symbol that operates on values i.e operands

// arithmetic operators
let a = 15;
let b = 20;
console.log(a + b);  // + operator (bi[2]-operands)nary operator
console.log(a - b);
console.log(a / b);
console.log(a * b);
console.log(a % b);
console.log(a ** b);

// assignment operators
let score = 0;

score = score + 10; // long way
score += 10;        // short way (same thing) ✅

score -= 5;   // score = score - 5
score *= 2;   // score = score * 2
score /= 2;   // score = score / 2

// Increment and Decrement (add/subtract 1)
score++;  // score = score + 1
score--;  // score = score - 1

// String Operators
let first = "Vivek";
let second = "Patil";
console.log(first+ " " +second);

// formatted string - in python

console.log(`Your name is: ${first} ${second}, Welcome to the future!!`)

// comparision operators
console.log(5 > 3)    // true  — is 5 greater than 3?
5 < 3    // false — is 5 less than 3?
5 >= 5   // true  — is 5 greater than or equal to 5?
5 <= 4   // false — is 5 less than or equal to 4?

// Equality — THE MOST IMPORTANT ONE TO GET RIGHT
5 == "5"   // true  ← dangerous! JS converts types to match (called coercion)
5 === "5"  // false ← safe! checks value AND type

5 != "5"   // false ← loose (with coercion)
5 !== "5"  // true  ← strict ✅

// Logical Operators
console.log(true && true);
console.log(true && false);
console.log(false && false);

console.log(true || true);
console.log(true || false);
console.log(false || false);

console.log(5<3 || 5>3);