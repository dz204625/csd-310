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

    # supplier table
    cursor.execute("SELECT supplier_id, supplier_name, supplier_product1, supplier_product2 FROM supplier;")
    suppliers  = cursor.fetchall()

    print("--  DISPLAYING supplier TABLE --")
    for supplier in suppliers:
            print(f"SUPPLIER ID: {supplier[0]}\nSUPPLIER NAME: {supplier[1]}\nSUPPLIER PRODUCT 1: {supplier[2]}\nSUPPLIER PRODUCT 2: {supplier[3]}")

    # products table 
    cursor.execute("SELECT product_id, product_name, inventory FROM product")
    products = cursor.fetchall()

    print("--  DISPLAYING products TABLE --")
    for product in products:
        print(f"PRODUCT ID: {product[0]}\nPRODUCT NAME: {product[1]}\nINVENTORY: {product[2]}")

    # distributor table
    cursor.execute("SELECT distributor_id, distributor_name, product_id FROM distributor")
    distributors = cursor.fetchall()

    print("-- DISPLAYING Distributor Information --")
    for distributor in distributors:
        print(f"DISTRIBUTOR ID: {distributor[0]}\nDISTRIBUTOR NAME: {distributor[1]}\nPRODUCT ID: {distributor[2]}")
    
    # employee table
    cursor.execute("SELECT employee_id, first_name, last_name, role_name FROM employee")
    employees = cursor.fetchall()

    print("-- DISPLAYING Employee Information --")
    for employee in employees:
        print(f"EMPLOYEE ID: {employee[0]}\nFIRST NAME: {employee[1]}\nLAST NAME: {employee[2]}\nROLE: {employee[3]}")

    # orders table
    cursor.execute("SELECT order_id, product_id, distributor_id, order_date, quantity FROM orders")
    orders = cursor.fetchall()

    print("-- DISPLAYING Order Information --")
    for order in orders:
        print(f"ORDER ID: {order[0]}\nPRODUCT ID: {order[1]}\nDISTRIBUTOR ID: {order[2]}\nORDER DATE: {order[3]}\nQUANTITY: {order[4]}")

    # supplier_delivery table
    cursor.execute("SELECT delivery_id, product_id, quantity, supplier_id, expected_delivery_date, actual_delivery_date FROM supplier_delivery")
    deliveries = cursor.fetchall()

    print("-- DISPLAYING Supplier Delivery Information --")
    for delivery in deliveries:
        print(f"DELIVERY ID: {delivery[0]}\nPRODUCT ID: {delivery[1]}\nQUANTITY DELIVERED: {delivery[2]}\nSUPPLIER ID: {delivery[3]}\nEXPECTED DELIVERY DATE: {delivery[4]}\nACTUAL DELIVERY DATE: {delivery[5]}")
    
    # employee_hours table
    cursor.execute("SELECT hours_id, employee_id, work_date, work_hours FROM employee_hours")
    employee_hours = cursor.fetchall()

    print("-- DISPLAYING Employee Work Hours Information --")
    for record in employee_hours:
        print(f"HOURS ID: {record[0]}\nEMPLOYEE ID: {record[1]}\nWORK DATE: {record[2]}\nWORK HOURS: {record[3]}")

    # report 1: generate delivery information
    cursor.execute(""" 
            SELECT 
            supplier.supplier_name,
            product.product_name,
            supplier_delivery.quantity,
            supplier_delivery.expected_delivery_date,
            supplier_delivery.actual_delivery_date
            FROM 
                supplier_delivery
            JOIN 
                supplier ON supplier_delivery.supplier_id = supplier.supplier_id
            JOIN 
                product ON product.product_id = supplier_delivery.product_id
            ORDER BY 
                supplier_delivery.expected_delivery_date DESC;
            """)
    deliveries = cursor.fetchall()
    print("\n--  DISPLAYING  Report 1: Supplier Delivery Information --\n")
    print("Supplier Name | Product Name |  Quantity Delivered | Expected Delivery Date | Actual Delivery Date")
    print("-" * 100)
    
    for delivery in deliveries:
        print(f"{delivery[0]} | {delivery[1]} | {delivery[2]} | {delivery[3]} | {delivery[4]}")

    # report 2: generate wine orders with distributions information
    cursor.execute(""" 
            SELECT 
            orders.order_id,
            product.product_name,
            distributor.distributor_id,
            distributor.distributor_name,
            orders.quantity,
            orders.order_date
            FROM 
                orders
            JOIN 
                product ON orders.product_id = product.product_id
            JOIN 
                distributor ON orders.distributor_id = distributor.distributor_id
            ORDER BY 
                orders.order_date DESC;
            """)
    order_distributions = cursor.fetchall()
 
    print("\n-- DISPLAYING Report 2: Wine Orders with Distribution Information --\n")
    print("Order ID | Product Name | Distributor ID | Distributor Name | Quantity | Order Date")
    print("-" * 100)

    for order_distribution in order_distributions:
        print(f"{order_distribution[0]} | {order_distribution[1]} | {order_distribution[2]} | {order_distribution[3]} | {order_distribution[4]} | {order_distribution[5]}")

    # report 3: generate employee work time for past month
    cursor.execute(""" 
                SELECT  employee.employee_id,
                CONCAT(employee.first_name, ' ', employee.last_name) AS employee_name,
                SUM(employee_hours.work_hours) AS total_hours_worked
                FROM 
                    employee_hours
                JOIN 
                    employee ON employee_hours.employee_id = employee.employee_id
                GROUP BY 
                    employee.employee_id
                ORDER BY 
                    employee.employee_id;
                """)
    employee_hours = cursor.fetchall()
    
    print("\n-- DISPLAYING Report 3: Employee Work Time for the Past Month --\n")
    print("Employee ID | Employee Name | Total Hours Worked")
    print("-" * 60)

    for employee_hour in employee_hours:
        print(f"{employee_hour[0]} | {employee_hour[1]} | {employee_hour[2]}")

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