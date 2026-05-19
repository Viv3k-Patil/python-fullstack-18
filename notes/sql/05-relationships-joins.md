# Day 5: Relationships & JOINs

---

## Start Here: Why Multiple Tables?

So far you have worked with one table at a time. But real databases never have just one table. A real application might have dozens or hundreds.

Here is why. Imagine storing all information about a company in one table:

| order_id | customer_name | customer_email       | customer_city | product_name | product_price | quantity |
|----------|---------------|----------------------|---------------|--------------|---------------|----------|
| 1        | Riya Sharma   | riya@email.com       | Pune          | Notebook     | 45.00         | 2        |
| 2        | Riya Sharma   | riya@email.com       | Pune          | Pen Set      | 120.00        | 1        |
| 3        | Arjun Mehta   | arjun@email.com      | Mumbai        | Notebook     | 45.00         | 5        |
| 4        | Riya Sharma   | riya@email.com       | Pune          | Highlighter  | 60.00         | 3        |

Look at the problems:

- Riya's name, email, and city are repeated three times. If she changes her email, you have to update three rows — and you might miss one.
- The Notebook's price appears twice. If the price changes, every row that has that product must be updated.
- This kind of repetition is called **data redundancy**. It leads to **inconsistency**, wasted storage, and maintenance nightmares.

The solution is to split the data into separate tables and **relate** them to each other. This is called **normalisation** — and it is the entire point of a *relational* database.

Split the one table into three:

**customers**

| customer_id | name        | email           | city   |
|-------------|-------------|-----------------|--------|
| 1           | Riya Sharma | riya@email.com  | Pune   |
| 2           | Arjun Mehta | arjun@email.com | Mumbai |

**products**

| product_id | name        | price  |
|------------|-------------|--------|
| 1          | Notebook    | 45.00  |
| 2          | Pen Set     | 120.00 |
| 3          | Highlighter | 60.00  |

**orders**

| order_id | customer_id | product_id | quantity |
|----------|-------------|------------|----------|
| 1        | 1           | 1          | 2        |
| 2        | 1           | 2          | 1        |
| 3        | 2           | 1          | 5        |
| 4        | 1           | 3          | 3        |

Now Riya's information lives in exactly one place. The Notebook's price lives in exactly one place. The `orders` table connects them using IDs — `customer_id` and `product_id`.

These connecting columns are what **relationships** are built on.

---

## Primary Keys and Foreign Keys

Before you can understand JOINs, you need to understand the two types of keys that create relationships.

### Primary Key

A **primary key** is a column (or set of columns) that uniquely identifies each row in a table. No two rows can have the same primary key. No row can have a NULL primary key.

```sql
CREATE TABLE customers (
    customer_id  INT          PRIMARY KEY,
    name         VARCHAR(100),
    email        VARCHAR(150),
    city         VARCHAR(50)
);
```

`customer_id` is the primary key. Every customer gets a unique ID. You can always find exactly one customer by their ID.

### Foreign Key

A **foreign key** is a column in one table that references the primary key of another table. It is how you say "this row belongs to that row over there."

```sql
CREATE TABLE orders (
    order_id     INT          PRIMARY KEY,
    customer_id  INT,         -- references customers.customer_id
    product_id   INT,         -- references products.product_id
    quantity     INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id)  REFERENCES products(product_id)
);
```

The `customer_id` in `orders` is a foreign key. It must match an existing `customer_id` in the `customers` table — you cannot create an order for a customer who doesn't exist.

### The relationship visualised

```
customers                orders                 products
-----------              --------               ----------
customer_id  <---------- customer_id            product_id
name                     order_id               name
email                    product_id  ----------> product_id
city                     quantity               price
```

The arrows show the relationships. `orders` is in the middle because it connects customers to products. This kind of table is called a **junction table** or **bridge table**.

---

## Types of Relationships

### One-to-Many (most common)

One row in table A relates to many rows in table B.

