import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
# Parse Data
cmd = "SELECT name, mark, students.id \
       FROM students, courses \
       WHERE students.id = courses.id"
raw_scores = c.execute(cmd)

# Generate A Dictionary With Values
averages = dict()
for i in raw_scores:
    if i[0] in averages:
        averages[i[0]][0] += i[1]
        averages[i[0]][1] += 1
    else:
        averages[i[0]] = [i[1], 1, i[2]]

#for i in averages:
#    print averages[i][0], averages[i][1]

# Add Averages To Database
cmd = "CREATE TABLE gradebook (name TEXT, id INTEGER, average REAL)"
c.execute(cmd)
for i in averages:
    avg = float(averages[i][0]) / averages[i][1]
    sid = averages[i][2]
    cmd = "INSERT INTO gradebook VALUES ('%s', %s, %s)"%(i, sid, avg)
    c.execute(cmd)
    print i, sid, avg #Debugging

#==========================================================
db.commit() #save changes
db.close()  #close database


