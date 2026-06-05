Think of `yield` as a **pause-and-resume** button inside a function. Everything before `yield` runs *now*, `yield` hands something out, and everything after `yield` runs *later* when the caller is finished.

Let’s build intuition in two stages:

1. Plain Python `yield`  
2. FastAPI `yield` in dependencies

***

## 1. Intuition for `yield` in plain Python

### Mental model

Imagine a function is a movie:

- With `return`:  
  You press play, the whole movie runs once, and then it stops forever.
- With `yield`:  
  The movie is split into episodes. Each time you call `next(...)`, you watch the next episode. The movie remembers where you stopped.

So:

- `return value` → “Here is the final value. End of story.”
- `yield value` → “Here is a value for now. I’ll pause here and can continue next time.”

### Simple examples

#### Example 1: Counting

```python
def count_to_three():
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")
    yield 3
    print("End")
```

Now try in a Python REPL:

```python
gen = count_to_three()

next(gen)  # prints "Start", returns 1
next(gen)  # prints "After first yield", returns 2
next(gen)  # prints "After second yield", returns 3
```

Notice:

- First `next(gen)` runs from the top until it hits `yield 1`, then pauses.
- Second `next(gen)` resumes *after* `yield 1` and goes until `yield 2`, then pauses.
- Third `next(gen)` resumes after `yield 2`, etc.

The function is **not restarted** each time; it’s resumed from where it paused.

#### Example 2: Infinite sequence

```python
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1
```

This function can generate infinitely many numbers, one at a time, without storing them all in memory. It produces values **on demand**.

***

## 2. Intuition for `yield` in FastAPI dependencies

FastAPI uses that “before / yield / after” split to handle **setup and cleanup** around each request.

A good analogy: `yield` in a dependency is like a manual `with` block:

```python
with open_db() as db:
    # use db
# after this, db is closed
```

The `yield`-based dependency lets FastAPI internally do something very similar for each HTTP request.

### Basic pattern

A typical FastAPI DB dependency:

```python
async def get_db():
    db = DBSession()          # 1. setup
    try:
        yield db              # 2. give db to the endpoint
    finally:
        db.close()            # 3. cleanup (always runs)
```

What conceptually happens for a single request:

1. FastAPI calls `get_db()` until it hits `yield db`.  
   - This is the **setup** part (create DB session).
2. The value after `yield` (`db`) is injected into your path operation function.
3. Your endpoint finishes (or raises an error).
4. FastAPI resumes `get_db()` after the `yield`, so `finally: db.close()` runs.  
   - This is the **cleanup**.

So in words:

> “Create the resource before `yield`, hand it to the endpoint at `yield`, and after the endpoint is done, continue the function to clean things up.”

### Example: file dependency

Here’s a super-simple, almost-pseudocode example with a file:

```python
def get_config_file():
    f = open("config.json")
    try:
        yield f          # endpoint uses f
    finally:
        f.close()        # always close file
```

Usage:

```python
from fastapi import Depends, FastAPI

app = FastAPI()

@app.get("/config")
def read_config(f = Depends(get_config_file)):
    return {"first_line": f.readline()}
```

Per request:

- Open file (before `yield`)
- Give file handle to endpoint (`yield f`)
- After endpoint finishes, close file (after `yield`)

### Example: timing middleware-style dependency

You can also use `yield` to wrap behavior around a request, like a simple timing / logging dependency:

```python
import time

def log_time():
    start = time.time()
    print("Request started")
    try:
        # value is optional; you can yield None
        yield
    finally:
        duration = time.time() - start
        print(f"Request ended, took {duration:.3f}s")
```

Use in endpoint:

```python
@app.get("/items")
def list_items(_ = Depends(log_time)):
    return ["a", "b", "c"]
```

For each request:

- Before `yield`: log start time.
- Endpoint runs.
- After `yield`: log how long the request took.

There is no “db object” to pass here; you just want “run some code before and after”. `yield` still gives you that hook.

***

## Key contrast: `return` vs `yield` in dependencies

- Use **`return`** when:
  - You just want to compute a value once and inject it.
  - There is no cleanup or “afterwards” logic.

- Use **`yield`** when:
  - You need to both:
    - Do something **before** the endpoint runs (setup),
    - And do something **after** the endpoint finishes (cleanup), especially for resources.