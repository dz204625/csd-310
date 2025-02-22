/*
    Title: winetables.sql
    
*/

-- drop database user if exists 
DROP USER IF EXISTS 'wine_user'@'localhost';

CREATE USER 'wine_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'grapes';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON wine.* TO 'wine_user'@'localhost';

-- drop tables if they are present
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS products;

-- create the role table 
CREATE TABLE user_roles (
    role_id     INT             NOT NULL        AUTO_INCREMENT,
    role_name   VARCHAR(75)     NOT NULL,
     
    PRIMARY KEY(role_id)
); 

-- create the owners table 
CREATE TABLE owners (
    owner_id     INT             NOT NULL AUTO_INCREMENT,
    owner_name  CHAR(50)    NOT NULL,
    role_id     INT             NOT NULL, 
        
    PRIMARY KEY(owner_id)

    -- CONSTRAINT fk_role
    -- FOREIGN KEY(role_id)
    --     REFERENCES role(role_id)
); 

-- create the employees table and set the foreign key
CREATE TABLE employee (
    employee_id   INT             NOT NULL        AUTO_INCREMENT,
    role_id     INT             NOT NULL,
    employee_name    VARCHAR(50) NOT NULL,	
    
    PRIMARY KEY(employee_id)
    -- FOREIGN KEY(role_id)
    );

-- create the order table and set the foreign key
CREATE TABLE orders (
    order_id   INT             NOT NULL        AUTO_INCREMENT,
    product_id  INT     NOT NULL,
    tracking_id VARCHAR(75)      NOT NULL,
    order_date VARCHAR(75)   NOT NULL,
    order_quantity INT     NOT NULL,

    PRIMARY KEY(order_id)
    -- FOREIGN KEY(product_id)
    -- FOREIGN KEY(tracking_id)
    );

-- create the product table and set the foreign key
CREATE TABLE products (
    product_id  INT     NOT NULL        AUTO_INCREMENT,
    product_name  VARCHAR(75)     NOT NULL,
    inventory   INT     NOT NULL,
    supplier_id     INT     NOT NULL,
	
    PRIMARY KEY(product_id)
    );

-- create the suppliers table and set the foreign key
CREATE TABLE suppliers (
    supplier_id INT NOT NULL AUTO_INCREMENT,
    supplier_name  VARCHAR(75)     NOT NULL,
    supplier_product1  VARCHAR(75)     NOT NULL,
    supplier_product2  VARCHAR(75)     NOT NULL,
    
    PRIMARY KEY(supplier_id)
);
    
-- insert role records
INSERT INTO user_roles(role_name)
    VALUES('Owner');    

INSERT INTO user_roles(role_name)
    VALUES('Fiance and Payroll'); 

INSERT INTO user_roles(role_name)
    VALUES('Marketing'); 

INSERT INTO user_roles(role_name)
   VALUES('Production'); 

INSERT INTO user_roles(role_name)
  VALUES('Distribution'); 

-- insert owner records
INSERT INTO owners(owner_name, role_id)
    VALUES('Stan Bacchus', (SELECT role_id FROM user_roles WHERE role_name = 'Owner'));

INSERT INTO owners(owner_name, role_id)
    VALUES('Davis Bacchus', (SELECT role_id FROM user_roles WHERE role_name = 'Owner'));

-- insert employee records
INSERT INTO employee(employee_name, role_id)
    VALUES ('Janet Collins', (SELECT role_id FROM user_roles WHERE role_name = 'Fiance and Payroll'));

INSERT INTO employee(employee_name, role_id)
    VALUES ('Roz Murphy', (SELECT role_id FROM user_roles WHERE role_name = 'Marketing'));

INSERT INTO employee(employee_name, role_id)
    VALUES ('Bob Ulrich', (SELECT role_id FROM user_roles WHERE role_name = 'Marketing'));

INSERT INTO employee(employee_name, role_id)
    VALUES ('Henry Doyle', (SELECT role_id FROM user_roles WHERE role_name = 'Production'));

INSERT INTO employee(employee_name, role_id)
    VALUES ('Maria Costanza', (SELECT role_id FROM user_roles WHERE role_name = 'Distribution'));

-- insert into suppliers
INSERT INTO suppliers(supplier_name, supplier_product1, supplier_product2)
    VALUES('Supplier_1', 'bottles', 'corks');

INSERT INTO suppliers(supplier_name, supplier_product1, supplier_product2)
    VALUES('Supplier_2', 'labels', 'boxes');

INSERT INTO suppliers(supplier_name, supplier_product1, supplier_product2)
    VALUES('Supplier_3', 'vats', 'tubing');

-- insert into products
INSERT INTO products(product_name, inventory, supplier_id)
    VALUES('Merlot', 100, (SELECT supplier_id FROM suppliers WHERE supplier_name = 'Supplier_1'));

INSERT INTO products(product_name, inventory, supplier_id)
    VALUES('Cabernet', 100, (SELECT supplier_id FROM suppliers WHERE supplier_name = 'Supplier_2'));

INSERT INTO products(product_name, inventory, supplier_id)
    VALUES('Chablis', 100, (SELECT supplier_id FROM suppliers WHERE supplier_name = 'Supplier_3'));

INSERT INTO products(product_name, inventory, supplier_id)
    VALUES('Chardonnay', 100, (SELECT supplier_id FROM suppliers WHERE supplier_name = 'Supplier_1'));

INSERT INTO products(product_name, inventory, supplier_id)
    VALUES('Pinot noir', 500, (SELECT supplier_id FROM suppliers WHERE supplier_name = 'Supplier_3'));

INSERT INTO products(product_name, inventory, supplier_id)
    VALUES('Riesling', 150, (SELECT supplier_id FROM suppliers WHERE supplier_name = 'Supplier_1'));

-- insert into orders
INSERT INTO orders(order_date, order_quantity, tracking_id, product_id)
    VALUES('JAN 1 2024', 20, '12345', (SELECT product_id FROM products WHERE product_name = 'Merlot'));

INSERT INTO orders(order_date, order_quantity, tracking_id, product_id)
    VALUES('JAN 2 2024', 32, '123456', (SELECT product_id FROM products WHERE product_name = 'Cabernet'));

INSERT INTO orders(order_date, order_quantity, tracking_id, product_id)
    VALUES('JAN 5 2024', 32, '1234567', (SELECT product_id FROM products WHERE product_name = 'Riesling'));

INSERT INTO orders(order_date, order_quantity, tracking_id, product_id)
    VALUES('JAN 8 2024', 102, '2564789', (SELECT product_id FROM products WHERE product_name = 'Cabernet'));

INSERT INTO orders(order_date, order_quantity, tracking_id, product_id)
    VALUES('JAN 8 2024', 32, '6547895', (SELECT product_id FROM products WHERE product_name = 'Riesling'));

INSERT INTO orders(order_date, order_quantity, tracking_id, product_id)
    VALUES('JAN 9 2024', 102, '5468521', (SELECT product_id FROM products WHERE product_name = 'Cabernet'));




