- One customer can place many orders. One order belongs to one customer.
- One department can have many employees. One employee belongs to one department.
- One author can write many books. One book has one author.

This is the most common relationship type. The foreign key always lives on the "many" side.

```
customers (one)  →  orders (many)
```

### One-to-One

One row in table A relates to exactly one row in table B, and vice versa.

- One employee has one employee profile. One profile belongs to one employee.
- One person has one passport. One passport belongs to one person.

Less common. Often used to split a table when some columns are accessed infrequently.

### Many-to-Many

Many rows in table A relate to many rows in table B.

- One student can enrol in many courses. One course can have many students.
- One order can contain many products. One product can appear in many orders.

You cannot directly implement many-to-many with just two tables. You need a **junction table** in the middle.

```
students  ←→  student_courses  ←→  courses
```

---

## Setting Up the Tables for Today

Create these four tables and insert the data. All examples in this session use these.

```sql
CREATE TABLE departments (
    department_id   INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE employees (
    employee_id   INT PRIMARY KEY,
    name          VARCHAR(100),
    department_id INT,
    salary        DECIMAL(10, 2),
    manager_id    INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE projects (
    project_id   INT PRIMARY KEY,
    project_name VARCHAR(100),
    department_id INT,
    budget        DECIMAL(12, 2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE employee_projects (
    employee_id INT,
    project_id  INT,
    role        VARCHAR(50),
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id)  REFERENCES projects(project_id)
);
```

```sql
INSERT INTO departments VALUES
    (1, 'Engineering'),
    (2, 'Marketing'),
    (3, 'HR'),
    (4, 'Finance'),
    (5, 'Design');

INSERT INTO employees VALUES
    (1,  'Ananya Sharma',  1, 72000.00, 3),
    (2,  'Rohan Mehta',    2, 55000.00, 5),
    (3,  'Priya Nair',     1, 85000.00, NULL),
    (4,  'Kiran Joshi',    3, 48000.00, 6),
    (5,  'Siddharth Rao',  2, 91000.00, NULL),
    (6,  'Neha Kulkarni',  3, 61000.00, NULL),
    (7,  'Aditya Verma',   4, 52000.00, NULL),
    (8,  'Swati Patil',    1, 78000.00, 3),
    (9,  'Manish Gupta',   4, 67000.00, 7),
    (10, 'Divya Reddy',    4, 74000.00, 7),
    (11, 'Ravi Shankar',   NULL, 58000.00, NULL);  -- no department assigned yet

INSERT INTO projects VALUES
    (1, 'Website Redesign',   2, 500000.00),
    (2, 'API Development',    1, 800000.00),
    (3, 'HR Portal',          3, 200000.00),
    (4, 'Data Pipeline',      1, 650000.00),
    (5, 'Brand Campaign',     2, 350000.00),
    (6, 'Internal Audit',     NULL, 150000.00);  -- no department assigned

INSERT INTO employee_projects VALUES
    (1,  2, 'Developer'),
    (3,  2, 'Lead'),
    (8,  2, 'Developer'),
    (1,  4, 'Developer'),
    (3,  4, 'Reviewer'),
    (2,  1, 'Coordinator'),
    (5,  1, 'Lead'),
    (5,  5, 'Lead'),
    (2,  5, 'Coordinator'),
    (4,  3, 'Administrator'),
    (6,  3, 'Lead'),
    (7,  6, 'Auditor'),
    (9,  6, 'Auditor');
```

Notice the intentional design:
- Employee 11 (Ravi Shankar) has no department (`NULL`)
- The Design department (id 5) has no employees
- Project 6 (Internal Audit) has no department assigned
- These gaps exist so you can see exactly how different JOIN types behave

---

## What is a JOIN?

A JOIN combines rows from two or more tables based on a related column between them.

Without JOIN, you can only query one table at a time. With JOIN, you can ask questions that span multiple tables:

- "Show me each employee's name and their department name"
- "Which employees worked on which projects?"
- "Show me all departments and how many employees each has"

The syntax structure is:

```sql
SELECT   columns
FROM     table_a
JOIN     table_b ON table_a.key = table_b.key;
```

`ON` specifies the condition that connects the two tables — almost always a foreign key equalling a primary key.

There are four main types of JOIN. Each one decides what to do when a row in one table has no match in the other table.

---

## INNER JOIN — Only Matching Rows

`INNER JOIN` returns rows that have a match in **both** tables. If a row in either table has no match, it is excluded entirely.

```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;
```

Result:

| name           | department_name |
|----------------|-----------------|
| Ananya Sharma  | Engineering     |
| Rohan Mehta    | Marketing       |
| Priya Nair     | Engineering     |
| Kiran Joshi    | HR              |
| Siddharth Rao  | Marketing       |
| Neha Kulkarni  | HR              |
| Aditya Verma   | Finance         |
| Swati Patil    | Engineering     |
| Manish Gupta   | Finance         |
| Divya Reddy    | Finance         |

Notice:
- Ravi Shankar (employee 11) is **not here** — his `department_id` is NULL, so he has no match in `departments`
- The Design department is **not here** — no employees have `department_id = 5`

INNER JOIN only shows rows where both sides have a match.

### Using table aliases to keep queries clean

When joining tables, always use aliases to avoid writing the full table name repeatedly:

```sql
SELECT e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.department_id;
```

`e` is the alias for `employees`, `d` for `departments`. The result is identical — the query is just much easier to read.

### INNER JOIN with WHERE, ORDER BY, aggregates

JOIN works with every clause you already know:

```sql
-- Employees in Engineering, with their department name
SELECT e.name, d.department_name, e.salary
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.department_id
WHERE d.department_name = 'Engineering'
ORDER BY e.salary DESC;
```

```sql
-- Count of employees per department (only departments that have employees)
SELECT d.department_name, COUNT(e.employee_id) AS headcount
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY headcount DESC;
```

Result:

| department_name | headcount |
|-----------------|-----------|
| Engineering     | 3         |
| Finance         | 3         |
| Marketing       | 2         |
| HR              | 2         |

---

## LEFT JOIN — All Rows from the Left Table

`LEFT JOIN` returns **all rows from the left table**, plus matching rows from the right table. When there is no match on the right side, the right-side columns show `NULL`.

The "left" table is the one listed first — directly after `FROM`.

```sql
SELECT e.name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.department_id;
```

Result:

| name           | department_name |
|----------------|-----------------|
| Ananya Sharma  | Engineering     |
| Rohan Mehta    | Marketing       |
| Priya Nair     | Engineering     |
| Kiran Joshi    | HR              |
| Siddharth Rao  | Marketing       |
| Neha Kulkarni  | HR              |
| Aditya Verma   | Finance         |
| Swati Patil    | Engineering     |
| Manish Gupta   | Finance         |
| Divya Reddy    | Finance         |
| Ravi Shankar   | NULL            |

Now Ravi Shankar appears — even though he has no department. His `department_name` is `NULL` because there is no matching department.

The Design department still does not appear — it is not in the left table (`employees`).

### When to use LEFT JOIN

Use LEFT JOIN when you want to keep all records from the left table regardless of whether they have a match. Common use cases:

- "Show all employees, and their department if they have one"
- "Show all customers, and their orders if they have placed any"
- "Show all students, and their exam scores if they took the exam"

### Finding rows with NO match — the NULL trick

One of the most powerful uses of LEFT JOIN is finding rows that have **no** match in another table:

```sql
-- Employees who have not been assigned to any department
SELECT e.name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
```

Result:

| name         |
|--------------|
| Ravi Shankar |

The logic: after LEFT JOIN, rows with no match have `NULL` in the right table's columns. Filter for those NULLs to find the unmatched rows. This pattern is extremely common in real work.

