---

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
