from .dbConnection import *

def delet():

    delete="DESCRIBE employee" 


    mycursor.execute(delete)
    tb=mycursor.fetchall()

    print(tb)