create table students (
    student_id serial PRIMARY key, -- auto incrementing integer
      student_name text,
      student_class INTEGER,
      student_marks NUMERIC
)

insert into students(student_name, student_class, student_marks)
VALUES
('vivek', 9, 90),
('raj', 8, 80),
('raj', 8, 95)



select * from students
DROP TABLE students
SELECT student_id, student_name from students 
SELECT student_marks FROM students

select * from students
where student_name = 'vivek'

select * from students
where student_marks < 90

select * from students
where student_class = 8 or student_class = 10

SELECT * from students
WHERE student_name = 'raj'
ORDER BY student_marks ASC
-- logical operators
-- OR ||
-- AND &&

-- comparator operators
-- equal to  =
-- not equal to !=students
-- greater thanstudents
-- less thanstudents
-- greater than or equals tostudents
-- less thatn or equals

select * from students
ORDER BY student_class ASC

select * from students
where student_marks > 85
order by student_name ASC
limit 2


-- updating data from table
update students
set student_name = 'Akshata', student_class = 6
where student_id = 2 or student_id = 3

-- delete

delete from students
where student_id = 3




--- add a new column to table
alter table students
add column student_email varchar(50)

alter table students
drop COLUMN student_email

alter table students
rename COLUMN student_marks to marks

-- change name of the table
alter table students
RENAME to newgen_students

-- data type of columnnewgen_students
alter table newgen_students
alter column student_name type varchar(200)



create table employee (
    employee_id serial primary key,
      employee_name varchar(250),
      employee_dept varchar(200),
      employee_salary integer
)

INSERT INTO employee (employee_name, employee_dept, employee_salary) VALUES
('Arjun Sharma', 'Human Resources', 115577),
('Priya Patel', 'Engineering', 57386),
('Rohan Gupta', 'Marketing', 49960),
('Ananya Iyer', 'Marketing', 118051),
('Vikram Singh', 'Engineering', 128956),
('Sanya Malhotra', 'Finance', 67186),
('Kabir Reddy', 'Finance', 57479),
('Ishani Das', 'Marketing', 120781),
('Amit Verma', 'Product Management', 110444),
('Meera Nair', 'Marketing', 95011);

INSERT INTO employee (employee_name, employee_dept, employee_salary) VALUES
('Arjun Sharmasadasdsadsdfasdfasdfasdfasdfasdf', 'Human Resources', 15000)


select * from employee


select employee_dept, avg(employee_salary), max(employee_salary), max(employee_name)
from employee
group by employee_dept
HAVING avg(employee_salary)<75000


create table records (
    id serial primary key,
      name varchar(250),
      gender varchar(200)
)

INSERT INTO records (name, gender) VALUES
('Alex Johnson', 'Non-binary'),
('Maria Garcia', 'Female'),
('James Smith', 'Male'),
('Sam Rivera', 'Agender'),
('Li Wei', 'Male'),
('Sarah Connor', 'Female'),
('Jordan Taylor', 'Genderfluid'),
('Aarav Patel', 'Male'),
('Elena Rossi', 'Female'),
('Taylor Vance', 'Bigender');


create table records (
    id serial primary key,
      name varchar(250),
      gender varchar(200)
)

INSERT INTO records (name, gender) VALUES
('Alex Johnson', 'Non-binary'),
('Maria Garcia', 'Female'),
('James Smith', 'Male'),
('Sam Rivera', 'Agender'),
('Li Wei', 'Male'),
('Sarah Connor', 'Female'),
('Jordan Taylor', 'Genderfluid'),
('Aarav Patel', 'Male'),
('Elena Rossi', 'Female'),
('Taylor Vance', 'Bigender');



create table records (
    id serial primary key,
      name varchar(250),
      gender varchar(200)
)

