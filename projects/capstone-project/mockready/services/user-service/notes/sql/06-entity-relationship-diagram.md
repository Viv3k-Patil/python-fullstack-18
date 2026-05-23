# Day 6: Schema Design

---

## Start Here: What is a Schema?

You have learned how to create tables, query them, and join them together. But so far, tables have just appeared — ready to use. In real life, someone has to *design* them first.

A **schema** is the blueprint of a database. It defines:
- What tables exist
- What columns each table has
- What data types those columns use
- How tables relate to each other
- What rules the data must follow

Think of it like the floor plan of a building. Before a single brick is laid, an architect draws exactly where every room goes, how they connect, and what goes in each one. A database schema is that floor plan. A bad schema — like a bad floor plan — causes problems that are expensive and painful to fix later.

Bad schema design leads to:
- Duplicate data stored in multiple places
- Data that contradicts itself
- Queries that are slow or impossible to write
- Applications that break when requirements change

Good schema design leads to:
- Data stored in exactly one place
- Queries that are easy to write and fast to run
- A database that can grow and change without breaking

This session teaches you how to think about and design schemas properly.

---

## The Building Blocks of a Schema

Every schema is made of three things:

**1. Tables** — where data lives. Each table represents one concept: a customer, a product, an order, a payment.

**2. Columns** — the attributes of that concept. A customer has a name, email, phone number, city.

**3. Constraints** — rules that the database itself enforces, so bad data can never get in.

You already know tables and columns. Let us now go deep on constraints — because they are what separates a well-designed schema from a fragile one.

---

## Constraints — Enforcing Rules at the Database Level

A constraint is a rule attached to a column or table that the database enforces automatically. If you try to insert or update data that violates a constraint, the database rejects it — no exceptions.

This is important. If you rely on your application code to validate data, the data is only as safe as every developer who ever writes code against that database. One mistake, one forgotten check, and bad data gets in. Constraints in the database are a safety net that cannot be bypassed.

### PRIMARY KEY

Every table should have a primary key. It uniquely identifies each row. No two rows can have the same primary key value. A primary key column cannot be NULL.

```sql
CREATE TABLE customers (
    customer_id  INT          PRIMARY KEY,
    name         VARCHAR(100),
    email        VARCHAR(150)
);
```

A primary key can span multiple columns — called a **composite primary key**. Used when no single column uniquely identifies a row, but the combination does.

```sql
CREATE TABLE order_items (
    order_id    INT,
    product_id  INT,
    quantity    INT,
    PRIMARY KEY (order_id, product_id)
    -- one order cannot have the same product listed twice
);
```

### NOT NULL

Ensures that a column must always have a value — it cannot be left empty.

```sql
CREATE TABLE customers (
    customer_id  INT          PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,    -- name is required
    email        VARCHAR(150) NOT NULL,    -- email is required
    phone        VARCHAR(15)              -- phone is optional (can be NULL)
);
```

Use `NOT NULL` on every column that is logically required. If a customer must have a name and email to exist in your system, enforce that in the schema — do not leave it to chance.

### UNIQUE

Ensures that all values in a column are different from each other. Unlike PRIMARY KEY, a `UNIQUE` column can contain NULLs (in most databases, multiple NULLs are allowed because NULL is not equal to NULL).

```sql
CREATE TABLE customers (
    customer_id  INT          PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    email        VARCHAR(150) NOT NULL UNIQUE   -- no two customers can share an email
);
```

You can also put a `UNIQUE` constraint across multiple columns together:

```sql
CREATE TABLE employee_skills (
    employee_id  INT,
    skill        VARCHAR(50),
    UNIQUE (employee_id, skill)
    -- an employee cannot have the same skill listed twice
);
```

### DEFAULT

Sets a default value for a column when no value is provided during `INSERT`.

```sql
CREATE TABLE orders (
    order_id     INT          PRIMARY KEY,
    customer_id  INT          NOT NULL,
    status       VARCHAR(20)  DEFAULT 'pending',
    created_at   DATETIME     DEFAULT CURRENT_TIMESTAMP
);
```

