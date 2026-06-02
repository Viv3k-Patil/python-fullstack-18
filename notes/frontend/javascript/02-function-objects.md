# JavaScript — Day 2: Functions, Loops, Arrays & Objects

> You've got variables and conditionals down. Today we learn how to *organise* code and work with collections of data. This is where JavaScript starts feeling like a real tool.

---

## Chapter 1 — Functions: Reusable Blocks of Code

A function is a **named recipe**. You write it once, then call it by name whenever you need it. Without functions, you'd copy-paste the same code everywhere — a nightmare to fix later.

```js
// Without functions — messy
console.log("Welcome, Rahul! You have 3 messages.");
console.log("Welcome, Priya! You have 7 messages.");
console.log("Welcome, Amit! You have 0 messages.");

// With a function — clean ✅
function showWelcome(name, messageCount) {
  console.log(`Welcome, ${name}! You have ${messageCount} messages.`);
}

showWelcome("Rahul", 3);
showWelcome("Priya", 7);
showWelcome("Amit", 0);
```

### 1.1 Anatomy of a function

```js
function greet(name) {         // 'name' is a parameter (input placeholder)
  let message = `Hello, ${name}!`;
  return message;              // return sends a value back to the caller
}

let result = greet("Arjun");   // 'Arjun' is the argument (actual value)
console.log(result);           // "Hello, Arjun!"
```

- **Parameters** = variables listed in the function definition (the placeholders)
- **Arguments** = actual values you pass when calling the function
- **`return`** = sends a value back. Without it, functions return `undefined`

```js
function add(a, b) {
  return a + b;
}

let sum = add(5, 3);   // sum = 8
console.log(sum + 2);  // 10 — you can use the returned value directly
```

### 1.2 Three ways to write functions

**1. Function Declaration** — hoisted, can be called before it's defined

```js
sayHello(); // ✅ Works — declarations are hoisted

function sayHello() {
  console.log("Hello!");
}
```

**2. Function Expression** — stored in a variable, NOT hoisted

```js
const sayHello = function() {
  console.log("Hello!");
};

sayHello(); // ✅ Works only after this line
```

**3. Arrow Function** — modern, shorter syntax (ES6+)

```js
// Regular function
const add = function(a, b) { return a + b; };

// Arrow function — same thing
const add = (a, b) => { return a + b; };

// Even shorter — if single expression, drop the braces and return
const add = (a, b) => a + b;

// Single parameter — can drop parentheses
const double = n => n * 2;

// No parameters — empty parens required
const greet = () => console.log("Hi!");
```

**Analogy:** Arrow functions are like texting shorthand — same meaning, fewer characters.

### 1.3 Default Parameters

```js
function createUser(name, role = "viewer") {
  console.log(`${name} joined as ${role}`);
}

createUser("Priya", "admin");  // "Priya joined as admin"
createUser("Rahul");           // "Rahul joined as viewer" ← default kicks in
```

### 1.4 Rest Parameters — accept unlimited arguments

```js
function sum(...numbers) {     // ...numbers collects all arguments into an array
  let total = 0;
  for (let n of numbers) {
    total += n;
  }
  return total;
}

sum(1, 2, 3);        // 6
sum(10, 20, 30, 40); // 100
```

### 1.5 Functions are values — pass them around

In JavaScript, functions are "first-class citizens" — you can store them in variables, pass them to other functions, and return them from functions.

```js
function runTwice(fn) {     // fn is a function passed as an argument
  fn();
  fn();
}

function sayHi() {
  console.log("Hi!");
}

runTwice(sayHi);
// Hi!
// Hi!
```

A function passed to another function is called a **callback**. You'll see this constantly.

---

## Chapter 2 — Loops: Doing Things Repeatedly

**Analogy:** Imagine you have to stamp "Paid" on 100 invoices. Instead of writing 100 stamp actions, you write one and say "do this 100 times." That's a loop.

