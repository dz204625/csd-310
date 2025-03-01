/*
    Title: winetables.sql
*/

-- drop database user if exists 
DROP USER IF EXISTS 'wine_user'@'localhost';
CREATE USER 'wine_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'grapes';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON wine.* TO 'wine_user'@'localhost';

-- drop tables if they are present
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS distributor;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS supplier_delivery;
DROP TABLE IF EXISTS employee_hours;

-- create supplier table
CREATE TABLE supplier (
        supplier_id INT AUTO_INCREMENT PRIMARY KEY,
        supplier_name VARCHAR(255),
        supplier_product1 VARCHAR(255),
        supplier_product2 VARCHAR(255)
);

-- insert data to supplier table
INSERT INTO supplier (supplier_name, supplier_product1, supplier_product2)
VALUES
    ("Supplier 1", "bottles", "corks"),
    ("Supplier 2", "corks", "boxes");

-- create product table
CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    inventory INT NOT NULL
);

-- -- insert data to product table
INSERT INTO product (product_name, inventory)
VALUES
    ('Merlot', 100),
    ("Cabernet", 100),
    ("Chablis", 100),
    ("Chardonnay", 100),
    ("Riesling", 100),
    ("Pinot noir", 100);

-- create distributor table
CREATE TABLE distributor (
    distributor_id INT AUTO_INCREMENT PRIMARY KEY,
    distributor_name VARCHAR(255) NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

-- -- insert data to distributor table
INSERT INTO distributor (distributor_name, product_id)
VALUES
    ('Distributor 1', 1),
    ("Distributor 2", 2),
    ("Distributor 3", 3),
    ("Distributor 4", 4),
    ("Distributor 5", 5),
    ("Distributor 6", 6);

-- create employee table
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    role_name VARCHAR(255)
);

-- -- insert data to distributor table
INSERT INTO employee (first_name, last_name, role_name)
VALUES
    ("Janet", "Collins", "Finance Manager"),
    ("Roz", "Murphy", "Marketing Head"),
    ("Bob", "Ulrich", "Marketing Assistant"),
    ("Henry", "Doyle", "Production Manager"),
    ("Maria", "Costanza", "Distribution Manager"),
    ("Stan", "Bacchus", "Owner"),
    ("Davis", "Bacchus", "Owner");

-- create orders table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    distributor_id INT,
    order_date DATE,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (distributor_id) REFERENCES distributor(distributor_id)
);

-- -- insert data to orders table
INSERT INTO orders (product_id, distributor_id, order_date, quantity)
VALUES
    (1, 1, "2025-02-10", 3),
    (2, 2, "2025-02-12", 6),
    (3, 3, "2025-02-13", 2),
    (4, 4, "2025-02-15", 4),
    (5, 5, "2025-02-15", 9),
    (6, 6, "2025-02-28", 5);

-- create supplier_delivery table
CREATE TABLE supplier_delivery (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    supplier_id INT,
    expected_delivery_date DATE,
    actual_delivery_date DATE,
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

-- insert data to supplier_delivery table
INSERT INTO supplier_delivery (product_id, quantity, supplier_id, expected_delivery_date, actual_delivery_date)
VALUES
    (1, 20, 1, "2025-02-10", "2025-02-13"),
    (2, 60, 2, "2025-02-12", "2025-02-18"),
    (3, 90, 1, "2025-02-13", "2025-02-16"),
    (4, 54, 2, "2025-02-15", "2025-02-19"),
    (5, 80, 1, "2025-02-15", "2025-02-25"),
    (6, 67, 2, "2025-02-28", "2025-02-23");

-- create employee_hours table
CREATE TABLE employee_hours (
    hours_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    work_date DATE,
    work_hours INT,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

-- -- insert data to employee_hours table
INSERT INTO employee_hours (employee_id, work_date, work_hours)
VALUES
    (1, "2025-01-05", 40),  
    (1, "2025-02-05", 38), 
    (2, "2025-01-06", 42), 
    (2, "2025-02-06", 40), 
    (3, "2025-01-07", 40), 
    (3, "2025-02-07", 39), 
    (4, "2025-01-08", 45), 
    (4, "2025-02-08", 44),
    (5, "2025-01-09", 40),
    (5, "2025-02-09", 41);
