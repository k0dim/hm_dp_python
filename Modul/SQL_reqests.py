from urllib import request
import psycopg2
from tkinter import messagebox as mb
    

#0 Создаем БД
def create_db(schema, table_1, table_2):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                
                    cur.execute(f'''
                        CREATE SCHEMA {schema}
                        CREATE TABLE IF NOT EXISTS {schema}.{table_1}(
                            persone_id SERIAL PRIMARY KEY,
                            name VARCHAR(40) NOT NULL,
                            surename VARCHAR(40) NOT NULL,
                            email VARCHAR(40) UNIQUE NOT NULL
                        )
                        CREATE TABLE IF NOT EXISTS {schema}.{table_2}(
                            phone_id SERIAL PRIMARY KEY,
                            persone_id INT NOT NULL REFERENCES {schema}.{table_1}(persone_id),
                            num_phone INT UNIQUE
                        );
                        ''')
                    conn.commit()
                    mb.showinfo("Успех", "Вроде бы получилось (но это не точно)")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


#1 Добавляем в таблицу 'persone'
def insert_persone_db(name_in_db, surename_in_db, email_in_db):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    INSERT INTO cust.persone(name, surename, email)
                        VALUES(%s, %s, %s);
                    ''',(name_in_db, surename_in_db, email_in_db))
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось. Транзация зафиксирована")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


#2 Добавляем в таблицу 'phone'
def insert_phone_db(persone_id_in_db, num_phone_in_db):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    INSERT INTO cust.phone(persone_id, num_phone)
                        VALUES(%s,%s);
                    ''',(persone_id_in_db, num_phone_in_db))
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось. Транзация зафиксирована")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

#3.1 Изменения в БД persone (name)
def update_persone_db_name(value, persone_id):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    UPDATE cust.persone
                        SET name = %s
                        WHERE persone_id = %s;  
                    ''',(value, persone_id))
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось. Транзация зафиксирована")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

#3.2 Изменения в БД persone (surename)
def update_persone_db_surename(value, persone_id):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    UPDATE cust.persone
                        SET surename = %s
                        WHERE persone_id = %s;  
                    ''',(value, persone_id))
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось. Транзация зафиксирована")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

#3.3 Изменения в БД persone (email)
def update_persone_db_email(value, persone_id):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    UPDATE cust.persone
                        SET email = %s
                        WHERE persone_id = %s;  
                    ''',(value, persone_id))
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось. Транзация зафиксирована")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

#4 Удалить запись в БД phone
def delete_phone_db(num_phone):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    DELETE FROM cust.phone
                        WHERE num_phone = %s; 
                    ''',(num_phone,))
            conn.commit()
            mb.showinfo("Успех", "Вроде бы получилось. Транзация зафиксирована")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

#5 Удалить запись в БД persone
def delete_persone_db(persone_id):
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    DELETE FROM cust.phone
                        WHERE persone_id = %s;
                    DELETE FROM cust.persone
                        WHERE persone_id = %s;
                    ''',(persone_id, persone_id))
            conn.commit()
        mb.showinfo("Успех", "Вроде бы получилось. Транзация зафиксирована")
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

#6 Поиск по БД
def select_db(sql_reqest_select):
    request_select = ('''
                    SELECT c.persone_id, name, surename, email, num_phone
                    FROM cust.persone c 
                        LEFT JOIN cust.phone p
                            ON c.persone_id = p.persone_id
                    WHERE c.persone_id is not null
                    ''')
    all_request = request_select + sql_reqest_select
    try:
        with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(all_request)
        mb.showinfo("Успех", 'fetchall', cur.fetchall())
    except:
        mb.showerror("Ошибка", "Вроде не получилось. Откат транзакции")
        conn.rollback()
    finally:
        cur.close()
        conn.close()