Now if you insert an order without specifying `status`, it automatically gets `'pending'`. If you do not specify `created_at`, it gets the current date and time.

```sql
INSERT INTO orders (order_id, customer_id)
VALUES (1, 42);
-- status = 'pending', created_at = now(), automatically
```

### CHECK

Enforces a condition that every value in a column must satisfy. If an insert or update violates the condition, it is rejected.

```sql
CREATE TABLE products (
    product_id  INT            PRIMARY KEY,
    name        VARCHAR(100)   NOT NULL,
    price       DECIMAL(10,2)  NOT NULL CHECK (price > 0),
    stock       INT            DEFAULT 0 CHECK (stock >= 0),
    discount    DECIMAL(5,2)   CHECK (discount BETWEEN 0 AND 100)
);
```

- `price > 0` — a product cannot have a zero or negative price
- `stock >= 0` — stock cannot go negative
- `discount BETWEEN 0 AND 100` — discount must be a valid percentage

```sql
-- This will be rejected by the database:
INSERT INTO products VALUES (1, 'Notebook', -45.00, 100, 0);
-- ERROR: CHECK constraint failed: price > 0
```

### FOREIGN KEY

Enforces referential integrity — ensures that a value in one table actually exists in another table. You already saw this in Day 5. Here it is in full context:

```sql
CREATE TABLE orders (
    order_id    INT  PRIMARY KEY,
    customer_id INT  NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

This ensures you cannot create an order for a customer who does not exist. It also controls what happens when you try to delete a customer who has orders.

#### ON DELETE and ON UPDATE behaviour

When a referenced row is deleted or updated, the database needs to know what to do with the rows that point to it. You have four options:

| Option | What happens |
|---|---|
| `RESTRICT` | Reject the delete/update if any referencing rows exist (default) |
| `CASCADE` | Automatically delete/update the referencing rows too |
| `SET NULL` | Set the foreign key column to NULL in referencing rows |
| `SET DEFAULT` | Set the foreign key column to its default value |

```sql
CREATE TABLE orders (
    order_id    INT  PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE SET NULL    -- if customer is deleted, keep the order but set customer_id to NULL
        ON UPDATE CASCADE     -- if customer_id changes, update it in orders too
);
```

```sql
CREATE TABLE order_items (
    item_id   INT  PRIMARY KEY,
    order_id  INT  NOT NULL,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE     -- if an order is deleted, delete all its items too
);
```

Choosing the right behaviour matters. Deleting a customer and losing all their order history is very different from keeping the orders but marking the customer as unknown.

---

## Naming Conventions

Consistent naming makes schemas readable and maintainable. Agree on a convention before you start, and stick to it.

### Common conventions

| What | Convention | Example |
|---|---|---|
| Table names | lowercase, plural, underscores | `customers`, `order_items`, `employee_skills` |
| Column names | lowercase, underscores | `first_name`, `created_at`, `is_active` |
| Primary key | `table_name_id` or just `id` | `customer_id`, `product_id` |
| Foreign key | same name as the primary key it references | `customer_id` in `orders` references `customer_id` in `customers` |
| Boolean columns | start with `is_` or `has_` | `is_active`, `has_discount`, `is_verified` |
| Timestamp columns | end with `_at` | `created_at`, `updated_at`, `deleted_at` |
| Junction tables | combine both table names | `employee_projects`, `student_courses` |

### Why naming matters

```sql
-- Hard to understand: what does this query do?
SELECT c.n, o.dt, p.pr
FROM c
JOIN o ON c.cid = o.cid
JOIN p ON o.pid = p.pid;

