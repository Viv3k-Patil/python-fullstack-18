# JavaScript — Day 2: Functions, Arrays, Objects & Prototypes

---

## 1. Functions — Every Variation

### Function Declaration
```js
function add(a, b) {
  return a + b;
}
```
Hoisted fully. Can be called before declaration.

### Function Expression
```js
const add = function (a, b) {
  return a + b;
};
```
Not hoisted. Stored in variable.

### Arrow Function
```js
const add = (a, b) => a + b;

// With body
const greet = (name) => {
  const msg = `Hello, ${name}`;
  return msg;
};

// Single param — no parens needed
const double = n => n * 2;

// No params
const greet = () => "Hello!";
```

Arrow functions:
- No `this`, `arguments`, `super`, or `new.target`
- Cannot be used as constructors
- Best for callbacks and short functions

### Default Parameters
```js
function greet(name = "World", greeting = "Hello") {
  return `${greeting}, ${name}!`;
}

greet();              // "Hello, World!"
greet("Alice");       // "Hello, Alice!"
greet("Bob", "Hey");  // "Hey, Bob!"
```

### Rest Parameters
Collects remaining arguments into an array.

```js
function sum(...numbers) {
  return numbers.reduce((acc, n) => acc + n, 0);
}

sum(1, 2, 3, 4); // 10
```

### Spread Operator
Expands an array into individual elements.

```js
const nums = [1, 2, 3];
Math.max(...nums); // 3

function add(a, b, c) { return a + b + c; }
add(...nums); // 6

const merged = [...[1, 2], ...[3, 4]]; // [1, 2, 3, 4]
```

**Analogy:** Rest is a funnel — many arguments pour into one array. Spread is the opposite — one array fans out into many arguments.

---

## 2. Higher-Order Functions

A **higher-order function** is a function that takes another function as an argument or returns one.

```js
// Takes a function
function applyTwice(fn, value) {
  return fn(fn(value));
}
applyTwice(x => x * 2, 3); // 12

// Returns a function
function multiplier(factor) {
  return n => n * factor;
}
const triple = multiplier(3);
triple(5); // 15
```

---

## 3. Array Methods — The Core Toolkit

All these methods are **pure** — they don't mutate the original array.

### `map` — Transform each element

```js
const nums = [1, 2, 3, 4];
const doubled = nums.map(n => n * 2);
// [2, 4, 6, 8]

const users = [{ name: "Alice" }, { name: "Bob" }];
const names = users.map(u => u.name);
// ["Alice", "Bob"]
```

### `filter` — Keep elements that pass a test

```js
const nums = [1, 2, 3, 4, 5, 6];
const evens = nums.filter(n => n % 2 === 0);
// [2, 4, 6]

const adults = users.filter(u => u.age >= 18);
```

### `reduce` — Collapse array to a single value

**Analogy:** `reduce` is like a snowball rolling downhill — it starts small (initial value) and accumulates as it rolls through the array.

```js
const nums = [1, 2, 3, 4, 5];

const sum = nums.reduce((acc, n) => acc + n, 0);
// 15

const product = nums.reduce((acc, n) => acc * n, 1);
// 120

// Flatten with reduce
const nested = [[1, 2], [3, 4], [5]];
const flat = nested.reduce((acc, arr) => [...acc, ...arr], []);
// [1, 2, 3, 4, 5]

// Group by
const people = [
  { name: "Alice", dept: "Engineering" },
  { name: "Bob", dept: "Design" },
  { name: "Carol", dept: "Engineering" }
];

const byDept = people.reduce((acc, person) => {
  const key = person.dept;
  acc[key] = acc[key] || [];
  acc[key].push(person);
  return acc;
}, {});
// { Engineering: [...], Design: [...] }
```

### `find` and `findIndex`

```js
const users = [{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }];

users.find(u => u.id === 2);      // { id: 2, name: "Bob" }
users.findIndex(u => u.id === 2); // 1
```

### `some` and `every`

```js
const nums = [1, 2, 3, 4, 5];

nums.some(n => n > 4);  // true  — at least one passes
nums.every(n => n > 0); // true  — all pass
nums.every(n => n > 3); // false — not all pass
```

### `flat` and `flatMap`

```js
[1, [2, [3, [4]]]].flat();    // [1, 2, [3, [4]]]
[1, [2, [3, [4]]]].flat(Infinity); // [1, 2, 3, 4]

// flatMap = map + flat(1)
const sentences = ["hello world", "foo bar"];
sentences.flatMap(s => s.split(" "));
// ["hello", "world", "foo", "bar"]
```

### Mutating methods (use carefully)

```js
const arr = [1, 2, 3];

arr.push(4);       // [1, 2, 3, 4] — add to end
arr.pop();         // removes last
arr.unshift(0);    // add to start
arr.shift();       // remove from start
arr.splice(1, 2);  // remove 2 elements at index 1
arr.sort();        // sorts in-place (lexicographic by default!)
arr.reverse();     // reverses in-place
```

