# @asynccontextmanager and Middleware

## Intuition First: What Problem Are We Solving?

Imagine you're building a FastAPI app that needs:
- A **database connection pool** that starts when the app starts and closes when the app shuts down
- An **async HTTP client** for external API calls
- A **Redis connection** that's shared across all requests

You need to:
1. **Initialize** these resources **once** when the app starts
2. **Share** them across all requests
3. **Clean up** properly when the app shuts down

Normal functions can't do this because they don't support `await` inside setup/teardown. That's where `@asynccontextmanager` comes in.

***

## 1. Context Managers – Intuition (Sync Version First)

### What Is a Context Manager?

A context manager is a Python pattern that handles **setup** and **cleanup** automatically using the `with` statement.

### Classic Example – File Handling

```python
# Without context manager (WRONG)
file = open("data.txt", "r")
content = file.read()
# What if an error happens here? File never closes!
file.close()

# With context manager (CORRECT)
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closes, even if error occurs
```

**What happens?**
- `open()` is the setup (opens file)
- Code inside `with` block runs
- `close()` is the cleanup (automatically called, even on error)

### How Context Managers Work

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        # Setup: open file
        self.file = open(self.filename, "r")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup: close file
        self.file.close()
        # Return False to propagate exceptions, True to suppress
        return False

# Usage
with FileManager("data.txt") as f:
    content = f.read()
# File automatically closed
```

**Key methods:**
- `__enter__()` → setup code, returns something usable in `with` block
- `__exit__()` → cleanup code, runs even if error occurs

***

## 2. Async Context Managers – Why We Need Them

### Problem: Async Resources Need Async Cleanup

What if your resource needs `await` to open or close?

```python
# ❌ WRONG: Can't use await in __enter__ and __exit__
class Database:
    def __enter__(self):
        self.conn = await connect_to_db()  # ❌ SyntaxError: await not allowed
```

**Solution:** Use async context managers with `__aenter__()` and `__aexit__()`.

### Async Context Manager Class Pattern

```python
class AsyncDatabase:
    def __init__(self):
        self.conn = None
    
    async def __aenter__(self):
        # Setup with await
        self.conn = await connect_to_db()
        return self.conn
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Cleanup with await
        await self.conn.close()
        return False

# Usage
async with AsyncDatabase() as conn:
    await conn.execute("SELECT * FROM users")
# Connection automatically closed
```

**Key methods:**
- `__aenter__()` → async setup (uses `await`)
- `__aexit__()` → async cleanup (uses `await`)
- Use `async with` instead of `with`

***

## 3. @asynccontextmanager – The Easy Way

### What Is @asynccontextmanager?

`@asynccontextmanager` is a decorator from Python's `contextlib` module that lets you write async context managers as **functions** instead of classes.

### Syntax Comparison

**Class-based (verbose):**
```python
class AsyncDatabase:
    async def __aenter__(self):
        self.conn = await connect_to_db()
        return self.conn
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
```

**Function-based (clean):**
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def get_database():
    conn = await connect_to_db()  # Setup
    try:
        yield conn
    finally:
        await conn.close()  # Cleanup
```

**Why use `@asynccontextmanager`?**
- Much cleaner and more readable
- Uses `yield` instead of `__aenter__`/`__aexit__`
- Automatic exception handling
- Less boilerplate code

***

## 4. How @asynccontextmanager Works

### The Pattern

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def resource_manager():
    # ── SETUP ──────────────────────────────────────
    resource = await create_resource()
    
    try:
        yield resource  # Hand control to the 'with' block
    finally:
        # ── CLEANUP ─────────────────────────────────────
        await resource.close()
```

### Breakdown

| Part | What It Does |
|---|---|
| `@asynccontextmanager` | Decorator that makes this an async context manager |
| `async def` | Must be async function |
| `yield resource` | Pauses here, returns `resource` to `async with` block |
| Code before `yield` | Setup (runs when entering) |
| Code after `yield` | Cleanup (runs when exiting) |
| `try/finally` | Ensures cleanup runs even on error |

### Complete Example

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def database_connection():
    # Setup
    conn = await connect_to_database()
    print("Database connected")
    
    try:
        yield conn
    finally:
        # Cleanup
        await conn.close()
        print("Database closed")

# Usage
async with database_connection() as conn:
    await conn.execute("SELECT * FROM users")
# Automatically closes after block
```

### What Happens Step by Step

1. `async with database_connection()` → calls the function, runs setup
2. `yield conn` → pauses, returns `conn` to the `as conn` part
3. Code inside `async with` block runs
4. Block exits (normal or error) → runs `finally` block
5. `await conn.close()` → cleanup runs
6. Function exits

