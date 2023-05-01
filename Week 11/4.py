import psycopg2
from need import host, user, password, db_name

try:
    conn = psycopg2.connect(database=db_name, 
                            user=user, 
                            password=password, 
                            host=host)
    
    
    conn.autocommit = True
    
    cur = conn.cursor() 

    limit = input("Enter limit :")
    offset = input("Enter offset :")
    
    # формируем SQL-запрос для получения данных с пагинацией
    query = f"SELECT * FROM lab11 LIMIT {limit} OFFSET {offset}"
    
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
      
    
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if conn:
        cur.close()
        conn.close()
        print("[INFO] PostgreSQL connection closed")    