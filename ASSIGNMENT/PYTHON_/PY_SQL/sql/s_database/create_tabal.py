from .dbConnection import *

def c_tabal():
    tabal_name=input("enter tabal name:")
    tabal_data=input("taval data:")

    sql=f'create table {tabal_name} ({tabal_data})'
    mycursor.execute(sql)