-- Immediately readable
SELECT c.name, o.created_at, p.price
FROM customers AS c
JOIN orders    AS o ON c.customer_id = o.customer_id
JOIN products  AS p ON o.product_id  = p.product_id;
```

Good naming is documentation. You should be able to read a well-named schema and understand the business without any other explanation.

---

## Normalisation — Organising Data Properly

**Normalisation** is the process of structuring a database to reduce redundancy and ensure data integrity. It is done in steps called **normal forms**. Each normal form builds on the previous one.

You do not need to memorise the formal definitions. You need to understand the problems each normal form solves and recognise them in real schemas.

### The un-normalised starting point

Imagine a school stores all data in one table:

| student_id | student_name | course_1     | teacher_1 | course_2    | teacher_2 |
|------------|--------------|--------------|-----------|-------------|-----------|
| 1          | Riya         | Mathematics  | Mr. Rao   | Physics     | Ms. Nair  |
| 2          | Arjun        | Mathematics  | Mr. Rao   | Chemistry   | Mr. Iyer  |
| 3          | Sara         | Biology      | Ms. Patil | NULL        | NULL      |

Problems are immediately visible:
- Columns repeat (`course_1`, `course_2`) — what if a student takes 5 courses?
- Teacher data is repeated across rows
- NULLs everywhere for students taking fewer courses
- Adding a third course requires altering the table structure

### First Normal Form (1NF) — Eliminate Repeating Groups

**Rule:** Every column must hold a single, atomic value. No repeating groups of columns. Each row must be unique.

The fix: instead of `course_1`, `course_2` columns, make each course enrolment its own row.

```sql
-- VIOLATES 1NF
CREATE TABLE student_courses_bad (
    student_id   INT,
    student_name VARCHAR(100),
    course_1     VARCHAR(100),
    teacher_1    VARCHAR(100),
    course_2     VARCHAR(100),
    teacher_2    VARCHAR(100)
);

-- SATISFIES 1NF
CREATE TABLE enrolments (
    student_id   INT,
    student_name VARCHAR(100),
    course       VARCHAR(100),
    teacher      VARCHAR(100)
);
```

Now each row has one course. A student taking 5 courses has 5 rows. Adding a sixth course requires inserting a row, not changing the table structure.

| student_id | student_name | course      | teacher   |
|------------|--------------|-------------|-----------|
| 1          | Riya         | Mathematics | Mr. Rao   |
| 1          | Riya         | Physics     | Ms. Nair  |
| 2          | Arjun        | Mathematics | Mr. Rao   |
| 2          | Arjun        | Chemistry   | Mr. Iyer  |
| 3          | Sara         | Biology     | Ms. Patil |

Better — but there are still problems. Riya's name is stored twice. Mr. Rao's name is stored twice. If Mr. Rao's name changes, you have to update every row that mentions him.

### Second Normal Form (2NF) — Eliminate Partial Dependencies

**Rule:** Must be in 1NF. Every non-key column must depend on the *entire* primary key, not just part of it.

This only applies when the primary key is composite (multiple columns). In the `enrolments` table above, the primary key would be `(student_id, course)`. But `student_name` depends only on `student_id` — not on the course. That is a **partial dependency**.

The fix: separate the data into tables where each piece of information depends fully on its table's key.

```sql
CREATE TABLE students (
    student_id   INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL
);

CREATE TABLE courses (
    course_id    INT PRIMARY KEY,
    course_name  VARCHAR(100) NOT NULL,
    teacher      VARCHAR(100) NOT NULL
);

CREATE TABLE enrolments (
    student_id  INT,
    course_id   INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)
);
```

Now:
- `student_name` is stored once in `students`
- `teacher` is stored once in `courses`
- `enrolments` only stores the relationship

### Third Normal Form (3NF) — Eliminate Transitive Dependencies

**Rule:** Must be in 2NF. Every non-key column must depend directly on the primary key — not on another non-key column.

Example: imagine you add a `city` and `city_postal_code` column to `students`:

| student_id | student_name | city | city_postal_code |
|------------|--------------|------|-----------------|
| 1          | Riya         | Pune | 411001          |
| 2          | Arjun        | Pune | 411001          |

`city_postal_code` depends on `city`, not on `student_id`. That is a **transitive dependency**. If Pune's postal code changes, you have to update every student row from Pune.

The fix: move `city` and its attributes to their own table.

```sql
CREATE TABLE cities (
    city_id          INT PRIMARY KEY,
    city_name        VARCHAR(100) NOT NULL,
    city_postal_code VARCHAR(10)  NOT NULL
);

