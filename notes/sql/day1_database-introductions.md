## Syllabus Overview — All 9 Sessions

| Day | Topic | What They'll Be Able to Do |
|-----|-------|---------------------------|
| 1 | What is a database? SQL vs NoSQL mental model | Explain why databases exist, difference between relational and document DBs |
| 2 | SQL Basics — Reading data | Write SELECT, WHERE, ORDER BY, LIMIT, DISTINCT queries |
| 3 | SQL — Aggregations & Grouping | GROUP BY, HAVING, COUNT, SUM, AVG, MIN, MAX, NULL handling |
| 4 | Relationships & JOINs | Primary/foreign keys, INNER/LEFT/RIGHT/FULL JOIN, many-to-many |
| 5 | Writing Data + Transactions | INSERT, UPDATE, DELETE, ACID, transactions, rollback |
| 6 | Schema Design & Normalization | 1NF/2NF/3NF, ERDs, design a real-world schema from scratch |
| 7 | PostgreSQL Deep Dive | Indexes, EXPLAIN/ANALYZE, window functions, CTEs, JSON columns, views |
| 8 | NoSQL — MongoDB Foundations | Documents, collections, CRUD, schema patterns, when to use NoSQL |
| 9 | MongoDB Advanced | Aggregation pipeline, indexes, embedding vs referencing, transactions |

---

## Session Goals — Day 1

By the end of this session, students will understand:

- Why flat file storage (spreadsheets, CSVs) breaks at scale
- What a DBMS is and what problems it solves
- The fundamental difference between relational and document databases
- What SQL is and what it isn't
- How PostgreSQL and MongoDB fit into the real world
- Hands-on: create a table, insert rows, run a basic query

---

## Part 1 — The Problem (Why Databases Exist)

### 1.1 Everyone Has Already Used a Database

Before showing any tool or concept, anchor this in what students already know.

Ask: *"How many of you have stored data in Excel, Google Sheets, or even a text file?"*

Almost every hand goes up. That's the starting point. A spreadsheet is a database — just an extremely limited one. Today's goal is to understand exactly where it breaks and what people built to fix those breaks.

---

### 1.2 The Spreadsheet Wall — Building the Problem From Scratch

Imagine you are building a student management system for a school. You start with a single sheet:

```
| student_name | class | marks | teacher_name | teacher_phone | teacher_email        |
|--------------|-------|-------|--------------|---------------|----------------------|
| Arjun        | 10    | 88    | Ms. Priya    | 9876543210    | priya@school.com     |
| Sneha        | 10    | 92    | Ms. Priya    | 9876543210    | priya@school.com     |
| Ravi         | 11    | 76    | Mr. Kumar    | 9123456780    | kumar@school.com     |
| Meera        | 10    | 81    | Ms. Priya    | 9876543210    | priya@school.com     |
```

For 20 students, this works fine. Now ask: what happens at scale?

**Problem 1 — Update Anomaly**
Ms. Priya changes her phone number. You must update every single row where her name appears. With 5,000 students and 200 teachers, this becomes a maintenance nightmare. Worse — if someone updates 4,800 rows and misses 200, your data is now internally inconsistent. Half your rows are lying to you. This is called an **update anomaly**.

**Problem 2 — Insert Anomaly**
You want to add a new teacher to the system before any student is assigned to them. You can't — the table requires student data. The teacher has nowhere to live independently. This is an **insert anomaly**.

**Problem 3 — Delete Anomaly**
Ravi graduates and you delete his row. You've now lost Mr. Kumar's contact information entirely because Ravi was his only student. This is a **delete anomaly**.

**Problem 4 — Querying Pain**
Find all students in Class 10 who scored above 85, with their teacher's email, sorted by marks descending. In a spreadsheet: multiple manual filters, VLOOKUP or INDEX-MATCH, and it breaks if someone sorts the sheet. At 10 lakh rows, the spreadsheet crashes.

**Problem 5 — Concurrency**
Two people open the same file at the same time. One adds a student. The other updates marks. When the second person saves, the first person's insert is gone. There is no conflict detection. No locking. No merge.

