# Slide 1 — Day 6

# Building Real Programs & Introduction to Loops

Today we will build real programs using Python.

Topics for today:

• Calculator Program
• Largest of Three Numbers
• ATM Machine Simulator
• Repetition Problem in Programming
• Introduction to Loops

Goal:

By the end of today, you will be able to build small programs and understand **why loops are needed**.

---

# Slide 2 — What We Have Learned So Far

So far we know:

• Variables
• Input from user
• Arithmetic operators
• Comparison operators
• If / Else conditions

Today we will combine these concepts to build **real applications**.

---

# Slide 3 — Program 1: Simple Calculator

A calculator performs operations on numbers.

Operations:

1 Add
2 Subtract
3 Multiply
4 Divide

User enters numbers and chooses the operation.

---

# Slide 4 — Calculator Program

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result:", num1 + num2)

elif choice == 2:
    print("Result:", num1 - num2)

elif choice == 3:
    print("Result:", num1 * num2)

elif choice == 4:
    print("Result:", num1 / num2)

else:
    print("Invalid option")
```

---

# Slide 5 — Largest of Three Numbers

Problem:

Find the **largest number** among three numbers.

Example:

Numbers → 10, 25, 15

Largest number → **25**

---

# Slide 6 — Largest Number Program

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)

elif b >= a and b >= c:
    print("Largest number is:", b)

else:
    print("Largest number is:", c)
```

---

# Slide 7 — Logical Operator

Python logical operator:

```
and
```

Example:

```
a >= b and a >= c
```

Meaning:

The condition is true only when **both conditions are true**.

---

# Slide 8 — Program 3: ATM Machine

An ATM machine allows users to:

1 Check balance
2 Withdraw money
3 Deposit money
4 Exit

We will simulate a simple ATM program.

---

# Slide 9 — ATM Program

```python
balance = 5000

print("Welcome to ATM")

print("1 Check Balance")
print("2 Withdraw Money")
print("3 Deposit Money")
print("4 Exit")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Transaction successful")
        print("Remaining balance:", balance)

    else:
        print("Insufficient balance")

elif choice == 3:
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("Money deposited")
    print("New balance:", balance)

elif choice == 4:
    print("Thank you for using ATM")

else:
    print("Invalid option")
```

---

# Slide 10 — Updating Variables

Variables can change during program execution.

Example:

```
balance = balance - amount
```

If balance = 5000 and withdrawal = 1000

New balance becomes:

```
4000
```

---

# Slide 11 — A Problem in Our Programs

In our calculator:

After one calculation → program stops.

In our ATM:

After one operation → program stops.

But in real life:

Programs continue running.

Example:

ATM allows multiple transactions.

---

# Slide 12 — Example of Repetition

Calculator example:

```
2 + 3
5 * 6
10 / 2
```

ATM example:

```
Check balance
Withdraw money
Deposit money
Check balance again
```

Programs must be able to **repeat tasks automatically**.

---

# Slide 13 — Repetition Problem

Without repetition we would need to write code like this:

```
print(1)
print(2)
print(3)
print(4)
print(5)
```

But imagine printing numbers up to **1000**.

This would require writing **1000 lines of code**.

---

# Slide 14 — Solution: Loops

Loops solve the repetition problem.

Definition:

A loop allows a program to **repeat a block of code multiple times automatically**.

Instead of writing the same code again and again.

---

# Slide 15 — Types of Loops in Python

Python mainly has two types of loops:

```
while loop
for loop
```

These loops allow programs to run **repeatedly**.

---

# Slide 16 — Example Idea Using ATM

Imagine an ATM program that keeps running.

Logic:

```
Show ATM menu
Perform operation
Return to menu
Repeat
```

This is possible using **loops**.

---

# Slide 17 — What We Will Learn Next

Next session we will learn:

• While loop
• For loop
• Range function
• Repeating programs automatically

We will upgrade our programs to build:

• Continuous calculator
• Real ATM system
• Small games

---

# Slide 18 — Summary

Today we learned:

• Calculator program
• Largest of three numbers
• ATM machine simulator
• Problem of repetition in programming
• Introduction to loops

Loops will allow programs to **run continuously and automate tasks**.

---

If you want, I can also convert this into a **ready-to-use PowerPoint (.pptx)** so you can directly use it for your class.
