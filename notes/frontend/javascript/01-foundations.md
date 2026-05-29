---

## Before We Write Any Code — Setting Up

### What is JavaScript?

JavaScript is the language that makes websites *do things*. HTML is the skeleton, CSS is the clothes, and JavaScript is the muscles. It started in browsers but now runs everywhere — including your computer directly, thanks to **Node.js**.

### Step 1 — Install Node.js

Node.js lets you run JavaScript on your computer without a browser.

1. Go to **https://nodejs.org**
2. Download the **LTS version** (the one that says "Recommended For Most Users")
3. Run the installer — keep clicking Next, nothing tricky
4. Open your **Terminal** (Mac/Linux) or **Command Prompt** (Windows)
5. Type this and press Enter:

```
node --version
```

If you see something like `v20.11.0` — you're good. Node is installed. 🎉

---

### Step 2 — Install VS Code (your code editor)

VS Code is where you'll write your code. Think of it like Microsoft Word, but for code.

1. Go to **https://code.visualstudio.com**
2. Download and install it (just keep clicking Next)

#### Useful VS Code extensions for beginners

Once VS Code is open, click the **Extensions icon** on the left sidebar (looks like 4 squares). Search and install these:

| Extension | Why you need it |
|---|---|
| **Prettier** | Auto-formats your code so it looks clean |
| **ESLint** | Warns you about mistakes before you run code |
| **JavaScript (ES6) code snippets** | Helpful shortcuts for common code |

---

### Step 3 — Run your first JavaScript file

1. Create a folder on your Desktop called `js-practice`
2. Open VS Code → File → Open Folder → select `js-practice`
3. Create a new file called `day1.js`
4. Type this inside:

```js
console.log("Hello, World!");
```

5. Open the **Terminal inside VS Code** (View → Terminal)
6. Type:

```
node day1.js
```

You should see:

```
Hello, World!
```

**`console.log()`** is how JavaScript prints/shows something. Think of it as JavaScript saying something out loud. You'll use it constantly.

---

## Chapter 1 — Variables: Storing Information

A variable is like a **labelled box**. You put something in it, give it a name, and use that name later to get it back.

```js
let playerName = "Arjun";
let score = 0;
let isGameOver = false;
```

### Three ways to create a variable

```js
var oldWay = "avoid this";   // old, causes weird bugs — don't use
let changeable = "I can change"; // use this when the value will change
const fixed = "I won't change";  // use this when the value stays the same
```

**Rule of thumb:** Always reach for `const` first. If you need to change the value later, switch to `let`. Forget `var` exists.

```js
const myName = "Priya";
myName = "Rahul"; // ❌ Error! You can't change a const

let age = 20;
age = 21; // ✅ Fine, let can be changed
```

**Analogy:** `const` is like carving your name in stone. `let` is like writing it on a whiteboard.

---

## Chapter 2 — Data Types: What Kind of Thing Is It?

Every piece of data in JavaScript has a *type*. Like how in real life, "42" is a number but "hello" is text — JavaScript cares about the difference.

### The main types you'll use daily

```js
// 1. Number — any number, with or without decimals
let temperature = 36.6;
let appleCount = 5;

// 2. String — text, always in quotes
let greeting = "Namaste!";
let city = 'Mumbai';
let message = `Hello, ${greeting}`; // backticks let you embed variables!

// 3. Boolean — only two values: true or false
let isRaining = false;
let isLoggedIn = true;

// 4. Undefined — a variable that exists but has no value yet
let futureValue;
console.log(futureValue); // undefined

// 5. Null — intentionally empty (you set it to nothing on purpose)
let selectedItem = null;
```

### Check the type of something with `typeof`

```js
typeof 42          // "number"
typeof "hello"     // "string"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object"  ← this is a famous old bug, just know it
```

---

## Chapter 3 — Operators: Doing Things With Values

Operators are the **action words** of JavaScript. They let you do math, compare things, and combine logic.

### 3.1 Arithmetic Operators (Math)

```js
let a = 10;
let b = 3;

a + b   // 13  → addition
a - b   // 7   → subtraction
a * b   // 30  → multiplication
a / b   // 3.33... → division
a % b   // 1   → remainder (modulo) — "10 divided by 3 leaves remainder 1"
a ** b  // 1000 → power (10 to the power of 3)
```

