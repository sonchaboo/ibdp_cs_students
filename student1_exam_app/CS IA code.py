from tkinter import *
from datetime import date
import re

import time
from tkinter import messagebox as mb


from datetime import datetime


#from wno import window


# def finishexam(root):
#     finishexam.geometry('1000x1000')
#     #global root
#     root.destroy()
#     end = Tk()
#     f_top = Frame(end)
#     f_bot = Frame(end)
#     a = Label(text="Exam Finished", font=('Arial', 16, 'bold'), width=50)
#     a.grid(row=1, column=1, columnspan=1)
#     #Button(end, text="See performed exams").grid(row=2, column=1, columnspan=2)
#     end.mainloop()
def finishexam(root):
   #global root
   root.destroy()
   end = Tk()
   f_top = Frame(end)
   f_bot = Frame(end)
   a = Label(text="Exam Finished", font=('Arial', 16, 'bold'), width=50)
   a.grid(row=1, column=1, columnspan=1)

   end.mainloop()

import sqlite3

def startexam():
    start.destroy()
    import pygame as pg
    pg.init()
    pg.mixer.music.load('sound_the_alarm-[AudioTrimmer.com].mp3')
    root = Tk()

    #root.geometry('500x300')
    f_top = Frame(root)
    f_bot = Frame(root)

    with sqlite3.connect('Sasha.db') as connection:
            cursor = connection.cursor()
            cursor.execute("select * from ExamManager")
            data = [row for row in cursor.fetchall()]
            print(data)

    Label(text=date.today().strftime("%d/%m/%Y"), font=('Arial', 16)).grid(row=1, column=2, columnspan=1)
    label = Label(text="")
    label.grid(row=1, column=3, columnspan=4)
    Label(text="Centre Number:", font=('Arial', 16)).grid(row=1, column=7, columnspan=2)
    Entry().grid(row=2, column=7, columnspan=2)
    # def clock():
    #     now = time.strftime("%H:%M:%S")
    #     label.config(text=now)
    #     label.after(1000, clock)
    # clock()

    def clock():
        now = time.strftime("%H:%M:%S")
        with sqlite3.connect('Sasha.db') as connection:
            cursor = connection.cursor()
            cursor.execute("select * from ExamManager")
            data = [row for row in cursor.fetchall()]
        times = [data[i][2] + ':00' for i in range(len(data))]

        index = []
        f = '%H:%M:%S'
        alarm = (datetime.strptime(now, f) - datetime.strptime('00:05:00', f) + datetime.strptime('00:10:00', f)).strftime("%H:%M:%S")
        print(times, alarm)
        #print(alarm, times)
        if alarm in times:
            #print(alarm, times)
            pg.mixer.music.play()
            index = [i for i in range(len(times)) if alarm == times[i]]
            for i in index:
                a = Label(text="!", bg='red', font=("Comic Sans MS", 24, "bold"))
                a.grid(row=4 + i, column=2, columnspan=4)

        if now in times:
            index = [i for i in range(len(times)) if now == times[i]]
            for i in index:
                # a = Label(text="!", bg='red', font=("Comic Sans MS", 24, "bold"))
                # a.grid(row=4 + i, column=1, columnspan=4)
                Label(text="finished", bg="#4db6eb").grid(row=4+i, column=6, columnspan=1, )

            # a.grid_forget()

        label.config(text=now, font=('Arial', 16, 'bold'))
        label.after(1000, clock)


    clock()


    def recreate_table():


        with sqlite3.connect('Sasha.db') as connection:
            cursor = connection.cursor()
            cursor.execute("select * from ExamManager")
            data = [row for row in cursor.fetchall()]
        butt = []
        for i in range(len(data)):
            b = Button(text="End", font=('Arial', 16))
            butt.append(b)

        for i in range(len(data)):
            for j in range(len(data[0])):
                if j != len(data[0]) - 1:

                    e = Entry(root, width=10, fg='blue', font=('Arial', 16))
                    e.grid(row=4 + i, column=3 + j, sticky='nsew', columnspan=1)
                    e.insert(END, data[i][j])
                else:
                    butt[i].grid(row=4 + i, column=3 + len(data[0]) - 1, columnspan=1)

        for i in range(len(butt)):
            butt[i].config(command=lambda i=i: end_32(4 + i))

    def window():
        root2 = Tk()
        def check(a,b,c):

            subject = a.get()
            st = b.get()
            ed = c.get()



            time_re = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')

            def is_time_format(s):
                return bool(time_re.match(s))
            if subject != '' and bool(time_re.match(st)) == True and bool(time_re.match(ed)) == True:
                answer = mb.askyesno(
                    title = "New Exam",
                    message="Insert new exam?")
                if answer:
                    with sqlite3.connect('Sasha.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("Insert into ExamManager(Subject, start, end, flag) values(?, ?, ?, ?)",(a.get(), b.get(), c.get(), 0))
                        connection.commit()
                        recreate_table()
                        root2.destroy()
            else:
                mb.showerror(
                    "Error",
                    "Please enter appropriate information")

        Label(root2, text="Enter Subject:", font=('Arial', 16)).grid(row=3, column=3, columnspan=1)
        Label(root2, text="Enter Start time:", font=('Arial', 16)).grid(row=3, column=4, columnspan=1)
        Label(root2, text="Enter End time:", font=('Arial', 16)).grid(row=3, column=5, columnspan=1)

        a = Entry(root2, width=50)
        a.grid(row=5, column=3, columnspan=1)
        b = Entry(root2, width=20)
        b.grid(row=5, column=4, columnspan=1)
        c = Entry(root2, width=20)
        c.grid(row=5, column=5, columnspan=1)
        Button(root2, text="Approve",font=('Arial', 16), command=lambda:check(a,b,c)).grid(row=5, column=6, columnspan=1)
        root2.mainloop()


    Button(text="Enter new subject", font=('Arial', 16), highlightbackground='#2eed24', command=window).grid(row=2, column=1, columnspan=3)

    def end_all ():
        for i in range(len(data)):
             Label(text="finished", font=('Arial', 16), bg='red').grid(row=4+i, column=6, columnspan=1,)
        #root.destroy()
        finishexam(root)



    Button(text="End all", highlightbackground='#24d9ed', font=('Arial', 16), command=end_all).grid(row=3, column=7, columnspan=3)


    Label(text="Subject:", font=('Arial', 16)).grid(row=3, column=3, columnspan=1)
    Label(text="Start:", font=('Arial', 16)).grid(row=3, column=4, columnspan=1)
    Label(text="End:", font=('Arial', 16)).grid(row=3, column=5, columnspan=1)




    def end_32(i):
        Label(text="finished", font=('Arial', 16), bg='red').grid(row=i, column=6, columnspan=1, )

    start.end_32('1000x1000')

    butt= []

    for i in range(len(data)):
        b = Button(text="End")
        butt.append(b)

    for i in range(len(data)):
            for j in range(len(data[0])):
                if j != len(data[0]) - 1:

                    e = Entry(root, width=10, fg='blue', font=('Arial', 16))
                    e.grid(row=4+i, column=3+j, sticky='nsew', columnspan=1)
                    e.insert(data[i][j]);
                else:
                    butt[i].grid(row=4+i, column=3+len(data[0]) - 1, columnspan=1)

    for i in range(len(butt)):
        butt[i].config(command=lambda i=i: end_32(4 + i))
    root.mainloop()



def startpage():
    start = Tk()

    l1 = Label(start, text="Exam Manager", width=15, bg='#9ceb4d', fg='blue')
    b1 = Button(start, text="Start", width=10, bg='#9ceb4d', fg='black', command=startexam)
    l1.pack(side=TOP, pady=50)
    b1.pack(side=TOP, pady=10)
    start.mainloop()

start = Tk()
start.geometry('400x400')
with sqlite3.connect('Sasha.db') as connection:
    cursor = connection.cursor()
    cursor.execute("delete from ExamManager")

Label(start, text="Exam Manager", width=15, font=('Arial', 30, 'bold'), bg='grey', fg='black').pack(side=TOP, pady=50)
b1 = Button(start, text="Start", width=10, font=('Arial', 16, 'bold'), highlightbackground='#9ceb4d',command=startexam)
b1.pack(side=TOP, pady=10)
start.mainloop()









