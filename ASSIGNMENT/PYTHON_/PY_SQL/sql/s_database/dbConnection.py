import mysql.connector 

conn = mysql.connector.connect(
    user='root', 
    password='2312',
    host='127.0.0.1',
    database='test'
    )

mycursor = conn.cursor()

