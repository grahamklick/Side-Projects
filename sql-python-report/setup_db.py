import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor() #bridge bt .py and .db

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    amount REAL
)
""")

cursor.execute("DELETE FROM sales")

sample_data = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 75),
    ("Laptop", 1300),
    ("Mouse", 30),
    ("Monitor", 300)
]

cursor.executemany(
    "INSERT INTO sales (product, amount) VALUES (?, ?)",
    sample_data
)

conn.commit()
conn.close()

print("sales.db createda nd sample data loaded")