# Day 7 — Modules, Random Module & Lists

---

# 1. Introduction

Today we move one step further in Python learning.

Until now we learned:

* variables
* data types
* operators
* conditions
* loops

But real programs need two important things:

1. **Reusing existing code** (Modules)
2. **Storing multiple values together** (Data Structures)

Today we will learn both.

---

# 2. Warmup — Algorithm Thinking

Before learning new topics, we start with a **small algorithm problem**.

### Problem

Check if a number is **even or odd**.

Example

Input

```
7
```

Output

```
Odd
```

---

## Theory

This problem helps students understand **algorithm thinking**.

Algorithm means:

> A step-by-step procedure to solve a problem.

Every program follows an algorithm.

Example algorithm for this problem:

Step 1 — take number input
Step 2 — divide number by 2
Step 3 — check remainder
Step 4 — print even or odd

---

## Important Operator

We use the **modulus operator `%`**

```
%
```

It gives the **remainder after division**.

Example:

```
10 % 2 = 0
7 % 2 = 1
```

So

```
number % 2 == 0 → even
number % 2 != 0 → odd
```

---

## Code

```python
number = int(input("Enter number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## Explanation

Step 1

```
input()
```

gets user input.

Step 2

```
int()
```

converts string to integer.

Step 3

```
number % 2
```

checks remainder.

Step 4

Program prints result.

---

# 3. Python Modules

Now we move to an important Python concept.

### What is a Module?

A **module** is a file that contains Python code such as:

* functions
* variables
* classes

These are written by other developers so we can **reuse them**.

Instead of writing everything from scratch, we simply **import the module**.

---

## Real Life Analogy

Think of modules like a **toolbox**.

Example:

A mechanic does not build tools every day.

He uses tools like:

* screwdriver
* wrench
* hammer

Similarly in programming we use ready-made tools.

---

## Why Modules Are Important

Modules provide many advantages.

### Code Reusability

You do not need to rewrite common logic.

Example:

* mathematical calculations
* random numbers
* date and time

---

### Faster Development

Programs can be built faster because most functionality already exists.

---

### Tested Code

Modules are written and tested by many developers, so they are reliable.

---

### Organization

Modules help organize large programs into multiple files.

---

## Types of Modules

There are two main types.

### 1. Built-in Modules

These are provided by Python.

Examples:

```
math
random
datetime
os
sys
```

---

### 2. User Defined Modules

Developers can create their own modules.

Example:

```
calculator.py
database.py
utils.py
```

These can be imported into other programs.

---

# 4. Importing Modules

To use a module we must **import it**.

### Syntax

```python
import module_name
```

Example

```python
import random
```

This tells Python:

> Load the random module so we can use its functions.

---

# 5. Random Module

The **random module** generates random values.

Random values are widely used in software.

Examples:

* games
* password generators
* OTP systems
* simulations
* testing systems

---

## Common Functions in Random Module

### randint()

Generates a random integer between two values.

Example:

```
random.randint(start, end)
```

---

### Example

```python
import random

number = random.randint(1, 10)

print(number)
```

Output changes every time.

Example outputs:

```
3
7
9
2
```

---

## random.choice()

This function selects a **random element from a sequence**.

Example syntax

```
random.choice(sequence)
```

---

### Example

```python
import random

fruits = ["apple", "banana", "mango"]

print(random.choice(fruits))
```

Possible output:

```
apple
banana
mango
```

---

# 6. Fun Example — Dice Simulator

Let's simulate a **dice roll**.

A real dice produces numbers between **1 and 6**.

We can simulate this using Python.

---

### Code

```python
import random

dice = random.randint(1, 6)

print("Dice result:", dice)
```

Each time we run the program, the result will change.

Example outputs:

```
Dice result: 3
Dice result: 6
Dice result: 1
```

---

# 7. Lists — First Data Structure

Now we learn our first **data structure**.

### What is a Data Structure?

A data structure is a way to **organize and store data efficiently**.

Programs often need to store **many values together**.

For this we use **lists**.

---

## What is a List?

A **list** is a collection of multiple values stored in a single variable.

Example concept:

```
10, 20, 30, 40
```

In Python we store these values using **square brackets**.

---

## List Syntax

```python
numbers = [10, 20, 30, 40]
```

Here

```
numbers
```

is the variable name.

The list contains **four elements**.

---

## Characteristics of Lists

Lists have several important properties.

### Ordered

Items maintain the order in which they were inserted.

```
[10,20,30]
```

10 comes first.

---

### Mutable

Lists can be modified.

Elements can be:

* added
* removed
* changed

---

### Allow Duplicate Values

Example

```
[10,10,20,30]
```

Duplicates are allowed.

---

### Can Store Different Data Types

Example

```python
data = [10, "Python", True]
```

---

# 8. Accessing List Elements

Each element in a list has a **position number called index**.

Important rule:

> Index starts from **0**

Example list

```
[10, 20, 30, 40]
```

Indexes

```
0 → 10
1 → 20
2 → 30
3 → 40
```

---

### Access Syntax

```python
list_name[index]
```

Example

```python
numbers = [10,20,30,40]

print(numbers[0])
print(numbers[2])
```

Output

```
10
30
```

---

# 9. Adding Items to List

We can add elements using the **append()** method.

### append()

Adds an element at the end of the list.

---

### Example

```python
numbers = [1,2,3]

numbers.append(4)

print(numbers)
```

Output

```
[1,2,3,4]
```

---

# 10. Nested Lists

A **nested list** means a list inside another list.

Example structure

```
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

This structure is often used to represent:

* tables
* matrices
* grids
* game boards

---

### Example Code

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0])
print(matrix[1][2])
```

Output

```
[1,2,3]
6
```

---

# 11. For Loop with Lists

Lists are commonly used with loops.

Loops allow us to **process each element of a list**.

---

### Example

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

Output

```
apple
banana
mango
```

---

## Explanation

The loop automatically picks one element at a time.

Iteration sequence:

```
fruit = apple
fruit = banana
fruit = mango
```

---

# 12. Mini Project — Random Password Generator

Now students combine everything they learned.

We will build a **simple password generator**.

---

## Step 1 — Import Random

```python
import random
```

---

## Step 2 — Define Characters

```python
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%"
```

---

## Step 3 — Combine All Characters

```python
all_chars = letters + numbers + symbols
```

---

## Step 4 — Generate Password

```python
password = ""

for i in range(8):
    password += random.choice(all_chars)

print("Generated Password:", password)
```

Example output

```
a7@k2#d1
```

---

# 13. Summary

Today we learned:

* algorithm thinking
* modulus operator
* Python modules
* random module
* lists
* accessing list elements
* nested lists
* loops with lists
* password generator project