**The `%` operator is super useful.** It tells you the remainder after division.

```js
10 % 2  // 0 → even number! (no remainder)
11 % 2  // 1 → odd number!
15 % 5  // 0 → divisible by 5!
```

### 3.2 Assignment Operators (Updating values)

```js
let score = 0;

score = score + 10; // long way
score += 10;        // short way (same thing) ✅

score -= 5;   // score = score - 5
score *= 2;   // score = score * 2
score /= 2;   // score = score / 2

// Increment and Decrement (add/subtract 1)
score++;  // score = score + 1
score--;  // score = score - 1
```

### 3.3 String Operators (Joining text)

The `+` operator joins strings together. This is called **concatenation**.

```js
let firstName = "Rahul";
let lastName = "Sharma";

let fullName = firstName + " " + lastName;
console.log(fullName); // "Rahul Sharma"
```

But there's a better way — **template literals** (backtick strings):

```js
let name = "Priya";
let age = 25;

// Old way (messy)
console.log("Hello, my name is " + name + " and I am " + age + " years old.");

// New way (clean) ✅
console.log(`Hello, my name is ${name} and I am ${age} years old.`);
```

Inside backticks, anything inside `${ }` gets treated as code — it runs and the result is placed in the string.

### 3.4 Comparison Operators (Asking yes/no questions)

These always return `true` or `false`.

```js
5 > 3    // true  — is 5 greater than 3?
5 < 3    // false — is 5 less than 3?
5 >= 5   // true  — is 5 greater than or equal to 5?
5 <= 4   // false — is 5 less than or equal to 4?

// Equality — THE MOST IMPORTANT ONE TO GET RIGHT
5 == "5"   // true  ← dangerous! JS converts types to match (called coercion)
5 === "5"  // false ← safe! checks value AND type

5 != "5"   // false ← loose (with coercion)
5 !== "5"  // true  ← strict ✅
```

**Golden rule: Always use `===` and `!==`.** The double-equals `==` tries to be helpful and converts types — this causes sneaky bugs.

```js
// Why == is dangerous:
0 == false    // true  ← confusing!
0 === false   // false ← correct and expected
"" == false   // true  ← wait, what?
"" === false  // false ← makes sense
```

**Analogy:** `==` is like a lazy security guard who accepts a photocopy of your ID. `===` is the strict one who wants the original.

### 3.5 Logical Operators (Combining conditions)

```js
// && → AND: both sides must be true
true && true   // true
true && false  // false
false && true  // false

// || → OR: at least one side must be true
true || false  // true
false || false // false
true || true   // true

// ! → NOT: flips true to false and vice versa
!true   // false
!false  // true
```

Real example:

```js
let age = 20;
let hasTicket = true;

// Can this person enter a concert?
let canEnter = age >= 18 && hasTicket;
console.log(canEnter); // true — they're 18+ AND have a ticket
```

---

## Chapter 4 — Conditionals: Making Decisions

Code needs to make decisions. "If it's raining, take an umbrella. Otherwise, wear sunglasses." That's what conditionals do.

### 4.1 `if` statement

```js
let temperature = 38;

if (temperature > 35) {
  console.log("It's very hot today! Stay hydrated.");
}
```

The code inside `{ }` only runs **if** the condition in `( )` is `true`.

### 4.2 `if...else` statement

```js
let isRaining = true;

if (isRaining) {
  console.log("Carry an umbrella ☂️");
} else {
  console.log("Enjoy the sunshine ☀️");
}
```

### 4.3 `if...else if...else` — Multiple choices

```js
let score = 72;

if (score >= 90) {
  console.log("Grade: A");
} else if (score >= 75) {
  console.log("Grade: B");
} else if (score >= 60) {
  console.log("Grade: C");
} else {
  console.log("Grade: F");
}
// Output: "Grade: C"
```

JavaScript checks from top to bottom and stops at the **first** condition that's true.

### 4.4 `switch` statement — When you have many exact matches

When you're comparing one value against many specific options, `switch` is cleaner than a long chain of `else if`.

