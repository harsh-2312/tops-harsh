from .dbConnection import *

def show():
    sql="show databases"
    mycursor.execute(sql)
    dbs=mycursor.fetchall()

    for ds in dbs:
        print(ds)