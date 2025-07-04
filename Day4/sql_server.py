import mysql.connector
from mysql.connector import Error


config = {
    'host': 'localhost',
    'user': 'root',  
    'password': '',  
    'database': 'employees',
    'raise_on_warnings': True
}


connection = mysql.connector.connect(**config)
cursor = connection.cursor(dictionary=True)

query = "SELECT * FROM employees limit 10"

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row['gender'] + "123")