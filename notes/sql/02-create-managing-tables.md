# Day 2: Creating and Managing Tables in SQL

---

## Start Here: What is a Table?

Everything in a relational database lives in a **table**.

A table is exactly what it sounds like — rows and columns, like a spreadsheet. But unlike a spreadsheet, a table has strict rules:

- Every column has a **name**
- Every column has a **data type** — it only accepts a certain kind of value
- Every row is one complete **record**

| id | name  | age | city   |
|----|-------|-----|--------|
| 1  | Riya  | 21  | Pune   |
| 2  | Arjun | 23  | Mumbai |
| 3  | Sara  | 22  | Delhi  |

This table has 4 columns and 3 rows. Each row is one student. Each column is one piece of information about that student.

This is the foundation of everything in SQL. Every query you write, every report you generate — it all comes back to tables.

---

## Data Types — What Kind of Data Goes Where?

Before you create a table, you must decide what *type* of data each column holds. SQL enforces this strictly — you cannot store text in a number column, and you cannot do math on a text column.

Choosing the right data type matters for three reasons:
1. **Correctness** — wrong types lead to wrong results
2. **Storage** — the right type uses less space
3. **Operations** — you can only sort, add, or compare values if the type is right

### The Most Common Data Types

| Data Type | What it stores | Example values |
|---|---|---|
| `INT` | Whole numbers, positive or negative | `21`, `500`, `-3`, `0` |
| `BIGINT` | Very large whole numbers | `9000000000` |
| `DECIMAL(p, s)` | Numbers with decimals. `p` = total digits, `s` = digits after decimal | `45000.50`, `3.14` |
| `FLOAT` | Approximate decimal numbers (not exact — avoid for money) | `3.14159` |
| `VARCHAR(n)` | Variable-length text, up to `n` characters | `'Riya'`, `'Pune'` |
| `CHAR(n)` | Fixed-length text, always exactly `n` characters | `'M'`, `'F'` |
| `TEXT` | Long text with no practical size limit | A paragraph, a product description |
| `DATE` | A calendar date | `'2024-01-15'` |
| `DATETIME` | A date and a time together | `'2024-01-15 10:30:00'` |
| `TIMESTAMP` | Date + time, often auto-set when a row is created | `'2024-01-15 10:30:00'` |
| `BOOLEAN` | True or false | `TRUE`, `FALSE` |

### Understanding `DECIMAL(p, s)`

`DECIMAL(10, 2)` means:
- Up to **10 digits total**
- **2 of those digits** are after the decimal point
- So the maximum value is `99999999.99`

```sql
price DECIMAL(10, 2)   -- good for money: 99999999.99
rating DECIMAL(3, 1)   -- good for ratings: 9.9
```

### Understanding `VARCHAR(n)` vs `CHAR(n)`

- `VARCHAR(100)` stores up to 100 characters. If you store `'Riya'` (4 characters), it uses 4 characters of space.
- `CHAR(10)` always uses exactly 10 characters. If you store `'M'`, it pads the rest with spaces: `'M         '`.

Use `CHAR` only for fixed-length values like gender codes (`'M'`/`'F'`) or country codes (`'IN'`/`'US'`). For everything else, use `VARCHAR`.

### Choosing the right type — common mistakes

```sql
-- WRONG: storing age as text wastes space and breaks math
age VARCHAR(10)

-- RIGHT
age INT

-- WRONG: storing price as INT loses decimal precision
price INT   -- 45000 stored instead of 45000.50

-- RIGHT
price DECIMAL(10, 2)

-- WRONG: storing a phone number as INT
-- phone numbers can start with 0, and INT drops leading zeros
-- also, you never do math on phone numbers
phone INT

-- RIGHT
phone VARCHAR(15)

-- WRONG: using TEXT for everything is lazy and slow
name TEXT

-- RIGHT
name VARCHAR(100)
```

---

## Creating a Table — `CREATE TABLE`

Now that you know data types, you can define a table properly.

```sql
CREATE TABLE students (
    id       INT,
    name     VARCHAR(100),
    age      INT,
    city     VARCHAR(50)
);
```

Breaking it down line by line:

- `CREATE TABLE students` — tells SQL to create a new table named `students`
- The opening `(` starts the column definitions
- Each line inside defines one column: `column_name  data_type`
- Columns are separated by commas
- The last column has **no comma** after it
- `)` closes the definition
- `;` ends the statement

