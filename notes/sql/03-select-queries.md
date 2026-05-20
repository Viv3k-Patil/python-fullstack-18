# Day 3: Retrieving Data — SELECT Queries

---

## Start Here: The Point of a Database

You have spent two days learning how to create tables and put data into them. Today is where it gets interesting — **getting data out**.

In real life, a database can have millions of rows. You never want all of it at once. You want specific rows, specific columns, in a specific order. That is what `SELECT` is for.

`SELECT` is the most used command in SQL. Every report, every search result, every dashboard — all of it starts with a `SELECT` query. Mastering it is the core of SQL.

---

## The Simplest SELECT

Let's say you have this table called `students`:

| id | name  | age | city   | marks |
|----|-------|-----|--------|-------|
| 1  | Riya  | 21  | Pune   | 88    |
| 2  | Arjun | 23  | Mumbai | 74    |
| 3  | Sara  | 22  | Delhi  | 91    |
| 4  | Karan | 20  | Pune   | 65    |
| 5  | Meera | 24  | Mumbai | 79    |

The simplest query you can write:

```sql
SELECT * FROM students;
```

- `SELECT` — the command to retrieve data
- `*` — means "all columns"
- `FROM students` — which table to get data from

This returns every column, every row. All 5 rows, all 5 columns.

The `*` is called a **wildcard**. It is convenient but should be used carefully — in real applications, always specify exactly which columns you need. Fetching unnecessary columns wastes memory and slows things down.

---

## Selecting Specific Columns

Instead of `*`, list the column names you want:

```sql
SELECT name, city FROM students;
```

Result:

| name  | city   |
|-------|--------|
| Riya  | Pune   |
| Arjun | Mumbai |
| Sara  | Delhi  |
| Karan | Pune   |
| Meera | Mumbai |

Only those two columns are returned — even though the table has more.

```sql
SELECT name, marks FROM students;
```

Result:

| name  | marks |
|-------|-------|
| Riya  | 88    |
| Arjun | 74    |
| Sara  | 91    |
| Karan | 65    |
| Meera | 79    |

The columns appear in the order you write them in the query — not necessarily the order they are stored in the table.

```sql
SELECT marks, name, city FROM students;
```

Result:

| marks | name  | city   |
|-------|-------|--------|
| 88    | Riya  | Pune   |
| 74    | Arjun | Mumbai |
| 91    | Sara  | Delhi  |
| 65    | Karan | Pune   |
| 79    | Meera | Mumbai |

---

## The FROM Clause

`FROM` tells SQL which table to read data from. Without it, SQL has no idea where to look.

```sql
SELECT name FROM students;
--              ^^^^^^^^
--              this is the FROM clause
```

It seems simple now because we are working with one table. Later, when you work with multiple tables and joins, the `FROM` clause becomes more powerful. For now, always remember: `SELECT` says *what*, `FROM` says *where from*.

### The order of a SELECT statement

A SQL query is written in this order:

```sql
SELECT  columns
FROM    table
WHERE   condition
ORDER BY column
LIMIT   number;
```

You will learn each part today. They must always appear in this order. SQL is strict about this.

---

## The WHERE Clause — Filtering Rows

`WHERE` lets you filter — you only get back the rows that match a condition. This is where the real power of SQL begins.

```sql
SELECT * FROM students
WHERE city = 'Pune';
```

Result:

| id | name  | age | city | marks |
|----|-------|-----|------|-------|
| 1  | Riya  | 21  | Pune | 88    |
| 4  | Karan | 20  | Pune | 65    |

Only rows where `city` equals `'Pune'` are returned.

### Comparison operators

You can use these operators in a `WHERE` clause:

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `WHERE age = 21` |
| `!=` or `<>` | Not equal to | `WHERE city != 'Pune'` |
| `>` | Greater than | `WHERE marks > 80` |
| `<` | Less than | `WHERE marks < 70` |
| `>=` | Greater than or equal to | `WHERE marks >= 80` |
| `<=` | Less than or equal to | `WHERE age <= 22` |

```sql
-- Students with marks greater than 80
SELECT name, marks FROM students
WHERE marks > 80;
```

Result:

| name | marks |
|------|-------|
| Riya | 88    |
| Sara | 91    |

