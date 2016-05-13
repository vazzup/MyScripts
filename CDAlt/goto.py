#!/usr/bin/env python3
import os, sqlite3 as sql, sys
import subprocess
tofind = sys.argv[1]

connection = sql.connect(os.path.expanduser("~")+"/.dirdb.db")
cursor = connection.cursor()
#Check how many directories of name
cursor.execute(""" SELECT count(dirID) FROM Directories WHERE dirName IS (?)""", (tofind, ))
count = 0
for row in cursor:
    count+=row[0]

#Select dirID and path of directories that match given name
cursor.execute("""SELECT dirID, dirPath FROM Directories WHERE dirName IS (?)""",(tofind, ))

mypath = ""

#If more than one directory, ask user to choose id of directory he/she wants to go to
if count > 1:
    print("Multiple Directories")
    print("Type the ID of the folder you want to visit:")
    for row in cursor:
        print(row[0], row[1])
    while mypath == "":
        choice = int(input().strip())
        cursor.execute("""SELECT dirID, dirPath FROM Directories WHERE dirName IS (?)""",(tofind, ))
        for row in cursor:
            if choice == row[0]:
                mypath += row[1]
                print("Match Found")
                break
        if mypath == "":
            print("No such ID")
#otherwise just go ahead
else:
    for row in cursor:
        mypath = row[1]
mypath.strip()
os.system("gnome-terminal --working-directory="+mypath)
