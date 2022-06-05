from tkinter import *
import sqlite3
from CreateToolTip import CreateToolTip

from csIA import chbtns




def new_random(root,data,civpicks,version):
    # global chbtns
    # , data,civpicks
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
            #print(i,r,c)
            var1 = BooleanVar()
            var1.set(0)
            c1 = Checkbutton(root, text=data[i],
                    variable=var1,
                    onvalue=1, offvalue=0)
            button1_ttp = CreateToolTip(c1, desc[i])
            civpicks.append(var1)
            c1.grid(row=r, column=c)
            chbtns.append(c1)
    
    return chbtns