### Sorting correctly

```js
// ❌ Wrong — sorts as strings
[10, 1, 21, 2].sort(); // [1, 10, 2, 21]

// ✅ Correct — numeric sort
[10, 1, 21, 2].sort((a, b) => a - b); // [1, 2, 10, 21]

// Sort objects
const users = [{ age: 30 }, { age: 22 }, { age: 25 }];
users.sort((a, b) => a.age - b.age);
```

---

## 4. Destructuring

### Array destructuring

```js
const [a, b, c] = [1, 2, 3];
// a=1, b=2, c=3

// Skip elements
const [first, , third] = [1, 2, 3];

// Rest
const [head, ...tail] = [1, 2, 3, 4];
// head=1, tail=[2,3,4]

// Default values
const [x = 0, y = 0] = [10];
// x=10, y=0

// Swap variables
let p = 1, q = 2;
[p, q] = [q, p];
```

### Object destructuring

```js
const user = { name: "Alice", age: 30, city: "Mumbai" };

const { name, age } = user;

// Rename while destructuring
const { name: userName, age: userAge } = user;

// Default values
const { score = 100, level = 1 } = user;

// Nested destructuring
const { address: { city, zip } } = { address: { city: "Pune", zip: "411001" } };

// Rest
const { name: n, ...rest } = user;
// n = "Alice", rest = { age: 30, city: "Mumbai" }
```

### In function parameters

```js
function display({ name, age = 0, role = "user" }) {
  console.log(`${name} (${age}) — ${role}`);
}

display({ name: "Alice", age: 30 }); // Alice (30) — user
```

---

## 5. Objects — Deep Dive

### Shorthand syntax

```js
const name = "Alice";
const age = 30;

// Old
const user = { name: name, age: age };

// Shorthand
const user = { name, age };
```

### Computed property names

```js
const key = "dynamicKey";
const obj = {
  [key]: "value",
  [`${key}_extra`]: "extra"
};
// { dynamicKey: "value", dynamicKey_extra: "extra" }
```

### Object spread and `Object.assign`

```js
const defaults = { theme: "light", lang: "en" };
const userPrefs = { theme: "dark" };

const config = { ...defaults, ...userPrefs };
// { theme: "dark", lang: "en" }  — right side wins

// Deep clone? No! Spread is SHALLOW
const original = { a: { b: 1 } };
const copy = { ...original };
copy.a.b = 99;
console.log(original.a.b); // 99 — still shared!
```

### Object methods

```js
const obj = { a: 1, b: 2, c: 3 };

Object.keys(obj);    // ["a", "b", "c"]
Object.values(obj);  // [1, 2, 3]
Object.entries(obj); // [["a",1], ["b",2], ["c",3]]

// Convert entries back to object
Object.fromEntries([["a", 1], ["b", 2]]); // { a: 1, b: 2 }

// Check property
"a" in obj;                    // true
obj.hasOwnProperty("a");      // true

// Freeze — prevent modification
const frozen = Object.freeze({ x: 1 });
frozen.x = 99; // silently fails (throws in strict mode)

// Seal — prevent add/delete, allow modify
const sealed = Object.seal({ x: 1 });
sealed.x = 99; // ✅ works
sealed.y = 2;  // ❌ fails
```

---

## 6. Prototypes — The Real Inheritance System

**Analogy:** Prototypes are like a family recipe book. You check your own book first. If the recipe isn't there, you borrow from your parent's book. If they don't have it either, you check their parent's book — all the way up to the original cookbook.

Every object in JavaScript has an internal link to another object called its **prototype**. When you access a property, JS walks up this chain.

```js
const animal = {
  breathe() {
    return "breathing";
  }
};

const dog = Object.create(animal);
dog.bark = function () { return "woof"; };

dog.bark();    // "woof"    — found on dog
dog.breathe(); // "breathing" — found on animal (prototype)

Object.getPrototypeOf(dog) === animal; // true
```

### `prototype` vs `__proto__`

- `obj.__proto__` — the prototype of an instance (non-standard, but works)
- `Fn.prototype` — the object that will be set as `__proto__` for instances created by `new Fn()`

```js
function Person(name) {
  this.name = name;
}

Person.prototype.greet = function () {
  return `Hi, I'm ${this.name}`;
};

const alice = new Person("Alice");
alice.greet(); // "Hi, I'm Alice"

alice.__proto__ === Person.prototype; // true
Person.prototype.constructor === Person; // true
```

### Prototype chain

```js
alice.__proto__             // Person.prototype
alice.__proto__.__proto__   // Object.prototype
alice.__proto__.__proto__.__proto__ // null  ← end of chain
```

---

## 7. Classes — Syntactic Sugar over Prototypes

Classes don't change the underlying prototype system — they're just a cleaner syntax.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound.`;
  }

  toString() {
    return `Animal: ${this.name}`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Must call super before using 'this'
    this.breed = breed;
  }

  speak() {
    return `${this.name} barks!`;
  }
}