**Problem 6 — No Data Integrity**
Nothing stops someone from entering "abc" in the marks column, or leaving teacher_name empty, or adding the same student twice. The data has no rules. It trusts the human.

These six problems are not Excel's fault — they are **fundamental limitations of flat file storage**. And every one of them has a direct solution in a proper database system.

---

### 1.3 The Four Things You Need From Storage

Before naming the solution, let students derive what a storage system must do well:

1. **Store data durably** — survive crashes, power cuts, restarts
2. **Retrieve data fast** — even with millions of records
3. **Handle multiple users simultaneously** — without corrupting data
4. **Enforce rules** — types, required fields, relationships, uniqueness

A spreadsheet fails at 3 and 4, struggles at 2. A proper DBMS solves all four.

---

## Part 2 — What Is a DBMS?

### 2.1 The Core Concept

A **Database Management System (DBMS)** is software that sits between your application and your data. You never interact with the raw data directly. You send requests to the DBMS in a formal language, and it handles storage, retrieval, concurrency, integrity, and backups.

The **database** is the data itself. The **DBMS** is the system that manages it. People often use these terms interchangeably — don't let that confuse you.

**The Library Analogy**

Imagine a library with 10 million books across 50 floors. You don't wander the floors yourself searching. You walk up to the librarian and say: *"I want all books on machine learning, published after 2020, available right now, sorted by rating."* The librarian knows the exact location of every book, fetches them in seconds, and ensures nobody else checks out the same copy you're reading.

The DBMS is the librarian. The database is the library. SQL (or the query language) is the language you speak to the librarian.

The librarian also:
- Prevents two people from checking out the same last copy simultaneously (concurrency control)
- Keeps a log of every transaction in case the library burns down (durability / write-ahead logging)
- Refuses to accept a book without an ISBN (data integrity / constraints)
- Knows exactly who has what, and for how long (transaction management)

---

### 2.2 What a DBMS Does That a File Cannot

| Capability | Flat File | DBMS |
|------------|-----------|------|
| Fast search on any column | Scan entire file | Index lookup, O(log n) |
| Multiple simultaneous writers | Last-save wins | Locking, MVCC |
| Enforce data types | No | Yes (schema) |
| Enforce relationships | No | Foreign keys |
| Rollback a failed operation | No | Transactions |
| Handle 100GB+ of data | Crash | Query planner optimizes |
| Audit who changed what | No | Transaction logs |
| Backup and recovery | Manual | Built-in |

---

### 2.3 The Two Big Families

**Relational Databases (SQL)**
Data is organized in tables. Tables are related to each other through keys. You query them using SQL. Extremely mature, enforces structure, great for complex queries and relationships. Examples: PostgreSQL, MySQL, Oracle, SQLite, SQL Server.

**NoSQL Databases**
"NoSQL" means "not only SQL" — the data model is not always tabular. Covers several subcategories:

- **Document stores** — data stored as JSON-like documents (MongoDB, CouchDB)
- **Key-value stores** — simple lookup by key (Redis, DynamoDB in simple mode)
- **Column-family stores** — rows can have different columns (Cassandra, HBase)
- **Graph databases** — data modeled as nodes and edges (Neo4j)

In this course, we focus on **PostgreSQL** (relational) and **MongoDB** (document). These are the two most widely used databases in modern software development and the ones you'll encounter most in the job market.

---

## Part 3 — Relational Databases in Depth

### 3.1 Tables, Rows, Columns — The Core Model

A relational database organizes data into **tables** (also called relations). Each table has:
- **Columns** (also called fields or attributes) — define the structure, the "what"
- **Rows** (also called records or tuples) — the actual data, one entity per row
- **Schema** — the set of rules that defines what columns exist and what types they hold

The key insight: **each table should represent exactly one thing**. A students table stores students. A teachers table stores teachers. A classes table stores classes. You connect them through relationships — you don't duplicate data.

Going back to the broken spreadsheet — here is how a relational database solves it:

**teachers table:**
```
| id | name      | phone      | email             |
|----|-----------|------------|-------------------|
| 1  | Ms. Priya | 9876543210 | priya@school.com  |
| 2  | Mr. Kumar | 9123456780 | kumar@school.com  |
```

