Absolutely — here are **practice queries plus sample data** you can run with the views, indexes, and `EXPLAIN ANALYZE` notes.

## Sample tables

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(150) NOT NULL UNIQUE,
    city        VARCHAR(50),
    is_active   BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE orders (
    order_id     INT PRIMARY KEY,
    customer_id  INT NOT NULL,
    order_date   DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status       VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

## Sample data

```sql
INSERT INTO customers (customer_id, name, email, city, is_active) VALUES
(101, 'Riya',  'riya@gmail.com',  'Pune',   TRUE),
(102, 'Arjun', 'arjun@gmail.com', 'Delhi',  TRUE),
(103, 'Sara',  'sara@gmail.com',  'Mumbai', FALSE),
(104, 'Neha',  'neha@gmail.com',  'Pune',   TRUE);

INSERT INTO orders (order_id, customer_id, order_date, total_amount, status) VALUES
(1, 101, '2026-05-01', 500.00, 'completed'),
(2, 101, '2026-05-03', 300.00, 'completed'),
(3, 102, '2026-05-02', 700.00, 'pending'),
(4, 101, '2026-05-05', 200.00, 'completed'),
(5, 104, '2026-05-06', 900.00, 'completed'),
(6, 104, '2026-05-07', 150.00, 'cancelled');
```

## View practice

### 1. Active customers view
```sql
CREATE VIEW active_customers AS
SELECT customer_id, name, email, city
FROM customers
WHERE is_active = TRUE;
```

### 2. Customer order summary view
```sql
CREATE VIEW customer_order_summary AS
SELECT
    c.customer_id,
    c.name,
    c.city,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name, c.city;
```

### Queries using the views
```sql
SELECT * FROM active_customers;

SELECT * FROM customer_order_summary;

SELECT name, total_spent
FROM customer_order_summary
ORDER BY total_spent DESC;
```

## Index practice

### 1. Index on email
```sql
CREATE INDEX idx_customers_email ON customers(email);
```

### 2. Index on customer_id in orders
```sql
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

### 3. Composite index
```sql
CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date);
```

## Queries to test indexes

### Search by email
```sql
SELECT *
FROM customers
WHERE email = 'riya@gmail.com';
```

### Find all orders for one customer
```sql
SELECT *
FROM orders
WHERE customer_id = 101;
```

### Find customer orders in date order
```sql
SELECT *
FROM orders
WHERE customer_id = 101
ORDER BY order_date;
```

## `EXPLAIN ANALYZE` practice

### Before index
```sql
EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE email = 'riya@gmail.com';
```

### After index
```sql
EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE email = 'riya@gmail.com';
```

### For customer orders
```sql
EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE customer_id = 101
ORDER BY order_date;
```

### For view query
```sql
EXPLAIN ANALYZE
SELECT *
FROM customer_order_summary
WHERE total_spent > 500;
```

## Easy experiments

Try these one by one:

1. Run a query **without** an index.
2. Add the index.
3. Run the same query again.
4. Compare the execution plan.

That is the best way to build intuition.

## Good learning sequence

Start with:

- `SELECT * FROM customers;`
- `SELECT * FROM orders WHERE customer_id = 101;`
- `CREATE VIEW active_customers AS ...`
- `CREATE INDEX idx_customers_email ON customers(email);`
- `EXPLAIN ANALYZE SELECT ...`

## One practical example

```sql
SELECT name, email
FROM active_customers
WHERE city = 'Pune';
```

This shows how a view can reduce repeated filtering logic.

Would you like me to make this into a **full practice sheet with 20 questions and answers**?
