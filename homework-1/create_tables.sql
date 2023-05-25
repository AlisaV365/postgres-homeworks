-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	id serial PRIMARY KEY,
	customer_id varchar(50) NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);


CREATE TABLE employees
(
	first_name varchar(50),
	last_name varchar(50),
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE orders
(
	id serial PRIMARY KEY,
	order_id int NOT NULL,
	customer_id varchar(50) NOT NULL,
	employee_id int NOT NULL,
	order_date varchar(50) NOT NULL,
	ship_city varchar(50) NOT NULL
);

