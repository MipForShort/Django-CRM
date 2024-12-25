import mysql.connector

# setup mysql db connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'mip',
    passwd = ''
)

# preparing cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS Northwind")

print("All done!")