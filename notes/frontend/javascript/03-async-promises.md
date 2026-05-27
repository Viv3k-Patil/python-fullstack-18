# JavaScript — Day 3: Async, Promises, Event Loop & Error Handling

---

## 1. The Event Loop — How Async Actually Works

JavaScript is **single-threaded** but handles async operations through the **event loop**.

**The key components:**

- **Call Stack** — Where JS executes code (one frame at a time)
- **Web APIs / Node APIs** — Browser/Node handles async work here (timers, fetch, events)
- **Callback Queue (Task Queue)** — Completed macro-task callbacks wait here
- **Microtask Queue** — Promise callbacks (`.then`, `.catch`) wait here — **higher priority**
- **Event Loop** — Continuously checks: "Is the call stack empty? If yes, move next task from queues."

**Priority:** Call Stack → Microtask Queue → Callback (Macro) Queue

```js
console.log("1");

setTimeout(() => console.log("2"), 0);

Promise.resolve().then(() => console.log("3"));

console.log("4");

// Output: 1, 4, 3, 2
```

**Why?** `1` and `4` run synchronously. `Promise.then` goes to the microtask queue. `setTimeout` goes to the macro-task queue. Microtasks run before macro-tasks.

**Analogy:** Imagine a restaurant kitchen. The chef (call stack) cooks one dish at a time. Orders come in (async tasks). The sous chef handles prep work (Web APIs). Completed hot dishes (microtasks/promises) skip ahead of regular takeout orders (setTimeout callbacks) and get served first.

```js
console.log("start");

setTimeout(() => console.log("timeout 1"), 0);
setTimeout(() => console.log("timeout 2"), 0);

Promise.resolve()
  .then(() => console.log("promise 1"))
  .then(() => console.log("promise 2")); // chained promise — also microtask

console.log("end");

// start → end → promise 1 → promise 2 → timeout 1 → timeout 2
```

---

## 2. Callbacks — The Original Async Pattern

```js
function fetchData(url, onSuccess, onError) {
  setTimeout(() => {
    if (url) onSuccess({ data: "result" });
    else onError(new Error("No URL"));
  }, 1000);
}

fetchData(
  "https://api.example.com",
  (data) => console.log(data),
  (err) => console.error(err)
);
```

### Callback Hell

```js
// The pyramid of doom
getUser(userId, (user) => {
  getPosts(user.id, (posts) => {
    getComments(posts[0].id, (comments) => {
      getAuthor(comments[0].authorId, (author) => {
        console.log(author); // 4 levels deep — hard to read, hard to error handle
      });
    });
  });
});
```

Promises and async/await solve this.

---

## 3. Promises

A **Promise** is an object representing a value that will be available now, in the future, or never.

**Three states:**
- **Pending** — initial state
- **Fulfilled** — operation succeeded
- **Rejected** — operation failed

Once settled (fulfilled or rejected), a promise cannot change state.

**Analogy:** A promise is like ordering food at a restaurant. You get a receipt (the promise). You don't have the food yet (pending). Either the food arrives (fulfilled) or they tell you it's sold out (rejected). You don't stand at the counter waiting — you sit down and come back when called.

```js
const promise = new Promise((resolve, reject) => {
  const success = true;

  setTimeout(() => {
    if (success) {
      resolve("Data loaded!");
    } else {
      reject(new Error("Something went wrong"));
    }
  }, 1000);
});

promise
  .then((data) => console.log(data))     // "Data loaded!"
  .catch((err) => console.error(err))
  .finally(() => console.log("Done"));   // Always runs
```

### Promise Chaining

Each `.then` returns a new promise. This flattens the callback pyramid.

```js
fetch("/api/user")
  .then((res) => res.json())
  .then((user) => fetch(`/api/posts/${user.id}`))
  .then((res) => res.json())
  .then((posts) => console.log(posts))
  .catch((err) => console.error("Any error in chain:", err));
```

### Creating resolved/rejected promises

```js
Promise.resolve(42).then(v => console.log(v));  // 42
Promise.reject(new Error("fail")).catch(e => console.log(e.message)); // "fail"
```

---

## 4. Promise Combinators

### `Promise.all` — All or nothing

Resolves when **all** promises resolve. Rejects as soon as **any** one rejects.

