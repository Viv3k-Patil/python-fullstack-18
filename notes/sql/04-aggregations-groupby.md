# Day 4: Aggregations & Grouping — COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING

---

## Start Here: From Rows to Summaries

So far, every query you wrote returned rows — one row of output for each row of data (or filtered data). That is useful, but databases are often asked a different kind of question:

- "How many students passed?"
- "What is the average salary in the Engineering department?"
- "Which department has the highest total spend?"
- "What is the lowest and highest marks scored?"

These questions don't ask for individual rows. They ask for a **summary** — a single number that describes a group of rows. This is what **aggregate functions** do.

Think of it like this: aggregation is the difference between reading every entry in a ledger versus asking an accountant for the total.

---

## Aggregate Functions — The Big Five

SQL has five core aggregate functions. Each one takes a group of values and collapses them into a single result.

| Function | What it does |
|---|---|
| `COUNT()` | Counts the number of rows |
| `SUM()` | Adds up all values |
| `AVG()` | Calculates the average |
| `MIN()` | Returns the smallest value |
| `MAX()` | Returns the largest value |

We will use this table for all examples today:

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

---

## COUNT — Counting Rows

`COUNT` answers the question: "How many rows match?"

### Count all rows

```sql
SELECT COUNT(*) FROM employees;
```

Result:

| COUNT(*) |
|----------|
| 10       |

`COUNT(*)` counts every row — including rows with `NULL` values in any column.

### Count rows in a specific column

```sql
SELECT COUNT(salary) FROM employees;
```

This counts rows where `salary` is **not NULL**. If any rows had a missing salary, they would not be counted here but would be counted by `COUNT(*)`. This distinction matters — more on NULL later.

### Count with a WHERE filter

```sql
SELECT COUNT(*) FROM employees
WHERE department = 'Engineering';
```

Result:

| COUNT(*) |
|----------|
| 4        |

Four employees are in Engineering.

### Count distinct values

```sql
SELECT COUNT(DISTINCT department) FROM employees;
```

Result:

| COUNT(DISTINCT department) |
|---------------------------|
| 4                         |

There are 4 unique departments: Engineering, Marketing, HR, Finance.

### Giving COUNT a readable name

```sql
SELECT COUNT(*) AS total_employees FROM employees;
```

Result:

| total_employees |
|-----------------|
| 10              |

Always alias your aggregate results — raw column headers like `COUNT(*)` are ugly in reports.

---

## SUM — Adding Values Up

`SUM` adds up all values in a numeric column.

```sql
SELECT SUM(salary) AS total_salary FROM employees;
```

Result:

| total_salary |
|--------------|
| 683000.00    |

The total salary bill for all 10 employees.

### SUM with a filter

```sql
SELECT SUM(salary) AS engineering_payroll
FROM employees
WHERE department = 'Engineering';
```

Result:

| engineering_payroll |
|--------------------|
| 326000.00           |

Total salary of Engineering employees only (72000 + 85000 + 91000 + 78000).

### SUM only works on numbers

If you try `SUM(name)` or `SUM(city)`, SQL will throw an error. `SUM` is strictly for numeric columns.

---

## AVG — Calculating the Average

`AVG` computes the arithmetic mean of a numeric column.

```sql
SELECT AVG(salary) AS average_salary FROM employees;
```

Result:

| average_salary |
|----------------|
| 68300.00       |

(683000 ÷ 10 = 68300)

### AVG with a filter

```sql
SELECT AVG(salary) AS avg_engineering_salary
FROM employees
WHERE department = 'Engineering';
```

Result:

| avg_engineering_salary |
|------------------------|
| 81500.00               |

(326000 ÷ 4 = 81500)

### Rounding AVG results

`AVG` can return many decimal places. Use `ROUND()` to control this:

```sql
SELECT ROUND(AVG(salary), 2) AS avg_salary FROM employees;
```

`ROUND(value, decimal_places)` — rounds to the specified number of decimal places.

---

## MIN and MAX — Smallest and Largest Values

`MIN` returns the lowest value. `MAX` returns the highest. Both work on numbers, text (alphabetical), and dates (earliest/latest).

```sql
SELECT MIN(salary) AS lowest_salary,
       MAX(salary) AS highest_salary
FROM employees;
```

Result:

| lowest_salary | highest_salary |
|---------------|----------------|
| 48000.00      | 91000.00       |

### MIN and MAX on dates

```sql
SELECT MIN(join_date) AS earliest_joiner,
       MAX(join_date) AS latest_joiner
FROM employees;
```

Result:

| earliest_joiner | latest_joiner |
|-----------------|---------------|
| 2018-06-05      | 2023-02-14    |

`MIN` on a date gives the earliest date. `MAX` gives the most recent.

### MIN and MAX on text

```sql
SELECT MIN(name) AS first_alphabetically,
       MAX(name) AS last_alphabetically
FROM employees;
```

Result:

| first_alphabetically | last_alphabetically |
|----------------------|---------------------|
| Aditya Verma         | Swati Patil         |

`MIN` on text gives the value that comes first alphabetically. `MAX` gives the last.

---

## Using Multiple Aggregates Together

You can run multiple aggregate functions in one query:

```sql
SELECT
    COUNT(*)              AS total_employees,
    SUM(salary)           AS total_payroll,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary)           AS min_salary,
    MAX(salary)           AS max_salary
FROM employees;
```

Result:

| total_employees | total_payroll | avg_salary | min_salary | max_salary |
|-----------------|---------------|------------|------------|------------|
| 10              | 683000.00     | 68300.00   | 48000.00   | 91000.00   |

One row. Five different summary statistics. This is a common pattern for summary reports.

---

## The Problem with Raw Aggregates

The queries above give you totals and averages for the **entire** table. But what if you want:

- "What is the total salary **per department**?"
- "How many employees are in **each city**?"
- "What is the average salary **per department**?"

Running separate queries with `WHERE department = 'Engineering'`, then `WHERE department = 'Marketing'` and so on is tedious and doesn't scale. What if there are 50 departments?

This is exactly what `GROUP BY` solves.

---

## GROUP BY — Aggregating by Category

`GROUP BY` splits the rows into groups based on a column, then applies the aggregate function to each group separately.

### The intuition

Without `GROUP BY`:
```
All 10 employees → COUNT(*) → 10
```

With `GROUP BY department`:
```
Engineering group (4 rows) → COUNT(*) → 4
Marketing group   (2 rows) → COUNT(*) → 2
HR group          (2 rows) → COUNT(*) → 2
Finance group     (2 rows) → COUNT(*) → 2
```

SQL divides the rows into buckets first, then aggregates each bucket.

### COUNT per group

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```

Result:

| department  | employee_count |
|-------------|----------------|
| Engineering | 4              |
| Marketing   | 2              |
| HR          | 2              |
| Finance     | 2              |

One row per department. Each row shows the count for that department.

### SUM per group

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;
```

Result:

| department  | total_salary |
|-------------|--------------|
| Engineering | 326000.00    |
| Marketing   | 116000.00    |
| HR          | 100000.00    |
| Finance     | 141000.00    |

### AVG per group

```sql
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department;
```

Result:

| department  | avg_salary |
|-------------|------------|
| Engineering | 81500.00   |
| Marketing   | 58000.00   |
| HR          | 50000.00   |
| Finance     | 70500.00   |

### MIN and MAX per group

```sql
SELECT department,
       MIN(salary) AS lowest,
       MAX(salary) AS highest
FROM employees
GROUP BY department;
```

Result:

| department  | lowest   | highest  |
|-------------|----------|----------|
| Engineering | 72000.00 | 91000.00 |
| Marketing   | 55000.00 | 61000.00 |
| HR          | 48000.00 | 52000.00 |
| Finance     | 67000.00 | 74000.00 |

### GROUP BY with multiple aggregates

```sql
SELECT
    department,
    COUNT(*)              AS headcount,
    SUM(salary)           AS total_payroll,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary)           AS min_salary,
    MAX(salary)           AS max_salary
FROM employees
GROUP BY department;
```

Result:

| department  | headcount | total_payroll | avg_salary | min_salary | max_salary |
|-------------|-----------|---------------|------------|------------|------------|
| Engineering | 4         | 326000.00     | 81500.00   | 72000.00   | 91000.00   |
| Marketing   | 2         | 116000.00     | 58000.00   | 55000.00   | 61000.00   |
| HR          | 2         | 100000.00     | 50000.00   | 48000.00   | 52000.00   |
| Finance     | 2         | 141000.00     | 70500.00   | 67000.00   | 74000.00   |

