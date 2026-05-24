# 📚 DATABASE FUNDAMENTALS

---

## 🧠 1. Database

### Definition

A **database** is an organized collection of data stored in a structured format to enable efficient access, retrieval, and management.

---

### Characteristics

* 📦 Structured and organized
* ⚡ Efficient data retrieval
* 🔄 Supports updates and modifications
* 📈 Scalable for large datasets

---

## ❓ 2. Need for Databases

### Limitations of Traditional Methods (Excel, Files)

* 🚫 Poor handling of large data
* 🔗 No relationship management
* 🔁 Data duplication
* 🐢 Performance degradation at scale
* 👥 Limited multi-user access
* ⚠️ Higher risk of inconsistency

---

## ⚔️ 3. Database vs Excel

| Aspect         | Excel 📊           | Database 🗄️    |
| -------------- | ------------------ | --------------- |
| Purpose        | Data analysis      | Data management |
| Data Size      | Limited            | Very large      |
| Multi-user     | Limited            | Supported       |
| Relationships  | Not supported      | Supported       |
| Performance    | Degrades with size | Optimized       |
| Data Integrity | Weak               | Strong          |
| Security       | Basic              | Advanced        |

---

## 🧩 4. Types of Databases

---

### 4.1 🏗️ Relational Database (RDBMS)

**Definition**
Stores data in tables (rows and columns) with defined relationships.

**Features**

* Fixed schema
* Uses SQL
* Supports constraints (Primary Key, Foreign Key)

**Examples**

* MySQL
* PostgreSQL
* Oracle

---

### 4.2 ⚡ NoSQL Database

**Definition**
Non-relational databases with flexible schema.

**Types**

* Document
* Key-value
* Column-based
* Graph

**Features**

* Schema-less or flexible schema
* High scalability
* Optimized for specific workloads

**Examples**

* MongoDB
* Redis

---

### 4.3 🌐 Other Types

* Distributed Databases
* Cloud Databases
* Graph Databases

---

## 🧠 5. DBMS (Database Management System)

### Definition

A **DBMS** is software that enables users to create, manage, and interact with databases.

---

## ⚙️ 6. Functions of DBMS

---

### 6.1 📦 Data Storage

* Stores and organizes data internally

---

### 6.2 🔍 Data Retrieval

* Provides querying capability (e.g., SQL)

```sql
SELECT * FROM customers;
```

---

### 6.3 ✏️ Data Manipulation

* Insert, update, delete operations

---

### 6.4 🛡️ Data Integrity

* Maintains accuracy and consistency
* Enforces constraints

---

### 6.5 🔐 Security

* Access control and authorization

---

### 6.6 👥 Concurrency Control

* Handles multiple users simultaneously
* Prevents conflicts

---

### 6.7 💾 Backup & Recovery

* Data backup mechanisms
* Recovery from failures

---

## 📖 7. Core Terminology

| Term        | Meaning                       |
| ----------- | ----------------------------- |
| Table       | Structured collection of data |
| Row         | Single record                 |
| Column      | Attribute/field               |
| Primary Key | Unique identifier             |
| Foreign Key | Reference to another table    |
| Query       | Request to access data        |

---

## 🧾 8. Summary

* 📦 Database: structured data storage
* ⚙️ DBMS: software managing the database
* 🧩 Types: Relational and NoSQL
* 🚀 Databases support scalability, relationships, and reliability beyond traditional tools like Excel

---
