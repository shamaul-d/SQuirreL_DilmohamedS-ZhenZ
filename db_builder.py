import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

# db.close()

q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"
c.execute(q)    #run SQL query
fObj = open("peeps.csv") 
d=csv.DictReader(fObj)
for k in d:
    p = "INSERT INTO students VALUES ('%s', %s, %s)"%(k['name'], k['age'], k['id'])
    c.execute(p)

# Making Courses ? ? ? ?

q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(q)
raw = open("courses.csv")
parsed = csv.DictReader(raw)
for k in parsed:
    stuff = "INSERT INTO courses VALUES ('%s', %s, %s)"%(k['code'], k['mark'], k['id'])
    c.execute(stuff)

#==========================================================
db.commit() #save changes
db.close()  #close database