This is the kind of table you would see in a real HR report.

### GROUP BY multiple columns

You can group by more than one column. Each unique combination of values becomes its own group.

```sql
SELECT department, city, COUNT(*) AS count
FROM employees
GROUP BY department, city;
```

Result:

| department  | city      | count |
|-------------|-----------|-------|
| Engineering | Pune      | 2     |
| Engineering | Bangalore | 1     |
| Engineering | Mumbai    | 1     |
| Marketing   | Mumbai    | 1     |
| Marketing   | Pune      | 1     |
| HR          | Pune      | 1     |
| HR          | Delhi     | 1     |
| Finance     | Mumbai    | 1     |
| Finance     | Hyderabad | 1     |

Each unique (department, city) pair is its own row.

### GROUP BY with ORDER BY

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;
```

Result:

| department  | total_salary |
|-------------|--------------|
| Engineering | 326000.00    |
| Finance     | 141000.00    |
| Marketing   | 116000.00    |
| HR          | 100000.00    |

Engineering has the highest payroll. You can `ORDER BY` the alias you gave the aggregate.

### GROUP BY with WHERE

`WHERE` filters rows **before** they are grouped. So you can use `WHERE` to exclude rows before aggregating.

```sql
SELECT department, COUNT(*) AS active_count
FROM employees
WHERE is_active = TRUE
GROUP BY department;
```

This counts only active employees per department. Kiran Joshi (HR, inactive) and Swati Patil (Engineering, inactive) are excluded before grouping.

Result:

| department  | active_count |
|-------------|--------------|
| Engineering | 3            |
| Marketing   | 2            |
| HR          | 1            |
| Finance     | 2            |

---

## The Golden Rule of GROUP BY

This is the most important rule, and it trips up almost every beginner:

> **Every column in your SELECT must either be inside an aggregate function OR be listed in GROUP BY.**

```sql
-- WRONG: name is neither grouped nor aggregated
SELECT name, department, COUNT(*)
FROM employees
GROUP BY department;
```

This fails because `name` is not in the `GROUP BY`. SQL doesn't know which name to show — there are 4 employees in Engineering, so which name should appear?

```sql
-- RIGHT: only department is selected, and it is in GROUP BY
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

-- RIGHT: name is aggregated (MIN picks one value per group)
SELECT department, MIN(name) AS first_name_alphabetically, COUNT(*)
FROM employees
GROUP BY department;
```

The fix is always one of two things: add the column to `GROUP BY`, or wrap it in an aggregate function.

---

## HAVING — Filtering Groups

`WHERE` filters individual rows before grouping. But what if you want to filter **after** grouping — for example, "only show departments with more than 2 employees"?

You cannot use `WHERE` for this, because the count doesn't exist until after `GROUP BY` runs. This is where `HAVING` comes in.

`HAVING` filters groups after aggregation.

### HAVING with COUNT

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
```

Result:

| department  | employee_count |
|-------------|----------------|
| Engineering | 4              |

Only Engineering has more than 2 employees.

### HAVING with SUM

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 120000;
```

Result:

| department  | total_salary |
|-------------|--------------|
| Engineering | 326000.00    |
| Finance     | 141000.00    |

Departments where total salary exceeds 120,000.

### HAVING with AVG

```sql
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 65000;
```

Result:

| department  | avg_salary |
|-------------|------------|
| Engineering | 81500.00   |
| Finance     | 70500.00   |

### WHERE vs HAVING — side by side

This is critical. Know the difference deeply.

| | WHERE | HAVING |
|---|---|---|
| Filters | Individual rows | Groups (after GROUP BY) |
| Runs | Before grouping | After grouping |
| Can use aggregates? | No | Yes |
| Used with | Any SELECT | Only with GROUP BY |

```sql
-- WHERE: filter rows before grouping
-- Only include active employees, then count per department
SELECT department, COUNT(*) AS active_headcount
FROM employees
WHERE is_active = TRUE          -- runs first, on rows
GROUP BY department;

-- HAVING: filter groups after grouping
-- Group all employees by department, then only show large departments
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2;           -- runs after, on groups

