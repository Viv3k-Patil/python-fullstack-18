# 🔥 1. What is Exception Handling?

👉 Exception handling is:

👉 **Managing errors in a controlled, predictable, and standardized way**

---

## 🧠 Why it matters (Industry)

Without proper handling:

* APIs crash ❌
* Clients get unclear errors ❌
* Debugging becomes hard ❌
* Security issues (leaking internal info) ❌

---

# 🎯 Goal

👉 Every error should return:

```json
{
  "success": false,
  "message": "Something went wrong",
  "error_code": "TEAM_NOT_FOUND"
}
```

---

# 🔥 2. Types of Errors

---

## ✅ 1. Client Errors (4xx)

👉 Mistake from user

* Invalid input
* Resource not found
* Unauthorized

Example:

```text
404 → Team not found
```

---

## ✅ 2. Server Errors (5xx)

👉 Problem in backend

* DB down
* Code bug
* unexpected exception

---

# 🔥 3. Basic Python Exception Handling

---

## ✅ Syntax

```python
try:
    risky_code()
except Exception as e:
    handle_error(e)
```

---

## ⚠️ Problem

👉 This is NOT scalable in APIs:

* Repetitive ❌
* Messy ❌

---

# 🔥 4. FastAPI Standard → `HTTPException`

---

## ✅ Example

```python
from fastapi import HTTPException

@app.get("/teams/{team_id}")
def get_team(team_id: int):
    for team in teams:
        if team.id == team_id:
            return team

    raise HTTPException(
        status_code=404,
        detail="Team not found"
    )
```

---

## 🧠 Why use this?

* Sets HTTP status code correctly
* Structured error response
* Industry standard

---

# 🔥 5. Anatomy of `HTTPException`

```python
HTTPException(
    status_code=404,
    detail="Team not found"
)
```

---

## Fields

| Field       | Meaning       |
| ----------- | ------------- |
| status_code | HTTP status   |
| detail      | error message |

---

# 🔥 6. Common Status Codes (Must Know)

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not found             |
| 422  | Validation error      |
| 500  | Internal server error |

---

# 🔥 7. Validation Errors (Pydantic)

👉 FastAPI automatically validates input

---

## Example

```python
class Team(BaseModel):
    name: str
```

Request:

```json
{
  "name": 123
}
```

👉 Response:

```json
{
  "detail": [
    {
      "msg": "Input should be a valid string"
    }
  ]
}
```

---

## 🧠 Important

👉 You DO NOT handle this manually
👉 FastAPI + Pydantic handles it

---

# 🔥 8. Global Exception Handling (VERY IMPORTANT)

👉 Catch ALL unhandled errors

---

## ✅ Code

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error"
        }
    )
```

---

## 🧠 Why needed?

* Prevents app crash
* Hides internal details
* Consistent response

---

# 🔥 9. Custom Exception (INDUSTRY LEVEL)

---

## Step 1: Create custom exception

```python
class TeamNotFoundException(Exception):
    def __init__(self, team_id: int):
        self.team_id = team_id
```

---

## Step 2: Handle it globally

```python
@app.exception_handler(TeamNotFoundException)
def team_not_found_handler(request: Request, exc: TeamNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": f"Team {exc.team_id} not found"
        }
    )
```

---

## Step 3: Use it

```python
def get_team(team_id: int):
    for team in teams:
        if team.id == team_id:
            return team

    raise TeamNotFoundException(team_id)
```

---

# 🧠 Why custom exceptions?

* Clean business logic
* Reusable
* Centralized handling

---

# 🔥 10. Exception Handling in Services Layer

---

## ❌ Bad

```python
@app.get("/teams/{id}")
def get_team():
    # logic here ❌
```

---

## ✅ Good

```python
# service.py
def get_team_service(team_id):
    for team in teams:
        if team.id == team_id:
            return team
    raise TeamNotFoundException(team_id)
```

---

👉 Route becomes clean:

```python
@app.get("/teams/{id}")
def get_team(id: int):
    return get_team_service(id)
