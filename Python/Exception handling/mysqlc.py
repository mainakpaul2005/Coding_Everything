import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qypw2005"
)

print(mydb)