```js
const p1 = fetch("/api/users").then(r => r.json());
const p2 = fetch("/api/posts").then(r => r.json());
const p3 = fetch("/api/comments").then(r => r.json());

const [users, posts, comments] = await Promise.all([p1, p2, p3]);
// All 3 fetches run in parallel — faster than sequential!
```

### `Promise.allSettled` — Wait for all, regardless

Returns an array of result objects — never rejects.

```js
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject("oops"),
  Promise.resolve(3)
]);

results.forEach((result) => {
  if (result.status === "fulfilled") console.log(result.value);
  else console.log(result.reason);
});
// 1, "oops", 3
```

### `Promise.race` — First one wins

Resolves/rejects with the **first** settled promise.

```js
// Timeout pattern
function withTimeout(promise, ms) {
  const timeout = new Promise((_, reject) =>
    setTimeout(() => reject(new Error("Timeout")), ms)
  );
  return Promise.race([promise, timeout]);
}

await withTimeout(fetch("/api/slow"), 3000);
```

### `Promise.any` — First success wins

Resolves with the first **fulfilled** promise. Rejects only if **all** reject.

```js
const fastest = await Promise.any([
  fetch("https://server1.com/data"),
  fetch("https://server2.com/data"),
  fetch("https://server3.com/data")
]);
// Whichever server responds first wins
```

---

## 5. `async` / `await`

`async`/`await` is syntactic sugar over promises. It makes async code read like synchronous code.

```js
async function loadUser(id) {
  const response = await fetch(`/api/users/${id}`);
  const user = await response.json();
  return user; // This wraps the return value in a resolved promise
}

loadUser(1).then(user => console.log(user));
```

Rules:
- `async` functions **always return a Promise**
- `await` can only be used inside `async` functions (or top-level in modules)
- `await` pauses execution **of the async function only** — not the whole thread

### Error handling with `async`/`await`

```js
// try/catch approach
async function fetchUser(id) {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error("Failed to fetch user:", err);
    return null; // or rethrow
  } finally {
    console.log("Fetch attempt complete");
  }
}

// Helper to avoid try/catch repetition
async function safeAwait(promise) {
  try {
    const data = await promise;
    return [null, data];
  } catch (err) {
    return [err, null];
  }
}

const [err, user] = await safeAwait(fetchUser(1));
if (err) console.error(err);
else console.log(user);
```

### Sequential vs Parallel

```js
// ❌ Sequential — unnecessarily slow (waits for each before starting next)
const user = await fetchUser(1);   // wait ~1s
const posts = await fetchPosts(1); // wait another ~1s
// total: ~2s

// ✅ Parallel — run simultaneously
const [user, posts] = await Promise.all([fetchUser(1), fetchPosts(1)]);
// total: ~1s (both run at same time)

// ✅ Start both, await later
const userPromise = fetchUser(1);
const postsPromise = fetchPosts(1);
// ... do other sync work ...
const user = await userPromise;
const posts = await postsPromise;
```

---

## 6. Error Handling

### The `Error` object

```js
const err = new Error("Something went wrong");
err.message; // "Something went wrong"
err.name;    // "Error"
err.stack;   // Stack trace string
```

### Custom errors

```js
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

class NetworkError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.name = "NetworkError";
    this.statusCode = statusCode;
  }
}

function processUser(user) {
  if (!user.name) throw new ValidationError("Name is required", "name");
  if (!user.email) throw new ValidationError("Email is required", "email");
}

try {
  processUser({ name: "" });
} catch (err) {
  if (err instanceof ValidationError) {
    console.log(`Field "${err.field}" failed: ${err.message}`);
  } else {
    throw err; // rethrow unknown errors
  }
}
```

### Error boundaries in async code

```js
async function robustFetch(url, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error(`Status ${res.status}`);
      return await res.json();
    } catch (err) {
      if (attempt === retries) throw err;
      console.log(`Attempt ${attempt} failed, retrying...`);
      await new Promise(r => setTimeout(r, 1000 * attempt)); // exponential backoff
    }
  }
}
```

---

## 7. Generators

A **generator** is a function that can pause and resume execution, yielding values one at a time.

**Analogy:** A generator is like a TV show on demand. You watch one episode (call `.next()`), then pause. The show holds its place. When you return, it continues exactly where it stopped.

