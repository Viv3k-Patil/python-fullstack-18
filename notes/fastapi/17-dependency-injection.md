***

## 1. What is Dependency Injection (DI)?

- Dependency Injection is a pattern where a function or class **receives** the objects it needs (dependencies) from the outside instead of creating them internally. [medium](https://medium.com/@azizmarzouki/mastering-dependency-injection-in-fastapi-clean-scalable-and-testable-apis-5f78099c3362)
- This creates **loose coupling**: business logic does not care *how* a dependency is built, only that it gets one. [medium](https://medium.com/@azizmarzouki/mastering-dependency-injection-in-fastapi-clean-scalable-and-testable-apis-5f78099c3362)

***

## 2. DI in FastAPI: core idea

- FastAPI has a built-in DI system; dependencies are declared using `Depends`. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/)
- A “dependency” is any callable (function, async function, or class) whose return value will be passed into path operation functions. [medium](https://medium.com/@melthaw/exploring-fastapi-dependency-injection-a-comprehensive-guide-103bc48d111f)

Basic example:

```python
from fastapi import Depends, FastAPI

app = FastAPI()

def get_token():
    return "fixed-token"

@app.get("/items")
def read_items(token: str = Depends(get_token)):
    return {"token": token}
```

- Here `get_token` is the dependency.  
- FastAPI calls `get_token()` for each request and injects its return value into `read_items`. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/)

***

## 3. Where dependencies can be used

- In endpoint parameters (most common): inject services, DB sessions, auth info. [medium](https://medium.com/@melthaw/exploring-fastapi-dependency-injection-a-comprehensive-guide-103bc48d111f)
- On a router: shared dependencies for all routes in that router, such as authentication or logging. [medium](https://medium.com/@azizmarzouki/mastering-dependency-injection-in-fastapi-clean-scalable-and-testable-apis-5f78099c3362)
- On the app: global dependencies for every request. [medium](https://medium.com/@azizmarzouki/mastering-dependency-injection-in-fastapi-clean-scalable-and-testable-apis-5f78099c3362)

Examples:

```python
from fastapi import APIRouter, Depends, FastAPI

router = APIRouter()

def auth_check():
    ...

@router.get("/users", dependencies=[Depends(auth_check)])
def list_users():
    ...

app = FastAPI(dependencies=[Depends(auth_check)])
app.include_router(router)
```

***

## 4. Dependencies with `yield` (setup + cleanup)

Pattern:

```python
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

- Code before `yield` runs at the beginning of the request: setup. [getorchestra](https://www.getorchestra.io/guides/fastapi-dependencies-with-yield-a-comprehensive-tutorial)
- The value after `yield` (here `db`) is injected into the endpoint. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)
- Code after `yield` runs after the response is sent: cleanup, even if an exception happens. [getorchestra](https://www.getorchestra.io/guides/fastapi-dependencies-with-yield-a-comprehensive-tutorial)

Usage:

```python
@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    ...
```

Typical uses:

- Open DB session then close it. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)
- Start a transaction and commit/rollback in the cleanup section. [getorchestra](https://www.getorchestra.io/guides/fastapi-dependencies-with-yield-a-comprehensive-tutorial)
- Open files, acquire locks, or allocate resources and release them afterwards. [getorchestra](https://www.getorchestra.io/guides/fastapi-dependencies-with-yield-a-comprehensive-tutorial)

***

## 5. Types of dependencies

1. Function dependencies  
   - Simple functions returning values or yielding resources. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/)

2. Class-based dependencies  

```python
from fastapi import Depends

class Settings:
    def __init__(self):
        self.app_name = "MyApp"

@app.get("/info")
def info(settings: Settings = Depends()):
    return {"name": settings.app_name}
```

- FastAPI instantiates the class and injects the instance. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/)

3. Nested dependencies  
   - A dependency can depend on other dependencies, forming a graph. [medium](https://medium.com/@melthaw/exploring-fastapi-dependency-injection-a-comprehensive-guide-103bc48d111f)

***

## 6. Why DI is useful in FastAPI

- Separation of concerns: endpoints focus on HTTP and business logic, not wiring. [oneuptime](https://oneuptime.com/blog/post/2026-02-02-fastapi-dependency-injection/view)
- Reusability: the same dependency function can be used across many endpoints. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/)
- Testability: dependencies can be overridden in tests to inject fakes/mocks. [oneuptime](https://oneuptime.com/blog/post/2026-02-02-fastapi-dependency-injection/view)
- Consistent resource management: `yield`-style dependencies give a standard place for setup/teardown. [fastapi.tiangolo](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)

***