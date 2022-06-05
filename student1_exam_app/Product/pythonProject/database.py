import sqlite3

with sqlite3.connect('Sasha.db') as connection:
        cursor = connection.cursor()
        cursor.execute("create table ExamManager(Subject varchar(200), start varchar(200), end varchar(200), flag int)")
        # cursor.execute("insert into ExamManager values ('Maths', '12:34', '13:34', 0)")
        # cursor.execute("insert into ExamManager values ('Spanish', '17:34', '18:34', 0)")
        # cursor.execute("insert into ExamManager values ('Art', '16:34', '18:34', 0)")

        # cursor.execute('delete from ExamManager')


        cursor.execute("select * from ExamManager")
        print(cursor.fetchall())