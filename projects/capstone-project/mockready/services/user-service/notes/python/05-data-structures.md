# Day 5 – Operators, Logic & Decision Making

## Agenda

Today we will learn:

1. Arithmetic operators
2. Order of operations (PEMDAS)
3. Built-in math functions
4. Comparison operators
5. Logical operators
6. f-strings
7. Decision making using `if / else`

Goal:

> By the end of this session you will be able to write programs that calculate values and make decisions.

---

# What Are Operators?

Operators are **symbols used to perform operations on values or variables**.

Example:

```python
5 + 3
```

Here:

* `5` and `3` → operands
* `+` → operator

Operators tell the computer **what action to perform**.

---

# Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning             | Example  |
| -------- | ------------------- | -------- |
| `+`      | Addition            | `5 + 2`  |
| `-`      | Subtraction         | `5 - 2`  |
| `*`      | Multiplication      | `5 * 2`  |
| `/`      | Division            | `5 / 2`  |
| `%`      | Modulus (remainder) | `5 % 2`  |
| `**`     | Power               | `2 ** 3` |
| `//`     | Floor division      | `5 // 2` |

Example:

```python
a = 10
b = 3

print(a + b)
print(a * b)
print(a % b)
```

---

# Order of Operations (PEMDAS)

Python follows this order:

```
Parentheses
Exponents
Multiplication
Division
Addition
Subtraction
```

Example:

```python
print(2 + 3 * 4)
```

Output:

```
14
```

Using parentheses:

```python
print((2 + 3) * 4)
```

Output:

```
20
```

---

# Built-in Math Functions

Python provides useful math functions.

### round()

Rounds a number.

```python
print(round(3.14159, 2))
```

Output

```
3.14
```

---

### abs()

Returns absolute value.

```python
print(abs(-10))
```

Output

```
10
```

---

### pow()

Power function.

```python
print(pow(2, 3))
```

Output

```
8
```

---

# Example Using Math Functions

```python
price = 123.456

rounded_price = round(price, 2)

print(rounded_price)
```

Output

```
123.46
```

---

# Comparison Operators

Comparison operators compare two values and return **True or False**.

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not equal        |
| `>`      | Greater          |
| `<`      | Less             |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

Example:

```python
print(10 > 5)
print(10 == 5)
```

Output

```
True
False
```

---

# Boolean Values

Comparison operators return **Boolean values**.

```
True
False
```

Example:

```python
age = 18
print(age >= 18)
```

Output

```
True
```

---

# Logical Operators

Logical operators combine conditions.

| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | Both conditions must be true |
| `or`     | At least one condition true  |
| `not`    | Reverses condition           |

Example:

```python
age = 20
citizen = True

print(age >= 18 and citizen)
```

Output

```
True
```

---

# Logical Operator Example

```python
print(True or False)
```

Output

```
True
```

---

# f-Strings (Formatted Strings)

f-strings allow us to insert variables inside text.

Syntax

```python
f"text {variable}"
```

Example:

```python
name = "Vivek"
score = 90

print(f"{name} scored {score} marks")
```

Output

```
Vivek scored 90 marks
```

---

# f-Strings With Calculations

```python
a = 10
b = 5

print(f"The sum of {a} and {b} is {a + b}")
```

Output

```
The sum of 10 and 5 is 15
```

---

# Decision Making

Programs often need to **make decisions**.

Example:

* If age ≥ 18 → allowed to vote
* Otherwise → not allowed

This is done using **if statements**.

---

# if Statement

Syntax

```python
if condition:
    statement
```

Example

```python
age = 20

if age >= 18:
    print("You can vote")
```

---

# if / else

If the condition is false, `else` runs.

```python
age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

Output

```
You cannot vote
```

---

# Interesting Program 1 – Even or Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
```

Concepts used

* modulus
* comparison
* if/else
* f-strings

---

# Interesting Program 2 – Student Grade Checker

```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
```

Good example of **decision making**.

---

# Interesting Program 3 – Login System

Uses logical operators.

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
```

Students usually enjoy this example.

---

# Small Exercise

Write a program that:

1. Takes two numbers from the user
2. Calculates their sum
3. Displays the result using an f-string

Example output

```
The sum of 10 and 5 is 15
```

---

# Summary

Today we learned:

* Arithmetic operators
* Order of operations (PEMDAS)
* Built-in math functions
* Comparison operators
* Logical operators
* f-strings
* Decision making using `if / else`

These allow programs to **calculate values and make decisions**.

---
