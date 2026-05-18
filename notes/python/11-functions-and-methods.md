# 🎓 Day 11 — Python Functions, max() and min()

---

# Slide 1 — Title

## Python Programming

### Day 11

Topics:

✔ Functions
✔ Parameters
✔ Lambda Functions
✔ Recursion
✔ max() and min()

Instructor: **Vivek Patil**

---

# Slide 2 — What is a Function?

A **function** is a reusable block of code that performs a specific task.

Functions help to:

✔ Avoid repeating code
✔ Organize programs
✔ Improve readability
✔ Make programs modular

Example

```python
def greet():
    print("Hello")
```

Calling the function

```python
greet()
```

Output

```
Hello
```

---

# Slide 3 — Syntax of a Function

```
def function_name(parameters):
    statements
    return value
```

Example

```python
def add(a, b):
    return a + b
```

Calling the function

```python
result = add(5, 3)
print(result)
```

Output

```
8
```

---

# Slide 4 — Function Without Parameters

Functions can work **without inputs**.

Example

```python
def welcome():
    print("Welcome to Python")

welcome()
```

Output

```
Welcome to Python
```

---

# Slide 5 — Function With Parameters

Parameters allow passing **input values**.

Example

```python
def greet(name):
    print("Hello", name)

greet("Vivek")
```

Output

```
Hello Vivek
```

---

# Slide 6 — Function With Return Value

Functions can return values using **return**.

Example

```python
def square(num):
    return num * num

result = square(4)
print(result)
```

Output

```
16
```

---

# Slide 7 — Default Parameters

Default values are used if no argument is provided.

Example

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Vivek")
```

Output

```
Hello Guest
Hello Vivek
```

---

# Slide 8 — Keyword Arguments

Arguments can be passed using **parameter names**.

Example

```python
def student(name, age):
    print(name, age)

student(age=20, name="Rahul")
```

Output

```
Rahul 20
```

---

# Slide 9 — Variable Length Arguments (*args)

Used when the **number of arguments is unknown**.

Example

```python
def add_numbers(*numbers):
    print(numbers)

add_numbers(1, 2, 3, 4)
```

Output

```
(1, 2, 3, 4)
```

Example

```python
def total(*nums):
    return sum(nums)

print(total(10, 20, 30))
```

Output

```
60
```

---

# Slide 10 — Keyword Variable Arguments (**kwargs)

Used to accept multiple **key-value arguments**.

Example

```python
def student_info(**data):
    print(data)

student_info(name="Vivek", age=25)
```

Output

```
{'name': 'Vivek', 'age': 25}
```

---

# Slide 11 — Lambda Functions

A **lambda function** is a small anonymous function.

Syntax

```
lambda arguments : expression
```

Example

```python
square = lambda x: x * x

print(square(5))
```

Output

```
25
```

---

# Slide 12 — Recursion

Recursion is when **a function calls itself**.

Example — Factorial

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

Output

```
120
```

---

# Slide 13 — Scope of Variables

Two types of variables exist.

### Local Variable

Defined inside a function.

Example

```python
def test():
    x = 10
```

---

### Global Variable

Defined outside function.

Example

```python
x = 20

def test():
    print(x)
```

Output

```
20
```

---

# Slide 14 — Docstrings

Docstrings are used to **document functions**.

Example

```python
def add(a, b):
    """This function returns sum of two numbers"""
    return a + b
```

Access documentation

```python
print(add.__doc__)
```

Output

```
This function returns sum of two numbers
```

---

# Slide 15 — Built-in Functions

Python has many built-in functions.

Examples

```
print()
len()
type()
max()
min()
sum()
```

Today we focus on:

✔ `max()`
✔ `min()`

---

# Slide 16 — max() Function

`max()` returns the **largest value**.

Example

```python
numbers = [10, 45, 7, 23]

print(max(numbers))
```

Output

```
45
```

---

# Slide 17 — max() with Multiple Values

Example

```python
print(max(10, 20, 30, 5))
```

Output

```
30
```

---

# Slide 18 — min() Function

`min()` returns the **smallest value**.

Example

```python
numbers = [10, 45, 7, 23]

print(min(numbers))
```

Output

```
7
```

---

# Slide 19 — Real Example

Student marks example.

```python
marks = [65, 78, 92, 56, 88]

print("Highest:", max(marks))
print("Lowest:", min(marks))
```

Output

```
Highest: 92
Lowest: 56
```

---

# Slide 20 — Practice Exercises

1️⃣ Write a function to return **maximum of two numbers**

Example

```
Input: 10, 20
Output: 20
```

---

2️⃣ Write a function to return **minimum of three numbers**

```
Input: 5, 8, 2
Output: 2
```

---

3️⃣ Write a function to return **max and min from list**

Example

```
numbers = [5, 12, 8, 20]
```

Output

```
Max = 20
Min = 5
```

---

# Slide 21 — Quick Summary

| Concept           | Purpose                    |
| ----------------- | -------------------------- |
| Function          | reusable code block        |
| Parameters        | input to function          |
| Return            | output from function       |
| Default arguments | optional values            |
| *args             | multiple arguments         |
| **kwargs          | multiple keyword arguments |
| Lambda            | short anonymous function   |
| Recursion         | function calling itself    |

---
