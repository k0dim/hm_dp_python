from tkinter.ttk import Combobox
from tkinter import *
from Modul.info_insert import *

# Функция для кнопки 'Выбрать'
def clicked():
    combo_values = comdo.get()
    # print(combo_values)
    if combo_values == 'Создать БД':
        create_db('customer', 'persone', 'phone')
    elif combo_values == 'Добавить клиента':
        window_info()
    elif combo_values == 'Добавить телефон':
        window_phone()
    elif combo_values == 'Изменить информацию клиента':
        window_update_info()
    elif combo_values == 'Удалить телефона':
        window_delete_phone()
    elif combo_values == 'Удалить клиента':
        window_delete_pers()

window = Tk()
# Имя окна
window.title("Работа с PostgreSQL из Python")
# Размер окна
window.geometry('700x250')
# Текст
lbl = Label(window, text="Доброго времени суток!", font=("Arial Bold", 20))
lbl.grid(column=1, row=0)
lbl = Label(window, text="Выберите нужное действие:", font=("Arial Bold", 14))
lbl.grid(column=0, row=3)
# Выплывающий список
comdo= Combobox(window)
comdo['values'] = ('Создать БД', 'Добавить клиента', 'Добавить телефон', 'Изменить информацию клиента', 'Удалить телефона', 'Удалить клиента', 'Найти клиента')
comdo.current(0)
comdo.grid(column=1, row=3)
# Кнопка "Выбрать"
btn = Button(window, text='Выбрать', command=clicked)
btn.grid(column=2, row=3)
window.mainloop()