CREATE TABLE students (
    student_id  INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    city_id     INT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);
```

### A Practical Summary of Normal Forms

| Normal Form | The Problem It Solves |
|---|---|
| 1NF | Repeating columns, non-atomic values |
| 2NF | Columns that depend on only part of a composite key |
| 3NF | Columns that depend on another non-key column |

In practice, you design for 3NF by default. It covers the vast majority of real-world cases.

---

## When to Denormalise — and Why

Normalisation is the goal for most schemas. But sometimes, deliberately breaking the rules of normalisation is the right choice. This is called **denormalisation**.

When a query needs to join 6 tables to produce a report that runs millions of times per day, those joins become expensive. Sometimes you store a calculated or repeated value to avoid that join cost.

For example, storing `total_price` directly in the `orders` table even though it could be computed by joining `order_items` and `products`. This is redundant — but it makes the "show me all orders with their total" query instant instead of expensive.

The rule: **normalise first, then denormalise deliberately where you have a measured performance problem.** Never denormalise speculatively. The costs of redundancy (inconsistency, maintenance complexity) are real.

---

## Surrogate Keys vs Natural Keys

When choosing a primary key, you have two options.

### Natural Key

A natural key is a column that already exists in the data and is naturally unique — something the real world gives you.

- Email address as a customer's primary key
- ISBN as a book's primary key
- PAN number as a person's primary key

**Problems with natural keys:**
- They can change. A person can change their email. An ISBN system can change.
- They can be long. Joining on a 150-character email string is slower than joining on an integer.
- They can be confidential. Exposing someone's government ID in URLs or logs is a security problem.

### Surrogate Key

A surrogate key is an artificial key that has no meaning in the real world — the database generates it purely for identification purposes.

```sql
CREATE TABLE customers (
    customer_id  INT AUTO_INCREMENT PRIMARY KEY,  -- MySQL
    -- or SERIAL PRIMARY KEY in PostgreSQL
    name         VARCHAR(100) NOT NULL,
    email        VARCHAR(150) NOT NULL UNIQUE
);
```

`AUTO_INCREMENT` (MySQL) or `SERIAL` (PostgreSQL) automatically generates the next integer when a row is inserted. You never think about it — the database handles it.

**Advantages of surrogate keys:**
- Stable — they never change
- Short — integers are fast to join on
- Meaningless — safe to expose in URLs and logs

**The common pattern:** use a surrogate key as the primary key, but still put a `UNIQUE` constraint on the natural identifier so it is enforced.

```sql
CREATE TABLE customers (
    customer_id  INT           AUTO_INCREMENT PRIMARY KEY,
    email        VARCHAR(150)  NOT NULL UNIQUE,   -- still enforced, just not the PK
    name         VARCHAR(100)  NOT NULL
);
```

---

## Indexes — Making Queries Fast

An **index** is a data structure the database maintains alongside a table to make lookups faster. Think of it like the index at the back of a textbook — instead of reading every page to find a topic, you go to the index, find the page number, and go directly there.

Without an index, a query like `WHERE email = 'riya@email.com'` scans every single row in the table. With an index on `email`, the database jumps directly to the matching row. On a table with millions of rows, this is the difference between milliseconds and minutes.

### Primary keys are automatically indexed

Every primary key column gets an index automatically. You do not have to do anything.

### Creating an index

```sql
-- Single column index
CREATE INDEX idx_customers_email ON customers(email);

-- Index on a column you frequently filter by
CREATE INDEX idx_orders_customer_id ON orders(customer_id);

-- Composite index (order matters — most selective column first)
CREATE INDEX idx_orders_customer_status ON orders(customer_id, status);
```

### UNIQUE indexes

When you add a `UNIQUE` constraint, an index is created automatically:

```sql
-- This creates both a constraint and an index
email VARCHAR(150) NOT NULL UNIQUE;
```

### When to add indexes

Add an index on columns that you:
- Frequently use in `WHERE` clauses
- Frequently use in `JOIN` conditions
- Frequently use in `ORDER BY`

Do not add indexes on every column. Each index takes up storage space and slows down `INSERT`, `UPDATE`, and `DELETE` — because every write must also update the index. Only index what you actually query on.

```sql
-- Common pattern: index foreign key columns
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

