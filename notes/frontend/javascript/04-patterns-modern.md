# JavaScript — Day 4: Modules, Design Patterns, Performance & Modern Features

---

## 1. ES Modules

ES Modules are the standard module system in modern JavaScript (ES6+).

### Named exports

```js
// math.js
export const PI = 3.14159;

export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}
```

```js
// main.js
import { add, subtract, PI } from "./math.js";
import { add as sum } from "./math.js"; // alias
import * as math from "./math.js";      // namespace import

math.add(1, 2);
math.PI;
```

### Default exports

```js
// user.js
export default class User {
  constructor(name) {
    this.name = name;
  }
}

// main.js
import User from "./user.js"; // any name, no braces
import MyUser from "./user.js"; // also valid
```

### Re-exporting (barrel files)

```js
// index.js — re-export from multiple modules
export { add, subtract } from "./math.js";
export { default as User } from "./user.js";
export * from "./utils.js";

// consumers import from one place
import { add, User } from "./index.js";
```

### Dynamic imports

```js
// Load a module only when needed
async function loadChart() {
  const { Chart } = await import("./chart.js");
  return new Chart();
}

// Code splitting in bundlers
button.addEventListener("click", async () => {
  const module = await import("./heavyModule.js");
  module.doThing();
});
```

### Module characteristics

- Always strict mode
- Top-level `this` is `undefined`
- Execute once — cached after first import
- Loaded asynchronously in browsers
- Use `.mjs` extension or `"type": "module"` in `package.json` for Node

---

## 2. Design Patterns

Design patterns are proven solutions to recurring problems.

### Module Pattern (pre-ES6)

Encapsulates private state using closures and IIFE.

```js
const ShoppingCart = (() => {
  let items = []; // private

  return {
    addItem(item) {
      items.push(item);
    },
    removeItem(id) {
      items = items.filter(i => i.id !== id);
    },
    getTotal() {
      return items.reduce((sum, i) => sum + i.price, 0);
    },
    getItems() {
      return [...items]; // return copy, not reference
    }
  };
})();

ShoppingCart.addItem({ id: 1, name: "Book", price: 299 });
ShoppingCart.getTotal(); // 299
ShoppingCart.items;      // undefined — private
```

### Singleton Pattern

Ensures only one instance of a class exists.

```js
class Config {
  static #instance = null;
  #settings = {};

  constructor() {
    if (Config.#instance) return Config.#instance;
    Config.#instance = this;
  }

  set(key, value) { this.#settings[key] = value; }
  get(key) { return this.#settings[key]; }
}

const config1 = new Config();
const config2 = new Config();
config1 === config2; // true — same instance
```

**Use case:** Database connections, global config, loggers.

### Observer Pattern (Pub/Sub)

Objects subscribe to events and get notified when they happen.

**Analogy:** A newspaper subscription. The newspaper (publisher) doesn't know who reads it. Subscribers sign up and receive every new edition. They can also unsubscribe.

```js
class EventEmitter {
  #events = {};

  on(event, listener) {
    if (!this.#events[event]) this.#events[event] = [];
    this.#events[event].push(listener);
    return () => this.off(event, listener); // returns unsubscribe fn
  }

  off(event, listener) {
    this.#events[event] = this.#events[event]?.filter(l => l !== listener);
  }

  emit(event, ...args) {
    this.#events[event]?.forEach(listener => listener(...args));
  }

  once(event, listener) {
    const wrapper = (...args) => {
      listener(...args);
      this.off(event, wrapper);
    };
    this.on(event, wrapper);
  }
}

const emitter = new EventEmitter();

const unsubscribe = emitter.on("data", (payload) => {
  console.log("Received:", payload);
});

emitter.emit("data", { id: 1 }); // Received: { id: 1 }
unsubscribe(); // cleanup
emitter.emit("data", { id: 2 }); // nothing — unsubscribed
```

### Factory Pattern

Creates objects without specifying the exact class.

```js
function createUser(type, name) {
  const base = { name, createdAt: Date.now() };

  const roles = {
    admin: { ...base, role: "admin", canDelete: true, canWrite: true },
    editor: { ...base, role: "editor", canDelete: false, canWrite: true },
    viewer: { ...base, role: "viewer", canDelete: false, canWrite: false }
  };

  if (!roles[type]) throw new Error(`Unknown user type: ${type}`);
  return roles[type];
}

const admin = createUser("admin", "Alice");
const viewer = createUser("viewer", "Bob");
```

### Strategy Pattern

Define a family of algorithms, encapsulate each one, and make them interchangeable.

