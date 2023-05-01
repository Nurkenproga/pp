import csv
import psycopg2
from need import host, user, password, db_name

try:
    #?connect to exist database
    connection = psycopg2.connect(
        host = host, 
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        
        
 
    #with connection.cursor() as cursor:
    #     cursor.execute("""
    #                    CREATE TABLE LAB11(
    #                     id serial PRIMARY KEY,
    #                     name varchar(50) NOT NULL, 
    #                     phone varchar(50) NOT NULL)
    #                    """)
    #    
    #     print("[INFO] created a new table")



    with open('phone.csv', 'r') as file:
        csv_reader = csv.reader(file)
    
        with connection.cursor() as cursor:
            #to skip first line in csv file
            next(csv_reader)
            
            for line in csv_reader:
                    cursor.execute(
                    f"""INSERT INTO lab11 (name, phone) VALUES
                    ('{line[0]}', '{line[1]}')"""
                )
                
            print("[INFO] Data was succesfully inserted")
    
    
 
    # name = input("Enter the name: ")
    # phone = input("Enter the phone number: ")
    
    # with connection.cursor() as cursor:
    #     cursor.execute(f"""
    #                    INSERT INTO lab11 (name, phone) VALUES ('{name}', '{phone}')
    #                    """)
        
    #     print("[INFO] Data was succesfully inserted")
        
    

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         UPDATE lab11
    #         SET name = 'Greg', 
    #             phone = '123456789'
    #         WHERE id = 1;
    #         """
    #     )
    #     print("[INFO] Data was succesfully updated")
        

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT phone FROM users WHERE name = 'Nurken';"""
    #     )
        
    #     print(cursor.fetchone())
        
    

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         DELETE FROM users
    #         WHERE id = '5' or
    #             name = 'Vip kazah'
    #         """
    #     )
        
    #     print("[INFO] Data was succesfully deleted")
    
    

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE lab11;"""
    #     )
        
    #     print("[INFO] table was deleted")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
    
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")