# JavaScript — Day 1: Foundations, Types, Scope & Closures

---

## 1. How JavaScript Executes Code

JavaScript is **single-threaded** and uses a **call stack** to manage execution. Before any code runs, the JS engine does two things:

1. **Memory creation phase** — variables are allocated (`undefined`), functions are stored in full.
2. **Execution phase** — code runs line by line.

```js
console.log(a); // undefined (not ReferenceError)
var a = 10;
console.log(a); // 10
```

This is **hoisting** — declarations are lifted to the top of their scope during the memory phase.

---

## 2. Data Types

### Primitives (passed by value)

| Type        | Example                    |
|-------------|----------------------------|
| `number`    | `42`, `3.14`, `NaN`, `Infinity` |
| `string`    | `"hello"`, `` `world` ``   |
| `boolean`   | `true`, `false`            |
| `null`      | `null`                     |
| `undefined` | `undefined`                |
| `symbol`    | `Symbol('id')`             |
| `bigint`    | `9007199254740991n`        |

### Objects (passed by reference)

Everything else — arrays, functions, objects, dates, regex.

```js
// Primitives: copy by value
let a = 5;
let b = a;
b = 99;
console.log(a); // 5 — unchanged

// Objects: copy by reference
let obj1 = { x: 1 };
let obj2 = obj1;
obj2.x = 99;
console.log(obj1.x); // 99 — mutated!
```

**Analogy:** Primitives are like handing someone a photocopy of a document. Objects are like handing them a key to a shared locker.

---

## 3. `typeof` Quirks

```js
typeof 42           // "number"
typeof "hello"      // "string"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object"   ← famous bug, never fixed
typeof {}           // "object"
typeof []           // "object"
typeof function(){} // "function"
typeof Symbol()     // "symbol"
typeof 1n           // "bigint"
```

To check for `null`:
```js
value === null // only reliable way
```

To check for array:
```js
Array.isArray([1, 2, 3]); // true
```

---

## 4. Type Coercion

JS converts types automatically in certain situations. This is a major source of bugs.

### Implicit coercion

```js
"5" + 3        // "53"  — number coerced to string
"5" - 3        // 2     — string coerced to number
"5" * "3"      // 15
true + 1       // 2
false + 1      // 1
null + 1       // 1
undefined + 1  // NaN
[] + []        // ""
[] + {}        // "[object Object]"
{} + []        // 0  (in some contexts)
```

### `==` vs `===`

`==` performs type coercion. `===` does not.

```js
0 == false    // true
0 === false   // false
null == undefined   // true
null === undefined  // false
NaN == NaN    // false  ← NaN is never equal to itself
```

**Rule:** Always use `===` unless you explicitly want coercion.

---

## 5. `var`, `let`, `const`

| Feature          | `var`        | `let`        | `const`      |
|------------------|--------------|--------------|--------------|
| Scope            | Function     | Block        | Block        |
| Hoisted          | Yes (undefined) | Yes (TDZ) | Yes (TDZ)  |
| Re-declarable    | Yes          | No           | No           |
| Re-assignable    | Yes          | Yes          | No           |

### Temporal Dead Zone (TDZ)

`let` and `const` are hoisted but not initialized. Accessing them before their declaration throws a `ReferenceError`.

```js
console.log(x); // ReferenceError: Cannot access 'x' before initialization
let x = 5;
```

**Analogy:** `var` is a whiteboard that's wiped clean (set to `undefined`) before class starts. `let`/`const` are locked lockers — they exist, but you can't open them until you get the key (declaration line).

```js
// Classic var trap in loops
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 3, 3, 3

// Fix with let
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 0, 1, 2
```

---

## 6. Scope

Scope defines where a variable is accessible.

### Types of scope

- **Global scope** — accessible everywhere
- **Function scope** — accessible only inside the function
- **Block scope** — accessible only inside `{}` (with `let`/`const`)
- **Module scope** — accessible only in the module

```js
let globalVar = "I'm global";

function outer() {
  let outerVar = "I'm in outer";

  function inner() {
    let innerVar = "I'm in inner";
    console.log(globalVar); // ✅
    console.log(outerVar);  // ✅
    console.log(innerVar);  // ✅
  }

  console.log(innerVar); // ❌ ReferenceError
}
```

### Scope chain

When JS looks up a variable, it searches the current scope, then the outer scope, then further out — all the way to global. This chain is called the **scope chain**.

**Analogy:** Imagine you're in a room inside a house inside a neighborhood. If you need a tool, you check your room first. Not there? Check the house. Not there? Check the neighborhood. This lookup chain is the scope chain.

---

## 7. Closures

A **closure** is a function that remembers the variables from its outer scope even after that scope has finished executing.

```js
function makeCounter() {
  let count = 0;

  return function () {
    count++;
    return count;
  };
}

const counter = makeCounter();
counter(); // 1
counter(); // 2
counter(); // 3
```

`count` is captured by the inner function. Even after `makeCounter()` returns, the inner function has a reference to `count` in its closure.

**Analogy:** A closure is like a backpack. When you leave a place (the outer function finishes), you still carry the backpack (closed-over variables) with you.

### Practical use cases

