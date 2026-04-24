import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Venky123456@",
    database="school_management"
)

cursor = conn.cursor(buffered=True)
print("Database connected sucessfully")
