import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    database="shop_db",
    user="root",
    password="kit2025"
)

if connection.is_connected():
    print("Подключился к базе!")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products;")
    for row in cursor.fetchall():
        print(row)

connection.close()