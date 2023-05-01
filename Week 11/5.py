import psycopg2
from need import host, user, password, db_name

try:
    conn = psycopg2.connect(database=db_name, 
                            user=user, 
                            password=password, 
                            host=host)
     
    conn.autocommit = True
    
    name = input("Имя которое нужно удалить :")
    phone = input("Номер который нужно удалить :")
    
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            DELETE FROM lab11
            WHERE name = '{name}' or
                phone = '{phone}'
            """
        )
        
        print("[INFO] Data was succesfully deleted")
    
    
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if conn:
        conn.close()    
        print("[INFO] PostgreSQL connection closed")