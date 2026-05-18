# Python Inheritance — Notes

---

## 1. Definition

* Inheritance allows a class (child) to acquire properties and methods of another class (parent).

---

## 2. Basic Structure

```python
class Parent:
    def method(self):
        pass

class Child(Parent):
    pass
```

---

## 3. Real-World Base Model Example

```python
from datetime import datetime

class BaseModel:
    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.created_by = created_by
        self.updated_by = created_by

    def update(self, updated_by):
        self.updated_at = datetime.now()
        self.updated_by = updated_by
```

```python
class User(BaseModel):
    def __init__(self, name, created_by):
        super().__init__(created_by)
        self.name = name


class Complaint(BaseModel):
    def __init__(self, text, created_by):
        super().__init__(created_by)
        self.text = text
```

---

## 4. Constructor Behavior

* If no `__init__` is defined → default constructor is used
* If child does not define constructor → parent constructor is used
* If child defines constructor → parent constructor is NOT called automatically
* Use `super()` to call parent constructor

```python
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")
```

---

## 5. Method Overriding

* Child class defines same method as parent
* Child method overrides parent method

```python
class BaseModel:
    def save(self):
        print("Base save")


class User(BaseModel):
    def save(self):
        print("User save")
```

---

## 6. Using `super()` in Overriding

```python
class User(BaseModel):
    def save(self):
        print("Custom logic")
        super().save()
```

---

## 7. Types of Inheritance

### 7.1 Single Inheritance

```python
class A:
    pass

class B(A):
    pass
```

---

### 7.2 Multiple Inheritance

```python
class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A, B):
    pass
```

---

### 7.3 Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

### 7.4 Hierarchical Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```

---

## 8. Method Resolution Order (MRO)

* Defines order in which methods are searched

```python
class A:
    def test(self):
        print("A")

class B:
    def test(self):
        print("B")

class C(A, B):
    pass

print(C.__mro__)
```

---

## 9. MRO Behavior

* Left-to-right resolution
* First matching method is executed

```python
class Hybrid(Dog, Cat):
    pass
```

MRO:

```
Hybrid → Dog → Cat → Animal
```

---

## 10. `super()` Behavior

* Calls next class in MRO

```python
class A:
    def process(self):
        print("A")
        super().process()

class B:
    def process(self):
        print("B")
        super().process()

class C(A, B):
    def process(self):
        print("C")
        super().process()

class D:
    def process(self):
        print("D")

class Final(C, D):
    pass

Final().process()
```

---

## 11. Multiple Inheritance Example (Animal)

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Dog start")
        super().speak()


class Cat(Animal):
    def speak(self):
        print("Cat start")
        super().speak()


class Hybrid(Dog, Cat):
    def speak(self):
        print("Hybrid start")
        super().speak()
```

Output:

```
Hybrid start
Dog start
Cat start
Animal sound
```

---

## 12. Controller Example

```python
class BaseController:
    def log(self, message):
        print(f"[LOG]: {message}")

    def authenticate(self, user):
        if user != "admin":
            raise Exception("Unauthorized")

    def success_response(self, data):
        return {"status": "success", "data": data}
```

```python
class UserController(BaseController):
    def get_user(self, user):
        self.authenticate(user)
        self.log("Fetching user")
        return self.success_response({"name": "Vivek"})
```

```python
class ComplaintController(BaseController):
    def create_complaint(self, user, text):
        self.authenticate(user)
        self.log("Creating complaint")
        return self.success_response({"complaint": text})
```

---

## 13. Multiple Inheritance with Mixins

```python
class LoggingMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class AuthMixin:
    def authenticate(self, user):
        if user != "admin":
            raise Exception("Unauthorized")


class UserController(AuthMixin, LoggingMixin):
    def get_user(self, user):
        self.authenticate(user)
        self.log("Fetching user")
        return {"name": "Vivek"}
```

---

## 14. Key Points

* Child class inherits methods and attributes from parent
* Child can override parent methods
* `super()` is used to call parent or next in MRO
* Multiple inheritance follows MRO
* Constructor is not automatically chained without `super()`
