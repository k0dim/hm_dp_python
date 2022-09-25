from tkinter.ttk import Combobox
from Modul.SQL_reqests import *
from tkinter import *

def window_info():
    def clicke():
        insert_persone_db(entry_name.get(), entry_surename.get(), entry_email.get())
    # Новое окно
    window = Tk()
    window.title("Добавить клиента")
    window.geometry('400x200')
    # Имя
    lbl_name = Label(window, text="Имя:", font=("Arial Bold", 14))
    lbl_name.grid(column=0, row=0)
    entry_name = Entry(window, width=10)
    entry_name.grid(column=1, row=0)
    # Фаилия
    lbl_surename = Label(window, text="Фамилия:", font=("Arial Bold", 14))
    lbl_surename.grid(column=0, row=1)
    entry_surename = Entry(window, width=10)
    entry_surename.grid(column=1, row=1)
    # E-mail
    lbl_email = Label(window, text="Эл. почта:", font=("Arial Bold", 14))
    lbl_email.grid(column=0, row=2)
    entry_email = Entry(window, width=10)
    entry_email.grid(column=1, row=2)
    # Кнопка
    but = Button(window, text="Добавить", command=clicke)
    but.grid(column=1, row=3)
    window.mainloop()


#2 Добавить номер телефона
def window_phone():
    def clicke():
        insert_phone_db(persone_id.get(), num_phone.get())
    # Новое окно
    window = Tk()
    window.title("Добавить номер")
    window.geometry('400x200')
    # Идентификатор клиента
    lbl_persone_id = Label(window, text="Идентификатор клиента:", font=("Arial Bold", 14))
    lbl_persone_id.grid(column=0, row=0)
    persone_id = Entry(window, width=10)
    persone_id.grid(column=1, row=0)
    # Номер телефона
    lbl_num_phone = Label(window, text="Номер телефона:", font=("Arial Bold", 14))
    lbl_num_phone.grid(column=0, row=1)
    num_phone = Entry(window, width=10)
    num_phone.grid(column=1, row=1)
    # Кнопка
    but = Button(window, text="Добавить", command= clicke)
    but.grid(column=1, row=3)
    window.mainloop()


#3 Изменить сведения о клиенте
def window_update_info():
    def clicke():
        if column.get() == 'name':
            update_persone_db_name(value.get(), persone_id.get())
        elif column.get() == 'surename':
            update_persone_db_surename(value.get(), persone_id.get())
        elif column.get() == 'email':
            update_persone_db_email(value.get(), persone_id.get())
    # Новое окно
    window = Tk()
    window.title("Изменить сведения о клиенте")
    window.geometry('500x200')
    # Колона
    lbl_column = Label(window, text="Изменяемый параметр:", font=("Arial Bold", 14))
    lbl_column.grid(column=0, row=0)
    column= Combobox(window)
    column['values'] = ("name", "surename", "email")
    column.current(0)
    column.grid(column=1, row=0)
    # Истинное значение
    lbl_value = Label(window, text="Истинное значение:", font=("Arial Bold", 14))
    lbl_value.grid(column=0, row=1)
    value = Entry(window, width=10)
    value.grid(column=1, row=1)
    # Пользователь
    lbl_persone_id = Label(window, text="Идентификатор пользователя:", font=("Arial Bold", 14))
    lbl_persone_id.grid(column=0, row=2)
    persone_id = Entry(window, width=10)
    persone_id.grid(column=1, row=2)
    # Кнопка
    but = Button(window, text="Изменить",command=clicke)
    but.grid(column=1, row=3)
    window.mainloop()

#4 Удалить номер
def window_delete_phone():
    def clicke():
        delete_phone_db(num_phone.get())
    # Новое окно
    window = Tk()
    window.title("Удалить номер")
    window.geometry('400x200')
    # Номер телефона
    lbl_num_phone = Label(window, text="Номер телефона:", font=("Arial Bold", 14))
    lbl_num_phone.grid(column=0, row=1)
    num_phone = Entry(window, width=10)
    num_phone.grid(column=1, row=1)
    # Кнопка
    but = Button(window, text="Удалить", command=clicke)
    but.grid(column=1, row=3)
    window.mainloop()