INSERT INTO records (name, gender) VALUES
('Alex Johnson', 'Non-binary'),
('Maria Garcia', 'Female'),
('James Smith', 'Male'),
('Sam Rivera', 'Agender'),
('Li Wei', 'Male'),
('Sarah Connor', 'Female'),
('Jordan Taylor', 'Genderfluid'),
('Aarav Patel', 'Male'),
('Elena Rossi', 'Female'),
('Taylor Vance', 'Bigender');

select * from records


SELECT gender,COUNT(*)
FROM records 
WHERE gender='Male' or gender='Female'
GROUP by gender
HAVING COUNT(*)>2

CREATE table mobile_phones (  
	mobile_id serial PRIMARY KEY ,
  	mobile_name VARCHAR(50),
  	mobile_model TEXT,
  	mobile_price INTEGER
)

INSERT INTO mobile_phones (mobile_name, mobile_model, mobile_price) VALUES
('Apple', 'iPhone 15 Pro', 999),
('Apple', 'iPhone 13', 599),
('Samsung', 'Galaxy S24 Ultra', 1199),
('Samsung', 'Galaxy S24 Ultra', 1199),
('Samsung', 'Galaxy S24 Ultra', 1199),
('Samsung', 'Galaxy A55', 450),
('Google', 'Pixel 8 Pro', 999),
('Google', 'Pixel 7a', 399),
('Xiaomi', 'Redmi Note 13', 250),
('OnePlus', '12R', 499),
('Nothing', 'Phone (2)', 599),
('Motorola', 'Edge 40', 350);

SELECT mobile_model ,sum(mobile_price)
FROM mobile_phones
WHERE mobile_id=1 or mobile_id=2
GROUP BY mobile_model
HAVING sum(mobile_price)>600

SELECT mobile_model,COUNT(*),sum(mobile_price)
FROM mobile_phones 
WHERE mobile_name='Samsung' or mobile_name='Google'
GROUP by mobile_model
ORDER by sum(mobile_price) DESC

INSERT into mobile_phones (mobile_name,mobile_model,mobile_price)
VALUES 
	('nokia','nokia-sirco',1000)
   
SELECT * FROM mobile_phones 

UPDATE mobile_phones 
SET mobile_model = 'sirco', mobile_price=999

DELETE FROM mobile_phones
WHERE mobile_model = 'sirco';


SELECT * FROM mobile_phones
ALTER  TABLE mobile_phones
add mfgdate DATE

DELETE FROM mobile_phones
WHERE mfgdate = NULL

SELECT mobile_name , mobile_price FROM mobile_phones

SELECT * FROM mobile_phones
WHERE mobile_id=13 or mobile_id=16

SELECT * FROM mobile_phones
WHERE mobile_name='Apple'
ORDER BY mobile_price DESC

SELECT mobile_name , max(mobile_price),COUNT(*)
FROM mobile_phones
WHERE mobile_price>500
GROUP BY mobile_name
HAVING max(mobile_price)>500

SELECT mobile_model ,COUNT(*)
FROM mobile_phones
GROUP BY mobile_model
HAVING COUNT(*)>2



create table customers (
    id serial primary key,
      name text,
      city text
)

insert into customers (name, city)
values 
('user1', 'city1'),
('user2', 'city2'),
('user3', 'city3'),
('user4', 'city4'),
('user5', 'city5')

create table books (
    id serial PRIMARY key,
      title text,
      genre text,
      price NUMERIC
)

INSERT INTO books (title, genre, price) VALUES
('The Great Gatsby', 'Classic', 12.99),
('To Kill a Mockingbird', 'Classic', 10.50),
('1984', 'Dystopian', 15.00),
('The Hobbit', 'Fantasy', 20.25),
('Project Hail Mary', 'Sci-Fi', 18.99),
('The Silent Patient', 'Thriller', 14.30),
('Atomic Habits', 'Self-Help', 16.00),
('The Shining', 'Horror', 11.95),
('Dune', 'Sci-Fi', 22.00),
('Becoming', 'Biography', 17.50);

select * from books

SELECT  genre,sum(price)
FROM books
WHERE genre='Classic'or  genre='Sci-Fi'
GROUP by genre
HAVING sum(price)>=15.00



CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    book_id INT REFERENCES books(id),
    quantity INT,
    paid_price NUMERIC,
    order_date DATE
)

INSERT into orders (customer_id,book_id,quantity,paid_price,order_date)
VALUES
		(1,2,3,100,'2025-10-12'),
		(2,4,3,100,'2025-10-12');
        
        
SELECT * FROM orders



create table students (
    id serial PRIMARY key,
      name text
);

create table grades (
    student_id int REFERENCES students(id),
      subject text,
      marks int
);

insert into students (name)
VALUES
('alice'),
('bob'),
('carol');

insert into grades (student_id, subject, marks)
VALUES
(1, 'maths', 85),
(1, 'science', 75),
(1, 'history', 89),
(2, 'history', 46),
(2, 'science', 76);


select * from students;
select * from grades;


select s.id, s.name, gr.marks
from students s
INNER join grades gr ON s.id = gr.student_id;



CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50) NOT NULL
);

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50) NOT NULL,
    DeptID INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);
-- department and employee table join
INSERT INTO Departments (DeptID, DeptName) VALUES 
(1, 'HR'),
(2, 'Engineering'),
(3, 'Marketing'),
(4, 'Sales');

INSERT INTO Employees (EmpID, EmpName, DeptID, Salary) VALUES 
(101, 'Alice Jones', 1, 60000),
(102, 'Bob Smith', 2, 85000),
(103, 'Charlie Brown', 2, 90000),
(104, 'David Miller', NULL, 50000);
select * from departments;


SELECT dept.DeptName,e.empname
from employees e
INNER JOIN departments dept ON e.deptid=dept.deptid;

-- left join
select *
from students s
left join grades gr on s.id = gr.student_id;

-- right joinstudents
select *
from students s
right join grades gr on s.id = gr.student_id;

-- full outer joinstudent
-- right joinstudents
select *
from students s
full OUTER join grades gr on s.id = gr.student_id;




-- ! find me all the student who has grades missing
select s.name , gr.marks
from students s
left join grades gr on s.id = gr.student_id
where gr.student_id is null;

--!find the students has marks is above 50
SELECT s.id , gr.subject
FROM students s
INNER JOIN grades gr on s.id = gr.student_id;
WHERE gr.marks>50;



create table accounts(
    id serial PRIMARY key,
      name text,
      balance integer
);

insert into accounts (name, balance)
VALUES
('alice', 5000),
('bob', 3000),
('charlie', 7000);

select * from accounts;

-- alice transfer 500 to bob



begin;

update accounts
set balance = balance - 500
where name = 'alice';

update accounts
set balance = balance + 500
where name = 'bob';

COMMIT;

ROLLBACK



CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) CHECK (salary >= 0)
);

INSERT INTO Employees (emp_id, employee_name, department, salary)
VALUES
(1, 'Aditi', 'HR', 45000),
(2, 'Rahul', 'IT', 60000),
(3, 'Sneha', 'Finance', 55000),
(4, 'Karan', 'IT', 70000);


SELECT * FROM employees;

SELECT * FROM employees
WHERE employee_name ='Aditi';

SELECT department,COUNT(employee_name),AVG(salary)
FROM employees
GROUP by department
HAVING AVG(salary)>50000

SELECT * FROM employees
WHERE salary>50000;




create table scores (
    student text,
      class text,
      marks int
)

insert into scores (student, class, marks)
values 
('alice', 'math', 87),
('bob', 'math', 87),
('carol', 'math', 67),
('david', 'science', 85),
('eve', 'science', 90),
('fin', 'science', 83)

select * from scores


select class, AVG(marks) as total
from scores
group by class;

select student, class, marks,
MIN(marks) over (PARTITION by class) as total_marks
from scores;

SELECT student, class,marks,
RANK() over (PARTITION by class ORDER BY marks DESC),
DENSE_RANK() OVER (PARTITION by class ORDER by marks DESC),
ROW_NUMBER() OVER (PARTITION by class ORDER by marks DESC),
 NTILE(2) over (PARTITION by class ORDER BY marks ASC)