**students table:**
```
| id | name  | class | marks | teacher_id |
|----|-------|-------|-------|------------|
| 1  | Arjun | 10    | 88    | 1          |
| 2  | Sneha | 10    | 92    | 1          |
| 3  | Ravi  | 11    | 76    | 2          |
| 4  | Meera | 10    | 81    | 1          |
```

Ms. Priya's phone number now lives in **exactly one place**. `teacher_id` in the students table is a **pointer** — it says "look up teacher with id=1 for full details." If the phone number changes, you update one row in one table. All 5,000 students who reference her get the correct number automatically — because they were never storing the number, only a reference.

This is not just a performance trick. It is a **design philosophy**: store every fact exactly once.

---

### 3.2 Primary Keys and Foreign Keys

**Primary Key**
Every row in a table must be uniquely identifiable. The column (or combination of columns) that uniquely identifies a row is the **primary key**. No two rows can have the same primary key. It cannot be NULL.

Common choices: an auto-incrementing integer (`SERIAL` in PostgreSQL), or a UUID.

```sql
CREATE TABLE teachers (
  id    SERIAL PRIMARY KEY,
  name  TEXT NOT NULL,
  phone TEXT
);
```

**Foreign Key**
A column in one table that references the primary key of another table. It creates the relationship. The DBMS enforces that you can't insert a `teacher_id` of 99 in the students table if there's no teacher with `id = 99`. This is **referential integrity**.

```sql
CREATE TABLE students (
  id         SERIAL PRIMARY KEY,
  name       TEXT NOT NULL,
  class      INTEGER,
  marks      NUMERIC,
  teacher_id INTEGER REFERENCES teachers(id)
);
```

**The Aadhaar Analogy**
Think of how India's Aadhaar system works. Your bank doesn't store your address — it stores your Aadhaar number. Your hospital doesn't store your name — it stores your Aadhaar number. If you move to a new city and update your address in the Aadhaar system, every institution that references your Aadhaar automatically has access to your new address. They weren't storing the data — they were storing a reference to the data. Foreign keys work the same way.

---

### 3.3 What Is SQL?

**SQL** stands for Structured Query Language. It was developed at IBM in the 1970s, standardized in 1986, and is still the dominant language for talking to relational databases. Almost every database you will touch professionally understands SQL.

SQL is **declarative**. You describe *what* you want, not *how* to get it. The DBMS figures out the "how" — it chooses the algorithm, the index to use, the join strategy. You write:

```sql
SELECT name, marks
FROM students
WHERE class = 10 AND marks > 80
ORDER BY marks DESC;
```

You didn't write a loop. You didn't tell it how to search. You described the result you want, and the database engine optimized and executed it.

SQL has four main categories of statements:

| Category | Full Name | Purpose | Examples |
|----------|-----------|---------|---------|
| DQL | Data Query Language | Read data | SELECT |
| DML | Data Manipulation Language | Write data | INSERT, UPDATE, DELETE |
| DDL | Data Definition Language | Define structure | CREATE, ALTER, DROP |
| DCL | Data Control Language | Permissions | GRANT, REVOKE |
| TCL | Transaction Control | Manage transactions | BEGIN, COMMIT, ROLLBACK |

Day 1 and 2 focus entirely on DQL (reading). Days 5 onward cover DML, DDL, TCL.

---

## Part 4 — Document Databases (NoSQL)

### 4.1 When Tables Don't Fit

Relational databases are powerful, but they assume your data has a consistent, predictable structure. Every row in a table follows the same schema. What if your data is naturally variable?

Consider Instagram posts. Some posts have:
- 1 photo. Others have 10. Some have a video.
- A location. Others don't.
- Tagged users. Others don't.
- Music. Others don't.
- A product link. Others don't.

In a relational table, you'd need columns for `photo_1`, `photo_2`, ..., `photo_10`, `video_url`, `location`, `tagged_user_1`, ... Most cells would be empty. This is called a **sparse table** and it's both wasteful and painful to query.

Or you'd normalize it into many small tables — a `post_photos` table, a `post_tags` table, a `post_locations` table — and join them every time you need a post. For a social media feed loading 50 posts per scroll, that's expensive.

---

### 4.2 Documents — The Core Model

