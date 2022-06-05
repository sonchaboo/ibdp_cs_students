import sqlite3

def recreate_table():
    global root
    with sqlite3.connect('Sasha.db') as connection:
        cursor = connection.cursor()
        cursor.execute("select * from ExamManager")
        data = [row for row in cursor.fetchall()]
    for i in range(len(data)):
        for j in range(len(data[0])):
            e = Entry(root, width=10, fg='blue', font=('Arial', 16, 'bold'))
            e.grid(row=4 + i, column=3 + j, sticky='nsew', columnspan=1)
            e.insert(END, data[i][j])