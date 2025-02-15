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

def show_films(cursor, title):
    # method to execute an inner join on all tables,
    # iterate over the dataset and out put the results to the terminal window.

    # inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # get the results fro the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {} \nStudio Name: {}".format(film[0], film[1], film[2], film[3]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    cursor.execute("INSERT INTO film (film_director, film_id, film_name, film_releaseDate, film_runtime, genre_id, studio_id) VALUES('James Cameron', '4', 'Titanic', '1997', '195', 3, 1)")

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    cursor.execute("UPDATE film SET genre_id=1 WHERE film_name='Alien';")

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE -Change Alien to Horror")

    cursor.execute("DELETE FROM film WHERE film_name='Gladiator';")
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


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