```

---

# 🔥 11. Logging with Exceptions (IMPORTANT)

---

```python
logger.error(f"Error fetching team: {team_id}")
```

👉 Always log before raising

---

# 🔥 12. Don’t Leak Internal Errors

---

## ❌ Bad

```json
{
  "error": "Database connection failed at line 52"
}
```

---

## ✅ Good

```json
{
  "message": "Internal server error"
}
```

---

# 🔥 13. Exception Flow (Industry)

```text
Client
  ↓
Route
  ↓
Service
  ↓
Exception raised
  ↓
Global handler
  ↓
Standard response
```

---

# 🔥 14. Best Practices

---

## ✅ DO

* Use `HTTPException` for API errors
* Use global handlers
* Use custom exceptions
* Keep responses consistent
* Log errors

---

## ❌ DON’T

* Return random error JSON
* Use try-except everywhere
* Leak internal errors
* Mix business logic in routes

---

# 🔥 15. Real Example (Full Flow)

---

```python
class TeamNotFoundException(Exception):
    pass


@app.exception_handler(TeamNotFoundException)
def handler(request: Request, exc: TeamNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": "Team not found"}
    )


def get_team_service(team_id):
    for team in teams:
        if team.id == team_id:
            return team
    raise TeamNotFoundException()


@app.get("/teams/{id}")
def get_team(id: int):
    return get_team_service(id)
```

---

# 🎯 One-Line Summary

👉 “Exception handling ensures APIs return consistent, meaningful errors without crashing.”

---


___________Detailed Notes__________________
Good — now we focus **only on exceptions (clean, structured, beginner → strong foundation)**. No Sonar, no noise.

---

# 📘 1. WHAT IS AN EXCEPTION?

👉 An **exception is a runtime error** that stops normal execution.

### Example

```python
x = int("abc")   # ValueError
```

👉 Program breaks unless handled

---

# 📘 2. BASIC EXCEPTION HANDLING

---

## 2.1 Simple try-except

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid number")
```

---

## 2.2 Generic exception

```python
try:
    x = int("abc")
except Exception as e:
    print(e)
```

👉 `e` = exception object

---

# 📘 3. FULL STRUCTURE

```python
try:
    risky_code()
except ValueError:
    handle_specific()
except Exception as e:
    handle_generic()
else:
    success_logic()
finally:
    cleanup()
```

---

## 3.1 Flow

| Case     | Execution              |
| -------- | ---------------------- |
| No error | try → else → finally   |
| Error    | try → except → finally |

---

# 📘 4. METHOD-LEVEL EXCEPTIONS (IMPORTANT)

---

## 4.1 Exception inside method

```python
def method():
    x = int("abc")   # error here
```

👉 If not handled → goes to caller

---

## 4.2 Caller handles

```python
def method():
    x = int("abc")

def main():
    try:
        method()
    except ValueError:
        print("Handled in main")
```

---

## 🔥 Concept: PROPAGATION

```text
Exception → bubbles up → until handled
```

---

# 📘 5. HANDLE vs PROPAGATE

---

## 5.1 Handle (stop propagation)

```python
def method():
    try:
        x = int("abc")
    except ValueError:
        print("Handled here")
```

👉 Caller never sees error

---

## 5.2 Propagate (re-raise)

```python
def method():
    try:
        x = int("abc")
    except ValueError:
        print("Logging")
        raise
```

👉 Caller will handle

---

# 📘 6. RAISING EXCEPTIONS

---

## 6.1 Raise manually

```python
raise ValueError("Invalid input")
```

---

## 6.2 Inside method

```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
```

---

## 6.3 Re-raise same exception

```python
try:
    x = int("abc")
except ValueError as e:
    raise
```

---

## 6.4 Raise new exception

```python
try:
    x = int("abc")
except ValueError:
    raise RuntimeError("Something failed")
```

---

## 6.5 Exception chaining (important)

