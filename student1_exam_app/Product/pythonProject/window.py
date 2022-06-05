from tkinter import *

from tkinter import messagebox as mb
import sqlite3
#from main23 import recreate_table
from new_table import recreate_table

def window():
    root2 = Tk()
    def check():

        answer = mb.askyesno(
            title="New Exam",
            message="Insert new exam?")

        if answer:

            with sqlite3.connect('Sasha.db') as connection:
                cursor = connection.cursor()

                cursor.execute("Insert into ExamManager(Subject, start, end, flag) values(?, ?, ?, ?)",(a.get(), b.get(), c.get(), 0))
                connection.commit()


                recreate_table()

                root2.destroy()

    Label(root2, text="Subject:").grid(row=3, column=3, columnspan=1)
    Label(root2, text="Start:").grid(row=3, column=4, columnspan=1)
    Label(root2, text="End:").grid(row=3, column=5, columnspan=1)


    a = Entry(root2, width=50)
    a.grid(row=5, column=1, columnspan=1)
    b = Entry(root2, width=20)
    b.grid(row=5, column=4, columnspan=1)
    c = Entry(root2, width=20)
    c.grid(row=5, column=5, columnspan=1)
    Button(root2, text="approve", command=check).grid(row=8, column=8, columnspan=8)
    root2.mainloop()










