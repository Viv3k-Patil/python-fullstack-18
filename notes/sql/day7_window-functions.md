# Day 7: Window Functions

## What They Mean

Window functions are used when you want to **analyze rows in context** without collapsing them into a single summary row. They let you keep the original table rows and add extra calculated information beside each row.

This is the key difference from `GROUP BY`. With `GROUP BY`, you are asking the database to compress many rows into fewer rows. With window functions, you are asking the database to look at a “window” of related rows and show a result for each original row.

A simple way to think about it is this:

- `GROUP BY` answers: “What is the total for this group?”
- Window functions answer: “For this row, what is the total/rank/previous value inside its group?”

That is why window functions feel more natural for analytics, reports, rankings, and time-based comparisons.

## Core Intuition

Imagine you have a table of orders. One order belongs to one customer, but that customer may have many orders.

If you use `GROUP BY customer_id`, you lose the individual orders and only see one summary row per customer.

If you use a window function, each order stays visible, but you can still show the customer’s total spending, the order number, or the running total beside it.

So the idea is:

- Keep the row.
- Look at related rows.
- Calculate something useful.
- Attach the answer to the current row.

That is why window functions are often called “analytics functions” or “windowed calculations.”

## Basic Pattern

The general syntax is:

```sql
function_name() OVER (
    PARTITION BY ...
    ORDER BY ...
)
```

The `OVER` clause is what turns a normal function into a window function.

### What each part does

- `PARTITION BY` divides rows into groups.
- `ORDER BY` arranges rows inside each group.
- Frame clauses decide which rows around the current row are included.

You do not always need all of them. Sometimes `OVER ()` is enough.

## `GROUP BY` vs Window Functions

These two ideas are often confused, so this difference is important.

### With `GROUP BY`

```sql
SELECT customer_id, SUM(amount)
FROM orders
GROUP BY customer_id;
```

This gives one row per customer. All order-level detail is gone.

### With a window function

```sql
SELECT
    order_id,
    customer_id,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id) AS customer_total
FROM orders;
```

This keeps every order row and adds the customer’s total beside it.

### The mental difference

- `GROUP BY` = compress.
- Window function = decorate.

That is the simplest way to remember it.

## Example Table

Suppose we have this orders table:

| order_id | customer_id | amount | order_date |
|---|---:|---:|---|
| 1 | 101 | 500 | 2026-05-01 |
| 2 | 101 | 300 | 2026-05-03 |
| 3 | 102 | 700 | 2026-05-02 |
| 4 | 101 | 200 | 2026-05-05 |

Now let us see how window functions think about this data.

For customer `101`, there are three rows. For customer `102`, there is one row. A window function can calculate something separately for each customer while still showing every order row.

## The Simplest Window

```sql
SELECT
    order_id,
    amount,
    SUM(amount) OVER () AS grand_total
FROM orders;
```

### What happens here

`OVER ()` means “use all rows as the window.”

So if the total of all orders is 1700, then every row will show 1700 in `grand_total`.

This is a good first example because it shows that a window function does not remove rows. It simply adds a calculated value to each row.

## Partitioning Into Groups

```sql
SELECT
    order_id,
    customer_id,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id) AS customer_total
FROM orders;
```

### What happens here

The rows are divided by `customer_id`.

- Customer `101` gets a total of `1000`.
- Customer `102` gets a total of `700`.

But all four rows remain in the output.

### Why this matters

This is useful when you want row-level detail and group-level summary together.

For example:

- Show each order.
- Show which customer placed it.
- Show that customer’s lifetime total.

That kind of result is very common in reporting.

## Ordering Inside the Window

`ORDER BY` inside `OVER` changes the meaning. It is used when the calculation depends on row sequence.

```sql
SELECT
    order_id,
    customer_id,
    amount,
    SUM(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS running_total
FROM orders;
```

### What happens here

For each customer, rows are sorted by date, and the sum grows step by step.

For customer `101`:

- First order = 500
- Second order = 800
- Third order = 1000

This is called a **running total** or **cumulative sum**.

### Why it feels different

Without `ORDER BY`, the function looks at the whole group at once.

With `ORDER BY`, it behaves more like “up to this point.”

That is why running totals are one of the most common uses of window functions.

## Row Numbering

```sql
SELECT
    order_id,
    customer_id,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS order_number
FROM orders;
```

### What this does

This gives each order a number within the customer’s history.

For customer `101`, the orders become 1, 2, 3 in time order.

### Why this is useful

It helps answer questions like:

- What was the first order?
- What was the third order?
- Which order is the latest one?

`ROW_NUMBER()` is one of the easiest window functions to understand because it simply counts rows in order.

## Ranking

Ranking functions are used when you want to compare rows by value.

```sql
SELECT
    product_name,
    sales,
    RANK() OVER (ORDER BY sales DESC) AS sales_rank
FROM products;
```

### What this means

Products with higher sales get a better rank. If two products tie, they share the same rank.

### Ranking functions in simple form

- `ROW_NUMBER()` = gives unique numbers.
- `RANK()` = gives the same rank to ties and skips numbers after ties.
- `DENSE_RANK()` = gives the same rank to ties but does not skip numbers.

