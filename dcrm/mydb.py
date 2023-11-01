import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "roottoor",
)
cursor = db.cursor()

cursor.execute("CREATE DATABASE Django")

