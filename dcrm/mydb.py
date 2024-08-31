import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345678'
)

#prepare a cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE danco")

print("All done")