```sql
-- Students who are not from Mumbai
SELECT name, city FROM students
WHERE city != 'Mumbai';
```

Result:

| name  | city  |
|-------|-------|
| Riya  | Pune  |
| Sara  | Delhi |
| Karan | Pune  |

### Combining conditions — AND, OR, NOT

**AND** — both conditions must be true:

```sql
SELECT * FROM students
WHERE city = 'Pune' AND marks > 70;
```

Result:

| id | name | age | city | marks |
|----|------|-----|------|-------|
| 1  | Riya | 21  | Pune | 88    |

Karan is from Pune but his marks are 65, so he does not qualify. Riya satisfies both conditions.

**OR** — at least one condition must be true:

```sql
SELECT * FROM students
WHERE city = 'Pune' OR city = 'Delhi';
```

Result:

| id | name  | age | city  | marks |
|----|-------|-----|-------|-------|
| 1  | Riya  | 21  | Pune  | 88    |
| 3  | Sara  | 22  | Delhi | 91    |
| 4  | Karan | 20  | Pune  | 65    |

**NOT** — negates a condition:

```sql
SELECT * FROM students
WHERE NOT city = 'Mumbai';
```

This is equivalent to `WHERE city != 'Mumbai'`.

### Combining AND and OR — use parentheses

When you mix `AND` and `OR`, SQL evaluates `AND` before `OR` — just like multiplication before addition in math. Use parentheses to make your logic explicit and avoid mistakes.

```sql
-- Students from Pune OR (from Mumbai AND scoring above 75)
SELECT name, city, marks FROM students
WHERE city = 'Pune' OR (city = 'Mumbai' AND marks > 75);
```

Result:

| name  | city   | marks |
|-------|--------|-------|
| Riya  | Pune   | 88    |
| Karan | Pune   | 65    |
| Meera | Mumbai | 79    |

Arjun is from Mumbai but scored 74, so he does not qualify.

### WHERE with text — case sensitivity

In most databases, text comparisons in `WHERE` are **case-insensitive** by default. But don't rely on this — it depends on the database and its settings. Always write text values exactly as they are stored.

```sql
WHERE city = 'pune'    -- may or may not match 'Pune' depending on database
WHERE city = 'Pune'    -- safer — match exactly as stored
```

### BETWEEN — a range check

Instead of writing `WHERE marks >= 70 AND marks <= 90`, you can use `BETWEEN`:

```sql
SELECT name, marks FROM students
WHERE marks BETWEEN 70 AND 90;
```

Result:

| name  | marks |
|-------|-------|
| Riya  | 88    |
| Arjun | 74    |
| Meera | 79    |

`BETWEEN` is inclusive — it includes both the lower and upper boundary values.

### IN — matching against a list

Instead of writing `WHERE city = 'Pune' OR city = 'Delhi' OR city = 'Mumbai'`, use `IN`:

```sql
SELECT name, city FROM students
WHERE city IN ('Pune', 'Delhi');
```

Result:

| name  | city  |
|-------|-------|
| Riya  | Pune  |
| Sara  | Delhi |
| Karan | Pune  |

You can also use `NOT IN` to exclude a list:

```sql
SELECT name, city FROM students
WHERE city NOT IN ('Mumbai', 'Delhi');
```

### LIKE — pattern matching in text

`LIKE` lets you search for partial matches in text columns. It uses two special characters:

- `%` — matches any sequence of characters (including none)
- `_` — matches exactly one character

```sql
-- Names that start with 'R'
SELECT name FROM students
WHERE name LIKE 'R%';
```

Result: `Riya`

```sql
-- Names that end with 'a'
SELECT name FROM students
WHERE name LIKE '%a';
```

Result: `Riya`, `Sara`, `Meera`

```sql
-- Names that contain 'ar' anywhere
SELECT name FROM students
WHERE name LIKE '%ar%';
```

Result: `Arjun`, `Karan`

```sql
-- Names where the second character is 'a'
SELECT name FROM students
WHERE name LIKE '_a%';
```

Result: `Karan`, `Sara` (second character is `a`)

### IS NULL — checking for missing values

When a column has no value, it is stored as `NULL`. You cannot check for NULL using `=` — you must use `IS NULL`.