***

## 5. FastAPI Lifespan – Real-World Use of @asynccontextmanager

### What Is Lifespan?

FastAPI's **lifespan** is the time from when the app starts to when it shuts down. You use `@asynccontextmanager` to manage resources during this time.

### Complete FastAPI Example

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
import httpx


# ── 1. Define the lifespan manager ────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── SETUP (app starts) ───────────────────────────
    print("App starting...")
    
    # Create shared resources
    app.state.httpx_client = httpx.AsyncClient()
    app.state.db_pool = await create_database_pool()
    
    yield  # App runs here
    
    # ── CLEANUP (app shuts down) ─────────────────────
    print("App shutting down...")
    
    await app.state.httpx_client.aclose()
    await app.state.db_pool.close()


# ── 2. Create app with lifespan ──────────────────────
app = FastAPI(lifespan=lifespan)


# ── 3. Use shared resources in routes ────────────────
@app.get("/users")
async def get_users():
    client = app.state.httpx_client
    db = app.state.db_pool
    
    # Use resources
    response = await client.get("https://api.example.com/users")
    users = await db.fetch_all("SELECT * FROM users")
    
    return users
```

### What Happens

**When app starts:**
1. Server calls `lifespan(app)`
2. Runs setup code (before `yield`)
3. Creates `httpx.AsyncClient()` and database pool
4. Stores them in `app.state`
5. Hits `yield` → app starts serving requests

**During app runtime:**
- All requests can access `app.state.httpx_client` and `app.state.db_pool`
- Resources are shared (not recreated per request)

**When app shuts down:**
1. Server resumes after `yield`
2. Runs cleanup code (after `yield`)
3. Closes HTTP client and database pool
4. App stops

***

## 6. Middleware – Intuition

### What Is Middleware?

Middleware is code that runs **around** your request handler. It can:
- Run code **before** the request reaches the handler
- Run code **after** the handler returns
- Modify the request or response
- Decide whether to even call the handler

### Real-World Examples

| Middleware | Purpose |
|---|---|
| **Logging** | Log every request (method, path, status, time) |
| **Authentication** | Check JWT token, add user to request |
| **CORS** | Add headers for cross-origin requests |
| **Timing** | Measure how long each request takes |
| **Error handling** | Catch exceptions, return formatted errors |

### Visual Flow

```
Request → Middleware 1 → Middleware 2 → Handler → Middleware 2 → Middleware 1 → Response
```

***

## 7. FastAPI Middleware – Two Types

### Type 1: HTTP Middleware (Starlette Middleware)

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # ── BEFORE handler ───────────────────────────
        print(f"Request: {request.method} {request.url}")
        
        # Call the handler
        response = await call_next(request)
        
        # ── AFTER handler ────────────────────────────
        print(f"Response status: {response.status_code}")
        
        return response


app = FastAPI()
app.add_middleware(LoggingMiddleware)
```

### What Happens

1. Request arrives
2. `dispatch()` runs **before** handler (logs request)
3. `await call_next(request)` → calls the actual handler
4. `dispatch()` continues **after** handler (logs response)
5. Returns response to client

### Type 2: Dependency-Based Middleware

```python
from fastapi import FastAPI, Depends, Request


async def auth_dependency(request: Request):
    # BEFORE: Check authentication
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No token")
    
    # Add user to request
    request.state.user = {"id": 123, "name": "Rahul"}
    
    # AFTER: Nothing needed here

app = FastAPI()

@app.get("/users")
async def get_users(user = Depends(auth_dependency)):
    # Handler can use user
    return {"user": user}
```

***

## 8. Combining @asynccontextmanager and Middleware

### Real-World Pattern: Shared Resources + Request Logging

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import httpx
import time


# ── 1. Lifespan manager ──────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # SETUP
    app.state.httpx_client = httpx.AsyncClient()
    app.state.db_pool = await create_database_pool()
    
    yield
    
    # CLEANUP
    await app.state.httpx_client.aclose()
    await app.state.db_pool.close()


# ── 2. Middleware ────────────────────────────────────
class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        print(f"{request.method} {request.url} took {process_time:.2f}s")
        
        return response


# ── 3. Create app ────────────────────────────────────
app = FastAPI(lifespan=lifespan)
app.add_middleware(TimingMiddleware)


# ── 4. Routes use shared resources ───────────────────
@app.get("/external")
async def get_external():
    client = app.state.httpx_client
    response = await client.get("https://api.example.com/data")
    return response.json()