FROM scores

SELECT
student,
class,
marks,
RANK() over (PARTITION by class ORDER BY marks DESC)
FROM
scores;

drop table scores



create table employee(
    name text,
      dept text,
      salary int
)

INSERT INTO employee (name, dept, salary) VALUES ('Ethan Hunt', 'Finance', 79219);
INSERT INTO employee (name, dept, salary) VALUES ('Alice Smith', 'Sales', 66278);
INSERT INTO employee (name, dept, salary) VALUES ('Ethan Hunt', 'Marketing', 112998);
INSERT INTO employee (name, dept, salary) VALUES ('Alice Smith', 'Sales', 84510);
INSERT INTO employee (name, dept, salary) VALUES ('Bob Johnson', 'Engineering', 119531);
INSERT INTO employee (name, dept, salary) VALUES ('Hannah Abbott', 'Engineering', 59088);
INSERT INTO employee (name, dept, salary) VALUES ('Diana Prince', 'Sales', 92675);
INSERT INTO employee (name, dept, salary) VALUES ('George Costanza', 'Human Resources', 84931);
INSERT INTO employee (name, dept, salary) VALUES ('Alice Smith', 'Marketing', 104072);
INSERT INTO employee (name, dept, salary) VALUES ('George Costanza', 'Marketing', 95366);

select * from employee 

SELECT
    name,
    dept,
    RANK() over (PARTITION by dept ORDER BY salary DESC),
    DENSE_RANK() OVER (PARTITION by dept ORDER BY salary DESC),
    ROW_NUMBER() over (PARTITION by dept ORDER by salary),
  
FROM
    employee








create table monthly_sales(
    agent_name text,
      month text,
      amount int
);

-- Insert dummy data
INSERT INTO monthly_sales (agent_name, month, amount) VALUES
-- Alice (Multiple entries)
('Alice Johnson', 'January', 5000),
('Alice Johnson', 'February', 7500),
('Alice Johnson', 'March', 6000),
('Alice Johnson', 'April', 8200),
('Alice Johnson', 'May', 9000),

-- Bob (Multiple entries)
('Bob Smith', 'January', 3000),
('Bob Smith', 'February', 4000),
('Bob Smith', 'March', 3500),

-- Others
('Charlie Brown', 'January', 12000),
('Charlie Brown', 'February', 11000),
('Diana Prince', 'April', 15000),
('Diana Prince', 'May', 16500),
('Ethan Hunt', 'March', 9500),
('Ethan Hunt', 'April', 10000);

select * from monthly_sales;

delete from monthly_sales

select
    agent_name,
    month,
    amount,
   LAG(amount) over (PARTITION by agent_name order by month) as prev,
   LEAD(amount) over (PARTITION by agent_name order by month) as next
from monthly_sales;




















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


CREATE VIEW my_view as
SELECT * FROM customers

SELECT
* FROM
my_view


CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);

INSERT INTO customers (first_name, last_name, email) VALUES 
('Alice', 'Smith', 'alice@email.com'),
('Bob', 'Johnson', 'bob.j@email.com'),
('Charlie', 'Brown', 'charlie.b@email.com');


CREATE table orders(
	order_id Serial PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id) ,
  	amount INT not NULL,
    order_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO orders (customer_id, amount, order_date) VALUES 
(1, 250, '2023-11-01'),
(2, 150, '2023-11-02'),
(1, 200,  '2023-11-05'),
(3, 900, '2023-11-10'),
(2, 65,  '2023-11-12');


SELECT * FROM orders

SELECT customer_id,amount,
sum(amount) OVER () as Total_amount
FROM orders;

SELECT customer_id,sum(amount)
FROM orders
WHERE customer_id=1
GROUP by customer_id
HAVING sum(amount)>200
order by customer_id ASC

SELECT
    order_id,
    customer_id,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS order_number