const dog = new Dog("Rex", "Labrador");
dog.speak();               // "Rex barks!"
dog instanceof Dog;        // true
dog instanceof Animal;     // true
```

### Static methods and properties

```js
class MathUtils {
  static PI = 3.14159;

  static circleArea(r) {
    return MathUtils.PI * r * r;
  }
}

MathUtils.circleArea(5); // 78.53...
// Static methods aren't on instances
new MathUtils().circleArea; // undefined
```

### Private fields (ES2022)

```js
class BankAccount {
  #balance; // private field

  constructor(initialBalance) {
    this.#balance = initialBalance;
  }

  deposit(amount) {
    this.#balance += amount;
  }

  get balance() {
    return this.#balance;
  }
}

const account = new BankAccount(1000);
account.deposit(500);
account.balance;  // 1500
account.#balance; // SyntaxError — truly private
```

### Getters and Setters

```js
class Temperature {
  #celsius;

  constructor(celsius) {
    this.#celsius = celsius;
  }

  get fahrenheit() {
    return this.#celsius * 9 / 5 + 32;
  }

  set fahrenheit(f) {
    this.#celsius = (f - 32) * 5 / 9;
  }
}

const temp = new Temperature(0);
temp.fahrenheit;      // 32
temp.fahrenheit = 212;
temp.fahrenheit;      // 212  (now 100°C internally)
```

---

## 8. Object Cloning — Shallow vs Deep

### Shallow clone

```js
const obj = { a: 1, b: { c: 2 } };

const clone1 = { ...obj };
const clone2 = Object.assign({}, obj);

clone1.a = 99;     // obj.a unchanged
clone1.b.c = 99;   // obj.b.c also changes! (shallow)
```

### Deep clone

```js
// Simple (loses functions, symbols, dates become strings)
const deep = JSON.parse(JSON.stringify(obj));

// Modern
const deep2 = structuredClone(obj); // ES2022 — handles more types
```

---

## 9. Map and Set

### `Map` — Key-value pairs with any key type

```js
const map = new Map();

map.set("name", "Alice");
map.set(42, "the answer");
map.set({ id: 1 }, "object key");

map.get("name");    // "Alice"
map.has(42);        // true
map.size;           // 3
map.delete(42);

// Iterate
for (const [key, value] of map) {
  console.log(key, value);
}

// From object
const obj = { a: 1, b: 2 };
const map2 = new Map(Object.entries(obj));
```

**When to use Map over Object:**
- Keys that aren't strings/symbols
- Need insertion-order guarantee
- Frequent add/delete operations
- Need `.size` quickly

### `Set` — Collection of unique values

```js
const set = new Set([1, 2, 3, 2, 1]);
// Set(3) { 1, 2, 3 } — duplicates removed

set.add(4);
set.has(3);    // true
set.delete(1);
set.size;      // 3

// Array from set
[...set]; // [2, 3, 4]

// Remove duplicates from array
const unique = [...new Set([1, 1, 2, 3, 3])];
// [1, 2, 3]

// Set operations
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);

const union = new Set([...a, ...b]);       // {1,2,3,4}
const intersection = new Set([...a].filter(x => b.has(x))); // {2,3}
const difference = new Set([...a].filter(x => !b.has(x)));  // {1}
```

### `WeakMap` and `WeakSet`

Hold **weak references** — if the key object has no other references, it can be garbage collected. Not iterable.

```js
const cache = new WeakMap();

function process(obj) {
  if (!cache.has(obj)) {
    cache.set(obj, expensiveComputation(obj));
  }
  return cache.get(obj);
}
// When obj is garbage collected, cache entry disappears automatically
```

---

## 10. Symbols

Symbols are unique, immutable primitive values — useful as unique property keys.

```js
const id = Symbol("id");
const id2 = Symbol("id");

id === id2; // false — always unique

const user = {
  [id]: 123,
  name: "Alice"
};

user[id];        // 123
user["id"];      // undefined — can't access with string
Object.keys(user); // ["name"] — symbols excluded
```

**Use case:** Library authors use symbols to add non-conflicting properties to objects they don't own.

---

## Quick Reference Cheatsheet — Day 2

```
map       → transform all      | filter → keep matching
reduce    → collapse to one    | find   → first match
some      → any passes?        | every  → all pass?
flat      → flatten nested     | flatMap → map + flat(1)

Destructuring:
  const { a, b } = obj     → object
  const [x, y] = arr       → array
  const { a: renamed } = obj  → rename
  const { a = default } = obj → default

Prototype chain: instance → Constructor.prototype → Object.prototype → null
class = syntactic sugar over prototypes
#field = truly private (ES2022)

Map  → any key type, ordered, has .size
Set  → unique values, fast .has()
WeakMap/WeakSet → garbage-collectible keys, no iteration

structuredClone(obj) → deep clone (ES2022)
```