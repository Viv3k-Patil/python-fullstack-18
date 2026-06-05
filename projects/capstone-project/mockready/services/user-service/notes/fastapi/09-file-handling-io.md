# 📘 1. What is File Handling (Deep Understanding)

**Definition:**
File handling is the process of interacting with files stored on disk to:

* create
* read
* update
* delete

👉 Files are stored **persistently** (unlike variables in RAM)

---

# 🧠 2. Types of Files (don’t restrict to text)

## 📝 Text Files

* `.txt`, `.csv`, `.json`, `.log`
* Human readable

## 🧊 Binary Files

* `.jpg`, `.png`, `.pdf`, `.mp4`, `.zip`
* Not human readable
* Must use binary mode (`rb`, `wb`)

---

# ⚙️ 3. Core Python Function → `open()`

```python
open(file_name, mode)
```

---

## 🔥 File Modes (important for interview)

| Mode   | Meaning                     |
| ------ | --------------------------- |
| `"r"`  | Read (error if not exists)  |
| `"w"`  | Write (overwrite or create) |
| `"a"`  | Append                      |
| `"x"`  | Create (error if exists)    |
| `"rb"` | Read binary                 |
| `"wb"` | Write binary                |

---

# 🧱 4. CREATE FILE (Write Operation)

## Example 1 — Basic Write

```python
with open("test.txt", "w") as f:
    f.write("Hello World")
```

### 🔍 Explanation

* `"w"` → creates file if not exists
* overwrites existing file
* `with` → auto closes file (VERY important)

---

## Example 2 — Multiple lines

```python
with open("data.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

---

## Example 3 — Binary file (image/pdf)

```python
with open("image.jpg", "wb") as f:
    f.write(binary_data)
```

👉 Teach clearly:

> Always use `"wb"` for non-text files

---

# 📖 5. READ FILE

## Example 1 — Read full content

```python
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## Example 2 — Read line by line

```python
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## Example 3 — Read specific size

```python
with open("test.txt", "r") as f:
    content = f.read(5)
```

👉 Reads first 5 characters

---

## Example 4 — Binary read

```python
with open("image.jpg", "rb") as f:
    data = f.read()
```

---

# ✏️ 6. UPDATE FILE

👉 Python does NOT have direct update mode
We simulate update using:

---

## Option 1 — Append

```python
with open("test.txt", "a") as f:
    f.write("\nNew line")
```

---

## Option 2 — Read + Rewrite (real update)

```python
with open("test.txt", "r") as f:
    content = f.read()

content = content.replace("Hello", "Hi")

with open("test.txt", "w") as f:
    f.write(content)
```

👉 Important teaching:

> Update = read → modify → write back

---

# ❌ 7. DELETE FILE

```python
import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
```

---

## 🔍 Explanation

* `os.path.exists()` → safety check
* `os.remove()` → deletes file

---

# 📂 8. File Handling with Folders

## Create folder

```python
import os

os.makedirs("data", exist_ok=True)
```

---

## Save file inside folder

```python
with open("data/test.txt", "w") as f:
    f.write("Hello")
```

---

## List files

```python
files = os.listdir("data")
print(files)
```

---

# 🧠 9. Advanced Concepts

## File Pointer

```python
f = open("test.txt", "r")
print(f.tell())   # position
f.seek(0)         # move pointer
```

---

## File Closing (why `with` is important)

```python
f = open("test.txt", "r")
# if not closed → memory leak risk
f.close()
```

👉 Always prefer `with`

---

# ⚠️ 10. Common Mistakes

* ❌ forgetting to close file
* ❌ using `"r"` on non-existing file
* ❌ using text mode for binary files
* ❌ overwriting accidentally with `"w"`
* ❌ not handling exceptions

---

# 🛡️ 11. Exception Handling (important)

```python
try:
    with open("test.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

---

# 🧱 12. CRUD using Python (complete example)

## Create

```python
def create_file(name, content):
    with open(name, "w") as f:
        f.write(content)
```

---

## Read

```python
def read_file(name):
    with open(name, "r") as f:
        return f.read()
```

---

## Update

```python
def update_file(name, new_content):
    with open(name, "w") as f:
        f.write(new_content)
```

---

## Delete

```python
import os

def delete_file(name):
    if os.path.exists(name):
        os.remove(name)
```

---

# 🧠 13. Real-world Use Cases

* Logs → `.log`
* Config → `.json`
* Reports → `.csv`
* Images → `.jpg`
* Resume upload → `.pdf`

---
