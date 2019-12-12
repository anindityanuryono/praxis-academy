import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="toko_mainan"
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

result = cursor.fetchone()

print(result)