Foreign key columns are almost always queried in JOINs, so they almost always need an index.

---

## Designing a Schema from Scratch — The Process

When you are given a new problem to model, follow this process:

**Step 1: Identify the entities.**
An entity is a real-world thing your system needs to track. Read the requirements and underline the nouns. "A customer places an order for products" → entities: customer, order, product.

**Step 2: Identify the attributes of each entity.**
What do you need to know about each one? Customer: name, email, phone, address. Order: date, status, total. Product: name, description, price, stock.

**Step 3: Identify the relationships.**
How do entities relate to each other?
- A customer places many orders. (One-to-many)
- An order contains many products. A product appears in many orders. (Many-to-many → needs a junction table)

**Step 4: Choose primary keys.**
Use surrogate keys (`AUTO_INCREMENT`) for all entities. Add `UNIQUE` constraints on natural identifiers.

**Step 5: Define foreign keys and constraints.**
Add `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK` constraints wherever the data requires it.

**Step 6: Add indexes.**
Index foreign keys and any other columns you expect to filter or join on frequently.

---

## A Complete Example — E-Commerce Schema

Let us walk through designing a schema for a simple e-commerce platform, step by step.

**Requirements:**
- Customers can register and place orders
- Orders can contain multiple products
- Each product belongs to a category
- Orders have statuses: pending, confirmed, shipped, delivered, cancelled
- Payments are tracked separately

**Entities:** customers, products, categories, orders, order items, payments

### Step 1 & 2: Tables and columns

```sql
-- Categories (simple lookup table)
CREATE TABLE categories (
    category_id   INT           AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(100)  NOT NULL UNIQUE,
    description   TEXT
);

-- Customers
CREATE TABLE customers (
    customer_id   INT           AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(100)  NOT NULL,
    email         VARCHAR(150)  NOT NULL UNIQUE,
    phone         VARCHAR(15),
    city          VARCHAR(50),
    created_at    DATETIME      DEFAULT CURRENT_TIMESTAMP
);

-- Products
CREATE TABLE products (
    product_id    INT            AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(150)   NOT NULL,
    description   TEXT,
    price         DECIMAL(10,2)  NOT NULL CHECK (price > 0),
    stock         INT            NOT NULL DEFAULT 0 CHECK (stock >= 0),
    category_id   INT,
    created_at    DATETIME       DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
        ON DELETE SET NULL
);

-- Orders
CREATE TABLE orders (
    order_id      INT           AUTO_INCREMENT PRIMARY KEY,
    customer_id   INT           NOT NULL,
    status        VARCHAR(20)   NOT NULL DEFAULT 'pending'
                                CHECK (status IN ('pending','confirmed','shipped','delivered','cancelled')),
    total_amount  DECIMAL(10,2) NOT NULL CHECK (total_amount >= 0),
    created_at    DATETIME      DEFAULT CURRENT_TIMESTAMP,
    updated_at    DATETIME      DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE RESTRICT
);

-- Order Items (junction table between orders and products)
CREATE TABLE order_items (
    item_id       INT            AUTO_INCREMENT PRIMARY KEY,
    order_id      INT            NOT NULL,
    product_id    INT            NOT NULL,
    quantity      INT            NOT NULL CHECK (quantity > 0),
    unit_price    DECIMAL(10,2)  NOT NULL CHECK (unit_price > 0),
    UNIQUE (order_id, product_id),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON DELETE RESTRICT
);

-- Payments
CREATE TABLE payments (
    payment_id     INT            AUTO_INCREMENT PRIMARY KEY,
    order_id       INT            NOT NULL UNIQUE,   -- one payment per order
    amount         DECIMAL(10,2)  NOT NULL CHECK (amount > 0),
    method         VARCHAR(30)    NOT NULL CHECK (method IN ('card','upi','netbanking','cod')),
    status         VARCHAR(20)    NOT NULL DEFAULT 'pending'
                                  CHECK (status IN ('pending','completed','failed','refunded')),
    paid_at        DATETIME,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE RESTRICT
);
```