### 2.1 `for` loop — when you know how many times

```js
for (let i = 0; i < 5; i++) {
  console.log(`Step ${i}`);
}
// Step 0
// Step 1
// Step 2
// Step 3
// Step 4
```

The three parts: `let i = 0` (start) | `i < 5` (keep going while true) | `i++` (do this after each round)

```js
// Count backwards
for (let i = 5; i >= 1; i--) {
  console.log(i);
}
// 5, 4, 3, 2, 1

// Count by 2s
for (let i = 0; i <= 10; i += 2) {
  console.log(i);
}
// 0, 2, 4, 6, 8, 10
```

### 2.2 `while` loop — when you don't know how many times

```js
let password = "";

while (password !== "secret123") {
  password = "secret123"; // In real code, you'd get this from user input
  console.log("Checking password...");
}

console.log("Access granted!");
```

⚠️ **Watch out for infinite loops!** If the condition never becomes false, your program hangs forever.

```js
// ❌ Infinite loop — don't run this!
while (true) {
  console.log("Help I'm stuck");
}
```

### 2.3 `do...while` — runs at least once

```js
let count = 0;

do {
  console.log(`Count: ${count}`);
  count++;
} while (count < 3);
// Count: 0
// Count: 1
// Count: 2
```

### 2.4 `break` and `continue`

```js
// break — exit the loop early
for (let i = 0; i < 10; i++) {
  if (i === 5) break;         // stop when i hits 5
  console.log(i);
}
// 0, 1, 2, 3, 4

// continue — skip this iteration, go to next
for (let i = 0; i < 6; i++) {
  if (i === 3) continue;      // skip 3
  console.log(i);
}
// 0, 1, 2, 4, 5
```

---

## Chapter 3 — Arrays: Ordered Lists

An array is an **ordered list** of values. Like a numbered shelf — slot 0, slot 1, slot 2...

```js
let fruits = ["mango", "banana", "apple"];
//              [0]       [1]      [2]

console.log(fruits[0]);  // "mango"   ← index starts at 0!
console.log(fruits[2]);  // "apple"
console.log(fruits.length); // 3
```

**Analogy:** An array is like a train. Each coach (element) has a seat number (index) starting from 0.

### 3.1 Common array methods

```js
let items = ["a", "b", "c"];

// Add/Remove at end
items.push("d");       // ["a", "b", "c", "d"] — add to end
items.pop();           // ["a", "b", "c"]       — remove from end

// Add/Remove at start
items.unshift("z");    // ["z", "a", "b", "c"] — add to start
items.shift();         // ["a", "b", "c"]       — remove from start

// Find something
items.indexOf("b");    // 1  — returns position, or -1 if not found
items.includes("b");   // true

// Copy a portion
items.slice(0, 2);     // ["a", "b"] — from index 0, up to (not including) 2

// Remove/replace items
items.splice(1, 1);    // removes 1 item at index 1 → ["a", "c"]
items.splice(1, 0, "X"); // insert "X" at index 1 without removing

// Join into a string
["hello", "world"].join(" ");  // "hello world"
["a", "b", "c"].join(", ");   // "a, b, c"
```

### 3.2 Looping over arrays

```js
let scores = [85, 72, 91, 68, 95];

// Classic for loop
for (let i = 0; i < scores.length; i++) {
  console.log(scores[i]);
}

// for...of — cleaner, preferred when you don't need the index
for (let score of scores) {
  console.log(score);
}

// forEach — callback style
scores.forEach(function(score) {
  console.log(score);
});

// Arrow function version
scores.forEach(score => console.log(score));
```

### 3.3 Powerful array methods — map, filter, reduce

These are the three most important array methods. Every JS developer uses them daily.

**`map`** — transform every item, returns new array (same length)

```js
let prices = [100, 200, 300];

// Add 18% GST to all prices
let withGST = prices.map(price => price * 1.18);
console.log(withGST); // [118, 236, 354]

// The original is unchanged!
console.log(prices);  // [100, 200, 300]
```