```sql
-- Students where phone number is missing
SELECT name FROM students
WHERE phone IS NULL;
```

```sql
-- Students where phone number is not missing
SELECT name FROM students
WHERE phone IS NOT NULL;
```

This is a common mistake — `WHERE phone = NULL` will never return any results. Always use `IS NULL`.

---

## ORDER BY — Sorting Results

By default, SQL returns rows in no guaranteed order. `ORDER BY` lets you sort the results.

### Ascending order (default)

```sql
SELECT name, marks FROM students
ORDER BY marks;
```

Result:

| name  | marks |
|-------|-------|
| Karan | 65    |
| Arjun | 74    |
| Meera | 79    |
| Riya  | 88    |
| Sara  | 91    |

`ASC` (ascending) is the default. Lowest to highest for numbers, A to Z for text.

You can write it explicitly:

```sql
ORDER BY marks ASC;
```

### Descending order

```sql
SELECT name, marks FROM students
ORDER BY marks DESC;
```

Result:

| name  | marks |
|-------|-------|
| Sara  | 91    |
| Riya  | 88    |
| Meera | 79    |
| Arjun | 74    |
| Karan | 65    |

`DESC` = descending. Highest to lowest for numbers, Z to A for text.

### Sorting by text

```sql
SELECT name, city FROM students
ORDER BY name ASC;
```

Result:

| name  | city   |
|-------|--------|
| Arjun | Mumbai |
| Karan | Pune   |
| Meera | Mumbai |
| Riya  | Pune   |
| Sara  | Delhi  |

Alphabetical order, A to Z.

### Sorting by multiple columns

You can sort by more than one column. The second column acts as a tiebreaker when the first column has equal values.

```sql
SELECT name, city, marks FROM students
ORDER BY city ASC, marks DESC;
```

This first sorts by city alphabetically. Within the same city, it sorts by marks from highest to lowest.

Result:

| name  | city   | marks |
|-------|--------|-------|
| Sara  | Delhi  | 91    |
| Meera | Mumbai | 79    |
| Arjun | Mumbai | 74    |
| Riya  | Pune   | 88    |
| Karan | Pune   | 65    |

Delhi comes first, then Mumbai (Meera before Arjun because 79 > 74), then Pune (Riya before Karan because 88 > 65).

### ORDER BY with WHERE

```sql
SELECT name, marks FROM students
WHERE city = 'Pune'
ORDER BY marks DESC;
```

First filter, then sort. The result is only Pune students, sorted by marks:

| name  | marks |
|-------|-------|
| Riya  | 88    |
| Karan | 65    |

---

## LIMIT — Controlling How Many Rows You Get Back

`LIMIT` restricts the number of rows returned. This is useful when you only need the top few results, or when you are browsing a large table.

```sql
SELECT name, marks FROM students
ORDER BY marks DESC
LIMIT 3;
```

Result — top 3 students by marks:

| name  | marks |
|-------|-------|
| Sara  | 91    |
| Riya  | 88    |
| Meera | 79    |

### LIMIT with OFFSET

`OFFSET` tells SQL how many rows to skip before starting to return results. This is how pagination works.

```sql
SELECT name, marks FROM students
ORDER BY marks DESC
LIMIT 2 OFFSET 0;    -- page 1: rows 1-2
```

```sql
SELECT name, marks FROM students
ORDER BY marks DESC
LIMIT 2 OFFSET 2;    -- page 2: rows 3-4
```

```sql
SELECT name, marks FROM students
ORDER BY marks DESC
LIMIT 2 OFFSET 4;    -- page 3: row 5
```

Think of it as: skip the first `OFFSET` rows, then return the next `LIMIT` rows.

### LIMIT without ORDER BY is unpredictable

```sql
-- BAD: no ORDER BY, you get 3 random rows (not necessarily top 3)
SELECT name, marks FROM students
LIMIT 3;

-- GOOD: with ORDER BY, you get the top 3 meaningfully
SELECT name, marks FROM students
ORDER BY marks DESC
LIMIT 3;
```

Always pair `LIMIT` with `ORDER BY` if you care about which rows you get.

---

## DISTINCT — Removing Duplicate Values

`DISTINCT` removes duplicate values from your result. It keeps only unique values.

Imagine you want to know which cities your students come from:

