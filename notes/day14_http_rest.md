Here are your **Day 14 Class Notes – HTTP & REST (Detailed, clean, no extra commentary)**

---

# 📘 DAY 14 – HTTP & REST

---

## 1. What is HTTP?

**HTTP (HyperText Transfer Protocol)** is a **communication protocol** used between **client (browser/app)** and **server**.

* It defines **rules for request & response**
* Works on **top of TCP/IP**
* Stateless protocol (no memory of previous requests)

---

## 2. Client–Server Flow

```
Client (Browser/Postman)
        ↓
   HTTP Request
        ↓
     Server
        ↓
   HTTP Response
        ↓
      Client
```

---

## 3. Structure of HTTP Request

### 3.1 Request Line

```
GET /hello HTTP/1.1
```

* **Method** → GET / POST / PUT / DELETE
* **Path (URI)** → /hello
* **Version** → HTTP/1.1

---

### 3.2 Headers (Metadata)

Example:

```
Host: example.com
User-Agent: Chrome
Content-Type: application/json
Authorization: Bearer token
```

Used for:

* Authentication
* Content type
* Client info

---

### 3.3 Body (Optional)

Used mainly in **POST / PUT**

Example:

```json
{
  "name": "Vivek",
  "age": 28
}
```

---

## 4. Structure of HTTP Response

### 4.1 Status Line

```
HTTP/1.1 200 OK
```

---

### 4.2 Status Codes

#### ✅ Success

* 200 → OK
* 201 → Created

#### ⚠️ Client Errors

* 400 → Bad Request
* 401 → Unauthorized
* 404 → Not Found

#### ❌ Server Errors

* 500 → Internal Server Error

---

### 4.3 Headers

```
Content-Type: application/json
Content-Length: 120
```

---

### 4.4 Body

```json
{
  "message": "Success"
}
```

---

## 5. Common HTTP Methods

| Method | Purpose              |
| ------ | -------------------- |
| GET    | Fetch data           |
| POST   | Create data          |
| PUT    | Update full resource |
| PATCH  | Partial update       |
| DELETE | Remove data          |

---

## 6. What is REST?

**REST (Representational State Transfer)** is an **architectural style** for designing APIs.

---

## 7. REST Principles

### 7.1 Stateless

* Each request is independent
* Server does NOT store client session

---

### 7.2 Client–Server Separation

* Frontend and backend are independent

---

### 7.3 Resource-Based

Everything is treated as a **resource**

Examples:

```
/users
/products
/orders
```

---

### 7.4 Standard HTTP Methods

```
GET    /users       → Get all users
GET    /users/1     → Get single user
POST   /users       → Create user
PUT    /users/1     → Update user
DELETE /users/1     → Delete user
```

---

### 7.5 Representation

Data is usually sent in:

* JSON (most common)
* XML (older systems)

---

## 8. REST API Example

### Request

```
POST /users HTTP/1.1
Content-Type: application/json
```

Body:

```json
{
  "name": "Vivek"
}
```

---

### Response

```
HTTP/1.1 201 Created
```

```json
{
  "id": 1,
  "name": "Vivek"
}
```

---

## 9. HTTP vs REST

| HTTP                        | REST                  |
| --------------------------- | --------------------- |
| Protocol                    | Architectural style   |
| Defines communication rules | Defines API design    |
| Works at low level          | Works at design level |

---

## 10. How Browser Sends Request

When you type URL:

```
https://example.com/users
```

### Steps:

1. DNS resolves domain → IP
2. TCP connection established
3. Browser sends HTTP request:

   ```
   GET /users HTTP/1.1
   Host: example.com
   ```
4. Server processes
5. Sends HTTP response
6. Browser renders UI

---

## 11. Stateless Nature (Important)

Each request is independent:

```
Request 1 → Login
Request 2 → Get data
```

Server does NOT remember → uses:

* Tokens (JWT)
* Sessions (handled externally)

---

## 12. Content-Type Examples

