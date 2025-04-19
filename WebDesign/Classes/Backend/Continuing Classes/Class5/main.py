import sqlite3
DB_name = "School.db"
con = sqlite3.connect(DB_name)
cur = con.cursor()
createTableQ = '''
create table if not exists students(
id integer primary key autoincrement,
F_name text,
L_name text,
age integer,
gender text,
course text,
email text,
phoneNumber numeric
)
'''

cur.execute(createTableQ)
insertionQ = '''
insert into students values 
    (NULL, "Jeffrey", "Bezos", 10, "Male", "Computer", "jeffreyb@gmail.com", 19547855),
    (NULL, 'Alice', 'Johnson', 19, 'Female', 'Computer Science', 'alice.johnson@univ.edu', '9876543210'),
    (NULL, 'Bob', 'Smith', 21, 'Male', 'Electrical Engineering', 'bob.smith@univ.edu', '9876543211'),
    (NULL, 'Charlie', 'Brown', 20, 'Male', 'Mechanical Engineering', 'charlie.brown@univ.edu', '9876543212'),
    (NULL, 'David', 'Williams', 22, 'Male', 'Civil Engineering', 'david.williams@univ.edu', '9876543213'),
    (NULL, 'Emma', 'Davis', 18, 'Female', 'Computer Science', 'emma.davis@univ.edu', '9876543214'),
    (NULL, 'Sophia', 'Taylor', 23, 'Female', 'Biotechnology', 'sophia.taylor@univ.edu', '9876543215'),
    (NULL, 'Michael', 'Anderson', 20, 'Male', 'Mathematics', 'michael.anderson@univ.edu', '9876543216'),
    (NULL, 'Olivia', 'Thomas', 19, 'Female', 'Physics', 'olivia.thomas@univ.edu', '9876543217'),
    (NULL, 'Daniel', 'Martinez', 22, 'Male', 'Economics', 'daniel.martinez@univ.edu', '9876543218'),
    (NULL, 'Liam', 'Harris', 21, 'Male', 'Psychology', 'liam.harris@univ.edu', '9876543219');
'''
cur.execute(insertionQ)
con.commit()
con.close()