```sql
SELECT city FROM students;
```

Result:

| city   |
|--------|
| Pune   |
| Mumbai |
| Delhi  |
| Pune   |
| Mumbai |

Pune and Mumbai appear twice each — because multiple students are from those cities. You don't want duplicates, you just want the unique cities:

```sql
SELECT DISTINCT city FROM students;
```

Result:

| city   |
|--------|
| Pune   |
| Mumbai |
| Delhi  |

Only 3 unique cities, no repetition.

### DISTINCT with multiple columns

When you use `DISTINCT` with multiple columns, it removes rows where **all selected columns together** are duplicates.

```sql
SELECT DISTINCT city, age FROM students;
```

This returns unique combinations of city and age — not just unique cities or unique ages.

### COUNT with DISTINCT — how many unique values?

```sql
SELECT COUNT(DISTINCT city) FROM students;
```

This counts how many unique cities exist in the table. Result: `3`.

You will learn more about `COUNT` and other aggregate functions in a future session. For now, just know that `DISTINCT` works inside them too.

---

## Aliases — Renaming Columns in Results

An **alias** gives a column or table a temporary name in your query result. It does not change anything in the database — it only changes what the output looks like.

### Column alias with AS

```sql
SELECT name AS student_name, marks AS total_marks
FROM students;
```

Result:

| student_name | total_marks |
|--------------|-------------|
| Riya         | 88          |
| Arjun        | 74          |
| Sara         | 91          |
| Karan        | 65          |
| Meera        | 79          |

The column `name` now appears as `student_name` in the output. The actual column in the table is still called `name`.

### When are aliases useful?

**1. Making output more readable:**

```sql
SELECT name AS "Student Name", marks AS "Exam Score"
FROM students;
```

Use double quotes when the alias has spaces.

**2. When columns have long or unclear names:**

```sql
SELECT emp_no AS id, f_name AS "First Name"
FROM employees;
```

**3. When you compute values:**

```sql
SELECT name, marks, marks * 1.1 AS adjusted_marks
FROM students;
```

Result:

| name  | marks | adjusted_marks |
|-------|-------|----------------|
| Riya  | 88    | 96.8           |
| Arjun | 74    | 81.4           |
| Sara  | 91    | 100.1          |
| Karan | 65    | 71.5           |
| Meera | 79    | 86.9           |

The column `marks * 1.1` is a computed value. Without an alias, the column header would literally show `marks * 1.1`. With the alias `adjusted_marks`, it is readable.

### The AS keyword is optional

In most databases, `AS` is optional. These two are identical:

```sql
SELECT name AS student_name FROM students;
SELECT name student_name FROM students;
```

But always use `AS` — it makes the query much easier to read.

### Table alias

You can also give tables an alias. This is more useful when working with multiple tables (joins), but good to know now:

```sql
SELECT s.name, s.marks
FROM students AS s;
```

Here `s` is an alias for `students`. Instead of writing `students.name`, you write `s.name`. Again — more relevant in joins, but the concept is the same.

---

## Putting It All Together

Here are some realistic queries combining everything from today:

```sql
-- Top 3 students from Pune, sorted by marks
SELECT name, marks
FROM students
WHERE city = 'Pune'
ORDER BY marks DESC
LIMIT 3;
```

```sql
-- Unique cities where students score above 75
SELECT DISTINCT city
FROM students
WHERE marks > 75
ORDER BY city ASC;
```

```sql
-- All students, showing name and a label for their score
SELECT name AS "Student", marks AS "Score", city AS "From"
FROM students
WHERE marks BETWEEN 70 AND 90
ORDER BY marks DESC;
```

```sql
-- Students not from Mumbai or Delhi, showing top 2 scorers
SELECT name, city, marks
FROM students
WHERE city NOT IN ('Mumbai', 'Delhi')
ORDER BY marks DESC
LIMIT 2;
```

---

## The Full SELECT Structure — Summary

```sql
SELECT   DISTINCT column1, column2 AS alias
FROM     table_name
WHERE    condition
ORDER BY column ASC/DESC
LIMIT    n OFFSET m;
```

These clauses must appear in this exact order. Not all of them are required every time — `WHERE`, `ORDER BY`, `LIMIT`, and `DISTINCT` are all optional — but when you use them, they go in this sequence.

