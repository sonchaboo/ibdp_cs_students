import random
from tkinter import *
import sqlite3
from os import startfile
from CreateToolTip import CreateToolTip
import tkinter.messagebox
from DRAFT import get_data
root = Tk()
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu = Menu(mainmenu, tearoff=0)

root.title("Civilization time saver")

root.geometry('1150x700')

with sqlite3.connect('Data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("select * from civ order by name")
        data = [row[1] for row in cursor.fetchall()]
        cursor.execute("select * from civ order by name")
        desc = [row[2] for row in cursor.fetchall()]

b1 = Button(text="Draft", 
            width=15, height=3)
b1.config(command=lambda:get_data(civpicks,data,Nplayers,Ncivs))

def new_random(version):
    global chbtns, data,civpicks
    for c in chbtns:
        c.grid_forget()
    with sqlite3.connect('Mark.db') as connection:
        cursor = connection.cursor()
        if version == 1:
            cursor.execute("select * from civ where vers = {} order by name".format(version))
        elif version == 2:
            cursor.execute("select * from civ where vers = {} or vers={} order by name".format(1,version))
        elif version == 3:
            cursor.execute("select * from civ where vers = {} or vers={} or vers={} order by name".format(1,2,version))
        elif version == 4:
            cursor.execute("select * from civ where vers = {} or vers={} or vers={} or vers={} order by name".format(1,2,3,version))
        data = [row[1] for row in cursor.fetchall()]
        if version == 1:
            cursor.execute("select * from civ where vers = {} order by name".format(version))
        elif version == 2:
            cursor.execute("select * from civ where vers = {} or vers={} order by name".format(1,version))
        elif version == 3:
            cursor.execute("select * from civ where vers = {} or vers={} or vers={} order by name".format(1,2,version))
        elif version == 4:
            cursor.execute("select * from civ where vers = {} or vers={} or vers={} or vers={} order by name".format(1,2,3,version))
        desc = [row[2] for row in cursor.fetchall()]

    civpicks=[]
    c=-1
    r=2
    chbtns=[]
    for i in range (len(data)):
            if i%3==0:
                    r+=1
                    c=0
            else:
                    c+=1
            var1 = BooleanVar()
            var1.set(0)
            c1 = Checkbutton(root, text=data[i],
                    variable=var1,
                    onvalue=1, offvalue=0)
            button1_ttp = CreateToolTip(c1, desc[i])
            civpicks.append(var1)
            c1.grid(row=r, column=c)
            chbtns.append(c1)

base = Button(text="Base", 
            width=15, height=3)
base.config(command=lambda:new_random(1))

RiseFall = Button(text="Rise&Fall", 
            width=15, height=3)
RiseFall.config(command=lambda:new_random(2))

GatheringStorm = Button(text="Gathering Storm", 
            width=15, height=3)
GatheringStorm.config(command=lambda:new_random(3))

DLC = Button(text="DLC", 
            width=15, height=3)
DLC.config(command=lambda:new_random(4))

def add_civ():
    root3 = Tk()
    Nwciv = Entry(root3,width=50)
    Nwdesc = Entry(root3,width=50)  
    l4=Label(root3, text="Enter new civilization")
    l4.pack()
    Nwciv.pack()
    l3=Label(root3, text="Enter description")
    l3.pack()
    Nwdesc.pack()
    upload = Button(root3,text="Upload", 
        width=15, height=3)
    def upload_civ():
        print(Nwciv.get(), Nwdesc.get())
        with sqlite3.connect('Mark.db') as connection:
            cursor = connection.cursor()
            cursor.execute("insert into civ (id,name,description,vers) values (?,?,?,?)", (0, Nwciv.get(), Nwdesc.get(), 4))
            root3.destroy()
    upload.config(command=upload_civ)
    upload.pack()

    root3.mainloop()

add = Button(text="Add civilization", 
            width=15, height=3)
add.config(command=add_civ)

def get_bans():
    with sqlite3.connect('Mark.db') as connection:
        cursor = connection.cursor()
        cursor.execute("select name, count(*) from bans group by name order by count(*) desc")
        text = ''
        for row in cursor.fetchall():
            text+=f"{row[0]}: {row[1]}\n"
        root2 = Tk()
        Label(root2, text=text).pack()
        root2.mainloop()

top_bans = Button(text="Top Bans", 
            width=15, height=3)
top_bans.config(command=get_bans)

Nplayers = Entry(width=50)
Ncivs = Entry(width=50)

l1 = Label(root,text="Number of players",
        font="Arial 32")
l2 = Label(root,text="Number of civilizations",
        font="Arial 32")

civpicks=[]
c=-1
r=2
chbtns = []
for i in range (len(data)):
        if i%3==0:
                r+=1
                c=0
        else:
                c+=1
        var1 = BooleanVar()
        var1.set(0)
        c1 = Checkbutton(root, text=data[i],
                 variable=var1,
                 onvalue=1, offvalue=0)
        button1_ttp = CreateToolTip(c1, desc[i])
        civpicks.append(var1)
        c1.grid(row=r, column=c)
        chbtns.append(c1)

b1.grid(row=1, column=1)
Nplayers.grid(row=2, column=0)
Ncivs.grid(row=2, column=2)
l1.grid(row=0, column=0)
l2.grid(row=0, column=2)
base.grid(row=1, column=4)
RiseFall.grid(row=2, column=4)
GatheringStorm.grid(row=3, column=4)
DLC.grid(row=4, column=4)
add.grid(row=5, column=4)
top_bans.grid(row=7, column=4)


root.mainloop()