```js
function* counter() {
  let i = 0;
  while (true) {
    yield i++;
  }
}

const gen = counter();
gen.next(); // { value: 0, done: false }
gen.next(); // { value: 1, done: false }
gen.next(); // { value: 2, done: false }
// ... infinite, but lazy — only runs when you ask
```

### Finite generator

```js
function* range(start, end, step = 1) {
  for (let i = start; i < end; i += step) {
    yield i;
  }
}

for (const n of range(0, 10, 2)) {
  console.log(n); // 0, 2, 4, 6, 8
}

[...range(1, 6)]; // [1, 2, 3, 4, 5]
```

### Two-way communication

```js
function* calculator() {
  let result = 0;
  while (true) {
    const input = yield result;
    result += input;
  }
}

const calc = calculator();
calc.next();   // Start — { value: 0, done: false }
calc.next(10); // { value: 10, done: false }
calc.next(5);  // { value: 15, done: false }
```

### Delegating generators with `yield*`

```js
function* inner() {
  yield 1;
  yield 2;
}

function* outer() {
  yield* inner(); // delegates to inner
  yield 3;
}

[...outer()]; // [1, 2, 3]
```

---

## 8. Iterators and Iterables

Any object with a `[Symbol.iterator]` method that returns an iterator is **iterable** (works with `for...of`, spread, destructuring).

```js
// Custom iterable
const range = {
  from: 1,
  to: 5,
  [Symbol.iterator]() {
    let current = this.from;
    const last = this.to;
    return {
      next() {
        return current <= last
          ? { value: current++, done: false }
          : { value: undefined, done: true };
      }
    };
  }
};

for (const n of range) {
  console.log(n); // 1, 2, 3, 4, 5
}

[...range]; // [1, 2, 3, 4, 5]
```

---

## 9. `setTimeout`, `setInterval`, `queueMicrotask`

```js
// Runs after at least N milliseconds
const id = setTimeout(() => console.log("later"), 1000);
clearTimeout(id); // cancel it

// Runs every N milliseconds
const intervalId = setInterval(() => console.log("tick"), 500);
clearInterval(intervalId); // cancel it

// Queue a microtask directly (runs before next macro-task)
queueMicrotask(() => {
  console.log("microtask");
});
```

### `setTimeout(fn, 0)` trick

```js
console.log("sync 1");
setTimeout(() => console.log("deferred"), 0);
console.log("sync 2");
// sync 1 → sync 2 → deferred
```

Used to defer work until the call stack is clear (e.g., after DOM updates).

---

## 10. Debounce and Throttle

These are essential patterns for controlling how often a function is called.

### Debounce — Wait until they stop

**Analogy:** You're typing a search query. Debounce waits until you stop typing for 300ms before firing the search. Every keystroke resets the timer.

```js
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

const search = debounce((query) => {
  console.log(`Searching for: ${query}`);
}, 300);

// Only fires 300ms after the last call
input.addEventListener("input", e => search(e.target.value));
```

### Throttle — Allow at most once per interval

**Analogy:** A nightclub with a one-person-per-second rule. No matter how many people line up, only one gets in per second.

```js
function throttle(fn, limit) {
  let inThrottle = false;
  return function (...args) {
    if (!inThrottle) {
      fn.apply(this, args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

const onScroll = throttle(() => {
  console.log("Scroll event handled");
}, 100);

window.addEventListener("scroll", onScroll);
```

---

## 11. AbortController — Cancel Fetch

```js
const controller = new AbortController();
const { signal } = controller;

const fetchWithCancel = fetch("/api/data", { signal });

// Cancel after 5 seconds
setTimeout(() => controller.abort(), 5000);

try {
  const data = await fetchWithCancel;
} catch (err) {
  if (err.name === "AbortError") {
    console.log("Fetch was cancelled");
  }
}
```

---

## Quick Reference Cheatsheet — Day 3

```
Event Loop priority: Call Stack → Microtasks → Macro-tasks
Promise states: pending → fulfilled | rejected (final)

Promise combinators:
  .all()         → all succeed or first failure wins
  .allSettled()  → wait for all, never rejects
  .race()        → first settled wins
  .any()         → first success wins

async fn always returns a Promise
await pauses the async fn only, not the thread
Sequential: slower | Parallel (Promise.all): faster

Generator: function* | yield pauses | .next() resumes
Custom iterables: [Symbol.iterator]() method

Debounce: delay until activity stops (search inputs)
Throttle: allow at most once per interval (scroll, resize)
```