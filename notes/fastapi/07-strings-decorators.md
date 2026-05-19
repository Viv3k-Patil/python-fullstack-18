---
String Methods
---

# 🔤 Case Conversion

### `capitalize()`

```python
"hello world".capitalize()   # 'Hello world'
```

### `casefold()`

```python
"HELLO".casefold()   # 'hello'
```

### `lower()`

```python
"HELLO".lower()   # 'hello'
```

### `upper()`

```python
"hello".upper()   # 'HELLO'
```

### `title()`

```python
"hello world".title()   # 'Hello World'
```

### `swapcase()`

```python
"HeLLo".swapcase()   # 'hEllO'
```

---

# 🔍 Searching & Finding

### `find()`

```python
"hello".find("l")   # 2
```

### `rfind()`

```python
"hello".rfind("l")   # 3
```

### `index()`

```python
"hello".index("e")   # 1
```

### `rindex()`

```python
"hello".rindex("l")   # 3
```

### `count()`

```python
"banana".count("a")   # 3
```

### `startswith()`

```python
"hello".startswith("he")   # True
```

### `endswith()`

```python
"hello".endswith("lo")   # True
```

---

# ✂️ Modifying Strings

### `replace()`

```python
"banana".replace("a", "x")   # 'bxnxnx'
```

### `strip()`

```python
"  hi  ".strip()   # 'hi'
```

### `lstrip()`

```python
"  hi".lstrip()   # 'hi'
```

### `rstrip()`

```python
"hi  ".rstrip()   # 'hi'
```

### `removeprefix()`

```python
"unhappy".removeprefix("un")   # 'happy'
```

### `removesuffix()`

```python
"file.txt".removesuffix(".txt")   # 'file'
```

---

# 🔀 Splitting & Joining

### `split()`

```python
"a,b,c".split(",")   # ['a', 'b', 'c']
```

### `rsplit()`

```python
"a,b,c".rsplit(",", 1)   # ['a,b', 'c']
```

### `splitlines()`

```python
"a\nb".splitlines()   # ['a', 'b']
```

### `join()`

```python
"-".join(["a", "b"])   # 'a-b'
```

### `partition()`

```python
"key=value".partition("=")   # ('key', '=', 'value')
```

### `rpartition()`

```python
"a=b=c".rpartition("=")   # ('a=b', '=', 'c')
```

---

# 📐 Alignment & Formatting

### `center()`

```python
"hi".center(6, "*")   # '**hi**'
```

### `ljust()`

```python
"hi".ljust(5, "-")   # 'hi---'
```

### `rjust()`

```python
"hi".rjust(5, "-")   # '---hi'
```

### `zfill()`

```python
"42".zfill(5)   # '00042'
```

### `expandtabs()`

```python
"a\tb".expandtabs(4)
```

---

# 🔢 Checking Methods (Boolean)

### `isalnum()`

```python
"abc123".isalnum()   # True
```

### `isalpha()`

```python
"abc".isalpha()   # True
```

### `isdigit()`

```python
"123".isdigit()   # True
```

### `isdecimal()`

```python
"123".isdecimal()   # True
```

### `isnumeric()`

```python
"123".isnumeric()   # True
```

### `islower()`

```python
"abc".islower()   # True
```

### `isupper()`

```python
"ABC".isupper()   # True
```

### `istitle()`

```python
"Hello World".istitle()   # True
```

### `isspace()`

```python
"   ".isspace()   # True
```

### `isidentifier()`

```python
"var_1".isidentifier()   # True
```

### `isprintable()`

```python
"abc".isprintable()   # True
```

### `isascii()`

```python
"abc".isascii()   # True
```

---

# 🔄 Encoding / Decoding

### `encode()`

```python
"hello".encode("utf-8")   # b'hello'
```

---

# 🧩 Miscellaneous

### `format()`

```python
"Hello {}".format("Vivek")   # 'Hello Vivek'
```

### `format_map()`

```python
"{name}".format_map({"name": "Vivek"})   # 'Vivek'
```

### `translate()`

```python
table = str.maketrans("a", "x")
"apple".translate(table)   # 'xpple'
```

### `maketrans()` (used with translate)