---

## RIGHT JOIN — All Rows from the Right Table

`RIGHT JOIN` is the mirror image of LEFT JOIN. It returns **all rows from the right table**, plus matching rows from the left table. When there is no match on the left side, left-side columns show `NULL`.

```sql
SELECT e.name, d.department_name
FROM employees AS e
RIGHT JOIN departments AS d ON e.department_id = d.department_id;
```

Result:

| name           | department_name |
|----------------|-----------------|
| Ananya Sharma  | Engineering     |
| Priya Nair     | Engineering     |
| Swati Patil    | Engineering     |
| Rohan Mehta    | Marketing       |
| Siddharth Rao  | Marketing       |
| Kiran Joshi    | HR              |
| Neha Kulkarni  | HR              |
| Aditya Verma   | Finance         |
| Manish Gupta   | Finance         |
| Divya Reddy    | Finance         |
| NULL           | Design          |

Now the Design department appears — even though it has no employees. Its `name` column is `NULL` because there is no matching employee.

Ravi Shankar does not appear — he is in the left table and has no department, and RIGHT JOIN only guarantees all rows from the right table.

### Finding departments with no employees

```sql
SELECT d.department_name
FROM employees AS e
RIGHT JOIN departments AS d ON e.department_id = d.department_id
WHERE e.employee_id IS NULL;
```

Result:

| department_name |
|-----------------|
| Design          |

### RIGHT JOIN vs LEFT JOIN — they are interchangeable

Any RIGHT JOIN can be rewritten as a LEFT JOIN by swapping the tables:

```sql
-- These two queries return the same result

-- RIGHT JOIN version
SELECT e.name, d.department_name
FROM employees AS e
RIGHT JOIN departments AS d ON e.department_id = d.department_id;

-- LEFT JOIN version (swap the tables)
SELECT e.name, d.department_name
FROM departments AS d
LEFT JOIN employees AS e ON e.department_id = d.department_id;
```

In practice, most developers just use LEFT JOIN for everything and reorder the tables. RIGHT JOIN is less common in real code — but you must understand it because you will encounter it.

---

## FULL OUTER JOIN — All Rows from Both Tables

`FULL OUTER JOIN` returns **all rows from both tables**. Matches are shown together. Non-matching rows from either side appear with `NULL` on the other side.

```sql
SELECT e.name, d.department_name
FROM employees AS e
FULL OUTER JOIN departments AS d ON e.department_id = d.department_id;
```

Result:

| name           | department_name |
|----------------|-----------------|
| Ananya Sharma  | Engineering     |
| Rohan Mehta    | Marketing       |
| Priya Nair     | Engineering     |
| Kiran Joshi    | HR              |
| Siddharth Rao  | Marketing       |
| Neha Kulkarni  | HR              |
| Aditya Verma   | Finance         |
| Swati Patil    | Engineering     |
| Manish Gupta   | Finance         |
| Divya Reddy    | Finance         |
| Ravi Shankar   | NULL            |
| NULL           | Design          |

Both unmatched rows appear: Ravi Shankar (no department) and Design (no employees).

### MySQL does not support FULL OUTER JOIN

MySQL does not have a native `FULL OUTER JOIN` keyword. You simulate it by combining a LEFT JOIN and a RIGHT JOIN with `UNION`:

```sql
SELECT e.name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.department_id

UNION

SELECT e.name, d.department_name
FROM employees AS e
RIGHT JOIN departments AS d ON e.department_id = d.department_id;
```

`UNION` combines the results of two queries and removes duplicates. The matched rows appear in both halves but `UNION` keeps only one copy. The unmatched rows from each side contribute the rows with `NULL`.

PostgreSQL and SQL Server support `FULL OUTER JOIN` natively.

---

## CROSS JOIN — Every Combination

`CROSS JOIN` returns every possible combination of rows from two tables — the **cartesian product**. There is no `ON` condition because every row on the left is matched with every row on the right.

