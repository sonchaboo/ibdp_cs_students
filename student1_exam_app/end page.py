from tkinter import *
root = Tk()
f_top = Frame(root)
f_bot = Frame(root)
a = Label("Exam Finished")(width=50)
a.grid(row=5, column=1, columnspan=1)
Button(root2, text="See performed exams", command=check).grid(row=8, column=3, columnspan=2)
Button(root2, text="Start Again", command=check).grid(row=8, column=6, columnspan=2)
root2.mainloop()


# from tkinter import *
#
# root = Tk()
#
# l1 = Label(root, text="Exam is finished", width=15, bg='grey', fg='black')
# b1 = Button(root, text="Start again", width=10, bg='green', fg='black')
# l1.pack(side=TOP, pady=50)
# b1.pack(side=TOP, pady=10)
# root.mainloop()
