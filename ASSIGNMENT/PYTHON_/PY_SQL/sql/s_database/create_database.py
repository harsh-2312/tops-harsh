from .dbConnection import *

def c_database():
    database_name = input("Enter database name: ")
    sql = f"create database {database_name}"

    mycursor.execute(sql)