-- Using both together
-- Among active employees, show departments with avg salary > 70000
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
WHERE is_active = TRUE          -- step 1: filter rows
GROUP BY department             -- step 2: group them
HAVING AVG(salary) > 70000;    -- step 3: filter groups
```

Result of the last query:

| department  | avg_salary |
|-------------|------------|
| Engineering | 82333.33   |
| Finance     | 70500.00   |

(Engineering average changes because Swati Patil is inactive and excluded before grouping.)

---

## NULL Handling in Aggregates

`NULL` means "no value" — not zero, not empty string, just absent. Aggregate functions treat `NULL` in a specific way that you must understand.

### The rule: aggregates ignore NULL

`SUM`, `AVG`, `MIN`, `MAX`, and `COUNT(column)` all **skip NULL values** automatically.

Let's say two employees have no salary recorded (NULL):

```sql
-- Hypothetical table with NULLs
-- Salaries: 72000, 85000, NULL, 91000, NULL

SELECT COUNT(*) FROM employees;        -- 5 (counts all rows)
SELECT COUNT(salary) FROM employees;   -- 3 (skips NULLs)
SELECT SUM(salary) FROM employees;     -- 248000 (skips NULLs)
SELECT AVG(salary) FROM employees;     -- 82666.67 (248000 ÷ 3, not ÷ 5)
```

This is the key danger with `AVG` and `NULL`. If 3 out of 10 salaries are `NULL`, `AVG` divides by 7 (not 10). This can give you a misleading average. Always check whether important columns have `NULL` values before aggregating.

### COUNT(*) vs COUNT(column)

```sql
SELECT COUNT(*)       FROM employees;  -- counts every row, including NULLs
SELECT COUNT(salary)  FROM employees;  -- counts rows where salary is NOT NULL
SELECT COUNT(DISTINCT city) FROM employees;  -- counts unique non-NULL cities
```

Always be deliberate about which one you use. If you want to know how many rows exist, use `COUNT(*)`. If you want to know how many rows have a value for a specific column, use `COUNT(column)`.

### Handling NULLs with COALESCE

`COALESCE(value, fallback)` returns the first non-NULL value. It is the standard way to replace NULLs with a default.

```sql
-- Treat NULL salary as 0 before averaging
SELECT AVG(COALESCE(salary, 0)) AS avg_salary FROM employees;
```

With this, NULL salaries are counted as 0, so the average is divided by all rows, not just the ones with values. Whether this is the right approach depends on what you are trying to measure — use it thoughtfully.

```sql
-- Show 'Unknown' instead of NULL for city
SELECT name, COALESCE(city, 'Unknown') AS city FROM employees;
```

### IFNULL — a simpler alternative (MySQL)

In MySQL, `IFNULL(value, fallback)` does the same thing as `COALESCE` with two arguments:

```sql
SELECT name, IFNULL(city, 'Unknown') AS city FROM employees;
```

`COALESCE` is preferred because it works across all databases. `IFNULL` is MySQL-specific.

---

## The Full Query Execution Order

By now you have learned several clauses. SQL does not execute them in the order you write them. Understanding the actual execution order helps you understand why certain things work and others don't.

```
1. FROM        -- which table(s) to read
2. WHERE       -- filter individual rows
3. GROUP BY    -- divide remaining rows into groups
4. HAVING      -- filter groups
5. SELECT      -- compute the output columns
6. DISTINCT    -- remove duplicate output rows
7. ORDER BY    -- sort the result
8. LIMIT       -- cut the result to n rows
```

This is why you **cannot** use a `SELECT` alias inside a `WHERE` clause — the alias doesn't exist yet when `WHERE` runs. And it's why you use `HAVING` (not `WHERE`) to filter aggregates — aggregates are computed in step 5, after `WHERE` has already run.

```sql
-- WRONG: WHERE runs before SELECT, so 'avg_salary' doesn't exist yet
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE avg_salary > 70000      -- ERROR
GROUP BY department;

-- RIGHT: HAVING runs after GROUP BY and SELECT
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 70000;  -- CORRECT
```

---

## Putting It All Together — Real Scenarios

### Scenario 1: Department summary report

```sql
SELECT
    department,
    COUNT(*)              AS headcount,
    SUM(salary)           AS total_payroll,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary)           AS min_salary,
    MAX(salary)           AS max_salary
