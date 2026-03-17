---

# 🎓 Day 4 – Python Basics (First Coding Class)
# Projects | % of course remaining, pyfiglet
---

# 🟦 Slide 1 — Title

## Day 4: Writing First Real Python Programs

Topics:

* Comments
* print()
* Strings
* New line
* Concatenation
* input()
* Variables
* Naming rules
* Data types
* Type checking
* Type errors

---

# 🟦 Slide 2 — What Is a Python Program?

A Python program is simply:

> A sequence of instructions executed by the interpreter.

Example:

```python
print("Hello")
print("World")
```

Execution is top-to-bottom.

---

# 🟦 Slide 3 — Comments

Comments are ignored by Python.

Used to explain code.

```python
# This is a comment
print("Hello")
```

Key rule:

* Starts with `#`
* Not executed

---

# 🟦 Slide 4 — print() Function

Used to display output.

```python
print("Hello World")
```

Important concept:

* print is a function
* Parentheses are required

---

# 🟦 Slide 5 — Strings

String = sequence of characters.

```python
print("Hello")
print('Python')
```

Can use:

* Double quotes
* Single quotes

---

# 🟦 Slide 6 — New Line (`\n`)

`\n` means new line.

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

Explain:

* `\n` = escape character

---

# 🟦 Slide 7 — String Concatenation

Concatenation = joining strings.

```python
print("Hello " + "World")
```

Important:

* Only same types allowed.

This fails:

```python
print("Age: " + 25)
```

Explain TypeError.

---

# 🟦 Slide 8 — input() Function

Used to take user input.

```python
name = input("Enter your name: ")
print("Hello " + name)
```

Important concept:

> input() always returns string.

Even if user enters number.

---

# 🟦 Slide 9 — Variables

Variable = container for storing data.

```python
x = 10
name = "Vivek"
```

Rules:

* No spaces
* Cannot start with number
* Case sensitive

Valid:

```
age
total_marks
studentName
```

Invalid:

```
1age
total marks
```

---

# 🟦 Slide 10 — Variable Naming Best Practices

Use:

* snake_case
* meaningful names

Bad:

```python
a = 5
```

Better:

```python
student_age = 5
```

---

# 🟦 Slide 11 — Data Types

Common data types:

| Type  | Example |
| ----- | ------- |
| int   | 5       |
| float | 3.14    |
| str   | "Hello" |
| bool  | True    |

---

# 🟦 Slide 12 — Checking Type

Use:

```python
print(type(5))
print(type("Hello"))
```

Output:

```
<class 'int'>
<class 'str'>
```

Connect to previous architecture discussion:

Everything in Python is an object.

---

# 🟦 Slide 13 — TypeError

Example:

```python
print("Age: " + 5)
```

Error:

```
TypeError
```

Why?

String + Integer not allowed.

Fix:

```python
print("Age: " + str(5))
```

---

# 🟦 Slide 14 — Converting Types

Convert using:

```python
int()
float()
str()
```

Example:

```python
age = input("Enter age: ")
age = int(age)
print(age + 5)
```

Explain:

* input gives string
* Need conversion

---

# 🟦 Slide 15 — Final Reference Program (Memory Demo)

Now use your reference program.

```python
import ctypes

# this is a comment
b = print("Hello, World!")
a = input("Press Enter to continue...\n")
address = bin(id(a))
print(f"The address of variable 'a' is: {address}")

print("Goodbye!")
```

Explain line by line:

* `import ctypes` → importing module
* `id(a)` → memory identity
* `bin()` → convert to binary
* f-string → formatted string

Important:

Don’t go too deep into memory here — just give preview.

---

# 🟦 Slide 16 — Execution Flow

When running program:

1. Interpreter reads file
2. Converts to bytecode
3. VM executes line by line
4. Output printed

Connect to previous sessions.

---

# 🟦 Slide 17 — Mini Practice Exercises

1. Take name and age from user.
2. Print:

   ```
   Hello Vivek, you are 30 years old.
   ```
3. Print number in binary using bin().

---

# 🟦 Slide 18 — Homework

1. Write program:

   * Take 2 numbers from user
   * Add them
   * Print result
2. Try causing TypeError intentionally.
3. Fix it.

---