FROM orders;


SELECT customer_id ,amount,
RANK() OVER (PARTITION by customer_id order by amount desc)
FROM orders


DELETE FROM orders






-- Create the table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10, 2),
    order_date DATE
);

-- Insert dummy data
INSERT INTO orders (order_id, customer_id, amount, order_date) VALUES
(101, 1, 50.00, '2023-01-01'),
(102, 2, 30.00, '2023-01-02'),
(103, 1, 25.50, '2023-01-03'),
(104, 3, 100.00, '2023-01-04'),
(105, 2, 45.00, '2023-01-05'),
(106, 1, 15.00, '2023-01-06'),
(107, 3, 60.00, '2023-01-07');

INSERT INTO orders(order_id,customer_id,amount,order_date)
VALUES 
(108,1,50.00,'2023-01-02');

SELECT * FROM orders

SELECT customer_id ,sum(amount)
FROM orders
GROUP by customer_id
HAVING sum(amount)>75
order by customer_id DESC

SELECT order_id, customer_id,amount,
RANK() OVER ( PARTITION by customer_id 
                     order BY order_date)
                     as order_number
						FROM orders;
                     
SELECT order_date,amount,
lag(amount) OVER (order by order_date ) as previous_amount,
LEAD(amount) OVER (order by order_date) as next_amount
FROM orders

SELECT
    order_id,
    customer_id,
    amount,
    ROUND(
        100.0 * amount / SUM(amount) OVER (PARTITION BY customer_id),
        2
    ) AS pct_of_customer_total
FROM orders;


---example of moving avg----
SELECT order_date,amount,
ROUND(AVG(amount) OVER (
    ORDER BY order_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
),2)as moving_avg	
FROM orders

SELECT order_date,amount,
AVG(amount) OVER (
    ORDER BY order_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)
FROM orders

CREATE VIEW my_orders as
SELECT * FROM 
orders
WHERE customer_id=1;

 SELECT * FROM my_orders

SELECT * FROM customers


CREATE VIEW cous_1 AS
SELECT * FROM customers
WHERE city='city1'

SELECT * FROM cous_1


CREATE VIEW order_summary as
 SELECT
     o.order_id,
    o.customer_id,
    c.name AS customer_name,
    o.amount
FROM orders o    
JOIN customers c on o.order_id=o.customer_id;


SELECT * FROM order_summary





-- Create Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Recreate orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


-- Insert sample customers
INSERT INTO customers (name) VALUES 
('Alice Johnson'), 
('Bob Smith'), 
('Charlie Brown');

-- Insert sample orders
INSERT INTO orders (customer_id, total_amount) VALUES 
(1, 150.50), 
(2, 89.99), 
(1, 45.00), 
(3, 210.00);

SELECT * FROM orders

CREATE VIEW order_summary as
 SELECT
     o.order_id,
    o.customer_id,
    c.name AS customer_name,
    o.total_amount
FROM orders o    
JOIN customers c on o.order_id=o.customer_id;


SELECT * FROM order_summary

SELECT customer_id, COUNT(*),sum(total_amount)
FROM order_summary
GROUP by customer_id


CREATE TABLE campus(
		campus_id serial PRIMARY key,
  		location VARCHAR(50)
)


CREATE TABLE users(
	USER_ID Serial PRIMARY KEY ,
    NAME VARCHAR(50) not null,
    email VARCHAR(50) UNIQUE,
  	hashed_passward BIGINT not NULL,
    ROLE TEXT not NULL,
    student_profile TEXT ,
    campus_id INTEGER,
 	 is_active BOOLEAN,
 	 at_created BOOLEAN,
  
  FOREIGN key (campus_id) REFERENCES campus(campus_id)
)







CREATE TABLE cabin(
	cabin_id serial PRIMARY key,
    campus_id INTEGER,
  	cabin_number int not null,
    is_active BOOLEAN,
  
   FOREIGN key (campus_id) REFERENCES campus(campus_id)
)
