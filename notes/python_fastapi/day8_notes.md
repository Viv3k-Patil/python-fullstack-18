# Day 8 – Lists, Tuples & For Loops

---

# Agenda

Today we will learn:

1. Why we need collections in programming
2. Lists – storing multiple values
3. Accessing values using indexes
4. Important list methods
5. Tuples – immutable collections
6. Difference between List vs Tuple
7. For loop – repeating tasks
8. Iterating through lists
9. Real-world examples

Goal:

> By the end of this session you will be able to store multiple values and process them using loops.

---

# Problem Before Collections

Before lists, we stored values like this:

```
student1 = "Rahul"
student2 = "Amit"
student3 = "Sara"
student4 = "John"
```

Problems:

• Too many variables
• Hard to manage
• Hard to process data
• Impossible to loop easily

Programming solution:

**Collections**

Collections store **multiple values in one variable.**

---

# What is a List?

A **list** is a collection that stores multiple values.

Lists are:

• Ordered
• Changeable (mutable)
• Allow duplicates

Example:

```
fruits = ["apple", "banana", "mango"]
```

One variable → multiple values.

---

# List Visualization

```
fruits = ["apple", "banana", "mango"]
```

| Index | Value  |
| ----- | ------ |
| 0     | apple  |
| 1     | banana |
| 2     | mango  |

Index always starts from **0**.

---

# Accessing List Elements

Example:

```
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[2])
```

Output

```
apple
mango
```

Explanation:

We use **index numbers** to access list items.

---

# Updating List Values

Lists are **mutable**, meaning we can change values.

Example:

```
fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)
```

Output:

```
['apple', 'orange', 'mango']
```

---

# Important List Methods

Lists come with **built-in methods**.

These methods help us modify lists easily.

Common ones:

• append()
• remove()
• pop()
• len()

---

# append() – Add Item

Adds an item at the end.

```
fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)
```

Output

```
['apple', 'banana', 'mango']
```

---

# remove() – Remove Item

Removes a specific item.

```
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)
```

Output

```
['apple', 'mango']
```

---

# pop() – Remove Last Item

Removes the last element.

```
numbers = [10,20,30]

numbers.pop()

print(numbers)
```

Output

```
[10,20]
```

---

# len() – Count Items

Returns number of items.

```
fruits = ["apple","banana","mango"]

print(len(fruits))
```

Output

```
3
```

---

# Real Life Example – Shopping List

```
shopping = ["milk", "bread", "eggs"]

shopping.append("butter")

print(shopping)
```

Output

```
['milk', 'bread', 'eggs', 'butter']
```

Lists are commonly used for:

• shopping items
• student marks
• product lists
• users in a system

---

# What is a Tuple?

A **tuple** is similar to a list but **cannot be modified**.

Example:

```
coordinates = (18.52, 73.85)
```

Tuples are:

• Ordered
• Immutable (cannot change)
• Allow duplicates

---

# Tuple Example

```
colors = ("red","green","blue")

print(colors[1])
```

Output

```
green
```

Tuples are accessed using indexes just like lists.

---

# Why Tuples Exist

Tuples are used when data **should not change**.

Examples:

• GPS coordinates
• Days of the week
• Database records
• Fixed configuration values

Example:

```
days = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
```

Days should **never change**.

---

# Difference Between List and Tuple

| Feature         | List | Tuple |
| --------------- | ---- | ----- |
| Brackets        | []   | ()    |
| Mutable         | Yes  | No    |
| Add elements    | Yes  | No    |
| Remove elements | Yes  | No    |

Example:

```
numbers_list = [1,2,3]
numbers_tuple = (1,2,3)
```

---

# What is a Loop?

Often we need to repeat tasks.

Example:

```
print("Hello")
print("Hello")
print("Hello")
```

This is repetitive.

Programming solution:

**Loops**

---

# What is a For Loop?

A **for loop repeats a block of code for each item in a collection.**

Example:

```
students = ["Rahul","Amit","Sara"]

for student in students:
    print(student)
```

Output

```
Rahul
Amit
Sara
```

---

# How For Loop Works

```
for item in collection:
    code to execute
```

Step-by-step:

1. Take first item
2. Run the code
3. Move to next item
4. Repeat until finished

---

# Real Life Example – Student Marks

```
marks = [85,90,78,92]

for mark in marks:
    print(mark)
```

Output

```
85
90
78
92
```

---

# Real Life Example – Shopping Cart

```
cart = ["milk","bread","eggs"]

for item in cart:
    print("Buy", item)
```

Output

```
Buy milk
Buy bread
Buy eggs
```

---

# Combining List + Loop

Calculate total marks.

```
marks = [80,70,90]

total = 0

for mark in marks:
    total = total + mark

print(total)
```

Output

```
240
```

---

# Practice Exercise 1

Create a list of 5 fruits.

Print each fruit using a **for loop**.

---

# Practice Exercise 2

Create a shopping list.

Add one item using `append()`.

Print the updated list.

---

# Practice Exercise 3

Create a tuple of 3 colors.

Print the **second color**.

---

# Practice Exercise 4

Print numbers from this list using a loop.

```
numbers = [10,20,30,40]
```

---

# Summary

Today we learned:

• What collections are
• Lists and how to use them
• List methods
• Tuples and immutability
• For loops
• Iterating through lists