**Analogy:** `map` is like a conveyor belt with a stamping machine. Every item goes through and comes out changed.

**`filter`** — keep only items that pass a test, returns new array (shorter or equal length)

```js
let ages = [15, 22, 17, 30, 16, 25];

let adults = ages.filter(age => age >= 18);
console.log(adults); // [22, 30, 25]
```

**`reduce`** — boil an array down to a single value

```js
let numbers = [1, 2, 3, 4, 5];

let total = numbers.reduce((accumulator, current) => {
  return accumulator + current;
}, 0); // 0 is the starting value

console.log(total); // 15
```

Think of `accumulator` as a running total and `current` as each item you process.

**Chaining them together** — this is where they shine:

```js
let products = [
  { name: "Shirt", price: 800, inStock: true },
  { name: "Shoes", price: 2500, inStock: false },
  { name: "Belt", price: 400, inStock: true },
  { name: "Watch", price: 5000, inStock: true },
];

// Get total value of in-stock items over ₹500
let total = products
  .filter(p => p.inStock && p.price > 500)   // Shirt filtered out (≤500), Shoes filtered out (not in stock)
  .map(p => p.price)                          // [2500 filtered, 5000] → [800 filtered too] → [5000]
  .reduce((sum, price) => sum + price, 0);

// Actually: filter keeps Shirt(800,inStock) and Watch(5000,inStock)
// map → [800, 5000]
// reduce → 5800

console.log(total); // 5800
```

### 3.4 Other useful array methods

```js
let nums = [3, 1, 4, 1, 5, 9, 2, 6];

// Sort (careful — sorts as strings by default!)
nums.sort((a, b) => a - b);  // [1, 1, 2, 3, 4, 5, 6, 9] ascending
nums.sort((a, b) => b - a);  // [9, 6, 5, 4, 3, 2, 1, 1] descending

// Find
nums.find(n => n > 4);       // 5 — returns first match
nums.findIndex(n => n > 4);  // returns index of first match

// Check if any/all pass a test
nums.some(n => n > 8);       // true — at least one is > 8
nums.every(n => n > 0);      // true — all are > 0

// Flatten nested arrays
[1, [2, 3], [4, [5]]].flat();    // [1, 2, 3, 4, [5]]
[1, [2, 3], [4, [5]]].flat(2);   // [1, 2, 3, 4, 5]  — depth 2
```

---

## Chapter 4 — Objects: Structured Data

An array stores a list. An **object** stores related data with named labels (called **keys** or **properties**).

```js
let person = {
  name: "Priya",
  age: 28,
  city: "Pune",
  isEmployee: true
};

// Access with dot notation
console.log(person.name);  // "Priya"
console.log(person.age);   // 28

// Access with bracket notation (useful when key is dynamic)
let key = "city";
console.log(person[key]);  // "Pune"

// Add or update
person.email = "priya@example.com";  // adds new property
person.age = 29;                     // updates existing

// Delete
delete person.isEmployee;
```

**Analogy:** An array is a numbered shelf. An object is a filing cabinet — each drawer has a label (key) and contains something (value).

### 4.1 Objects with methods

Objects can also store functions — these are called **methods**.

```js
let calculator = {
  value: 0,

  add(n) {
    this.value += n;    // 'this' refers to the calculator object
    return this;        // return 'this' enables chaining
  },

  subtract(n) {
    this.value -= n;
    return this;
  },

  result() {
    return this.value;
  }
};

calculator.add(10).add(5).subtract(3);
console.log(calculator.result()); // 12
```

### 4.2 Destructuring — pull values out cleanly

**Array destructuring:**

```js
let [first, second, third] = ["red", "green", "blue"];
console.log(first);  // "red"
console.log(third);  // "blue"

// Skip elements
let [, , last] = [1, 2, 3];
console.log(last); // 3

// Rest in destructuring
let [head, ...tail] = [1, 2, 3, 4, 5];
console.log(head); // 1
console.log(tail); // [2, 3, 4, 5]
```

