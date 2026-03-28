# 📘 Day 12 — Classes & Objects (Deep Dive)

---

## Slide 1 — Reality of Development

* Every application = **data + operations on data**
* Examples:

  * Instagram → users, posts, likes
  * Banking → accounts, transactions
  * E-commerce → products, orders

👉 Problem is not code
👉 Problem is **managing data properly**

---

## Slide 2 — Simple Data vs Complex Data

Simple:

```python
age = 25
```

Complex:

```python
name = "Vivek"
age = 25
email = "vivek@gmail.com"
phone = "1234567890"
```

👉 This is **one user**

Now imagine:

* 100 users
* 10,000 users

---

## Slide 3 — Scaling Problem

```python
user1_name = "A"
user1_age = 20

user2_name = "B"
user2_age = 25
```

Problems:

* Too many variables
* Naming confusion
* No grouping
* Hard to maintain
* Impossible to scale

---

## Slide 4 — Using Dictionary

```python
user = {
    "name": "Vivek",
    "age": 25
}
```

Advantages:

* Grouped data
* Cleaner than variables

---

## Slide 5 — Dictionary Limitations

```python
user["random"] = "something"
```

Problems:

* No restriction on structure
* No guarantee of required fields
* No behavior (only data)
* No reusability rules

👉 Still not enough for real applications

---

## Slide 6 — Need for Better Structure

We need:

* Fixed structure
* Data validation (basic level)
* Behavior attached to data
* Reusability
* Clean design

👉 This leads to **Classes**

---

## Slide 7 — What is a Class?

* A **blueprint for structured data**
* Defines:

  * What data exists
  * What actions can be performed

👉 Class = **Custom Data Type**

---

## Slide 8 — Creating a Class

```python
class User:
    pass
```

* `class` → keyword
* `User` → custom type name

👉 Nothing inside yet

---

## Slide 9 — Creating Object

```python
user1 = User()
```

* `user1` → object
* Instance of class

👉 Memory allocated for this object

---

## Slide 10 — Object Identity

```python
user1 = User()
user2 = User()
```

* Both are separate objects
* Stored at different memory locations

👉 Same structure, different data

---

## Slide 11 — Adding Attributes

```python
user1.name = "Vivek"
user1.age = 25
```

* Attributes = variables inside object

👉 Now object holds real data

---

## Slide 12 — Problem with Manual Assignment

```python
user1 = User()
user1.name = "Vivek"
user1.age = 25
```

Problems:

* Repetitive
* Error-prone
* Forgetting fields is common

👉 Need automation

---

## Slide 13 — Adding Behavior (Methods)

```python
class User:
    def greet(self):
        print("Hello user")
```

* Function inside class = **method**

---

## Slide 14 — Calling Method

```python
user1 = User()
user1.greet()
```

👉 Python automatically passes object as `self`

---

## Slide 15 — Understanding `self`

```python
class User:
    def greet(self):
        print(self)
```

* `self` = current object reference

Example:

```python
user1 = User()
print(user1)
```

👉 Both print same reference

---

## Slide 16 — Accessing Object Data

```python
class User:
    def greet(self):
        print(self.name)
```

```python
user1 = User()
user1.name = "Vivek"
user1.greet()
```

👉 Method can access object data

---

## Slide 17 — Constructor Introduction

Problem:

* Manual assignment is repetitive

Solution:

* Constructor

---

## Slide 18 — Constructor Syntax

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

* `__init__` runs automatically
* Initializes object

---

## Slide 19 — Object Creation with Constructor

```python
user1 = User("Vivek", 25)
user2 = User("Rahul", 30)
```

👉 Data is set during creation

---

## Slide 20 — Flow of Execution

When this runs:

```python
user1 = User("Vivek", 25)
```

Steps:

1. Object created
2. `__init__` called
3. `self.name = "Vivek"`
4. `self.age = 25`

---

## Slide 21 — Multiple Objects

```python
user1 = User("A", 20)
user2 = User("B", 25)
```

👉 Each object has its own data

---

## Slide 22 — Adding More Methods

```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

    def change_name(self, new_name):
        self.name = new_name
```

---

## Slide 23 — Using Methods

```python
user1 = User("Vivek")

user1.greet()
user1.change_name("Rahul")
user1.greet()
```

---

## Slide 24 — Real Example (Car)

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(self.brand, "is driving at", self.speed)

    def accelerate(self, value):
        self.speed += value
```

---

## Slide 25 — Using Car Class

```python
car1 = Car("BMW", 100)

car1.drive()
car1.accelerate(20)
car1.drive()
```

---

## Slide 26 — Key Concepts Recap

* Class → blueprint / structure
* Object → real instance
* Attribute → data inside object
* Method → function inside class
* `self` → current object
* `__init__` → constructor

---

## Slide 27 — Why Classes Matter

* Clean code
* Reusability
* Better structure
* Real-world modeling
* Easier debugging

---

## Slide 28 — Common Mistakes

❌ Missing `self`
❌ Forgetting to initialize attributes
❌ Calling method without object
❌ Treating class like dictionary

---

## Slide 29 — Practice

1. Create `Student` class

   * name, marks

2. Add methods:

   * display()
   * update_marks()

3. Create 2 students and test

---

## Slide 30 — Final Thought

* Code is temporary
* Structure is permanent

👉 Good developers:

* Think about **data design first**
* Then write code

🚀 Classes help you become a real developer
