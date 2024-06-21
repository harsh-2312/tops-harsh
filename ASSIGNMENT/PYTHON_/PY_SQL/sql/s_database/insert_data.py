from .dbConnection import *

def i_data():
    sql = """INSERT INTO tops (id, name , number) VALUES (%s, %s, %s)"""
    values = [
        (1,'John Doe', '1234567890'),
        (2,'Jane Smith',  '2345678901'),
        (3,'Michael Johnson',  '3456789012'),
        (4,'Emily Davis',  '4567890123'),
        (5,'Christopher Brown', '5678901234'),
        (6,'Jessica Wilson', '6789012345'),
        (7,'David Martinez', '7890123456'),
        (8,'Sarah Taylor', '8901234567'),
        (9,'Matthew Anderson', '9012345678'),
        (10,'Amanda Thomas', '0123456789')
    ]
    try:
        mycursor.executemany(sql, values)
        conn.commit()
        print(mycursor.rowcount, "records inserted.")
    except Exception as e:
        print("Error inserting records:", e)