```js
const sortStrategies = {
  bubble(arr) { /* bubble sort */ },
  quick(arr) { /* quick sort */ },
  merge(arr) { /* merge sort */ }
};

class Sorter {
  #strategy;

  constructor(strategy = "quick") {
    this.#strategy = sortStrategies[strategy];
  }

  setStrategy(strategy) {
    this.#strategy = sortStrategies[strategy];
  }

  sort(arr) {
    return this.#strategy([...arr]);
  }
}

const sorter = new Sorter("quick");
sorter.sort([3, 1, 2]);

sorter.setStrategy("merge"); // swap algorithm at runtime
```

### Proxy Pattern

Intercept and customize operations on an object.

```js
const validator = {
  set(target, prop, value) {
    if (prop === "age") {
      if (typeof value !== "number") throw new TypeError("Age must be a number");
      if (value < 0 || value > 150) throw new RangeError("Age out of range");
    }
    target[prop] = value;
    return true; // must return true for set
  },
  get(target, prop) {
    return prop in target ? target[prop] : `Property "${prop}" not found`;
  }
};

const user = new Proxy({}, validator);
user.age = 25;    // ✅
user.age = -5;    // RangeError
user.name = "Al"; // ✅
user.nonexistent; // Property "nonexistent" not found
```

---

## 3. Functional Programming Concepts

### Pure functions

A pure function always returns the same output for the same input and has no side effects.

```js
// Impure — depends on external state, has side effect
let tax = 0.18;
function getTotal(price) {
  console.log("computing"); // side effect
  return price + price * tax; // depends on external `tax`
}

// Pure
function getTotal(price, taxRate) {
  return price + price * taxRate;
}

getTotal(100, 0.18); // Always 118
```

### Function composition

Combine small functions into larger ones.

```js
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe    = (...fns) => x => fns.reduce((acc, fn) => fn(acc), x);

const double = x => x * 2;
const addTen = x => x + 10;
const square = x => x * x;

// compose: right to left
const transform = compose(square, addTen, double);
transform(3); // square(addTen(double(3))) = square(16) = 256

// pipe: left to right (more readable)
const transform2 = pipe(double, addTen, square);
transform2(3); // same result
```

### Currying

Transform a function with multiple arguments into a series of single-argument functions.

**Analogy:** Ordering a custom burger. Instead of specifying everything at once, you choose the bun, then the patty, then toppings — each step returns a "partially configured burger" until it's complete.

```js
// Manual curry
function add(a) {
  return function (b) {
    return a + b;
  };
}
const add5 = add(5);
add5(3); // 8
add5(10); // 15

// Auto-curry helper
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return function (...moreArgs) {
      return curried.apply(this, args.concat(moreArgs));
    };
  };
}

const curriedAdd = curry((a, b, c) => a + b + c);
curriedAdd(1)(2)(3);    // 6
curriedAdd(1, 2)(3);    // 6
curriedAdd(1)(2, 3);    // 6
curriedAdd(1, 2, 3);    // 6
```

### Immutability

```js
// Avoid mutating — return new values instead
const updateUser = (user, updates) => ({ ...user, ...updates });
const addItem = (arr, item) => [...arr, item];
const removeItem = (arr, id) => arr.filter(item => item.id !== id);

// Object.freeze for shallow immutability
const config = Object.freeze({ db: "postgres", port: 5432 });
config.port = 3000; // silently fails
```

---

## 4. Performance Patterns

### Lazy evaluation

Don't compute until needed.

```js
class LazyValue {
  #factory;
  #value;
  #computed = false;

  constructor(factory) {
    this.#factory = factory;
  }

  get value() {
    if (!this.#computed) {
      this.#value = this.#factory();
      this.#computed = true;
    }
    return this.#value;
  }
}

const heavy = new LazyValue(() => {
  console.log("Computing...");
  return expensiveComputation();
});

heavy.value; // Computing... [computed]
heavy.value; // [returns cached]
```

### Memoization

Cache results of expensive function calls.

```js
function memoize(fn) {
  const cache = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

const fibonacci = memoize(function (n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
});

fibonacci(40); // Fast — O(n) instead of O(2^n)
```

### Object pooling

Reuse objects instead of creating/destroying them (reduces GC pressure).

```js
class ObjectPool {
  #pool = [];
  #factory;

  constructor(factory) {
    this.#factory = factory;
  }

  acquire() {
    return this.#pool.length > 0 ? this.#pool.pop() : this.#factory();
  }

  release(obj) {
    this.#pool.push(obj);
  }
}

const pool = new ObjectPool(() => ({ x: 0, y: 0, active: false }));

const particle = pool.acquire();
particle.x = 100;
// ... use it ...
pool.release(particle); // return to pool for reuse
```

---

## 5. Proxy and Reflect

### Proxy traps

