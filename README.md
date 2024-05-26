import sqlite3 as s
from datetime import datetime

def gettime():
    time=datetime.now()
    #curtime=strftime.time("%H hours % Mminutes")
    return time
def makeconnection():
    connect= s.connect("projdata.db")
    return connect

def getdata():
    con=makeconnection()
    cur=con.cursor()

    cur.execute("SELECT * FROM QNA")
    return cur.fetchall()

def getfromprojectdb(ques):
    rows = getdata()
    ans=""
    for row in rows:#loop iterate in whole table rows
        if row[0] == ques:#row[0] represents ques colm and rows is totak no of rows(row[0] in ques means that ques entered by user even if vary from ques in table it will just check some of the related value/text from entered ques if single word matches it give ans)
            ans+=row[1]
            break

    return ans

print(getfromprojectdb("what is time"))

def processquery():
    ans=getfromprojectdb(input("enter your ques"))
    if ans=="gettime":
        return "time is" + str(gettime())
    else:
        return "nothing to return"
    # Write your code here :-)
print(processquery())
# Personal Assistant 
# python project
