import psycopg2
import csv
from need import host, user, password, db_name


try:
    #connect to exist database
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        
        print(f"Server version: {cursor.fetchone()}")

# cоздал таблицу
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE snake_users(
                id serial PRIMARY KEY,
                name varchar(50) NOT NULL,
                total varchar(50) NOT NULL
                )"""
        )
        print("[INFO] created a new table")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
    
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
        