```

### What Happens Per Request

```
Request → TimingMiddleware (start timer)
         → Route handler (uses httpx_client from app.state)
         → TimingMiddleware (stop timer, log)
         → Response
```

When app shuts down:
```
Lifespan cleanup → closes httpx_client and db_pool
```

***

## 9. Complete Working Example

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import httpx
import time


# ── Lifespan Manager ─────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # SETUP
    print("▶ App starting...")
    
    app.state.httpx_client = httpx.AsyncClient()
    app.state.db_pool = await create_database_pool()
    app.state.redis_client = await create_redis_client()
    
    yield
    
    # CLEANUP
    print("◀ App shutting down...")
    
    await app.state.httpx_client.aclose()
    await app.state.db_pool.close()
    await app.state.redis_client.close()


# ── Middleware ───────────────────────────────────────
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # BEFORE
        print(f"▶ {request.method} {request.url.path}")
        
        response = await call_next(request)
        
        # AFTER
        print(f"◀ {request.method} {request.url.path} → {response.status_code}")
        
        return response


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        
        return response


# ── Create App ───────────────────────────────────────
app = FastAPI(lifespan=lifespan)
app.add_middleware(LoggingMiddleware)
app.add_middleware(TimingMiddleware)


# ── Routes ───────────────────────────────────────────
@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/external")
async def get_external():
    client = app.state.httpx_client
    response = await client.get("https://api.github.com")
    return response.json()


# Helper functions (for example)
async def create_database_pool():
    class MockPool:
        async def close(self):
            print("DB pool closed")
    return MockPool()


async def create_redis_client():
    class MockRedis:
        async def close(self):
            print("Redis closed")
    return MockRedis()
```

***

## 10. Side-by-Side Comparison

| Concept | Purpose | When to Use |
|---|---|---|
| `@asynccontextmanager` | Manage async resources with setup/teardown | App lifecycle (lifespan), database connections, HTTP clients |
| `async with` | Use async context managers | When you need to create resource per request/block |
| `BaseHTTPMiddleware` | Wrap every request with before/after logic | Logging, timing, CORS, auth checks |
| `Depends()` | Inject dependencies into routes | Per-request validation, auth, database sessions |
| `app.state` | Store shared app-level data | Resources created in lifespan (httpx_client, db_pool) |

***

## 11. Common Mistakes

### Mistake 1: Forgetting `async` Before `with`

```python
# ❌ WRONG
with database_connection() as conn:
    await conn.execute("...")

# ✅ CORRECT
async with database_connection() as conn:
    await conn.execute("...")
```

### Mistake 2: Not Using `try/finally` for Cleanup

```python
# ❌ WRONG: Cleanup might not run on error
@asynccontextmanager
async def resource_manager():
    resource = await create_resource()
    yield resource
    await resource.close()

# ✅ CORRECT: Cleanup always runs
@asynccontextmanager
async def resource_manager():
    resource = await create_resource()
    try:
        yield resource
    finally:
        await resource.close()
```

### Mistake 3: Creating Resources Per Request Instead of in Lifespan

```python
# ❌ WRONG: Creates new client on every request
@app.get("/users")
async def get_users():
    client = httpx.AsyncClient()  # Created every time!
    response = await client.get("...")
    await client.aclose()
    return response.json()

# ✅ CORRECT: Shared client created once in lifespan
@app.get("/users")
async def get_users():
    client = app.state.httpx_client  # Shared, reused
    response = await client.get("...")
    return response.json()
```

### Mistake 4: Forgetting to Pass Lifespan to FastAPI

```python
# ❌ WRONG: Lifespan defined but not used
@asynccontextmanager
async def lifespan(app: FastAPI):
    ...

app = FastAPI()  # Missing lifespan=lifespan

# ✅ CORRECT
app = FastAPI(lifespan=lifespan)
```

***

## 12. Summary (Cheat Sheet)

| Code Pattern | What It Does |
|---|---|
| `@asynccontextmanager` | Makes async function into context manager |
| `async with manager() as x:` | Uses async context manager |
| `yield resource` | Pauses, returns resource to `async with` block |
| `try/finally` after `yield` | Ensures cleanup always runs |
| `lifespan(app: FastAPI)` | Manages app lifecycle (start/shutdown) |
| `app.state.resource` | Stores shared resources in app |
| `BaseHTTPMiddleware` | Middleware that wraps every request |
| `await call_next(request)` | Calls the next middleware or handler |
| `app.add_middleware(Middleware)` | Adds middleware to app |

**Final flow:**
```
App Start → Lifespan setup → app.state created → Middleware runs → Handler runs → Middleware runs → Lifespan cleanup → App Shutdown
```