```js
let day = "Monday";

switch (day) {
  case "Monday":
    console.log("Start of the week 😩");
    break;
  case "Friday":
    console.log("Almost weekend! 🎉");
    break;
  case "Saturday":
  case "Sunday":
    console.log("Weekend! 🥳");
    break;
  default:
    console.log("It's a regular weekday.");
}
```

⚠️ Don't forget `break`! Without it, JavaScript will fall through to the next case and keep running.

### 4.5 Ternary Operator — One-line if/else

Great for simple yes/no choices in one line.

```js
// Syntax: condition ? "if true" : "if false"

let age = 20;
let status = age >= 18 ? "Adult" : "Minor";
console.log(status); // "Adult"

// Instead of:
let status2;
if (age >= 18) {
  status2 = "Adult";
} else {
  status2 = "Minor";
}
```

**Only use ternary for simple cases.** If the logic gets complicated, write a proper `if/else` — don't be clever at the cost of readability.

### 4.6 Truthy and Falsy — What counts as "true"?

In a condition, JavaScript converts the value to true or false. Some values are naturally "false-ish":

**Falsy values** (treated as `false` in conditions):
```js
false
0
""          // empty string
null
undefined
NaN
```

**Everything else is truthy** (treated as `true`).

```js
let username = "";

if (username) {
  console.log("Welcome, " + username);
} else {
  console.log("Please enter a username."); // This runs — empty string is falsy
}
```

```js
let items = [1, 2, 3];

if (items.length) {
  console.log("You have items!"); // runs — 3 is truthy
}
```

---

## Chapter 5 — Putting It Together: Small Practice Programs

### Practice 1 — Grade Calculator

```js
let marks = 85;
let subject = "Maths";

if (marks >= 90) {
  console.log(`${subject}: Distinction`);
} else if (marks >= 75) {
  console.log(`${subject}: First Class`);  // This runs
} else if (marks >= 60) {
  console.log(`${subject}: Second Class`);
} else {
  console.log(`${subject}: Fail`);
}
```

### Practice 2 — Basic Calculator

```js
let num1 = 15;
let num2 = 4;
let operator = "+";

let result;

if (operator === "+") {
  result = num1 + num2;
} else if (operator === "-") {
  result = num1 - num2;
} else if (operator === "*") {
  result = num1 * num2;
} else if (operator === "/") {
  result = num1 / num2;
} else {
  result = "Unknown operator";
}

console.log(`${num1} ${operator} ${num2} = ${result}`);
// Output: 15 + 4 = 19
```

### Practice 3 — Odd or Even

```js
let number = 17;

if (number % 2 === 0) {
  console.log(`${number} is Even`);
} else {
  console.log(`${number} is Odd`); // This runs
}
```

---

## Chapter 6 — Common Beginner Mistakes

```js
// ❌ Using = instead of === in conditions
if (age = 18) { }  // This assigns 18 to age! Not a comparison.
if (age === 18) { } // ✅ This compares

// ❌ Forgetting quotes around strings
let name = Priya;  // ❌ Error — JS thinks Priya is a variable
let name = "Priya"; // ✅

// ❌ Forgetting break in switch
switch(x) {
  case 1:
    console.log("one"); // falls through to case 2!
  case 2:
    console.log("two");
}

// ❌ Using == instead of ===
if (score == "10") { } // might work but unsafe
if (score === 10)  { } // ✅ correct and clear

// ❌ Typos in variable names (JS is case-sensitive)
let myScore = 100;
console.log(myscore); // ❌ ReferenceError — not the same as myScore
console.log(myScore); // ✅
```

---

## Day 1 Cheat Sheet

```
Setup:        node --version → check Node | node filename.js → run file
Print:        console.log("hello")

Variables:    const (won't change) | let (will change) | forget var
Types:        number, string, boolean, null, undefined

Operators:
  Math:       + - * / % **
  Update:     += -= *= /= ++ --
  Compare:    === !== > < >= <=   ← always use === not ==
  Logic:      && (AND)  || (OR)  ! (NOT)

Conditionals:
  if (condition) { }
  if (condition) { } else { }
  if (cond1) { } else if (cond2) { } else { }
  switch (value) { case x: ... break; }
  condition ? "yes" : "no"   ← ternary

Falsy values: false, 0, "", null, undefined, NaN
Everything else is truthy.
```

---