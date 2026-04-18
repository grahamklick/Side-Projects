import sqlite3

conn = sqlite3.connect("analytics.db")
cursor = conn.cursor()

#Clear existing data
cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM customer")
cursor.execute("DELETE FROM products")

#Insert Customers
customers = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie")
]

cursor.executemany(
    "INSERT INTO customer (customer_id, customer_name) VALUES (?, ?)",
    customers
)

#Insert Products
products = [
    (1, "Laptop", 1200),
    (2, "Mouse", 25),
    (3, "Keyboard", 75),
    (4, "Monitor", 300)
]

cursor.executemany(
    "INSERT INTO products (product_id, product_name, price) VALUES (?, ?, ?)",
    products
)

#Insert Orders
orders = [
    (1, 1, 1, 1, "2024-01-09"), # Alice bought 1 Laptop
    (2, 1, 2, 2, "2024-03-11"), # Alice bought 2 Laptop
    (3, 2, 2, 1, "2024-07-26"), # Bob bought 1 Laptop
    (4, 2, 3, 1, "2024-02-03"), # Bob bought 1 Laptop
    (5, 3, 4, 2, "2024-05-22"), # Charlie bought 2 Laptop
]

cursor.executemany(
    "INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?, ?)",
    orders
)

conn.commit()
conn.close()

print("Sample data loaded into customers, products, and orders tables")