| Type                | Meaning     |
| ------------------- | ----------- |
| application/json    | JSON data   |
| text/html           | Web page    |
| multipart/form-data | File upload |

---

## 13. Query Params vs Path Params

### Path Param

```
/users/10
```

### Query Param

```
/users?page=1&limit=10
```

---

## 15. Headers vs Body

| Feature | Headers  | Body         |
| ------- | -------- | ------------ |
| Purpose | Metadata | Actual data  |
| Size    | Small    | Can be large |

---

## 16. Tools to Test APIs

* Browser (GET only)
* Postman

Perfect — now we go one level deeper.

---

# 🔥 RESTful API – Features + Example

---

## 1. What is a RESTful API?

👉 A **RESTful API** is an API that **follows REST principles using HTTP**

---

# ✅ 2. Core REST Features (Must Know)

---

## 2.1 Resource-Based (Most Important)

👉 Everything is a **resource (noun)** — NOT actions

❌ Wrong:

```id="d6t3e9"
GET /getUsers
POST /createUser
```

✅ Correct:

```id="9v6m7h"
/users
/orders
/products
```

---

## 2.2 Use of HTTP Methods

Each method has a clear purpose:

| Method | Use            |
| ------ | -------------- |
| GET    | Read           |
| POST   | Create         |
| PUT    | Full update    |
| PATCH  | Partial update |
| DELETE | Remove         |

---

## 2.3 Stateless

👉 Server does NOT remember previous request

Example:

```id="t1l4o9"
Request 1 → Login
Request 2 → Get profile (token required)
```

👉 Each request must carry:

* Auth token
* Required data

---

## 2.4 Uniform Interface

👉 Standard way of interaction

Example:

```id="7a9z4k"
GET    /users
GET    /users/1
POST   /users
DELETE /users/1
```

👉 Same pattern everywhere

---

## 2.5 Representation (Data Format)

👉 Data is sent in standard formats:

* JSON ✅ (most used)
* XML (rare)

Example:

```json id="3bq8kx"
{
  "id": 1,
  "name": "Vivek"
}
```

---

## 2.6 Client-Server Separation

👉 Frontend and backend are independent

* Frontend → React / Mobile
* Backend → API

---

## 2.7 Idempotency (Important)

👉 Same request multiple times → same result

| Method | Idempotent |
| ------ | ---------- |
| GET    | ✅          |
| PUT    | ✅          |
| DELETE | ✅          |
| POST   | ❌          |

---

# 🚀 3. Complete Real Example

Let’s design a **User API**

---

## Base URL

```id="q1d8fp"
/users
```

---

## 3.1 Get All Users

```id="j4k0as"
GET /users
```

Response:

```json id="d9p2zl"
[
  { "id": 1, "name": "Vivek" },
  { "id": 2, "name": "Rahul" }
]
```

---

## 3.2 Get Single User

```id="1k7x2o"
GET /users/1
```

---

## 3.3 Create User

```id="l2o9vz"
POST /users
```

Body:

```json id="pq6w1x"
{
  "name": "Vivek"
}
```

Response:

```json id="9b8s3m"
{
  "id": 1,
  "name": "Vivek"
}
```

---

## 3.4 Update User

```id="k8c5hn"
PUT /users/1
```

Body:

```json id="r4n0qx"
{
  "name": "Vivek Patil"
}
```

---

## 3.5 Delete User

```id="y7m2kd"
DELETE /users/1
```

---

# 🔥 4. How This Follows REST

| Rule              | Applied?                  |
| ----------------- | ------------------------- |
| Resource-based    | `/users` ✅                |
| HTTP methods      | GET, POST, PUT, DELETE ✅  |
| Stateless         | Token-based requests ✅    |
| Uniform interface | Same pattern everywhere ✅ |

---

# ⚠️ 5. Common Mistakes (Very Important)

❌ Using verbs in URL:

```id="p8v6tr"
/createUser
/deleteUser
```

❌ Mixing methods:

```id="x0n3zb"
POST /users/getAll
```

❌ Ignoring status codes

---

