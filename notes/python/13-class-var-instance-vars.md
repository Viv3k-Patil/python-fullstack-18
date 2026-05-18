# Python Class Variables and Instance Variables

## Intuition First: What Problem Are We Solving?

Imagine you're building a school management system. You need to create many `Student` objects. Some information is **unique to each student** (like their name, roll number, marks). Other information is **shared across all students** (like the school name, total number of students, or default grade policy).

Python gives us two tools:
- **Instance variables** → data that belongs to **one specific object**
- **Class variables** → data that belongs to the **class itself** and is shared by all objects

Understanding the difference prevents bugs where data accidentally gets shared or doesn't get shared when it should.

***

## 1. Instance Variables – Data Unique to Each Object

### Intuition

An instance variable is like a personal notebook for each student. Student A has their own name, Student B has their own name. They don't share notebooks.

### Definition

Instance variables are defined **inside methods** (usually `__init__`) using **`self.variable_name`**. Each object gets its own separate copy.

### Example – Building It Step by Step

**Step 1: Start with a class (no variables yet)**
```python
class Student:
    pass

s1 = Student()
s2 = Student()
```

**Step 2: Try to store data without instance variables (WRONG)**
```python
s1.name = "Rahul"
s2.name = "Priya"
```
This works, but it's ad-hoc. There's no guarantee every student has a `name`. Better to enforce it in `__init__`.

**Step 3: Add `__init__` with instance variables (CORRECT)**
```python
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
```

**Step 4: Create objects**
```python
s1 = Student("Rahul", "2024-CS-001", 85)
s2 = Student("Priya", "2024-CS-002", 92)
```

**Step 5: Access instance variables**
```python
print(s1.name)      # "Rahul"
print(s2.name)      # "Priya"
print(s1.marks)     # 85
print(s2.marks)     # 92
```

Each object has its **own** `name`, `roll_no`, and `marks`. Changing `s1.marks` does **not** affect `s2.marks`.

### Key Points About Instance Variables

| Aspect | Explanation |
|---|---|
| **Where defined** | Inside methods using `self.variable_name` |
| **Where typically created** | In `__init__` method |
| **Who owns it** | Each object (instance) owns its own copy |
| **Memory** | Separate memory for each object |
| **Use when** | Data is different for each object (name, age, marks, email) |

### Common Mistake – Forgetting `self`

```python
class Student:
    def __init__(self, name):
        name = name  # ❌ WRONG: creates local variable, not instance variable
```

What happens here?
- `name = name` creates a **local variable** inside `__init__`
- It disappears when `__init__` finishes
- `s1.name` will **not exist**

**Correct version:**
```python
class Student:
    def __init__(self, name):
        self.name = name  # ✅ CORRECT: creates instance variable
```

Now `s1.name` exists and persists.

***

## 2. Class Variables – Data Shared Across All Objects

### Intuition

A class variable is like a school notice board. Every student can see it, and if the school updates it, **all students see the updated value**. It's shared data.

### Definition

Class variables are defined **directly in the class body**, outside any method. They belong to the class itself, not to any individual object. All instances share the same copy.

### Example – Building It Step by Step

**Step 1: Add a class variable**
```python
class Student:
    school_name = "GP School Nagpur"  # class variable
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
```

**Step 2: Access class variable**
```python
s1 = Student("Rahul", "001")
s2 = Student("Priya", "002")

print(s1.school_name)  # "GP School Nagpur"
print(s2.school_name)  # "GP School Nagpur"
print(Student.school_name)  # Also works: Student.school_name
```

Both `s1` and `s2` see the **same** `school_name`.

**Step 3: Update class variable**
```python
Student.school_name = "New GP School Nagpur"

print(s1.school_name)  # "New GP School Nagpur"
print(s2.school_name)  # "New GP School Nagpur"
```

Both objects now see the **updated** value because they share the same class variable.

### Key Points About Class Variables

| Aspect | Explanation |
|---|---|
| **Where defined** | Directly in class body, outside methods |
| **Who owns it** | The class owns it, all instances share it |
| **Memory** | Single copy shared by all objects |
| **Access** | `ClassName.variable` or `object.variable` |
| **Use when** | Data is same for all objects (school name, role, counter, config) |

### Class Variable Use Cases

1. **Constants**
   ```python
   class Student:
       MAX_MARKS = 100  # constant shared by all
   ```

2. **Shared configuration**
   ```python
   class Student:
       grade_policy = "A if >=90, B if >=80"
   ```

3. **Counters**
   ```python
   class Student:
       total_students = 0
       
       def __init__(self, name):
           self.name = name
           Student.total_students += 1  # increment counter
   ```

