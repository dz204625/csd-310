""" import statements """
import mysql.connector
from mysql.connector import errorcode

import dotenv 
from dotenv import dotenv_values

dotenv.load_dotenv()

#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 

    # first query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio;")
    studio_data = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studio_data:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")

    # second query
    cursor.execute("SELECT * FROM genre;")
    genre_data = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genre_data:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")

    # third query
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
    film_data = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for short_film in film_data:
        print(f"Film Name: {short_film[0]}")
        print(f"Runtime: {short_film[1]}\n")

    # fourth query
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director ASC;")
    director_data = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in order--")
    for director in director_data:
        print(f"Film Name: {director[0]}")
        print(f"Director: {director[1]}\n")
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()