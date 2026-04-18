import sqlite3

conn = sqlite3.connect("analytics.db")
cursor = conn.cursor() #used to actually send commands to the DB

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")

conn.commit()
conn.close()

print("analytics.db created with customers, products, and orders tables")