**Object destructuring:**

```js
let user = { name: "Rahul", age: 25, city: "Delhi" };

let { name, age } = user;
console.log(name); // "Rahul"
console.log(age);  // 25

// Rename while destructuring
let { name: fullName, age: years } = user;
console.log(fullName); // "Rahul"

// Default values
let { name: n, email = "not provided" } = user;
console.log(email); // "not provided" — wasn't in object

// In function parameters (very common pattern)
function greetUser({ name, city }) {
  console.log(`Hello ${name} from ${city}!`);
}

greetUser(user); // "Hello Rahul from Delhi!"
```

### 4.3 Spread Operator `...`

Spread "unpacks" an array or object.

```js
// Copying arrays
let original = [1, 2, 3];
let copy = [...original];       // independent copy
copy.push(4);
console.log(original);          // [1, 2, 3] — unchanged

// Merging arrays
let a = [1, 2, 3];
let b = [4, 5, 6];
let merged = [...a, ...b];      // [1, 2, 3, 4, 5, 6]

// Copying objects
let user = { name: "Priya", age: 28 };
let updatedUser = { ...user, age: 29, city: "Pune" };
// { name: "Priya", age: 29, city: "Pune" }
// Later properties overwrite earlier ones
```

### 4.4 Looping over objects

```js
let scores = { maths: 90, science: 85, english: 78 };

// Get all keys
Object.keys(scores);    // ["maths", "science", "english"]

// Get all values
Object.values(scores);  // [90, 85, 78]

// Get key-value pairs
Object.entries(scores); // [["maths", 90], ["science", 85], ["english", 78]]

// Loop over entries
for (let [subject, score] of Object.entries(scores)) {
  console.log(`${subject}: ${score}`);
}
```

---

## Chapter 5 — Putting It All Together

### Practice — Student Report System

```js
const students = [
  { name: "Arjun", marks: [85, 92, 78, 90] },
  { name: "Priya", marks: [72, 68, 80, 75] },
  { name: "Rahul", marks: [95, 98, 92, 97] },
  { name: "Sneha", marks: [55, 62, 58, 60] },
];

function getGrade(average) {
  if (average >= 90) return "A";
  if (average >= 75) return "B";
  if (average >= 60) return "C";
  return "F";
}

function generateReport(students) {
  return students.map(student => {
    const total = student.marks.reduce((sum, mark) => sum + mark, 0);
    const average = total / student.marks.length;
    const grade = getGrade(average);

    return {
      name: student.name,
      average: average.toFixed(2),  // round to 2 decimal places
      grade
    };
  });
}

const report = generateReport(students);

report.forEach(({ name, average, grade }) => {
  console.log(`${name}: ${average} — Grade ${grade}`);
});
// Arjun: 86.25 — Grade B
// Priya: 73.75 — Grade C
// Rahul: 95.50 — Grade A
// Sneha: 58.75 — Grade F

// Who passed?
const passedStudents = report.filter(s => s.grade !== "F");
console.log(`Passed: ${passedStudents.length}/${students.length}`);
```

---

## Day 2 Cheat Sheet

```
Functions:
  function name(params) { return value; }
  const name = (params) => expression;
  Default params: fn(x, y = "default")
  Rest params: fn(...args)

Loops:
  for (let i = 0; i < n; i++) { }
  for (let item of array) { }
  while (condition) { }
  break → exit | continue → skip

Arrays:
  push/pop (end) | unshift/shift (start)
  indexOf | includes | slice | splice
  map → transform all
  filter → keep some
  reduce → combine into one
  find | findIndex | some | every | sort | flat

Objects:
  { key: value }  dot/bracket access
  Destructuring: const { a, b } = obj
  Spread: { ...obj, newKey: val }
  Object.keys() | .values() | .entries()
```