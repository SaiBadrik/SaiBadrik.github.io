import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
studentCreationQuery = '''
CREATE TABLE IF NOT EXISTS students
(rollno INTEGER PRIMARY KEY, 
name TEXT,
age INTEGER,
grade INTEGER,
section TEXT)'''
cur.execute(studentCreationQuery)
