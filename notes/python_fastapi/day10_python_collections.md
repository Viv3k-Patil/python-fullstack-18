# Day 10 – Sets and Dictionaries

---

# Agenda

Today we will learn:

1. What is a **Set**
2. Properties of Sets
3. Set methods
4. Real-life examples of Sets
5. What is a **Dictionary**
6. Key–Value concept
7. Dictionary methods
8. Real-life examples
9. Practice exercises

Goal:

> By the end of this session, you will understand how Python stores **unique values and key-value data**.

---

# What is a Set?

A **set** is a collection that stores **unique values**.

Sets are:

• Unordered
• Do not allow duplicates
• Mutable (can add/remove items)

Example:

```python
numbers = {1, 2, 3, 4}
```

---

# Example – Duplicate Removal

```python
numbers = {1, 2, 3, 3, 4, 4, 5}

print(numbers)
```

Output

```
{1, 2, 3, 4, 5}
```

Duplicates are **automatically removed**.

---

# When Are Sets Useful?

Sets are useful when we want **unique values only**.

Examples:

• Unique student IDs
• Unique email addresses
• Unique tags
• Removing duplicates from data

Example:

```python
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}

print(emails)
```

Output

```
{'a@gmail.com', 'b@gmail.com'}
```

---

# Set Methods

Common methods:

• add()
• remove()
• len()

---

# add() – Add Item

```python
numbers = {1,2,3}

numbers.add(4)

print(numbers)
```

Output

```
{1,2,3,4}
```

---

# remove() – Remove Item

```python
numbers = {1,2,3}

numbers.remove(2)

print(numbers)
```

Output

```
{1,3}
```

---

# Real-Life Example – Unique Visitors

```python
visitors = {"Rahul", "Amit", "Sara"}

visitors.add("John")

print(visitors)
```

Useful in:

• websites
• login systems
• analytics

---

# What is a Dictionary?

A **dictionary** stores data using **key–value pairs**.

Example:

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Computer Science"
}
```

Here:

| Key    | Value            |
| ------ | ---------------- |
| name   | Rahul            |
| age    | 21               |
| course | Computer Science |

---

# Accessing Dictionary Values

```python
student = {
    "name": "Rahul",
    "age": 21
}

print(student["name"])
```

Output

```
Rahul
```

---

# Updating Dictionary Values

```python
student = {
    "name": "Rahul",
    "age": 21
}

student["age"] = 22

print(student)
```

Output

```
{'name': 'Rahul', 'age': 22}
```

---

# Adding New Data

```python
student = {
    "name": "Rahul",
    "age": 21
}

student["city"] = "Pune"

print(student)
```

Output

```
{'name': 'Rahul', 'age': 21, 'city': 'Pune'}
```

---

# Dictionary Methods

Common methods:

• keys()
• values()
• items()

---

# keys()

Returns all keys.

```python
student = {"name":"Rahul","age":21}

print(student.keys())
```

Output

```
dict_keys(['name','age'])
```

---

# values()

Returns all values.

```python
print(student.values())
```

Output

```
dict_values(['Rahul',21])
```

---

# items()

Returns both key and value.

```python
print(student.items())
```

Output

```
dict_items([('name','Rahul'),('age',21)])
```

---

# Looping Through Dictionary

```python
student = {
    "name": "Rahul",
    "age": 21
}

for key, value in student.items():
    print(key, value)
```

Output

```
name Rahul
age 21
```

---

# Real-Life Example – User Profile

```python
user = {
    "username": "vivek",
    "email": "vivek@gmail.com",
    "role": "admin"
}

print(user["email"])
```

Used in:

• APIs
• databases
• backend systems

---

# Difference Between Set and Dictionary

| Feature    | Set         | Dictionary          |
| ---------- | ----------- | ------------------- |
| Structure  | Values only | Key-value pairs     |
| Duplicates | Not allowed | Keys must be unique |
| Brackets   | {}          | {}                  |
| Access     | No index    | Access by key       |

---

# Practice Exercise 1

Create a **set of 5 numbers**.

Add a new number using `add()`.

---

# Practice Exercise 2

Create a **set with duplicate numbers**.

Print the set and observe duplicates removed.

---

# Practice Exercise 3

Create a dictionary storing:

name
age
city

Print the name.

---

# Practice Exercise 4

Loop through a dictionary and print key and value.

---

# Summary

Today we learned:

• Sets and unique values
• Set methods
• Dictionaries and key-value storage
• Dictionary methods
• Looping through dictionaries