```python
try:
    x = int("abc")
except ValueError as e:
    raise RuntimeError("Wrapped error") from e
```

---

# 📘 7. MULTIPLE EXCEPTIONS

---

## 7.1 Multiple blocks

```python
try:
    risky()
except ValueError:
    handle_value()
except TypeError:
    handle_type()
```

---

## 7.2 Tuple handling

```python
except (ValueError, TypeError):
    print("Handled both")
```

---

# 📘 8. EXCEPTION OBJECT (VERY IMPORTANT)

---

## 8.1 Access object

```python
try:
    x = int("abc")
except Exception as e:
    print(type(e))
    print(str(e))
    print(e.args)
```

---

## 8.2 Contains

* message
* type
* arguments
* stack trace

---

# 📘 9. IMPORTANT CASES

---

## 9.1 finally always runs

```python
try:
    1 / 0
finally:
    print("Runs always")
```

---

## 9.2 return + finally

```python
def test():
    try:
        return "try"
    finally:
        print("finally")
```

👉 Output:

```
finally
try
```

---

## 9.3 finally overriding return (danger)

```python
def test():
    try:
        return "try"
    finally:
        return "finally"
```

👉 Output:

```
finally
```

---

# 📘 10. COMMON EXCEPTIONS

| Exception         | Example         |
| ----------------- | --------------- |
| ValueError        | int("abc")      |
| TypeError         | "1" + 2         |
| KeyError          | dict["missing"] |
| IndexError        | list[10]        |
| ZeroDivisionError | 1/0             |

---

# 📘 11. BEST PRACTICES

---

## ✅ Catch specific first

```python
except ValueError:
```

---

## ✅ Use generic at last

```python
except Exception as e:
```

---

## ✅ Log + re-raise

```python
except Exception as e:
    print(e)
    raise
```

---

## ❌ Don’t swallow

```python
except:
    pass   # BAD
```

---

## ❌ Don’t overuse try

👉 Only wrap risky code

---

# 📘 12. CLEAN PATTERN (IMPORTANT)

```python
try:
    risky()
except SpecificError as e:
    log(e)
    recover()
except Exception as e:
    log(e)
    raise
else:
    success()
finally:
    cleanup()
```

---

# 📘 13. FINAL MENTAL MODEL

```text
Error happens
   ↓
Exception object created
   ↓
Travels up (propagation)
   ↓
Handled OR crashes
```

---

# 🔥 FINAL SUMMARY

* Exception = runtime error
* `try/except` = handle error
* `raise` = throw error
* Propagation = bubbles up
* `finally` = always runs
* Exception object = contains full info

---

# 📘 1. BASIC IDEA (VERY IMPORTANT)

```text
Exception happens → FastAPI catches → sends HTTP response
```

👉 You don’t return errors manually
👉 You **raise exceptions**, FastAPI converts them

---

# 📘 2. SIMPLE FASTAPI EXAMPLE

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/divide")
def divide(a: int, b: int):
    return {"result": a / b}
```

---

## ❌ If error happens

Call:

```
/divide?a=10&b=0
```

👉 Response:

```json
{
  "detail": "Internal Server Error"
}
```

👉 Status: **500**

---

# 📘 3. USING HTTPException

👉 HTTPException

---

## Example

```python
from fastapi import HTTPException

