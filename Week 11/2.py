import psycopg2
from need import host, user, password, db_name

try:
  
    conn = psycopg2.connect(database=db_name, 
                            user=user, 
                            password=password, 
                            host=host)
    
    

    conn.autocommit = True
    
    cur = conn.cursor() 
    
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    
    #проверяем есть ли в таблице это имя
    query = f"SELECT * FROM lab11 WHERE name LIKE '{name}%'"
    
    cur.execute(query)
    
    res = cur.fetchone()
    
    
    #если уже есть такое имя, обновляем номер
    if res != None:
        query_update = (f"""UPDATE lab11
                        SET phone = '{phone}'
                        WHERE name LIKE '{name}%';
                        """)
        
        cur.execute(query_update)
        print("[INFO] Data was updated")
    #если нет подходящего имени в таблице то добавляем новый   
    else:
        query_insert = (f"""
                        INSERT INTO lab11 (name, phone) VALUES ('{name}', '{phone}')
                        """)
        cur.execute(query_insert)
        print("[INFO] Data was inserted")
    
    
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if conn:
        cur.close()
        conn.close()
        print("[INFO] PostgreSQL connection closed")