```sql
SELECT e.name, d.department_name
FROM employees AS e
CROSS JOIN departments AS d;
```

If `employees` has 11 rows and `departments` has 5 rows, the result has 55 rows (11 × 5). Every employee is paired with every department.

This is rarely what you want — but it has specific use cases:

- Generating all possible combinations (like a size × colour grid for products)
- Creating test data
- Pairing every item with every other item for comparison

```sql
-- Practical example: generate all possible (employee, project) pairings
-- to then check which ones are actually assigned
SELECT e.name, p.project_name
FROM employees AS e
CROSS JOIN projects AS p
ORDER BY e.name, p.project_name;
```

---

## SELF JOIN — A Table Joining Itself

A self join is when a table is joined to itself. It is used when rows in a table have a relationship with other rows in the same table.

The classic example is an employee-manager relationship. In our `employees` table, the `manager_id` column refers to another row in the same `employees` table.

```sql
SELECT
    e.name        AS employee,
    m.name        AS manager
FROM employees AS e
LEFT JOIN employees AS m ON e.manager_id = m.employee_id;
```

Result:

| employee       | manager        |
|----------------|----------------|
| Ananya Sharma  | Priya Nair     |
| Rohan Mehta    | Siddharth Rao  |
| Priya Nair     | NULL           |
| Kiran Joshi    | Neha Kulkarni  |
| Siddharth Rao  | NULL           |
| Neha Kulkarni  | NULL           |
| Aditya Verma   | NULL           |
| Swati Patil    | Priya Nair     |
| Manish Gupta   | Aditya Verma   |
| Divya Reddy    | Aditya Verma   |
| Ravi Shankar   | NULL           |

The trick: you join `employees` to itself using two different aliases — `e` for the employee, `m` for the manager. This lets you treat what is really one table as if it were two. Employees with no manager (`manager_id = NULL`) show `NULL` in the manager column because we used LEFT JOIN.

---

## Joining More Than Two Tables

You can chain multiple JOINs together. Each JOIN adds another table to the result.

```sql
-- Employee name, their department, and the projects they work on
SELECT
    e.name            AS employee,
    d.department_name AS department,
    p.project_name    AS project,
    ep.role
FROM employees AS e
INNER JOIN departments      AS d  ON e.department_id  = d.department_id
INNER JOIN employee_projects AS ep ON e.employee_id   = ep.employee_id
INNER JOIN projects          AS p  ON ep.project_id   = p.project_id
ORDER BY e.name, p.project_name;
```

Result:

| employee       | department  | project          | role        |
|----------------|-------------|------------------|-------------|
| Aditya Verma   | Finance     | Internal Audit   | Auditor     |
| Ananya Sharma  | Engineering | API Development  | Developer   |
| Ananya Sharma  | Engineering | Data Pipeline    | Developer   |
| Manish Gupta   | Finance     | Internal Audit   | Auditor     |
| Neha Kulkarni  | HR          | HR Portal        | Lead        |
| Priya Nair     | Engineering | API Development  | Lead        |
| Priya Nair     | Engineering | Data Pipeline    | Reviewer    |
| Rohan Mehta    | Marketing   | Brand Campaign   | Coordinator |
| Rohan Mehta    | Marketing   | Website Redesign | Coordinator |
| Siddharth Rao  | Marketing   | Brand Campaign   | Lead        |
| Siddharth Rao  | Marketing   | Website Redesign | Lead        |
| Swati Patil    | Engineering | API Development  | Developer   |
| Kiran Joshi    | HR          | HR Portal        | Administrator |

This single query spans four tables and answers a question that would be impossible to answer with just one table.

### The pattern for chaining JOINs

```sql
FROM   first_table AS a
JOIN   second_table AS b ON a.key = b.key
JOIN   third_table  AS c ON b.key = c.key
JOIN   fourth_table AS d ON c.key = d.key
```

