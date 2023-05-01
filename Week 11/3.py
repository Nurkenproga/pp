import psycopg2
from need import host, user, password, db_name

try:
    conn = psycopg2.connect(database=db_name, 
                            user=user, 
                            password=password, 
                            host=host)
    
    
    conn.autocommit = True
    
    cur = conn.cursor() 
    
    list_name = ['Askhat', 'Laplase', 'Patrick']
    list_phone = ['+77775671212', '+77771234567', '+777709877']
    
    for i in range(0, len(list_name)):
        if len(list_phone[i]) == 12:
            
            #проверяем есть ли в таблице это имя
            query = f"SELECT * FROM lab11 WHERE name LIKE '{list_name[i]}%'"
            
            cur.execute(query)
            
            res = cur.fetchone()
            
            
            #если уже есть такое имя, обновляем номер
            if res != None:
                query_update = (f"""UPDATE lab11
                                SET phone = '{list_phone[i]}'
                                WHERE name LIKE '{list_name[i]}%';
                                """)
                
                cur.execute(query_update)
                print("[INFO] Data was updated")
            #если нет подходящего имени в таблице то добавляем новый   
            else:
                query_insert = (f"""
                                INSERT INTO lab11 (name, phone) VALUES ('{list_name[i]}', '{list_phone[i]}')
                                """)
                cur.execute(query_insert)
                print("[INFO] Data was inserted")
        else:
            print(f"""[INFO] Incorrect length of number:
                  name: {list_name[i]}
                  phone: {list_phone[i]}
                  """)
    
    
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if conn:
        cur.close()
        conn.close()
        print("[INFO] PostgreSQL connection closed")