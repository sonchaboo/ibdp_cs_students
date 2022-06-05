import random
from tkinter import *
import sqlite3
from os import startfile
from CreateToolTip import CreateToolTip

from tkinter import messagebox as mb
import re


def get_data(civpicks,data,Nplayers,Ncivs):
    bans=[]
    nonbans=[]
    with sqlite3.connect('Mark.db') as connection:
        cursor = connection.cursor()
        for i in range(len(civpicks)):
            if civpicks[i].get()==True:
                    bans.append (data[i])
                    cursor.execute("insert into bans (name) values(?)", (data[i],))
            else:
                    nonbans.append (data[i])
    random.shuffle(nonbans)
    if Nplayers.get() == '':
        mb.showerror(
            "Error", 
            "The numbers should be written. Both into the civilizations per player field and number of players per game. The number of players or number of civilizations per player is too big, their multiplication after the banning phase should be less of equal to the number of left bans. If you can't solve problem individually you can write to my email and I will help you: iahogyeu@gmail.com")
    elif Ncivs.get() == '':
        mb.showerror(
            "Error", 
            "The numbers should be written. Both into the civilizations per player field and number of players per game. The number of players or number of civilizations per player is too big, their multiplication after the banning phase should be less of equal to the number of left bans. If you can't solve problem individually you can write to my email and I will help you: iahogyeu@gmail.com")
    elif not Ncivs.get().isdecimal():
        mb.showerror(
            "Error", 
            "The numbers should be written. Both into the civilizations per player field and number of players per game. The number of players or number of civilizations per player is too big, their multiplication after the banning phase should be less of equal to the number of left bans. If you can't solve problem individually you can write to my email and I will help you: iahogyeu@gmail.com")
    elif not Nplayers.get().isdecimal():
        mb.showerror(
            "Error", 
            "The numbers should be written. Both into the civilizations per player field and number of players per game. The number of players or number of civilizations per player is too big, their multiplication after the banning phase should be less of equal to the number of left bans. If you can't solve problem individually you can write to my email and I will help you: iahogyeu@gmail.com")
    else:
        Ncivs2=int(Ncivs.get())
        Nplayers2=int(Nplayers.get())
        if Ncivs2*Nplayers2>50:
            mb.showerror(
                "Error", 
                "The numbers should be written. Both into the civilizations per player field and number of players per game. The number of players or number of civilizations per player is too big, their multiplication after the banning phase should be less of equal to the number of left bans. If you can't solve problem individually you can write to my email and I will help you: iahogyeu@gmail.com")
        else:
            draft=f"N_players: {Nplayers2}\n N_cv: {Ncivs2}\n"
            s = 0
            e = Ncivs2
            for i in range (Nplayers2):
                draft += f'Player_{i+1}: {nonbans[s:e]}\n'
                s = e
                e += Ncivs2
            with open("draft.txt", "w", encoding="utf-8") as f:
                f.write(draft)
            startfile("draft.txt")