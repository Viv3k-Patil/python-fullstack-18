# 📘 Day 16 — Pydantic (FastAPI) Complete Notes

---

# 🧠 1. What is Pydantic?

> Pydantic is used to **define data structure + validate input automatically**

---

## 🔥 Why needed?

Without Pydantic:

```python
data = await request.json()
```

❌ No validation
❌ Manual parsing
❌ Error-prone

---

With Pydantic:

```python
def create_user(user: User):
```

✔ Auto validation
✔ Clean code
✔ Type safety

---

# 🧱 2. Basic Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

---

## 🧠 Key Points

* Inherits from `BaseModel`
* Uses type hints
* Auto JSON → object conversion

---

# 🧪 Behavior

| Input         | Result  |
| ------------- | ------- |
| Correct types | ✅       |
| Wrong type    | ❌ error |
| Missing field | ❌ error |

---

# 🧠 3. Optional Fields

```python
from typing import Optional

age: Optional[int] = None
```

---

## 🔥 Rule

| Code            | Meaning      |
| --------------- | ------------ |
| `Optional[int]` | Can be null  |
| `= None`        | Not required |

---

## 🎯 Important

> Optional ≠ optional field
> Default value makes it optional

---

# 🧠 4. Default Values

```python
age: int = 18
```

✔ Field not required
✔ Uses default if missing

---

# 🧠 5. Field Validation

```python
from pydantic import Field

class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0)
```

---

## 🔥 Common rules

| Rule       | Meaning       |
| ---------- | ------------- |
| gt         | greater than  |
| ge         | ≥             |
| lt         | <             |
| le         | ≤             |
| min_length | string length |
| max_length | string length |

---

# 🧠 6. Nested Models

```python
class Address(BaseModel):
    city: str

class User(BaseModel):
    name: str
    address: Address
```

---

## 🧠 Concept

> JSON object → nested model

---

# 🧠 7. List of Models

```python
from typing import List

class Team(BaseModel):
    players: List[Player]
```

---

## 🔥 Concept

> List of objects → List[Model]

---

# 🧠 8. Validators (VERY IMPORTANT)

---

# 🔹 8.1 field_validator

```python
from pydantic import field_validator

@field_validator("name")
def validate_name(cls, value):
    return value
```

---

## 🧠 Used for

* Single field validation
* Format checks

---

## 🧠 Parameters

| Param | Meaning     |
| ----- | ----------- |
| cls   | class       |
| value | field value |

---

---

# 🔹 8.2 model_validator

```python
from pydantic import model_validator

@model_validator(mode="after")
def validate(self):
    return self
```

---

## 🧠 Used for

* Cross-field validation
* Business rules

---

## 🔥 Example

```python
if self.price * self.qty != self.total:
    raise ValueError()
```

---

# 🧠 Validator Modes

---

## 🔹 BEFORE

```python
@model_validator(mode="before")
```

* Raw input
* Dict format

---

## 🔹 AFTER (most used)

```python
@model_validator(mode="after")
```

* Fully validated object
* Safe to use

---

# 🧠 Execution Flow

```text
1. model_validator(before)
2. field_validator(before)
3. type validation
4. field_validator(after)
5. model_validator(after)
```

---

# 🧠 9. cls vs self

| Context                | Used |
| ---------------------- | ---- |
| field_validator        | cls  |
| model_validator(after) | self |

---

## 🔥 Why?

* field → no object yet
* model → object created

---

# 🧠 10. Request vs Response Models

---

## 🔹 Request

```python
def create_user(user: UserCreate):
```

---

## 🔹 Response

```python
@app.post(..., response_model=UserResponse)
```

---

## 🎯 Rule

> Request → function param
> Response → decorator

---

# 🧠 11. model_dump()

```python
user_dict = user.model_dump()
```

---

## Used for

* DB storage
* Logging
* Serialization

---

# 🧠 12. Best Practices

---

## ✅ Do

* Separate schemas
* Use response_model
* Use validators properly

---

## ❌ Don’t

* Return raw objects
* Mix DB + schema
* Overuse validators

---

# 🧠 13. Design Principles

---

## 🔥 Golden Rules

1. One JSON object → one model
2. Use Field for simple rules
3. Use model_validator for business logic
4. Separate request & response

---

# 🧠 14. Real-world Pattern

```text
Request → Pydantic → Service → DB → Response Model
```

---

# 🎯 Final Summary

Pydantic gives you:

* Structure
* Validation
* Clean API contracts

---