### Step 3: Indexes

```sql
-- Foreign key columns (almost always queried in JOINs)
CREATE INDEX idx_products_category_id   ON products(category_id);
CREATE INDEX idx_orders_customer_id     ON orders(customer_id);
CREATE INDEX idx_order_items_order_id   ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
CREATE INDEX idx_payments_order_id      ON payments(order_id);

-- Frequently filtered columns
CREATE INDEX idx_orders_status          ON orders(status);
CREATE INDEX idx_customers_email        ON customers(email);  -- already UNIQUE, auto-indexed
```

### What the schema looks like as a diagram

```
categories
-----------
category_id  PK
name
description

       |
       | (one category → many products)
       ↓

products                    order_items                 orders
--------                    -----------                 ------
product_id    PK            item_id       PK            order_id     PK
name                        order_id      FK --------→  customer_id  FK --------→ customers
description                 product_id    FK ←--------  status                    ----------
price                       quantity                    total_amount              customer_id PK
stock                       unit_price                  created_at                name
category_id   FK                                        updated_at                email
created_at                                                                        phone
                                                               |                  city
                                                               | (one order        created_at
                                                               |  → one payment)
                                                               ↓
                                                        payments
                                                        --------
                                                        payment_id  PK
                                                        order_id    FK
                                                        amount
                                                        method
                                                        status
                                                        paid_at
```

### Sample queries on this schema

```sql
-- All orders by a specific customer with product details
SELECT
    o.order_id,
    o.status,
    p.name          AS product,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS line_total
FROM orders AS o
JOIN order_items AS oi ON o.order_id    = oi.order_id
JOIN products    AS p  ON oi.product_id = p.product_id
WHERE o.customer_id = 1
ORDER BY o.created_at DESC;

-- Total revenue per product category
SELECT
    c.name          AS category,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items AS oi
JOIN products    AS p  ON oi.product_id  = p.product_id
JOIN categories  AS c  ON p.category_id  = c.category_id
JOIN orders      AS o  ON oi.order_id    = o.order_id
WHERE o.status = 'delivered'
GROUP BY c.name
ORDER BY revenue DESC;

-- Customers who have never placed an order
SELECT c.name, c.email
FROM customers AS c
LEFT JOIN orders AS o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Products that are low on stock (less than 10 units)
SELECT name, stock
FROM products
WHERE stock < 10
ORDER BY stock ASC;
```

---

## Common Schema Design Mistakes

### 1. Storing multiple values in one column

```sql
-- BAD: cannot query individual tags
tags VARCHAR(200)   -- stores "electronics,sale,new"

-- GOOD: separate table
CREATE TABLE product_tags (
    product_id INT,
    tag        VARCHAR(50),
    PRIMARY KEY (product_id, tag)
);
```

### 2. Using the wrong data type

```sql
-- BAD: phone numbers lose leading zeros as INT
phone INT

-- BAD: storing money as FLOAT causes rounding errors
price FLOAT   -- 19.99 might be stored as 19.989999999

-- GOOD
phone VARCHAR(15)
price DECIMAL(10, 2)
```

### 3. No NOT NULL on required columns

```sql
-- BAD: an order with no customer_id is meaningless
CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT    -- allows NULL
);

-- GOOD
CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT NOT NULL
);
```

### 4. Skipping foreign keys

Relying on application code to maintain relationships means one bug can create orphan records — orders pointing to customers that do not exist, items pointing to orders that have been deleted. Foreign keys prevent this at the database level.

### 5. Storing calculated values without a reason

```sql
-- Problematic: total_items must be kept in sync manually
CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    total_items INT    -- you have to update this every time order_items changes
);

-- Better: compute it in a query when needed
SELECT order_id, COUNT(*) AS total_items
FROM order_items
GROUP BY order_id;
```

Only store calculated values if there is a proven performance reason to do so.

### 6. Generic column names

