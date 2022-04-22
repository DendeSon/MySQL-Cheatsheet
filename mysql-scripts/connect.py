from getpass import getpass
from mysql.connector import connect, Error

# Basic Connection to MySQL server
def connect_db():
    try:
        with connect(
            host = "localhost",
            user = input("Enter username: "),
            password = getpass("Enter password: "),
        ) as connection:
            print(connection)
    except Error as e:
        print(e)

# Connect to exisiting database
def connect_existing_db(database_name):
    try:
        with connect(
            host = "localhost",
            user = input("Enter username: "),
            password = getpass("Enter password: "), 
            database =  str(database_name),
        ) as connection:
            print(connection)
    except Error as e:
        print(e)

# Connect and create new database in MySQL server
def connect_new_db(database_name):
    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
        ) as connection:
            create_db_query = f"CREATE DATABASE {str(database_name)}"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
    except Error as e:
        print(e)

# Show database for entire MySQL server
def show_db():
    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
        ) as connection:
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)