**1. Data privacy (module pattern)**
```js
function createBankAccount(initialBalance) {
  let balance = initialBalance; // private

  return {
    deposit(amount) { balance += amount; },
    withdraw(amount) { balance -= amount; },
    getBalance() { return balance; }
  };
}

const account = createBankAccount(1000);
account.deposit(500);
console.log(account.getBalance()); // 1500
console.log(account.balance);      // undefined — can't access directly
```

**2. Memoization**
```js
function memoize(fn) {
  const cache = {};
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache[key] !== undefined) return cache[key];
    cache[key] = fn(...args);
    return cache[key];
  };
}

const expensiveAdd = memoize((a, b) => {
  console.log("Computing...");
  return a + b;
});

expensiveAdd(2, 3); // Computing... 5
expensiveAdd(2, 3); // 5 (cached)
```

**3. Partial application**
```js
function multiply(factor) {
  return (number) => number * factor;
}

const double = multiply(2);
const triple = multiply(3);

double(5); // 10
triple(5); // 15
```

---

## 8. Hoisting in Depth

### `var` hoisting

```js
console.log(name); // undefined
var name = "Alice";
// Treated as:
// var name; ← hoisted
// console.log(name); // undefined
// name = "Alice";
```

### Function declaration hoisting

```js
greet(); // "Hello!" — works because the whole function is hoisted

function greet() {
  console.log("Hello!");
}
```

### Function expression — NOT hoisted

```js
greet(); // TypeError: greet is not a function

var greet = function () {
  console.log("Hello!");
};
```

The variable `greet` is hoisted as `undefined`, so calling it before assignment throws a TypeError.

---

## 9. IIFE — Immediately Invoked Function Expression

An IIFE runs immediately after it's defined. Used to create isolated scope (pre-ES6 modules).

```js
(function () {
  let secret = "hidden";
  console.log("Runs immediately");
})();

console.log(secret); // ReferenceError
```

Arrow function IIFE:
```js
(() => {
  console.log("Also an IIFE");
})();
```

---

## 10. `this` Keyword

`this` refers to the **execution context** — what object the function is running in the context of.

| Context                  | `this` value          |
|--------------------------|-----------------------|
| Global (non-strict)      | `window` / `global`   |
| Global (strict mode)     | `undefined`           |
| Object method            | The object            |
| Arrow function           | Inherits from outer   |
| Constructor (`new`)      | New instance          |
| `call`, `apply`, `bind`  | Manually set          |

```js
const person = {
  name: "Alice",
  greet() {
    console.log(`Hi, I'm ${this.name}`);
  }
};
person.greet(); // Hi, I'm Alice

const greet = person.greet;
greet(); // Hi, I'm undefined (lost context)
```

### Arrow functions and `this`

Arrow functions don't have their own `this`. They inherit it from the surrounding lexical scope.

```js
const obj = {
  name: "Alice",
  regularFn: function () {
    setTimeout(function () {
      console.log(this.name); // undefined — 'this' is window/undefined
    }, 100);
  },
  arrowFn: function () {
    setTimeout(() => {
      console.log(this.name); // "Alice" — arrow captures outer 'this'
    }, 100);
  }
};

obj.regularFn();
obj.arrowFn();
```

### `call`, `apply`, `bind`

```js
function introduce(greeting, punctuation) {
  console.log(`${greeting}, I'm ${this.name}${punctuation}`);
}

const user = { name: "Bob" };

introduce.call(user, "Hello", "!");     // Hello, I'm Bob!
introduce.apply(user, ["Hey", "..."]);  // Hey, I'm Bob...

const boundFn = introduce.bind(user, "Hi");
boundFn("?"); // Hi, I'm Bob?
```

**`call`** — invoke immediately, args spread
**`apply`** — invoke immediately, args as array
**`bind`** — returns new function with fixed `this`

---

## 11. Strict Mode

```js
"use strict";

x = 10; // ReferenceError: x is not defined

function fn() {
  console.log(this); // undefined (not window)
}

// Prevents:
// - undeclared variables
// - deleting variables/functions
// - duplicate parameter names
// - writing to read-only properties
```

ES6 modules are strict by default.

---

## 12. Nullish Coalescing & Optional Chaining

### `??` — Nullish Coalescing

Returns the right side only if the left side is `null` or `undefined` (not falsy).

```js
const name = null ?? "Default";     // "Default"
const age = 0 ?? 25;                // 0  ← 0 is not null/undefined
const score = undefined ?? 100;     // 100

// vs ||
const age2 = 0 || 25;              // 25  ← 0 is falsy
```

### `?.` — Optional Chaining

Safely access nested properties without throwing if an intermediate value is null/undefined.

```js
const user = {
  profile: {
    address: {
      city: "Mumbai"
    }
  }
};

console.log(user?.profile?.address?.city);   // "Mumbai"
console.log(user?.settings?.theme);          // undefined (no error)
console.log(user?.getName?.());              // undefined (no error)
```

---

## Quick Reference Cheatsheet — Day 1

```
Primitives       → value copy    | Objects → reference copy
typeof null      → "object"      | NaN !== NaN
== coerces       → use ===       | TDZ for let/const
var → function scope | let/const → block scope
Hoisting: var=undefined, function=full, let/const=TDZ
Closure = function + its outer scope's variables
this = depends on call site (arrow fn inherits lexically)
?? checks null/undefined | ?. prevents property access errors
```