### Example

If sales are `100, 90, 90, 80`:

- `RANK()` gives `1, 2, 2, 4`
- `DENSE_RANK()` gives `1, 2, 2, 3`
- `ROW_NUMBER()` gives `1, 2, 3, 4`

That difference is important.

## Previous and Next Rows

Sometimes you want to compare a row with the row before it or after it.

```sql
SELECT
    order_date,
    amount,
    LAG(amount) OVER (ORDER BY order_date) AS previous_amount
FROM orders;
```

### What `LAG()` does

It gives the value from the previous row.

This is useful for:

- Comparing current and previous sales.
- Finding growth.
- Detecting changes over time.

### `LEAD()` works the other way

`LEAD()` gives the next row’s value.

So:

- `LAG()` = previous
- `LEAD()` = next

That makes them very useful for time series work.

## Running Total Intuition

A running total means the total keeps growing as you move down the rows.

If the amounts are:

- 500
- 300
- 200

Then the running total is:

- 500
- 800
- 1000

It is like reading the table from top to bottom and carrying forward the sum.

This is one of the best examples to understand why `ORDER BY` matters in a window.

## Why Window Functions Are Powerful

Window functions solve problems that are awkward with plain aggregates.

For example, if you want:

- each customer’s total spend,
- each order’s position in time,
- the previous order amount,
- the top product in each category,

you would usually need several separate queries or joins without window functions.

Window functions often let you do it in one query.

That makes your SQL cleaner, easier to read, and often more efficient.

## Common Use Cases

### 1. Running totals

Useful in finance, sales, and trend analysis.

### 2. Rankings

Useful for top products, top students, highest salaries, and leaderboard-style results.

### 3. Comparison with previous row

Useful for growth, decline, and change detection.

### 4. Percent of total

Useful when you want to show contribution of each row to the whole.

### 5. Top N per group

Useful when you want the top 3 products in each category or the top 5 employees in each branch.

## Percent of Total

```sql
SELECT
    order_id,
    customer_id,
    amount,
    ROUND(
        100.0 * amount / SUM(amount) OVER (PARTITION BY customer_id),
        2
    ) AS pct_of_customer_total
FROM orders;
```

### Meaning

This tells you how much each order contributed to that customer’s total spending.

For example, if a customer spent 1000 total and one order is 250, then that order contributes 25%.

This is a very practical analytic use of window functions.

## Top N Per Group

Suppose you want the top 2 products in every category.

```sql
SELECT *
FROM (
    SELECT
        category_id,
        product_name,
        sales,
        ROW_NUMBER() OVER (
            PARTITION BY category_id
            ORDER BY sales DESC
        ) AS rn
    FROM products
) t
WHERE rn <= 2;
```

### Why this works

First, each product gets a rank inside its category.

Then you filter the rows to keep only the best ones.

This is one of the most useful real-world patterns for window functions.

## Frame Clauses

A frame clause tells the database exactly which rows around the current row should be used.

Example:

```sql
AVG(amount) OVER (
    ORDER BY order_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)
```

### Meaning

For each row, take:

- the current row,
- the previous row,
- and the one before that.

Then compute the average.

This is often used for moving averages.

### Simple intuition

A frame is like a sliding basket of rows.

As you move from row to row, the basket moves too.

## Moving Average

```sql
SELECT
    order_date,
    amount,
    AVG(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3
FROM orders;
```

### Meaning

This gives the average of the current row and the two rows before it.

So instead of looking at one row alone, you look at a small moving group of rows.

That is useful for smoothing data and seeing trends.

## Important Terms

| Term | Meaning |
|---|---|
| Window | The set of rows being considered |
| Partition | A subgroup inside the window |
| Order | The sequence of rows inside a partition |
| Frame | The exact rows used around the current row |
| Running total | A cumulative sum over ordered rows |
| Ranking | Assigning positions to rows |

## How to Read a Window Query

When you see a query like this:

```sql
SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date)
```

Read it in parts:

- `SUM(amount)` = what calculation?
- `PARTITION BY customer_id` = for which group?
- `ORDER BY order_date` = in what sequence?

That reading habit makes window queries much easier to understand.

## Common Mistakes

### Forgetting that `GROUP BY` removes detail

If you still need each row, do not use `GROUP BY` too early.

### Using `ORDER BY` when it is not needed

Some window functions need only the group, not the order.

### Confusing `ROW_NUMBER()` and `RANK()`

`ROW_NUMBER()` never repeats numbers. `RANK()` does when values tie.

### Forgetting that window functions do not change row count

They add columns. They do not reduce rows.

### Expecting `LAST_VALUE()` to always mean the last row in the table

That function depends on the frame, so it can behave differently than expected.

## The Big Picture

Window functions sit between normal row-by-row SQL and grouped summary SQL.

They are useful because they give you:

- detail,
- summary,
- order,
- and context

all in the same result set.

That is why they are such an important topic in SQL.

## One-Sentence Summary

Window functions let you calculate over related rows while keeping each original row visible.