### Rules for naming tables and columns

- Names cannot have spaces — use underscore `_` instead (`student_name`, not `student name`)
- Names are case-insensitive in most databases, but convention is lowercase with underscores
- Names cannot be SQL reserved words like `SELECT`, `TABLE`, `FROM`
- Keep names descriptive but short

### A more realistic table

```sql
CREATE TABLE employees (
    id            INT,
    full_name     VARCHAR(100),
    email         VARCHAR(150),
    department    VARCHAR(50),
    salary        DECIMAL(10, 2),
    joining_date  DATE,
    is_active     BOOLEAN
);
```

Each column is clearly named, and the data type matches what the column will store.

---

## Inserting Data — `INSERT INTO`

A table with no rows is useless. Let's add records.

### Inserting one row

```sql
INSERT INTO students (id, name, age, city)
VALUES (1, 'Riya', 21, 'Pune');
```

Breaking it down:
- `INSERT INTO students` — which table to insert into
- `(id, name, age, city)` — which columns you are providing values for
- `VALUES` — the actual data, in the **same order** as the columns listed above
- Text values go inside **single quotes** `' '`
- Numbers do **not** need quotes
- Dates go inside single quotes too: `'2024-01-15'`

### Inserting multiple rows at once

Instead of running one INSERT per row, you can insert many rows in a single statement:

```sql
INSERT INTO students (id, name, age, city)
VALUES
    (1, 'Riya',   21, 'Pune'),
    (2, 'Arjun',  23, 'Mumbai'),
    (3, 'Sara',   22, 'Delhi'),
    (4, 'Karan',  20, 'Pune'),
    (5, 'Meera',  24, 'Hyderabad');
```

Each row of values is separated by a comma. The last row ends with `;`.

### What happens if you skip a column?

If you don't include a column in your INSERT, SQL either:
- Stores `NULL` (meaning "no value") if the column allows it
- Throws an error if the column does not allow `NULL`

```sql
-- inserting without city
INSERT INTO students (id, name, age)
VALUES (6, 'Vikram', 22);

-- city will be stored as NULL for this row
```

### Inserting with all columns (shorthand)

If you provide values for **every** column in the table, in the exact order they were defined, you can skip listing column names:

```sql
INSERT INTO students
VALUES (7, 'Ananya', 21, 'Bangalore');
```

This works but is risky — if the table structure changes later, this statement may break or insert data in the wrong columns. It is better practice to always list column names explicitly.

---

## Renaming a Table — `RENAME TABLE`

Sometimes you name a table quickly and later realize the name should be different.

```sql
RENAME TABLE students TO learners;
```

After this, the table `students` no longer exists — it is now called `learners`. All the data inside stays exactly the same. Only the name changes.

### In some databases (like PostgreSQL)

```sql
ALTER TABLE students RENAME TO learners;
```

Both do the same thing. `RENAME TABLE` is MySQL syntax. `ALTER TABLE ... RENAME TO` works in PostgreSQL and SQLite.

---

## Deleting a Table — `DROP TABLE`

`DROP TABLE` permanently deletes a table — the structure and all the data inside it.

```sql
DROP TABLE students;
```

This is **irreversible**. The table and every row in it are gone.

### DROP TABLE IF EXISTS

If you try to `DROP` a table that doesn't exist, SQL throws an error. To avoid this:

```sql
DROP TABLE IF EXISTS students;
```

This says: "Delete this table if it exists. If it doesn't exist, do nothing." This is safer and commonly used in scripts.

### DROP vs DELETE — a critical difference

This is one of the most important distinctions in SQL:

| | `DROP TABLE` | `DELETE FROM` |
|---|---|---|
| What it removes | The entire table (structure + all data) | Only the rows (structure stays) |
| Can you undo it? | No | Yes, if inside a transaction |
| Table still exists after? | No | Yes |

```sql
DROP TABLE students;
-- Table is gone completely. Cannot SELECT from it anymore.

DELETE FROM students;
-- Table still exists. It is now empty. You can INSERT new rows.
```

---

## Modifying a Table — `ALTER TABLE`

After creating a table, you often need to change it — add a column, remove one, rename one, or change a data type. `ALTER TABLE` handles all of this.

