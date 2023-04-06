from tkinter import *
import utils

from prettytable import PrettyTable

root = Tk()
root.title('Рабочее окно списания')
root.geometry("400x300")

mytable = PrettyTable()
mytable.title_names = ["Наименование", "Метраж"]
mytable.add_rows(utils.libre_dt)
table = mytable.get_string(start=0, end=100)

label = Label(text=f"{table}")
label.pack()

root.mainloop()