```js
const handler = {
  get(target, prop, receiver) {
    console.log(`Getting ${prop}`);
    return Reflect.get(target, prop, receiver);
  },
  set(target, prop, value, receiver) {
    console.log(`Setting ${prop} = ${value}`);
    return Reflect.set(target, prop, value, receiver);
  },
  has(target, prop) {
    return prop in target;
  },
  deleteProperty(target, prop) {
    console.log(`Deleting ${prop}`);
    return Reflect.deleteProperty(target, prop);
  },
  apply(target, thisArg, args) {
    console.log(`Calling with args: ${args}`);
    return Reflect.apply(target, thisArg, args);
  }
};

const obj = new Proxy({ name: "Alice" }, handler);
obj.name;        // Getting name
obj.age = 30;    // Setting age = 30
```

### Reactive data with Proxy

```js
function reactive(target, onChange) {
  return new Proxy(target, {
    set(obj, prop, value) {
      const old = obj[prop];
      obj[prop] = value;
      if (old !== value) onChange(prop, value, old);
      return true;
    }
  });
}

const state = reactive({ count: 0 }, (key, newVal, oldVal) => {
  console.log(`${key}: ${oldVal} → ${newVal}`);
});

state.count = 1; // count: 0 → 1
state.count = 2; // count: 1 → 2
```

---

## 6. Memory Management

JavaScript uses automatic **garbage collection** (mark-and-sweep algorithm).

### Memory leaks — common causes

**1. Forgotten event listeners**
```js
// ❌ Leak — listener added every render, never removed
function setupButton() {
  document.getElementById("btn").addEventListener("click", handler);
}

// ✅ Keep reference and remove when done
const btn = document.getElementById("btn");
btn.addEventListener("click", handler);
// Cleanup:
btn.removeEventListener("click", handler);
```

**2. Closures holding references**
```js
function createLeak() {
  const bigData = new Array(1000000).fill("data");
  return function () {
    // This closure captures bigData forever
    console.log(bigData.length);
  };
}
```

**3. Detached DOM nodes**
```js
let detached;
function createNode() {
  detached = document.createElement("div");
  document.body.appendChild(detached);
  document.body.removeChild(detached);
  // 'detached' still in memory because JS variable holds reference
}

// Fix: detached = null; when done
```

**4. Growing caches without limit**
```js
// ❌ Unlimited growth
const cache = {};
function memoize(key, fn) {
  cache[key] = fn(); // grows forever
  return cache[key];
}

// ✅ Use WeakMap — GC handles cleanup
const cache = new WeakMap();
```

---

## 7. Modern JavaScript Features

### Optional Chaining + Nullish Coalescing (patterns)

```js
// Real-world combined usage
const displayName = user?.profile?.displayName ?? user?.name ?? "Anonymous";
const theme = config?.ui?.theme?.color ?? "blue";
```

### Logical Assignment Operators (ES2021)

```js
// ||=  — assign if left side is falsy
let name = "";
name ||= "Default"; // name = "Default"

// &&=  — assign if left side is truthy
let user = { name: "Alice" };
user &&= { ...user, active: true }; // assigns only if user is truthy

// ??=  — assign if left side is null/undefined
let config = null;
config ??= { theme: "light" }; // assigns only if null or undefined
```

### Array and Object at rest (2022+)

```js
// Array.at() — negative indexing
const arr = [1, 2, 3, 4, 5];
arr.at(-1);  // 5  (last)
arr.at(-2);  // 4  (second to last)
arr.at(0);   // 1

// Object.hasOwn() — safer than hasOwnProperty
Object.hasOwn({ a: 1 }, "a");  // true
Object.hasOwn({ a: 1 }, "toString"); // false (inherited)
```

### `structuredClone` (2022)

```js
const original = {
  name: "Alice",
  scores: [1, 2, 3],
  date: new Date()
};

const clone = structuredClone(original);
clone.scores.push(4);
original.scores; // [1, 2, 3] — unaffected
clone.date instanceof Date; // true — Date preserved (unlike JSON.parse)
```

### Top-level await (ES2022, in modules)

```js
// In a .mjs file or type="module" script
const data = await fetch("/api/config").then(r => r.json());
export const config = data;
```

### `Promise.withResolvers` (ES2024)

```js
// Old way — resolver/reject functions trapped in constructor
let resolve, reject;
const promise = new Promise((res, rej) => {
  resolve = res;
  reject = rej;
});

// New way
const { promise, resolve, reject } = Promise.withResolvers();
setTimeout(() => resolve("done"), 1000);
await promise; // "done"
```

---

## 8. Regular Expressions