### Adding a new column

```sql
ALTER TABLE students
ADD COLUMN phone VARCHAR(15);
```

This adds a `phone` column to the existing `students` table. All existing rows will have `NULL` in this new column until you update them.

You can also add the column at a specific position (MySQL):

```sql
ALTER TABLE students
ADD COLUMN phone VARCHAR(15) AFTER name;
```

Or as the first column:

```sql
ALTER TABLE students
ADD COLUMN phone VARCHAR(15) FIRST;
```

### Dropping (removing) a column

```sql
ALTER TABLE students
DROP COLUMN city;
```

The `city` column and all its data are permanently removed from the table.

### Renaming a column

In MySQL:

```sql
ALTER TABLE students
RENAME COLUMN name TO full_name;
```

In older MySQL versions (before 8.0), `RENAME COLUMN` was not supported. The workaround was `CHANGE`:

```sql
ALTER TABLE students
CHANGE name full_name VARCHAR(100);
```

Note: with `CHANGE`, you must also re-specify the data type — even if it hasn't changed.

In PostgreSQL:

```sql
ALTER TABLE students
RENAME COLUMN name TO full_name;
```

### Changing a column's data type

```sql
ALTER TABLE students
MODIFY COLUMN age SMALLINT;
```

`MODIFY COLUMN` lets you change the data type of an existing column. In PostgreSQL, the syntax is:

```sql
ALTER TABLE students
ALTER COLUMN age TYPE SMALLINT;
```

**Be careful:** if the existing data doesn't fit the new type, the operation will fail. For example, if you try to change a `VARCHAR` column to `INT` but the column contains text values, SQL will throw an error.

### Multiple alterations at once (MySQL)

You can chain multiple changes in one `ALTER TABLE` statement:

```sql
ALTER TABLE students
ADD COLUMN phone VARCHAR(15),
RENAME COLUMN name TO full_name,
MODIFY COLUMN age SMALLINT;
```

---

## Deleting Data from a Table — `DELETE FROM`

`DELETE FROM` removes rows from a table. The table itself stays — only the data is removed.

### Delete all rows

```sql
DELETE FROM students;
```

This empties the table completely. The table structure — all the columns — remains. You can still insert new rows after this.

### Delete specific rows

Almost always, you only want to delete certain rows. You use a `WHERE` clause to specify which ones:

```sql
DELETE FROM students
WHERE id = 3;
```

This deletes only the row where `id` is 3. Every other row stays.

```sql
DELETE FROM students
WHERE city = 'Mumbai';
```

This deletes all rows where city is Mumbai.

**Warning:** If you forget the `WHERE` clause, you delete every single row. This is one of the most common and painful mistakes in SQL. Always double-check your `DELETE` statements.

### The safe habit — SELECT before DELETE

Before running a `DELETE`, run a `SELECT` with the same `WHERE` clause first:

```sql
-- First, check what you are about to delete
SELECT * FROM students WHERE city = 'Mumbai';

-- If the result looks right, then delete
DELETE FROM students WHERE city = 'Mumbai';
```

This way you see exactly what will be removed before it's gone.

---

## Adding a Date to a Table

Dates deserve special attention because they have a specific format SQL expects.

### Storing dates correctly

SQL stores dates as `'YYYY-MM-DD'`.

```sql
CREATE TABLE orders (
    id            INT,
    customer_name VARCHAR(100),
    order_date    DATE,
    delivery_date DATE
);

INSERT INTO orders (id, customer_name, order_date, delivery_date)
VALUES (1, 'Riya', '2024-01-15', '2024-01-20');
```

### Using DATETIME for date + time

```sql
CREATE TABLE logins (
    id          INT,
    username    VARCHAR(100),
    login_time  DATETIME
);

INSERT INTO logins (id, username, login_time)
VALUES (1, 'riya21', '2024-01-15 10:30:00');
```

### Auto-recording the current date/time

Instead of manually typing the date every time, you can tell SQL to automatically use the current date/time:

```sql
INSERT INTO logins (id, username, login_time)
VALUES (2, 'arjun99', NOW());
```

`NOW()` is a SQL function that returns the current date and time at the moment the query runs.

For just the current date (no time):