FROM employees
WHERE is_active = TRUE
GROUP BY department
ORDER BY total_payroll DESC;
```

### Scenario 2: Which cities have more than one employee?

```sql
SELECT city, COUNT(*) AS employee_count
FROM employees
GROUP BY city
HAVING COUNT(*) > 1
ORDER BY employee_count DESC;
```

Result:

| city   | employee_count |
|--------|----------------|
| Pune   | 3              |
| Mumbai | 3              |

### Scenario 3: Departments where average salary exceeds company average

```sql
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees)
ORDER BY avg_salary DESC;
```

This uses a **subquery** inside `HAVING` to compare each department's average against the overall company average. You will learn subqueries in detail later — for now, just notice that `HAVING` can take a calculated value as its threshold.

Result:

| department  | avg_salary |
|-------------|------------|
| Engineering | 81500.00   |
| Finance     | 70500.00   |

---

## Quick Reference

| What you want | SQL |
|---|---|
| Count all rows | `COUNT(*)` |
| Count non-NULL values | `COUNT(column)` |
| Count unique values | `COUNT(DISTINCT column)` |
| Total of a column | `SUM(column)` |
| Average of a column | `AVG(column)` |
| Rounded average | `ROUND(AVG(column), 2)` |
| Smallest value | `MIN(column)` |
| Largest value | `MAX(column)` |
| Group rows by a column | `GROUP BY column` |
| Filter after grouping | `HAVING condition` |
| Filter before grouping | `WHERE condition` |
| Replace NULL with a value | `COALESCE(column, default)` |

---

## The Full Structure So Far

```sql
SELECT   DISTINCT column, AGG_FUNCTION(column) AS alias
FROM     table
WHERE    row_condition
GROUP BY column
HAVING   group_condition
ORDER BY column ASC/DESC
LIMIT    n OFFSET m;
```

---

## Exercises

Use the same `employees` table from Day 3. Re-insert the data if needed.

**1.** Count the total number of employees in the company.

**2.** Count how many employees are currently active.

**3.** Find the total salary paid to all employees combined.

**4.** Find the average salary across the entire company. Round to 2 decimal places.

**5.** Find the highest and lowest salary in the company. Show both in the same query.

**6.** Find the earliest and latest joining dates.

**7.** Count how many employees are in each department.

**8.** Find the total salary paid per department. Sort by total salary from highest to lowest.

**9.** Find the average salary per department. Round to 2 decimal places. Sort by average salary descending.

**10.** For each department, show the headcount, total payroll, average salary, minimum salary, and maximum salary — all in one query.

**11.** Count how many employees are in each city, but only count active employees.

**12.** Find the total salary per city for active employees only.

**13.** Show only departments where the total salary exceeds `150000`.

**14.** Show only departments where the average salary is below `65000`.

**15.** Show only cities that have more than 1 employee.

**16.** Show departments with more than 1 active employee. (Hint: filter active first with `WHERE`, then filter groups with `HAVING`.)

**17.** Find the department with the highest average salary. Show only that one department. (Hint: `ORDER BY` + `LIMIT`.)

**18.** Show each department and the number of employees, but only for departments where all employees earn more than `50000`. Think carefully — which filter goes where?

**19.** Write a query that shows each city and its average salary, but only for cities where the average salary is between `55000` and `80000`. Sort alphabetically by city.

**20.** A finance manager asks: "For each department, how many employees joined before 2022, and what is their total salary?" Write that query. Show only departments with at least 1 such employee.

**21.** Explain in your own words why the following query will fail, and write the corrected version:

```sql
SELECT department, COUNT(*) AS headcount
FROM employees
WHERE headcount > 1
GROUP BY department;
```

**22.** What is the difference between these two queries? What will each return?

```sql
-- Query A
SELECT COUNT(*) FROM employees;

-- Query B
SELECT COUNT(city) FROM employees;
```

When would they return different results?

**23.** You are given this table where some salaries are NULL:

| id | name  | salary |
|----|-------|--------|
| 1  | Riya  | 80000  |
| 2  | Arjun | NULL   |
| 3  | Sara  | 60000  |
| 4  | Karan | NULL   |
| 5  | Meera | 70000  |

Without running SQL, predict the result of each:
- `COUNT(*)`
- `COUNT(salary)`
- `SUM(salary)`
- `AVG(salary)`
- `COALESCE`-based `AVG` treating NULLs as 0

Then explain which `AVG` is "correct" and when you would use each.
