# 📘 Day 13 – Backend Basics + FastAPI + Health API

---

## 🎯 Objective

* Understand URL, Request, Response, Server
* Setup FastAPI project
* Run first API
* Create Health API

---

## 🌐 1. URL (Uniform Resource Locator)

Example:

```bash
http://127.0.0.1:8000/hello
```

Breakdown:

* `http://` → protocol
* `127.0.0.1` → localhost
* `8000` → port
* `/hello` → route

---

## 📩 2. Request and Response

* Request → sent by client
* Response → returned by server

Example:

Request:

```bash
GET /hello
```

Response:

```json
{"msg": "Hello"}
```

---

## 🖥️ 3. Server

* Server = program that runs continuously
* Listens for requests
* Sends responses

---

## 📁 4. Project Setup

```bash
mkdir backend_project
cd backend_project
```

---

## ⚙️ 5. Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 📦 6. Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## 📄 7. Create File

```bash
main.py
```

---

## 🚀 8. First API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"msg": "Hello"}
```

---

## ▶️ 9. Run Server

```bash
uvicorn main:app --reload
```

---

## 🌍 10. Test API

```bash
http://127.0.0.1:8000/hello
```

---

## 📄 11. Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

## 🔄 12. Request–Response Flow

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AOMhE9T_tuC0pUoZyWKWSnQ.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2ASFUzZdIUHyMXvclO5ykEhQ.png)

![Image](https://www.producttalk.org/content/images/2025/08/how-rest-apis-work.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2Au0SNIUZLaXkcb4qv6c9sxw.png)

---

## ❤️ 13. Health API

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Test:

```bash
http://127.0.0.1:8000/health
```

---

## 📦 14. Dependencies File

Create:

```bash
pip freeze > requirements.txt
```

Example:

```txt
fastapi
uvicorn
```

---

## 📁 15. Folder Structure

```bash
backend_project/
   venv/
   main.py
   requirements.txt
```
