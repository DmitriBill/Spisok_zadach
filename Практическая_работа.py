import tkinter
from tkinter import messagebox
import sys # обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python
import threading # запуск нескольких операций одновременно в одном пространстве процесса. Потоки - позволяют одновременно запускать различные подпрограммы и могут упростить архитектуру проектов


duties = [] # Обязанности
timer = threading
thread = True


# Основные функции
def get_note(task=""):
    text = notice.get()
    interval = int(time.get())
    notice.delete(0, tkinter.END) # Содержимое в окне удаляется
    time.delete(0, tkinter.END) # Содержимое в окне удаляется
    adding_to_the_list(text, interval)
    if 0 < interval < 100000000:
        refresh_list()


def adding_to_the_list(text, interval):
    duties.append([text, interval])
    timer = threading.Timer(interval, time_is_over, [text])
    timer.start()


def present_time():
    if thread:
        present_timer = threading.Timer(1.0, present_time)
        present_timer.start()
    for task in duties:
        if task[1] == 0:
            duties.remove(task)
        task[1] -= 1
    refresh_list()



# Всплывающее окно
def time_is_over(task):
    tkinter.messagebox.showinfo("НАПОМИНАНИЕ", "Время для задачи : " + task)


def refresh_list():
    if duty_sheet.size() > 0:
        duty_sheet.delete(0, "end")
    for task in duties:
        duty_sheet.insert("end", " До задачи: " "'" + task[0] + "' осталось " + str(task[1]) + " секунд")


# Окно
if __name__ == '__main__': # Вызов функции и выводи что-то на стандартный поток вывода, внутри блока
    reminder = tkinter.Tk()
    reminder.geometry("316x315")
    reminder.title("НАПОМИНАНИЕ!")

    # Рамка
    window = tkinter.Frame(reminder)
    window.pack()


    # Экран
    screen = tkinter.Label(reminder, text="Задача:", justify = tkinter.LEFT) # Выравнивание текста
    screen_interval = tkinter.Label(reminder, text="Время (c):", justify = tkinter.LEFT)
    notice = tkinter.Entry(reminder, width=30, bg='lightyellow')
    time = tkinter.Entry(reminder, width=15, bg='lightyellow')
    btn1 = tkinter.Button(reminder, text='Добавить', fg="black", bg='orange', height=2, width=40, command=get_note)
    btn2 = tkinter.Button(reminder, text='Выход', fg="black", bg='lightblue', height=2, width=40, command=reminder.destroy) # Закрывается окно 
    duty_sheet = tkinter.Listbox(reminder, bg='lightyellow')

    if duties != "":
        present_time()

    
    # Размеры
    screen.place(x=-45, y=10, width=168, height=20)
    screen_interval.place(x=190, y=10, width=135, height=20)
    notice.place(x=17, y=30, width=180, height=25)
    time.place(x=230, y=30, width=70, height=25)
    btn1.place(x=16, y=60, width=70, height=25)
    btn2.place(x=230, y=60, width=52, height=25)
    duty_sheet.place(x=15, y = 100, width=286, height=200)

    reminder.mainloop()