```js
const pattern = /hello/i;    // Literal, case-insensitive
const pattern2 = new RegExp("hello", "i"); // Constructor form

// Test
/\d+/.test("abc123");        // true
/^\d+$/.test("abc123");      // false — must be all digits

// Match
"hello world".match(/\w+/g); // ["hello", "world"]

// Named capture groups
const datePattern = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
const { groups } = "2024-01-15".match(datePattern);
groups.year;  // "2024"
groups.month; // "01"
groups.day;   // "15"

// Replace
"hello world".replace(/world/, "JS");           // "hello JS"
"aabbcc".replace(/(.)\1/g, "$1");               // "abc" — deduplicate
"2024-01-15".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"); // "15/01/2024"

// Split
"one, two,  three".split(/,\s*/); // ["one", "two", "three"]

// Lookahead and lookbehind
/\d+(?= dollars)/.exec("100 dollars");   // "100" (followed by " dollars")
/(?<=\$)\d+/.exec("$100");               // "100" (preceded by "$")
```

---

## 9. Metaprogramming

### Reflect API

```js
// Reflect mirrors Proxy traps — use in handlers for default behavior
const handler = {
  get(target, key) {
    if (key === "secret") return "🔒";
    return Reflect.get(target, key); // default behavior
  }
};

const obj = new Proxy({ name: "Alice", secret: "password" }, handler);
obj.name;   // "Alice"
obj.secret; // "🔒"
```

### Property descriptors

```js
const obj = {};

Object.defineProperty(obj, "PI", {
  value: 3.14159,
  writable: false,   // cannot change value
  enumerable: false, // won't show in for...in or Object.keys
  configurable: false // cannot redefine or delete
});

Object.defineProperties(obj, {
  firstName: { value: "Alice", writable: true, enumerable: true, configurable: true },
  lastName:  { value: "Smith", writable: true, enumerable: true, configurable: true }
});

Object.getOwnPropertyDescriptor(obj, "PI");
// { value: 3.14159, writable: false, enumerable: false, configurable: false }
```

---

## 10. Interview-Level Patterns and Questions

### Implement `Promise.all` from scratch

```js
function myPromiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let remaining = promises.length;

    if (remaining === 0) return resolve([]);

    promises.forEach((promise, i) => {
      Promise.resolve(promise).then((value) => {
        results[i] = value;
        remaining--;
        if (remaining === 0) resolve(results);
      }).catch(reject);
    });
  });
}
```

### Implement `debounce` from scratch

```js
function debounce(fn, delay) {
  let timer = null;

  const debounced = function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
      timer = null;
    }, delay);
  };

  debounced.cancel = () => {
    clearTimeout(timer);
    timer = null;
  };

  return debounced;
}
```

### Deep equal comparison

```js
function deepEqual(a, b) {
  if (a === b) return true;
  if (a === null || b === null) return false;
  if (typeof a !== typeof b) return false;

  if (Array.isArray(a)) {
    if (!Array.isArray(b) || a.length !== b.length) return false;
    return a.every((item, i) => deepEqual(item, b[i]));
  }

  if (typeof a === "object") {
    const keysA = Object.keys(a);
    const keysB = Object.keys(b);
    if (keysA.length !== keysB.length) return false;
    return keysA.every(key => deepEqual(a[key], b[key]));
  }

  return false;
}
```

### Flatten object

```js
function flattenObject(obj, prefix = "", result = {}) {
  for (const key in obj) {
    const fullKey = prefix ? `${prefix}.${key}` : key;
    if (typeof obj[key] === "object" && obj[key] !== null && !Array.isArray(obj[key])) {
      flattenObject(obj[key], fullKey, result);
    } else {
      result[fullKey] = obj[key];
    }
  }
  return result;
}

flattenObject({ a: { b: { c: 1 } }, d: 2 });
// { "a.b.c": 1, "d": 2 }
```

---

## Quick Reference Cheatsheet — Day 4

```
Modules:
  named export → import { name } from "./file"
  default export → import Name from "./file"
  dynamic import → const m = await import("./file")

Design Patterns:
  Module    → IIFE + closures for private state
  Singleton → one instance (static #instance)
  Observer  → on/emit/off for event-driven code
  Factory   → create objects by type/config
  Strategy  → swappable algorithms
  Proxy     → intercept object operations

Functional:
  Pure functions → same input → same output, no side effects
  Compose   → right to left | Pipe → left to right
  Curry     → fn(a)(b)(c) instead of fn(a,b,c)
  Immutability → return new, don't mutate

Memory leaks:
  Remove event listeners | Null out references
  Use WeakMap for caches | Avoid detached DOM nodes

Modern:
  structuredClone() → deep clone with Date/Map/Set support
  Array.at(-1)      → last element
  Object.hasOwn()   → safer than hasOwnProperty
  ??= &&= ||=       → logical assignment (ES2021)
  Promise.withResolvers() → ES2024
```