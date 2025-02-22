import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values(".env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # owners table
    cursor.execute("SELECT owner_id, owner_name, role_id FROM owners")
    owners  = cursor.fetchall()
    print("--  DISPLAYING Owners TABLE --")
    for owner in owners:
            print(f"OWNER ID: {owner[0]}\nOWNER NAME: {owner[1]}\nROLE ID: {owner[2]}")

    # employee table
    cursor.execute("SELECT employee_id, role_id, employee_name FROM employee")
    employees  = cursor.fetchall()
    print("--  DISPLAYING employee TABLE --")
    for employee in employees:
        print(f"EMPLOYEE ID: {employee[0]}\nROLE ID:{employee[1]}\nEMPLOYEE NAME: {employee[2]}") 

    # roles table 
    cursor.execute("SELECT role_id, role_name FROM user_roles")  
    roles = cursor.fetchall()          
    print("--  DISPLAYING roles TABLE --")
    for role in roles:
        print(f"ROLE ID: {role[0]}\nROLE NAME: {role[1]}") 

    # suppliers table 
    cursor.execute("SELECT supplier_id, supplier_name, supplier_product1, supplier_product2 FROM suppliers")
    suppliers  = cursor.fetchall()
    print("--  DISPLAYING suppliers TABLE --")
    for supplier in suppliers:
        print(f"SUPPLIER ID: {supplier[0]}\nSUPPLIER NAME: {supplier[1]}\nSUPPLIER PRODUCTS1: {supplier[2]}\nSUPPLIER PRODUCTS2: {supplier[3]}")

    # products table 
    cursor.execute("SELECT product_id, product_name, inventory FROM products")
    products = cursor.fetchall()
    print("--  DISPLAYING products TABLE --")
    for product in products:
        print(f"PRODUCT ID: {product[0]}\nPRODUCT NAME: {product[1]}\nINVENTORY: {product[2]}")

    # orders table
    cursor.execute("SELECT order_id, product_id, tracking_id, order_date, order_quantity FROM orders")
    ordersData  = cursor.fetchall()
    print("--  DISPLAYING orders TABLE --")
    for order in ordersData:
        print(f"ORDER ID: {order[0]}\nPRODUCT ID: {order[1]}\nTRACKING ID: {order[2]}\nORDER DATE: {order[3]}\nQUANTITY: {order[4]}")

    cursor.close()
    db.close()

    print(f"Database user {config["user"]} connected to MySQL on host {config['host']} with database {config['database']}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