A document database stores each record as a self-contained **document** — typically in JSON (or BSON in MongoDB's case). Each document can have a completely different structure. There is no fixed schema.

```json
{
  "_id": "post_001",
  "user": "rahul_23",
  "caption": "Sunset at Lonavala",
  "media": [
    { "type": "image", "url": "img1.jpg" },
    { "type": "image", "url": "img2.jpg" }
  ],
  "location": { "name": "Lonavala", "lat": 18.75, "lng": 73.41 },
  "tags": ["@priya", "@amit"],
  "likes": 1402,
  "created_at": "2024-11-15T18:30:00Z"
}
```

```json
{
  "_id": "post_002",
  "user": "sneha_travels",
  "caption": "Monday mood",
  "media": [
    { "type": "video", "url": "reel.mp4", "duration": 30 }
  ],
  "likes": 234
}
```

Two posts. Completely different shapes. Both valid. No empty columns. No wasted space.

The database stores them in a **collection** (the MongoDB equivalent of a table). A collection is a group of documents, typically of the same general type, but without enforced structure.

---

### 4.3 SQL vs NoSQL — Not a War, a Tradeoff

A critical mindset to establish early: this is not about which is "better." It is about which is appropriate for the problem at hand.

| Dimension | Relational (PostgreSQL) | Document (MongoDB) |
|-----------|------------------------|--------------------|
| Data shape | Uniform, tabular | Variable, nested |
| Schema | Enforced (strict) | Flexible (optional) |
| Relationships | Native (JOINs, FK) | Manual (embed or reference) |
| Complex queries | Excellent | Good (aggregation pipeline) |
| Horizontal scaling | Harder | Easier |
| ACID transactions | Full, mature | Supported (multi-doc since v4) |
| Best for | Financial, ERP, reporting | Catalogs, feeds, user profiles |

**The Filing Cabinet vs WhatsApp Analogy**
A relational database is a filing cabinet with labeled folders. Every document in the "Tax Returns" folder must have the same format — date, income, deductions, total. It's rigid, but you can search across all folders instantly with perfect accuracy.

A document database is like WhatsApp. Every conversation (document) is its own world — some have photos, some have voice notes, some have polls, some are just text. Each chat is self-contained and fast to access individually, but searching across all chats simultaneously is harder.

Both are useful. Your phone needs both the filing cabinet (bank app) and WhatsApp.

---

## Part 5 — PostgreSQL and MongoDB in the Real World

### 5.1 PostgreSQL

PostgreSQL (pronounced "post-GRES-Q-L" or just "Postgres") is a free, open-source, object-relational database system. It has been in active development since 1986 and is consistently rated the most admired database by developers (Stack Overflow surveys).

**Who uses it:** Shopify, Instagram (started on Postgres), Airbnb, Apple, Cisco, Reddit, GitHub, GitLab.

**What makes it stand out:**
- Full ACID compliance
- Extremely rich SQL support (window functions, CTEs, lateral joins)
- Native JSON/JSONB column type — you can store documents inside a relational database
- Powerful extension system (PostGIS for geospatial, pg_vector for AI embeddings)
- Excellent performance with proper indexing
- Completely free — no enterprise license needed

### 5.2 MongoDB

MongoDB is the most popular document database. Launched in 2007, it stores data in BSON (Binary JSON) and scales horizontally out of the box.

**Who uses it:** Uber, eBay, LinkedIn, Adobe, SEGA, Forbes, The Weather Channel.

**What makes it stand out:**
- Schema-less by default — great for evolving data models
- Rich aggregation pipeline for complex analytics
- Native horizontal sharding (splitting data across many servers)
- Strong support for geospatial queries
- Atlas (managed cloud MongoDB) is widely used in production
- The query language feels natural to JavaScript developers

---

## Part 6 — Hands-On

### 6.1 PostgreSQL — First Contact

Use [db-fiddle.com](https://db-fiddle.com) (select PostgreSQL 15) or a local install. No setup needed in browser.

**Step 1: Talk to the database**
```sql
SELECT 'Hello, Database!' AS message;
```
This returns a single row with one column called `message`. Notice: no table involved. SQL can compute things directly.

**Step 2: Create a table**
```sql
CREATE TABLE teachers (
  id    SERIAL PRIMARY KEY,
  name  TEXT NOT NULL,
  phone TEXT
);

CREATE TABLE students (
  id         SERIAL PRIMARY KEY,
  name       TEXT NOT NULL,
  class      INTEGER NOT NULL,
  marks      NUMERIC(5, 2),
  teacher_id INTEGER REFERENCES teachers(id)
);
```

What's happening here:
- `SERIAL` — auto-incrementing integer, PostgreSQL generates the value
- `PRIMARY KEY` — this column uniquely identifies each row
- `NOT NULL` — this column cannot be empty
- `NUMERIC(5, 2)` — a number with up to 5 digits total, 2 after the decimal
- `REFERENCES teachers(id)` — this is a foreign key; the value must exist in teachers.id

**Step 3: Insert data**
```sql
INSERT INTO teachers (name, phone) VALUES
  ('Ms. Priya', '9876543210'),
  ('Mr. Kumar', '9123456780');

INSERT INTO students (name, class, marks, teacher_id) VALUES
  ('Arjun', 10, 88.00, 1),
  ('Sneha', 10, 92.50, 1),
  ('Ravi',  11, 76.00, 2),
  ('Meera', 10, 81.00, 1);
```

**Step 4: Read data**
```sql
SELECT * FROM students;

SELECT name, marks FROM students WHERE class = 10;

SELECT name, marks FROM students WHERE marks > 80 ORDER BY marks DESC;
```

**Step 5: Test referential integrity**
```sql
-- This should FAIL — teacher_id 99 does not exist
INSERT INTO students (name, class, marks, teacher_id)
VALUES ('Ghost', 10, 50, 99);
```

The database refuses. Error: *"insert or update on table "students" violates foreign key constraint"*. This is the database protecting your data — something no spreadsheet does.

**Step 6: A preview of JOINs**
```sql
SELECT students.name, students.marks, teachers.name AS teacher
FROM students
JOIN teachers ON students.teacher_id = teachers.id
WHERE students.class = 10
ORDER BY students.marks DESC;
```

This is a **JOIN** — combining data from two tables using the relationship. We will spend all of Day 4 on this. For now, just observe: you got student names, their marks, and their teacher's name — from two separate tables — in one query.

---

### 6.2 MongoDB — First Contact

Use [MongoDB Atlas](https://www.mongodb.com/atlas) (free tier) or install locally and run `mongosh`.

**Insert a document**
```javascript
db.students.insertMany([
  {
    name: "Arjun",
    class: 10,
    marks: 88,
    teacher: { name: "Ms. Priya", phone: "9876543210" }
  },
  {
    name: "Sneha",
    class: 10,
    marks: 92.5,
    teacher: { name: "Ms. Priya", phone: "9876543210" }
  },
  {
    name: "Ravi",
    class: 11,
    marks: 76,
    teacher: { name: "Mr. Kumar", phone: "9123456780" }
  }
])
```

Notice: the teacher is **embedded directly inside the student document**. There is no separate teachers collection referenced by ID. The data is self-contained. This is the "embedding" pattern in MongoDB — more on this in Day 8.

**Query the data**
```javascript
db.students.find()

db.students.find({ class: 10 })

db.students.find({ marks: { $gt: 80 } }, { name: 1, marks: 1, _id: 0 })
```

The `{ $gt: 80 }` is a MongoDB **query operator**. `$gt` means "greater than." MongoDB has dozens of these: `$lt`, `$gte`, `$in`, `$regex`, etc.

The second argument `{ name: 1, marks: 1, _id: 0 }` is a **projection** — it says "return only these fields." Equivalent to `SELECT name, marks` in SQL.

**Observe the difference**
In PostgreSQL: if Ms. Priya changes her phone, one update in the `teachers` table fixes everything.
In MongoDB as modeled above: you must update every student document that embeds her data. This is the tradeoff with embedding. There is no right or wrong answer — the right choice depends on access patterns. Day 8 covers this in depth.

---

## Part 7 — Concepts to Know Cold (Senior-Level Vocabulary)

These are not just buzzwords. These are things you'll be asked in every serious database interview and will encounter in every production system.

### ACID Properties
Every transaction in a relational database must be:
- **Atomic** — all operations in a transaction succeed, or none do. No partial writes.
- **Consistent** — the database moves from one valid state to another. Constraints are never violated.
- **Isolated** — concurrent transactions don't see each other's in-progress changes.
- **Durable** — once a transaction commits, it survives crashes. Written to disk (or WAL).

### What Is a Transaction?
A transaction is a unit of work — a group of operations that must all succeed or all fail together.

Classic example: bank transfer. Deduct ₹1000 from Account A. Add ₹1000 to Account B. If the system crashes between these two operations, Account A loses ₹1000 and Account B gets nothing. A transaction wraps both operations — either both happen, or neither does.

```sql
BEGIN;
  UPDATE accounts SET balance = balance - 1000 WHERE id = 'A';
  UPDATE accounts SET balance = balance + 1000 WHERE id = 'B';
COMMIT;
```

If anything goes wrong: `ROLLBACK;` — and the database returns to the state before the `BEGIN`.

### Indexes
An index is a data structure (typically a B-tree) that allows the database to find rows matching a condition without scanning every row. Without an index, finding all students with `class = 10` means reading every row — O(n). With an index on `class`, it's O(log n).

Indexes speed up reads but slow down writes (because the index must be updated on every insert/update/delete). You'll learn to use `EXPLAIN ANALYZE` in Day 7 to see whether indexes are being used.

### Normalization
The process of organizing a database to reduce redundancy and prevent anomalies. Involves splitting tables and creating relationships. The "normal forms" (1NF, 2NF, 3NF) are a set of rules that progressively eliminate redundancy. Covered fully in Day 6.

### Schema
The structure definition of a database — which tables exist, which columns each has, what types they are, what constraints apply. In SQL, the schema is enforced by the database itself. In MongoDB, schema is optional (enforced by application code or optional validation rules).

### CAP Theorem
States that in a distributed database system, you can only guarantee two of three properties simultaneously:
- **Consistency** — every read returns the most recent write
- **Availability** — every request gets a response (not necessarily the latest data)
- **Partition Tolerance** — the system keeps running even if network partitions occur

PostgreSQL prioritizes Consistency + Partition Tolerance. MongoDB (in certain configurations) can lean toward Availability + Partition Tolerance. This governs real architectural decisions at scale. Covered in depth in Day 10.

---

## Part 8 — Common Misconceptions to Address Now

**"NoSQL is faster than SQL"**
False in general. PostgreSQL with proper indexes outperforms MongoDB on many workloads. Speed depends on the query, the data model, the indexing strategy, and hardware. NoSQL is often faster for specific access patterns (fetching a single document), not universally.

**"NoSQL doesn't have a schema"**
Misleading. NoSQL databases are schema-flexible, not schema-free. In production, every MongoDB collection has an implicit schema defined by your application code. The schema is just not enforced by the database engine itself (unless you add validation rules).

**"SQL doesn't scale"**
False. PostgreSQL handles terabytes of data. Companies like Instagram ran on Postgres for years at massive scale. Sharding, read replicas, connection pooling — SQL databases scale. They just scale differently than NoSQL.

**"You pick one and never use the other"**
False. Most production systems use both. A typical stack might use PostgreSQL for user accounts, financial records, and reporting — and MongoDB for a product catalog, user activity feeds, or real-time event storage.

---

## Summary — What You Now Know

| Concept | One-Line Definition |
|---------|---------------------|
| Database | Organized, managed storage for structured data |
| DBMS | Software that manages the database (PostgreSQL, MongoDB) |
| Relational DB | Data in tables with enforced relationships |
| SQL | Declarative language to query relational databases |
| Table | A structured set of rows and columns representing one entity type |
| Primary Key | Unique identifier for a row |
| Foreign Key | A column referencing another table's primary key |
| Document DB | Data stored as flexible JSON-like documents |
| Collection | MongoDB's equivalent of a table |
| ACID | Atomicity, Consistency, Isolation, Durability |
| Transaction | A group of operations that succeed or fail together |
| Index | Data structure for fast lookup without full scan |
| Schema | The structure definition of a database |

---