---

## Quick Reference

| Clause / Keyword | What it does |
|---|---|
| `SELECT *` | Select all columns |
| `SELECT col1, col2` | Select specific columns |
| `FROM table` | Which table to read from |
| `WHERE condition` | Filter rows |
| `AND`, `OR`, `NOT` | Combine conditions |
| `BETWEEN a AND b` | Range check (inclusive) |
| `IN (list)` | Match against a list of values |
| `LIKE 'pattern'` | Partial text match (`%` = any chars, `_` = one char) |
| `IS NULL` / `IS NOT NULL` | Check for missing values |
| `ORDER BY col ASC` | Sort ascending (A-Z, low-high) |
| `ORDER BY col DESC` | Sort descending (Z-A, high-low) |
| `LIMIT n` | Return only n rows |
| `LIMIT n OFFSET m` | Skip m rows, then return n |
| `DISTINCT` | Remove duplicate values |
| `AS alias` | Rename a column in output |

---

## Exercises

Use this table for all exercises. Create it and insert the data before you start:

```sql
CREATE TABLE employees (
    id         INT,
    name       VARCHAR(100),
    department VARCHAR(50),
    city       VARCHAR(50),
    salary     DECIMAL(10, 2),
    join_date  DATE,
    is_active  BOOLEAN
);

INSERT INTO employees (id, name, department, city, salary, join_date, is_active)
VALUES
    (1,  'Ananya Sharma',  'Engineering',  'Pune',      72000.00, '2021-03-15', TRUE),
    (2,  'Rohan Mehta',    'Marketing',    'Mumbai',    55000.00, '2020-07-01', TRUE),
    (3,  'Priya Nair',     'Engineering',  'Bangalore', 85000.00, '2019-11-20', TRUE),
    (4,  'Kiran Joshi',    'HR',           'Pune',      48000.00, '2022-01-10', FALSE),
    (5,  'Siddharth Rao',  'Engineering',  'Mumbai',    91000.00, '2018-06-05', TRUE),
    (6,  'Neha Kulkarni',  'Marketing',    'Pune',      61000.00, '2021-09-30', TRUE),
    (7,  'Aditya Verma',   'HR',           'Delhi',     52000.00, '2023-02-14', TRUE),
    (8,  'Swati Patil',    'Engineering',  'Pune',      78000.00, '2020-04-22', FALSE),
    (9,  'Manish Gupta',   'Finance',      'Mumbai',    67000.00, '2019-08-11', TRUE),
    (10, 'Divya Reddy',    'Finance',      'Hyderabad', 74000.00, '2022-05-19', TRUE);
```

**1.** Select all columns from the `employees` table.

**2.** Select only `name`, `department`, and `salary` from the table.

**3.** Get all employees who work in `Engineering`.

**4.** Get all employees with a salary greater than `70000`.

**5.** Get all employees from `Pune` who are currently active (`is_active = TRUE`).

**6.** Get all employees whose salary is between `50000` and `75000`.

**7.** Get employees from either `Pune` or `Bangalore`. Use `IN`.

**8.** Get all employees whose name starts with `'S'`.

**9.** Get all employees whose name contains `'a'` anywhere in it.

**10.** List all employees sorted by salary from highest to lowest.

**11.** List all employees sorted by department alphabetically. Within the same department, sort by salary from highest to lowest.

**12.** Show only the top 3 highest-paid employees.

**13.** Show employees ranked 4th to 6th by salary (use `LIMIT` with `OFFSET`).

**14.** Show all unique departments in the company.

**15.** Show all unique cities where employees are located, sorted alphabetically.

**16.** Write a query that shows `name` and `salary`, but rename the columns to `"Employee Name"` and `"Monthly Pay"` in the output.

**17.** Write a query that shows each employee's name and their salary increased by 10%. Label the new column `"Revised Salary"`.

**18.** Get all active employees from Engineering or Finance, sorted by salary descending, showing only the top 5.

**19.** How many unique cities have employees earning more than `65000`? (Hint: use `COUNT` with `DISTINCT` inside.)

**20.** A manager asks: "Give me the name, department, and salary of all inactive employees, sorted alphabetically by name." Write that query.