#5 Удалить клиента
def window_delete_pers():
    def clicke():
        delete_persone_db(persone_id.get())
    # Новое окно
    window = Tk()
    window.title("Изменить сведения о клиенте")
    window.geometry('400x200')
    # ID клиента
    lbl_persone_id = Label(window, text="Идентификатор пользователя:", font=("Arial Bold", 14))
    lbl_persone_id.grid(column=0, row=2)
    persone_id = Entry(window, width=10)
    persone_id.grid(column=1, row=2)
    # Кнопка
    but = Button(window, text="Удалить", command= clicke)
    but.grid(column=1, row=3)
    window.mainloop()

# 6 Найти клиента
def select_db():
    def clicke():
        sql_reqest_select = ''
        if id_sql.get() == 1:
            sql_reqest_select = sql_reqest_select + f' AND persone_id = {persone_id.get()}'
        if name_sql.get() == 1:
            sql_reqest_select = sql_reqest_select + f' AND name = {entry_name.get()}'
        if surename_sql.get() == 1:
            sql_reqest_select = sql_reqest_select + f' AND surename = {entry_surename.get()}'
        if email_sql.get() == 1:
            sql_reqest_select = sql_reqest_select + f' AND email = {entry_email.get()}'
        if num_phone_sql.get() == 1:
            sql_reqest_select = sql_reqest_select + f' AND num_phone = {num_phone.get()}'
        select_db(sql_reqest_select)
    # Новое окно
    window = Toplevel()
    window.title("Добавить клиента")
    window.geometry('400x200')
    # ID клиента
    lbl_persone_id = Label(window, text="Идентификатор пользователя:", font=("Arial Bold", 14))
    lbl_persone_id.grid(column=0, row=0)
    persone_id = Entry(window, width=10)
    persone_id.grid(column=1, row=0)
    id_sql = IntVar()
    checkbox_id = Checkbutton(window, variable= id_sql)
    checkbox_id.grid(column=3, row=0)
    # Имя
    lbl_name = Label(window, text="Имя:", font=("Arial Bold", 14))
    lbl_name.grid(column=0, row=1)
    entry_name = Entry(window, width=10)
    entry_name.grid(column=1, row=1)
    name_sql = IntVar()
    checkbox_name = Checkbutton(window, variable= name_sql)
    checkbox_name.grid(column=3, row=1)
    # Фаилия
    lbl_surename = Label(window, text="Фамилия:", font=("Arial Bold", 14))
    lbl_surename.grid(column=0, row=2)
    entry_surename = Entry(window, width=10)
    entry_surename.grid(column=1, row=2)
    surename_sql = IntVar()
    checkbox_surename = Checkbutton(window, variable= surename_sql)
    checkbox_surename.grid(column=3, row=2)
    # E-mail
    lbl_email = Label(window, text="Эл. почта:", font=("Arial Bold", 14))
    lbl_email.grid(column=0, row=3)
    entry_email = Entry(window, width=10)
    entry_email.grid(column=1, row=3)
    email_sql = IntVar()
    checkbox_email = Checkbutton(window, variable= email_sql)
    checkbox_email.grid(column=3, row=3)
    # Номер телефона
    lbl_num_phone = Label(window, text="Номер телефона:", font=("Arial Bold", 14))
    lbl_num_phone.grid(column=0, row=4)
    num_phone = Entry(window, width=10)
    num_phone.grid(column=1, row=4)
    num_phone_sql = IntVar()
    checkbox_num_phone = Checkbutton(window, variable= num_phone_sql)
    checkbox_num_phone.grid(column=3, row=4)
    # Кнопка
    but = Button(window, text="Добавить", command=clicke)
    but.grid(column=1, row=5)
    window.mainloop()