Each new JOIN connects to something already in the query. Think of it as building a chain — each link must connect to the previous one.

---

## JOIN with GROUP BY — Aggregating Across Tables

JOINs and GROUP BY are often used together to produce grouped summaries across related tables.

```sql
-- Total budget of projects per department
SELECT d.department_name, SUM(p.budget) AS total_budget
FROM departments AS d
LEFT JOIN projects AS p ON d.department_id = p.department_id
GROUP BY d.department_name
ORDER BY total_budget DESC;
```

Result:

| department_name | total_budget |
|-----------------|--------------|
| Engineering     | 1450000.00   |
| Marketing       | 850000.00    |
| HR              | 200000.00    |
| Finance         | NULL         |
| Design          | NULL         |

Finance and Design have no projects, so their budget is NULL. If you want to show 0 instead:

```sql
SELECT d.department_name, COALESCE(SUM(p.budget), 0) AS total_budget
FROM departments AS d
LEFT JOIN projects AS p ON d.department_id = p.department_id
GROUP BY d.department_name
ORDER BY total_budget DESC;
```

```sql
-- Number of employees per department, including departments with zero employees
SELECT d.department_name, COUNT(e.employee_id) AS headcount
FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY headcount DESC;
```

Result:

| department_name | headcount |
|-----------------|-----------|
| Engineering     | 3         |
| Finance         | 3         |
| Marketing       | 2         |
| HR              | 2         |
| Design          | 0         |

Notice: we used `COUNT(e.employee_id)` not `COUNT(*)`. With a LEFT JOIN, rows where there is no employee have `NULL` in `e.employee_id`. `COUNT(e.employee_id)` skips NULLs, so Design correctly shows 0. `COUNT(*)` would show 1 for Design (counting the NULL row itself).

---

## JOIN Types — Visual Summary

```
Table A        Table B

   [A]            [B]
   [ ]            [ ]
   [AB]  ←match→ [AB]
   [ ]            [ ]

INNER JOIN  →  only [AB] rows (matched from both)
LEFT JOIN   →  all [A] rows + matched [AB] rows
RIGHT JOIN  →  all [B] rows + matched [AB] rows
FULL JOIN   →  all [A] + all [B] rows (matched ones together)
CROSS JOIN  →  every row in A paired with every row in B
```

---

## Common Mistakes with JOINs

### 1. Forgetting the ON condition

```sql
-- WRONG: no ON condition — accidental CROSS JOIN
SELECT e.name, d.department_name
FROM employees e, departments d;

-- RIGHT
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```

The old comma-separated syntax (`FROM a, b`) without a `WHERE` to connect them produces a cartesian product. Always use explicit JOIN syntax with an `ON` condition.

### 2. Ambiguous column names

When two tables have a column with the same name, you must qualify which table you mean:

```sql
-- WRONG: which table does department_id refer to?
SELECT department_id, name FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;

-- RIGHT: always prefix with table name or alias
SELECT e.department_id, e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.department_id;
```

### 3. Using WHERE to filter NULLs after LEFT JOIN

```sql
-- WRONG: this turns your LEFT JOIN into an INNER JOIN
SELECT e.name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.department_id
WHERE d.department_name = 'Engineering';
-- This excludes Ravi Shankar again, because NULL = 'Engineering' is false
```

If you filter on a column from the right table in a `WHERE` clause, rows with `NULL` (the unmatched ones) are automatically excluded. This defeats the purpose of a LEFT JOIN. Either:

- Use an INNER JOIN if you only want matched rows, or
- Move the filter into the `ON` condition if you want to keep unmatched rows

```sql
-- RIGHT: filter in ON keeps unmatched rows
SELECT e.name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.department_id = d.department_id
    AND d.department_name = 'Engineering';
```

Now Ravi Shankar appears with `NULL` department, and employees not in Engineering also appear with `NULL` department. This is different from the INNER JOIN behaviour — use it deliberately.