```sql
-- BAD: what do these columns mean?
CREATE TABLE records (
    id   INT PRIMARY KEY,
    val1 VARCHAR(100),
    val2 INT,
    val3 DATE,
    type INT
);

-- GOOD: immediately readable
CREATE TABLE employee_leaves (
    leave_id    INT PRIMARY KEY,
    reason      VARCHAR(100),
    days_taken  INT,
    start_date  DATE,
    leave_type  INT
);
```

---

## Quick Reference

| Constraint | Purpose |
|---|---|
| `PRIMARY KEY` | Uniquely identifies each row, no NULLs |
| `NOT NULL` | Column must always have a value |
| `UNIQUE` | All values in the column must be different |
| `DEFAULT value` | Fallback value when nothing is provided |
| `CHECK (condition)` | Value must pass a custom rule |
| `FOREIGN KEY ... REFERENCES` | Links column to a primary key in another table |
| `ON DELETE CASCADE` | Delete child rows when parent is deleted |
| `ON DELETE SET NULL` | Set FK to NULL when parent is deleted |
| `ON DELETE RESTRICT` | Block deletion if child rows exist |
| `AUTO_INCREMENT` / `SERIAL` | Auto-generate the next integer for PK |
| `CREATE INDEX` | Speed up lookups on a column |

---

## Exercises

**1.** A school management system needs to track: students, teachers, subjects, and which students are enrolled in which subjects (with enrolment date). Design the full schema with all tables, columns, data types, primary keys, foreign keys, and constraints. Write the `CREATE TABLE` statements.

**2.** Look at this table and list every normalisation problem you can find. Then rewrite it as a properly normalised schema (at least 3NF):

```
CREATE TABLE sales (
    sale_id        INT,
    salesperson    VARCHAR(100),
    salesperson_phone VARCHAR(15),
    salesperson_region VARCHAR(50),
    product_1_name VARCHAR(100),
    product_1_qty  INT,
    product_1_price DECIMAL(10,2),
    product_2_name VARCHAR(100),
    product_2_qty  INT,
    product_2_price DECIMAL(10,2),
    customer_name  VARCHAR(100),
    customer_email VARCHAR(150),
    customer_city  VARCHAR(50),
    sale_date      DATE
);
```

**3.** For the e-commerce schema from this session, write queries to answer:
   - How many products are in each category?
   - What is the total revenue from completed payments?
   - Which customers have placed more than 2 orders?
   - What is the average order value per customer?

**4.** A hospital needs to manage: patients, doctors, appointments (a patient sees a doctor at a scheduled time), and prescriptions (a doctor prescribes medicines to a patient during an appointment). Design the schema. Think carefully about what is one-to-many and what is many-to-many.

**5.** For each column below, choose the most appropriate data type and add at least one constraint that makes sense for it:
   - A student's roll number (unique within a school, format like `'2024-CS-001'`)
   - An employee's salary
   - A product's discount percentage (0 to 100)
   - A flight's departure time
   - Whether a user's email has been verified
   - A post's content on a blog (can be thousands of characters)
   - A country code (always exactly 2 characters, like `'IN'`)

**6.** You are given this schema for a library:

```sql
CREATE TABLE books (
    id    INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100)
);

CREATE TABLE members (
    id   INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE loans (
    id         INT PRIMARY KEY,
    book_id    INT,
    member_id  INT,
    loan_date  DATE,
    return_date DATE
);
```

Identify at least **five** improvements you would make to this schema. Write the improved version with all your changes applied and explain each one.

**7.** Explain in your own words: why do we add an index on foreign key columns? What happens if we forget to do this?

**8.** A developer says: "I will just store everything in one big table — it is simpler and I can filter with WHERE." Write a clear, specific argument for why this is wrong, using data consistency, update anomalies, and query complexity as your reasoning.

**9.** Design a schema for a food delivery app. It needs to track: restaurants, menu items (each item belongs to a restaurant and a category), customers, orders (a customer orders multiple items from one restaurant), and delivery agents (assigned to an order). Think through all entities, relationships, and constraints before writing any SQL.

**10.** You have a `users` table with 10 million rows. Queries on `WHERE email = ?` are very slow. What would you do, and why? Write the SQL for your solution.