@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}
```

---

## ✅ Client gets

```json
{
  "detail": "Cannot divide by zero"
}
```

👉 Status: **400**

---

# 📘 4. WHERE TO USE HTTPException

| Layer      | Use   |
| ---------- | ----- |
| Controller | ✅ Yes |
| Service    | ❌ No  |

---

# 📘 5. SERVICE + CONTROLLER FLOW

---

## Service layer

```python
def divide_service(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## Controller layer

```python
@app.get("/divide")
def divide(a: int, b: int):
    try:
        result = divide_service(a, b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

# 📘 6. PROBLEM WITH ABOVE APPROACH

👉 Writing try/except in every API ❌
👉 Not scalable ❌

---

# 📘 7. BETTER APPROACH → GLOBAL HANDLER

---

## Step 1: Custom exception

```python
class DivideByZeroException(Exception):
    pass
```

---

## Step 2: Service layer

```python
def divide_service(a, b):
    if b == 0:
        raise DivideByZeroException()
    return a / b
```

---

## Step 3: Controller

```python
@app.get("/divide")
def divide(a: int, b: int):
    return {"result": divide_service(a, b)}
```

👉 No try/except ✅

---

## Step 4: Global handler

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(DivideByZeroException)
def handler(request: Request, exc: DivideByZeroException):
    return JSONResponse(
        status_code=400,
        content={"message": "Cannot divide by zero"}
    )
```

---

# 📘 8. FLOW (VERY IMPORTANT)

```text
Client → Controller → Service
                    ↓
             Exception raised
                    ↓
        Global Exception Handler
                    ↓
              JSON response
                    ↓
                Client
```

---

# 📘 9. GENERIC EXCEPTION HANDLER

---

```python
@app.exception_handler(Exception)
def global_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Something went wrong"}
    )
```

---

# 📘 10. VALIDATION EXCEPTION (AUTO)

👉 RequestValidationError

---

## Example

```python
@app.get("/test")
def test(age: int):
    return {"age": age}
```

Call:

```
/test?age=abc
```

---

## Response

```json
{
  "detail": [
    {
      "msg": "value is not a valid integer"
    }
  ]
}
```

👉 Status: **422**

---

# 📘 11. OVERRIDE VALIDATION RESPONSE

```python
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
def validation_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"message": "Invalid input"}
    )
```

---

# 📘 12. HTTPException vs Custom Exception

| Feature         | HTTPException | Custom Exception |
| --------------- | ------------- | ---------------- |
| Easy            | ✅             | ❌                |
| Control         | ❌             | ✅                |
| Layer usage     | Controller    | Service          |
| Global handling | Optional      | Required         |

---

# 📘 13. BEST PRACTICE (BEGINNER)

---

## ✅ Use this pattern

```text
Controller → no try/except
Service → raise custom exception
Handler → convert to response
```

---

## ❌ Avoid

```text
try/except in every API ❌
HTTPException in service ❌
```

---

# 📘 14. SIMPLE COMPLETE EXAMPLE

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom Exception
class MyError(Exception):
    pass

# Service
def service():
    raise MyError()

# Controller
@app.get("/test")
def test():
    return service()

# Handler
@app.exception_handler(MyError)
def handler(request: Request, exc: MyError):
    return JSONResponse(
        status_code=400,
        content={"message": "Custom error"}
    )
```

---

# 📘 15. FINAL MENTAL MODEL

```text
Raise exception → FastAPI catches → Handler converts → JSON response
```

---

# 🔥 FINAL SUMMARY

* Use `HTTPException` for simple APIs
* Use **custom exception + global handler** for scalable apps
* Don’t write try/except everywhere
* Exception always becomes **JSON response**

---

# 📘 1. BIG PICTURE (START HERE)

```text
Client → FastAPI → Your Function → FastAPI → Client
```

👉 FastAPI does:

* Parse request
* Inject required objects
* Convert response to JSON

---

# 📘 2. WHAT IS INJECTION (CORE CONCEPT)

👉 Injection = FastAPI **automatically gives you objects**

```python
@app.get("/test")
def test(request: Request):
```

👉 You didn’t create `Request`
👉 FastAPI gives it

---

## 🧠 Rule

```text
If you declare parameter → FastAPI injects it
If you don’t → nothing is injected
```

---

# 📘 3. WHERE INJECTION WORKS

---

## ✅ Works ONLY in FastAPI-managed functions

```python
@app.get("/test")
def test(request: Request):
    return {}
```

```python
@router.get("/test")
def test(request: Request):
    return {}
```

---

## ❌ Does NOT work in normal functions

```python
def service(request: Request):   ❌
    pass
```

👉 Must pass manually:

```python
def service(request: Request):
    pass

@app.get("/test")
def test(request: Request):
    service(request)
```

---

# 📘 4. REQUEST HANDLING

---

## 4.1 Automatic extraction (MOST IMPORTANT)

```python
@app.get("/user/{id}")
def get_user(id: int, age: int):
    return {"id": id, "age": age}
```

👉 FastAPI automatically:

* `id` → path param
* `age` → query param

---

## 4.2 Request Body (BEST WAY)

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return user
```

👉 FastAPI:

* parses JSON
* validates
* converts to object

---

# 📘 5. REQUEST OBJECT (LOW LEVEL)

👉 Use when you need full request info

---

## Example

```python
from fastapi import Request

@app.get("/debug")
async def debug(request: Request):
    body = await request.body()

    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "query": dict(request.query_params),
        "body": body.decode() if body else None
    }
```

---

## What Request contains

| Field        | Use             |
| ------------ | --------------- |
| method       | GET/POST        |
| url          | full URL        |
| headers      | request headers |
| query_params | query           |
| path_params  | path            |
| body         | raw data        |
| client.host  | IP              |

---

## ⚠️ Important

### ❗ Body read once

```python
await request.body()
await request.json() ❌ may fail
```

---

### ❗ JSON error

```python
await request.json()
```

👉 Fails if:

* empty body
* invalid JSON

---

# 📘 6. RESPONSE HANDLING

---

## 6.1 Default response

```python
return {"msg": "ok"}
```

👉 FastAPI:

* converts to JSON
* sets status = 200

---

## 6.2 Response Object

```python
from fastapi import Response

@app.get("/test")
def test(response: Response):
    response.status_code = 201
    return {"msg": "created"}
```

---

## Use cases

* change status
* set headers
* set cookies

---

# 📘 7. JSONResponse (FULL CONTROL)

---

```python
from fastapi.responses import JSONResponse

return JSONResponse(
    status_code=201,
    content={"msg": "created"}
)
```

---

## Difference

| Type         | Purpose      |
| ------------ | ------------ |
| dict         | simple       |
| Response     | modify       |
| JSONResponse | full control |

---

# 📘 8. STATUS CODE METHODS

---

## Method 1

```python
@app.post("/user", status_code=201)
```

---

## Method 2

```python
response.status_code = 201
```

---

## Method 3

```python
JSONResponse(status_code=201)
```

---

# 📘 9. REQUEST + RESPONSE FLOW

```text
Client sends request
        ↓
FastAPI parses (path/query/body)
        ↓
Injects parameters (Request, models, etc.)
        ↓
Your function runs
        ↓
Return dict
        ↓
FastAPI converts → JSON
        ↓
Client receives response
```

---

# 📘 10. WHAT FASTAPI CAN INJECT

| Parameter            | Injected        |
| -------------------- | --------------- |
| `request: Request`   | request object  |
| `response: Response` | response object |
| `user: UserModel`    | parsed body     |
| `id: int`            | path/query      |

---

# 📘 11. BEST PRACTICES

---

## ✅ Use Pydantic for input

```python
def create(user: User):
```

---

## ✅ Return dict

```python
return {"msg": "ok"}
```

---

## ✅ Use Request only when needed

---

## ❌ Avoid

```python
await request.json()   ❌
```

---

## ❌ Don’t overuse JSONResponse

---

# 📘 12. COMMON MISTAKES

---

❌ Expecting Request in normal function
❌ Reading body multiple times
❌ Invalid JSON input
❌ Not setting content-type

---

# 📘 13. FINAL MENTAL MODEL

```text
FastAPI controls route → injects parameters
You don’t create request/response manually
You just declare what you need
```

---

# 🔥 FINAL SUMMARY

* Injection works only in FastAPI routes
* Request = full client data
* Response = what you send back
* Pydantic = best way for body
* JSONResponse = advanced control

---

