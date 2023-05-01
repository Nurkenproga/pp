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
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """CREATE TABLE users(
#                id serial PRIMARY KEY,
#                name varchar(50) NOT NULL,
#                phone varchar(50) NOT NULL
#                )"""
#        )
#        print("[INFO] created a new table")


#в таблицу ложу вещи
#    with open('phone.csv', 'r') as file:
#        csv_reader = csv.reader(file)
#        
#        with connection.cursor() as cursor:
#            next(csv_reader)
#            
#            for line in csv_reader:
#                cursor.execute(
#                    f"""INSERT INTO users (name, phone) VALUES
#                    ('{line[0]}', '{line[1]}')"""
#                )
#                
#           print("[INFO] Data was succesfully inserted")

# обновляю данные
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """
#            UPDATE users
#            SET name = 'Kamila',
#                phone = '+77470752305'
#                WHERE id = 5;
#                """
#        )
#        print("[INFO] Data was succesfully updated")

# ввод
#    name = input("Enter the name: ")
#    phone = input("Enter the phone number: ")
#    
#    with connection.cursor() as cursor:
#        cursor.execute(f"""
#                       INSERT INTO users (name, phone) VALUES ('{name}', '{phone}')
#                       """)
#        print("[INFO] Data was succesfully inserted")

# получить данные 
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """SELECT phone FROM users WHERE name = 'Nurken';"""
#        )
#        print(cursor.fetchone())

# удалить с таблицы кого то 
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """DELETE FROM users
#            WHERE id = '5' or 
#                name = 'Vip kazah'
#            """
#        )
#    print("[INFO] Data was succesfully deleted")


# удаляю
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """DROP TABLE USERS;"""
#        )
             
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
    
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
        