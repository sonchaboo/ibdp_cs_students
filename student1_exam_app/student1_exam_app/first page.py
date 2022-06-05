from tkinter import *

import sqlite3
start = Tk()

with sqlite3.connect('Sasha.db') as connection:
    cursor = connection.cursor()
    cursor.execute("delete from ExamManager")

l1 = Label(start, text="Exam Manager", width=15, bg='grey', fg='black')
b1 = Button(start, text="Start", width=10, bg='green', fg='black')
l1.pack(side=TOP, pady=50)
b1.pack(side=TOP, pady=10)
start.mainloop()