4. **Caching or shared resources**
   ```python
   class Database:
       connection_pool = []  # shared by all instances
   ```

***

## 3. Access Order – How Python Looks Up Attributes

When you write `obj.x`, Python searches in this order:

1. **Check instance dictionary first** (`obj.__dict__`)
2. **Check class dictionary** (`Student.__dict__`)
3. **Check parent classes** (if inheritance exists)

### Example

```python
class Student:
    school_name = "GP School"  # class variable
    
    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Rahul")

print(s1.name)         # "Rahul" → found in instance
print(s1.school_name)  # "GP School" → not in instance, found in class
```

### What If Instance and Class Have Same Name?

```python
class Student:
    role = "student"  # class variable
    
    def __init__(self, name):
        self.name = name
        # No instance variable called 'role' here

s1 = Student("Rahul")
print(s1.role)  # "student" → found in class
```

Now create an instance variable with the **same name**:

```python
s1.role = "teacher"  # creates instance variable 'role' for s1 ONLY

print(s1.role)       # "teacher" → instance variable found first
print(Student.role)  # "student" → class variable unchanged
```

**Key rule:** Python **always** checks the instance first. If found there, it doesn't look at the class.

***

## 4. Updating Class Variables – The Tricky Part

### Updating Through the Class (Correct)

```python
class Student:
    total_students = 0

Student.total_students = 10  # ✅ updates class variable for all

s1 = Student("Rahul")
s2 = Student("Priya")

print(s1.total_students)  # 10
print(s2.total_students)  # 10
```

### Updating Through an Instance (Creates Instance Variable)

```python
class Student:
    total_students = 0

s1 = Student("Rahul")
s1.total_students = 20  # ❌ creates instance variable for s1 ONLY

print(s1.total_students)   # 20 (instance variable)
print(s2.total_students)   # 0 (class variable, unchanged)
print(Student.total_students)  # 0 (class variable, unchanged)
```

**What happened?**
- `s1.total_students = 20` created a **new instance variable** on `s1`
- It did **not** update the class variable
- Now `s1` has its own `total_students` that shadows the class variable

### How to Update Class Variable Correctly from Inside a Method

```python
class Student:
    total_students = 0
    
    @classmethod
    def increment_total(cls):
        cls.total_students += 1  # ✅ updates class variable

Student.increment_total()
print(Student.total_students)  # 1
```

***

## 5. Side-by-Side Comparison

| Feature | Instance Variable | Class Variable |
|---|---|---|
| **Where defined** | Inside method using `self.var` | In class body, outside methods |
| **Who owns it** | Each object owns its own copy | Class owns it, all objects share |
| **Number of copies** | One per object | One total |
| **Used for** | Unique data (name, age, marks) | Shared data (constants, counters, config) |
| **Access** | `obj.var` | `ClassName.var` or `obj.var` |
| **Updated via class** | N/A | `ClassName.var = value` updates all |
| **Updated via instance** | `obj.var = value` affects only that object | `obj.var = value` creates instance variable (shadowing) |

***

## 6. Complete Working Example

```python
class Student:
    # Class variable
    school_name = "GP School Nagpur"
    total_students = 0
    
    def __init__(self, name, roll_no, marks):
        # Instance variables
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
        # Update class variable
        Student.total_students += 1
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"School: {Student.school_name}")
        print(f"Total Students: {Student.total_students}")

# Create objects
s1 = Student("Rahul", "2024-CS-001", 85)
s2 = Student("Priya", "2024-CS-002", 92)
s3 = Student("Amit", "2024-CS-003", 78)

# Access instance variables
print(s1.name)  # "Rahul"
print(s2.name)  # "Priya"

# Access class variable
print(Student.school_name)       # "GP School Nagpur"
print(Student.total_students)    # 3

# Update class variable
Student.school_name = "New GP School Nagpur"
print(s1.school_name)  # "New GP School Nagpur" (all see update)

# Mistake: shadowing class variable
s1.role = "honors_student"  # creates instance variable for s1 only
print(s1.role)  # "honors_student"
# s2.role will raise AttributeError
```

***

## 7. Summary (Cheat Sheet)

| Concept | Key Idea | Code Pattern |
|---|---|---|
| **Instance variable** | Unique per object | `self.name = name` in `__init__` |
| **Class variable** | Shared by all objects | `variable = value` in class body |
| **Access order** | Instance first, then class | `obj.x` → check `obj.__dict__`, then `Class.__dict__` |
| **Update class variable** | Use class name | `ClassName.var = value` |
| **Mistake to avoid** | `age = age` instead of `self.age = age` | Always use `self.` for instance variables |

**Final rule:**
- Use **instance variables** when data is different for each object
- Use **class variables** when data is the same for all objects