```sql
INSERT INTO orders (id, customer_name, order_date)
VALUES (2, 'Arjun', CURDATE());
```

### Setting a default value for a date column

You can make the date fill in automatically every time a row is inserted:

```sql
CREATE TABLE orders (
    id            INT,
    customer_name VARCHAR(100),
    order_date    DATE DEFAULT (CURDATE())
);
```

Now if you insert a row without specifying `order_date`, it automatically gets today's date.

---

## Putting It All Together — A Full Example

Let's build a complete table from scratch, insert data, and then make changes to it.

```sql
-- Step 1: Create the table
CREATE TABLE products (
    id           INT,
    product_name VARCHAR(100),
    price        DECIMAL(10, 2),
    stock        INT,
    added_on     DATE
);

-- Step 2: Insert some products
INSERT INTO products (id, product_name, price, stock, added_on)
VALUES
    (1, 'Notebook',    45.00,  200, '2024-01-10'),
    (2, 'Pen Set',     120.50, 500, '2024-01-10'),
    (3, 'Highlighter', 60.00,  300, '2024-01-12');

-- Step 3: We realize we need a category column — add it
ALTER TABLE products
ADD COLUMN category VARCHAR(50);

-- Step 4: We also need to track when the product was last updated
ALTER TABLE products
ADD COLUMN last_updated DATETIME;

-- Step 5: The column "product_name" is too long to type — rename it
ALTER TABLE products
RENAME COLUMN product_name TO name;

-- Step 6: Delete a product that is no longer sold
DELETE FROM products
WHERE id = 2;

-- Step 7: Check what's in the table now
SELECT * FROM products;
```

Notice how naturally each operation builds on the previous one. This is the normal workflow when working with a database.

---

## Quick Reference — All Commands from Today

| What you want to do | SQL command |
|---|---|
| Create a new table | `CREATE TABLE name (col type, ...);` |
| Rename a table | `RENAME TABLE old TO new;` |
| Delete a table permanently | `DROP TABLE name;` |
| Delete table only if it exists | `DROP TABLE IF EXISTS name;` |
| Add a column | `ALTER TABLE name ADD COLUMN col type;` |
| Remove a column | `ALTER TABLE name DROP COLUMN col;` |
| Rename a column | `ALTER TABLE name RENAME COLUMN old TO new;` |
| Change a column's data type | `ALTER TABLE name MODIFY COLUMN col newtype;` |
| Insert one row | `INSERT INTO name (cols) VALUES (vals);` |
| Insert multiple rows | `INSERT INTO name (cols) VALUES (...), (...);` |
| Delete all rows | `DELETE FROM name;` |
| Delete specific rows | `DELETE FROM name WHERE condition;` |

---

## Exercises

**1.** Create a table called `library` with the following columns:
   - `id` — whole number
   - `title` — text, up to 150 characters
   - `author` — text, up to 100 characters
   - `price` — decimal number with 2 decimal places
   - `published_on` — a date
   - `available` — true or false

**2.** Insert at least 5 books into the `library` table with realistic data.

**3.** After inserting, you realize you forgot a column `genre` (text, up to 50 characters). Add it to the table without recreating it.

**4.** Rename the column `title` to `book_title`.

**5.** One of the books is no longer available. Delete that specific row using its `id`. First write the `SELECT` to verify which row it is, then write the `DELETE`.

**6.** Rename the entire table from `library` to `books`.

**7.** What is the difference between `DROP TABLE books` and `DELETE FROM books`? Write one sentence each explaining what each command does and when you would use it.

**8.** You are designing a table to store employee records. For each piece of information below, choose the correct data type and explain why:
   - Employee ID
   - Full name
   - Email address
   - Monthly salary
   - Date of joining
   - Whether the employee is currently active
   - Employee's profile bio (could be several paragraphs)
   - Country code (always 2 characters, like `'IN'`, `'US'`)

**9.** A junior developer wrote this:

```sql
CREATE TABLE customers (
    customer_id INT,
    phone_number INT,
    balance FLOAT,
    signup_date VARCHAR(20)
);
```

List every mistake in this table definition and write the corrected version.

**10.** Without running any SQL, predict what will happen when you run this statement:

```sql
DELETE FROM library;
```

Then explain how you would recover if you ran this by mistake (think about what options you have and what options you don't).
