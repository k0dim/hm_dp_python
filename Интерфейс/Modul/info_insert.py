from Modul.SQL_reqests import *
from tkinter import *

#1 Добавить данные о клиенте
def window_info():
    # Новое окно
    window = Tk()
    window.title("Добавить клиента")
    window.geometry('400x200')
    # Имя
    lbl_name = Label(window, text="Имя:", font=("Arial Bold", 14))
    lbl_name.grid(column=0, row=0)
    name = Entry(window, width=10)
    name.grid(column=1, row=0)
    name = name.get()
    # Фамилия
    lbl_surename = Label(window, text="Фамилия:", font=("Arial Bold", 14))
    lbl_surename.grid(column=0, row=1)
    surename = Entry(window, width=10)
    surename.grid(column=1, row=1)
    surename = surename.get()
    # E-mail
    lbl_email = Label(window, text="Эл. почта:", font=("Arial Bold", 14))
    lbl_email.grid(column=0, row=2)
    email = Entry(window, width=10)
    email.grid(column=1, row=2)
    email = email.get()
    # dict_data = {'name':name, 'surename':surename, 'email':email}
    but = Button(window, text="Добавить")
    but.grid(column=1, row=3)
    but.bind('<Button-1>', insert_persone_db(name, surename, email))
    window.mainloop()

#2 Добавить номер телефона
def window_phone():
    # Новое окно
    window = Tk()
    window.title("Добавить номер")
    window.geometry('400x200')
    # Идентификатор клиента
    lbl_persone_id = Label(window, text="Идентификатор клиента:", font=("Arial Bold", 14))
    lbl_persone_id.grid(column=0, row=0)
    persone_id = Entry(window, width=10)
    persone_id.grid(column=1, row=0)
    persone_id = persone_id.get()
    # Номер телефона
    lbl_num_phone = Label(window, text="Номер телефона:", font=("Arial Bold", 14))
    lbl_num_phone.grid(column=0, row=1)
    num_phone = Entry(window, width=10)
    num_phone.grid(column=1, row=1)
    num_phone = num_phone.get()
    but = Button(window, text="Добавить")
    but.grid(column=1, row=3)
    but.bind('<Button-1>', insert_phone_db(persone_id, num_phone))
    window.mainloop()


#3 Изменить сведения о клиенте
def window_update_info():
    # Новое окно
    window = Tk()
    window.title("Изменить сведения о клиенте")
    window.geometry('400x200')
    # Колона
    lbl_column = Label(window, text="Изменяемый параметр:", font=("Arial Bold", 14))
    lbl_column.grid(column=0, row=0)
    column = Entry(window, width=10)
    column.grid(column=1, row=0)
    column = column.get()
    # Истинное значение
    lbl_value = Label(window, text="Истинное значение:", font=("Arial Bold", 14))
    lbl_value.grid(column=0, row=1)
    value = Entry(window, width=10)
    value.grid(column=1, row=1)
    value = value.get()
    # Пользователь
    lbl_persone_id = Label(window, text="Идентификатор пользователя:", font=("Arial Bold", 14))
    lbl_persone_id.grid(column=0, row=2)
    persone_id = Entry(window, width=10)
    persone_id.grid(column=1, row=2)
    persone_id = persone_id.get()
    but = Button(window, text="Изменить")
    but.grid(column=1, row=3)
    but.bind('<Button-1>', update_persone_db(persone_id, column, value, persone_id))
    window.mainloop()

#4 Удалить номер
def window_delete_phone():
    # Новое окно
    window = Tk()
    window.title("Удалить номер")
    window.geometry('400x200')
    # Номер телефона
    lbl_num_phone = Label(window, text="Номер телефона:", font=("Arial Bold", 14))
    lbl_num_phone.grid(column=0, row=1)
    num_phone = Entry(window, width=10)
    num_phone.grid(column=1, row=1)
    num_phone = num_phone.get()
    but = Button(window, text="Удалить")
    but.grid(column=1, row=3)
    but.bind('<Button-1>', delete_phone_db(num_phone))
    window.mainloop()

#5 Удалить клиента
def window_delete_pers():
    # Новое окно
    window = Tk()
    window.title("Изменить сведения о клиенте")
    window.geometry('400x200')
    # Номер телефона
    lbl_persone_id = Label(window, text="Идентификатор пользователя:", font=("Arial Bold", 14))
    lbl_persone_id.grid(column=0, row=2)
    persone_id = Entry(window, width=10)
    persone_id.grid(column=1, row=2)
    persone_id = persone_id.get()
    num_phone = num_phone.get()
    but = Button(window, text="Удалить")
    but.grid(column=1, row=3)
    but.bind('<Button-1>', delete_persone_db(persone_id))
    window.mainloop()