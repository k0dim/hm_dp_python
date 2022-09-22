import psycopg2
from tkinter import messagebox as mb
with psycopg2.connect(database= "customer", user= "postgres", password= "postgres") as conn:
    

#0 Создаем БД
    def create_db(schema, table_1, table_2):
        with conn.cursor() as cur:
            try:
                cur.execute(f'''
                    CREATE SCHEMA {schema}
                    CREATE TABLE IF NOT EXISTS {schema}.{table_1}(
                        persone_id INT PRIMARY KEY,
                        name VARCHAR(40) UNIQUE NOT NULL,
                        surename VARCHAR(40) UNIQUE NOT NULL,
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
                mb.showerror("Ошибка", "Вроде не получилось")

#1 Добавляем в таблицу 'persone'
    def insert_persone_db(name_in_db, surename_in_db, email_in_db):
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    INSERT INTO customer.persone(name, surename, email)
                        VALUES(%s,%s,%s);
                    '''),(name_in_db, surename_in_db, email_in_db)
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось (но это не точно)")
            except:
                mb.showerror("Ошибка", "Вроде не получилось")
        return 

#2 Добавляем в таблицу 'phone'
    def insert_phone_db(persone_id_in_db, num_phone_in_db):
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    INSERT INTO customer.phone(name, surename, email)
                        VALUES(%s,%s);
                    '''),({persone_id_in_db}, {num_phone_in_db})
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось (но это не точно)")
            except:
                mb.showerror("Ошибка", "Вроде не получилось")
        return 

#3 Изменения в БД persone
    def update_persone_db(column, value, persone_id):
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    UPDATE persone
                        SET %s = %s
                        WHERE persone_id = %s;  
                    '''),(column, value, persone_id)
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось (но это не точно)")
            except:
                mb.showerror("Ошибка", "Вроде не получилось")
        return 

#4 Удалить запись в БД phone
    def delete_phone_db(num_phone):
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    DELETE FROM phone
                        WHERE num_phone = %s; 
                    '''),(num_phone)
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось (но это не точно)")
            except:
                mb.showerror("Ошибка", "Вроде не получилось")
        return 

#5 Удалить запись в БД persone
    def delete_persone_db(persone_id):
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    DELETE FROM phone
                        WHERE persone_id = %s
                    DELETE FROM persone
                        WHERE persone_id = %s;
                    '''),(persone_id)
                conn.commit()
                mb.showinfo("Успех", "Вроде бы получилось (но это не точно)")
            except:
                mb.showerror("Ошибка", "Вроде не получилось")
        return 

#6 Поиск по БД
    def select_db():
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    SELECT *
                    FROM customer.customer c 
                        JOIN customer.phone p
                            ON c.persone_id = p.persone_id
                    WHERE name = '%s'
                    OR surename = '%s'
                    OR email = '%s'
                    OR num_phone = '%s';
                    ''')(1,2,3,4)
                print('fetchall', cur.fetchall())
                mb.showinfo("Успех", ('fetchall', cur.fetchall()))
            except:
                mb.showerror("Ошибка", "Вроде не получилось")
        return 