### 4. COUNT(*) vs COUNT(column) after LEFT JOIN

```sql
-- WRONG: counts the NULL row for departments with no employees
SELECT d.department_name, COUNT(*) AS headcount
FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY d.department_name;
-- Design shows headcount = 1 (wrong)

-- RIGHT: COUNT on a left-table column skips NULLs
SELECT d.department_name, COUNT(e.employee_id) AS headcount
FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY d.department_name;
-- Design shows headcount = 0 (correct)
```

---

## Quick Reference

| JOIN Type | Returns |
|---|---|
| `INNER JOIN` | Only rows with a match in both tables |
| `LEFT JOIN` | All rows from the left table; NULL for non-matches on right |
| `RIGHT JOIN` | All rows from the right table; NULL for non-matches on left |
| `FULL OUTER JOIN` | All rows from both tables; NULLs where no match |
| `CROSS JOIN` | Every combination of rows from both tables |
| `SELF JOIN` | A table joined to itself using two aliases |

---

## The Full Query Structure So Far

```sql
SELECT   DISTINCT e.col, d.col, AGG(col) AS alias
FROM     table_a AS a
JOIN     table_b AS b  ON a.key = b.key
JOIN     table_c AS c  ON b.key = c.key
WHERE    condition
GROUP BY column
HAVING   group_condition
ORDER BY column ASC/DESC
LIMIT    n OFFSET m;
```

---

## Exercises

Use the four tables created at the start of this session: `employees`, `departments`, `projects`, `employee_projects`.

**1.** Write a query that shows each employee's name and the name of their department. Use INNER JOIN.

**2.** Write the same query using LEFT JOIN. What is different in the result and why?

**3.** Show all departments and the employees in them. Include departments that have no employees. Which employee should be missing from this result and why?

**4.** Find all employees who have not been assigned to any department. (Hint: LEFT JOIN + IS NULL.)

**5.** Find all departments that currently have no employees assigned to them.

**6.** Show each employee's name, their department name, and their salary. Sort by salary descending.

**7.** Show the number of employees in each department. Include departments with zero employees.

**8.** Show the average salary per department. Only include departments that have at least one employee.

**9.** Show each project name and the name of the department it belongs to. Include projects with no department assigned.

**10.** Show each employee and the projects they are working on, along with their role. Use the `employee_projects` junction table.

**11.** Show the full picture: employee name, department name, project name, and role. Join all four tables.

**12.** Show each employee and their manager's name. Employees with no manager should still appear, with NULL in the manager column.

**13.** Show only employees whose manager is 'Priya Nair'.

**14.** Show each department and the total budget of all projects belonging to it. Include departments with no projects (show 0 instead of NULL for their budget).

**15.** Show each department and how many projects it has. Include departments with zero projects.

**16.** Show each project and the number of employees working on it. Sort by employee count descending.

**17.** Show only the projects that have more than 2 employees working on them.

**18.** Show each employee and how many projects they are assigned to. Include employees assigned to zero projects.

**19.** Show the department that has the highest total salary bill. Show department name and total salary.

**20.** Write a query that shows employees who are working on a project that belongs to a different department than their own. (Hint: join employee to their department, join project to its department, then compare.)

**21.** Show all employees and all departments — every possible combination. How many rows do you expect? Verify with your result.

**22.** The Design department was just created and has no employees yet. A manager runs this query:

```sql
SELECT d.department_name, COUNT(*) AS headcount
FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY d.department_name;
```

What will the headcount show for Design, and is it correct? Explain why and write the corrected query.

**23.** Explain the difference between putting a filter in the `ON` clause versus the `WHERE` clause in a LEFT JOIN. Use an example to show how the results differ.

**24.** Three developers argued about this query:

```sql
SELECT e.name, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id;
```

Developer A says it works fine. Developer B says it is dangerous. Developer C says it is outdated. Who is right, and what would you write instead?
