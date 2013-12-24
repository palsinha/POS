CREATE TABLE store(
STORE_ID VARCHAR(10) NOT NULL,
STATE VARCHAR(15),
CITY VARCHAR(20),
STREET_NAME VARCHAR(20),
POSTAL_CODE NUMBER NOT NULL(10),
WAREHOUSE_ID NUMBER(10),
PRIMARY KEY(STORE_ID)
FOREIGN KEY (warehouse_id) REFERENCING warehouse;

CREATE TABLE employees(
emp_id VARCHAR(10) NOT NULL,
email_id VARCHAR(15),
f_name VARCHAR(15),
l_name VARCHAR(15),
job_role VARCHAR(15),
store_id VARCHAR(15),
access_code VARCHAR(10)
PRIMARY KEY(emp_id),
FOREIGN KEY (access_code) REFERENCING emp_access,
FOREIGN KEY (store_id) REFERENCING store;

CREATE TABLE emp_access(
access_id VARCHAR(10) NOT NULL,
access_type VARCHAR(20),
access_code VARCHAR(10),
access_description VARCHAR(15),
PRIMARY KEY(access_id));

CREATE TABLE transactions(
transaction_id VARCHAR(10) NOT NULL,
store_id VARCHAR(15),
sku_number VARCHAR(10),
category VARCHAR(15),
sub_category VARCHAR(15),
quantity VARCHAR(10),
price VARCHAR(10),
qty_price VARCHAR(10),
discount_pct VARCHAR(10),
discount_price VARCHAR(10),
tax VARCHAR(10),
total_price VARCHAR(10),
transaction_type VARCHAR(10),
transaction_date DATE,
PRIMARY KEY(transaction_id),
FOREIGN KEY (store_id) REFERENCING store,
FOREIGN KEY (sku_number) REFERENCING item_details);

CREATE TABLE item_details(
sku_number VARCHAR(10),
item_description VARCHAR(25),
category VARCHAR(15),
category_id VARCHAR(10),
discount_pct VARCHAR(10),
size VARCHAR(10),
brand VARCHAR(20),
item_entered DATE,
updated_date DATE,
PRIMARY KEY(sku_number),
FOREIGN KEY (category_id) REFERENCING categories,
);

CREATE TABLE categories(
category_id VARCHAR(10),
sub_category VARCHAR(25),
PRIMARY KEY(category_id)
);

CREATE TABLE inventory(
inventory_id VARCHAR(10),
store_id VARCHAR(15),
sku_number VARCHAR(10),
quantity VARCHAR(10),
price VARCHAR(10),
item_status VARCHAR(5),
PRIMARY KEY(inventory_id),
FOREIGN KEY(store_id) REFERENCING store);
);

CREATE TABLE warehouse(
warehouse_id VARCHAR(10),
warehouse_name VARCHAR(15),
warehouse_location VARCHAR(10),
contact_number VARCHAR(10),
warehouse_type VARCHAR(10),
PRIMARY KEY(warehouse_id));

commit;

select * from store;
select * from employee;
select * from warehouse;
select * from inventory;
select * from categories;
select * from item_details;
select * from transactions;
select * from employees;
select * from emp_access;

