import sqlite3
DB_name = "School.db"
with sqlite3.connect(DB_name) as con:
  cur = con.cursor()

  #Q1
  displayRec = """
  select * from students
  """
  #Q2
  compSci = '''
  select * from students where course = 'Computer Science'
  '''

  #Q3
  namEm = '''
  select F_name, L_name, email from students
  '''

  #Q4
  age = '''
  select * from students where age > 20
  '''

  #Q5
  age18_21 = '''
  select * from students where age between 12 and 21
  '''

  #Q6
  startsA = '''
  select * from students where F_name like 'A%'
  '''

  #CLQ1
  secondA = '''
  select * from students where F_name like '_a%'
  '''

  #Q7
  sortAsc = '''
  select * from students order by age
  '''
  #CLQ2
  sortDesc = '''
  select * from students order by age DESC
  '''

  #Q8 (group by, function: count())
  groupCount = '''
  select course, count(*) from students group by course
  '''

  #Q9
  #id = int(input("Enter the id to be updated: "))
  #newAge = int(input("Updated Age: "))
  updateAge = '''
  update students set age= ? where id= ?
  '''
  #Q10
  id = int(input("Enter the id to be updated: "))
  deleteQ = '''
  delete from students where id = ?
  '''

  cur.execute(deleteQ, (id,))
  items = cur.fetchall()
  for item in items:
    print(item)