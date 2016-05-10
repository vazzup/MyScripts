import os, sys
import sqlite3 as sql

print("Creating databases...")
connection = sql.connect(os.path.expanduser("~")+"/.dirdb.db")
cursor = connection.cursor()
print("Creating table...")
cursor.execute("""CREATE TABLE IF NOT EXISTS Directories (dirID int primary key not NULL, dirName text, dirPath text)""")
cursor.execute("""SELECT max(dirID) FROM Directories""")
key = 0
for row in cursor:
    if row[0] is not None:
        key = row[0] + 1

original = key
print("Going through directories...")
for root, dirs, files in os.walk(os.path.expanduser("~"), topdown=True):
    dirs[:] = [d for d in dirs if not d[0] == '.']
    for name in dirs:
        path = os.path.join(root, name)
        realpath = ""
        flag =  False
        for i in path:
            if i == " ":
                realpath+="\\"
                flag = True
            realpath+=i
        if flag:
            print(realpath, name)
        cursor.execute("""SELECT dirPath FROM Directories WHERE dirPath IS (?)""", (realpath, ))
        ans = ""
        for row in cursor:
            ans = row[0]
        if ans != path:
            cursor.execute("""INSERT INTO Directories values(?,?,?)""",(key, name, realpath))
            key+=1
print(key - original, "directories added...")
connection.commit()