```python
str.maketrans("a", "x")
```

---

# 🧠 Final Summary

* String methods are **immutable operations** → return new string
* No method modifies original string

---
# Python Decorators — Complete Notes

---

# 1. Basic Decorator

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

```python
@decorator
def greet():
    print("Hello")
```

Equivalent:

```python
greet = decorator(greet)
```

---

# 2. Execution Flow

```text
decorator(func) → returns wrapper
wrapper() → executes extra logic + original function
```

---

# 3. Decorator with Arguments in Wrapped Function

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)
    return wrapper
```

```python
@decorator
def greet(name):
    print(f"Hello {name}")
```

---

# 4. Decorator Factory (Decorator with Parameters)

```python
def route(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(path)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

Usage:

```python
@route("/teams")
def get_teams():
    pass
```

---

# 5. Internal Transformation

```python
@route("/teams")
def get_teams():
    pass
```

Equivalent:

```python
get_teams = route("/teams")(get_teams)
```

---

# 6. Execution Order

```text
1. route("/teams")           → executed first
2. function is created       → get_teams
3. decorator(get_teams)      → executed next
4. result assigned           → get_teams
```

---

# 7. Timeline Example

```python
def route(path):
    print("STEP 1")

    def decorator(func):
        print("STEP 3")
        return func

    return decorator


@route("/teams")
def get_teams():
    pass
```

Output:

```text
STEP 1
STEP 3
```

---

# 8. Structure

```text
Decorator Factory → returns decorator
Decorator         → receives function
Wrapper           → executes logic
```

---

# 9. Why Multiple Layers

```text
Layer 1 → receives configuration (path)
Layer 2 → receives function
Layer 3 → executes wrapped logic
```

---

# 10. Constraint

```text
Function is not available when route(...) is executed
```

---

# 11. Invalid Pattern

```python
@decorator("teams", func)   # invalid
```

---

# 12. Valid Manual Call

```python
def decorator(path, func):
    return func

def get_teams():
    pass

get_teams = decorator("teams", get_teams)
```

---

# 13. Multiple Decorators

```python
@deco1
@deco2
def func():
    pass
```

Equivalent:

```python
func = deco1(deco2(func))
```

Execution order:

```text
deco1 → deco2 → func
```

---

# 14. Decorator Returning Values

```python
def decorator(func):
    def wrapper():
        return func() + 1
    return wrapper

@decorator
def num():
    return 5
```

Output:

```text
6
```

---

# 15. functools.wraps

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Purpose

* Preserves:

  * function name
  * docstring
  * metadata

---

# 16. Metadata Access

```python
def greet():
    """Hello function"""
    pass

print(greet.__name__)
print(greet.__doc__)
```

---

# 17. Class as Decorator

```python
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before")
        return self.func()
```

```python
@Decorator
def greet():
    print("Hello")
```

---

# 18. Decorator with State

```python
def counter():
    count = 0

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(count)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

---

# 19. Chaining Decorators with Parameters

```python
@route("/teams")
@auth_required("admin")
def get_teams():
    pass
```

Equivalent:

```python
get_teams = route("/teams")(auth_required("admin")(get_teams))
```

---

# 20. Execution Time vs Definition Time

```text
Definition time:
- decorator factory runs
- decorator runs

Runtime:
- wrapper runs
```

---

# 21. Decorator Without Wrapper

```python
def decorator(func):
    print("Registering")
    return func
```

---

# 22. Method Decorators

```python
class A:
    def decorator(func):
        def wrapper(self):
            return func(self)
        return wrapper
```

---

# 23. Static and Class Method Decorators

```python
class A:
    @staticmethod
    def f():
        pass

    @classmethod
    def g(cls):
        pass
```

---

# 24. Property Decorator

```python
class A:
    @property
    def value(self):
        return 10
```

---

# 25. Property Setter

```python
class A:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
```

---

# 26. Summary

```text
Decorator             → function wrapping another function
Decorator factory     → function returning decorator
Wrapper               → function executing logic
Definition time       → decorator execution
Runtime               → wrapper execution
wraps()               → preserves metadata
Stacking              → inner first, outer last
```

