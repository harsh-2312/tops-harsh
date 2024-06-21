from .dbConnection import *

def show_table():
    sql = 'select * from tops'
    mycursor.execute(sql)
    tables = mycursor.fetchall()

    for i in tables:
     print(i)