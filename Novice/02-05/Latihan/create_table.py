import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="toko_mainan"
)

cursor = db.cursor()
sql = """CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")