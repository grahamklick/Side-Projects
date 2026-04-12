import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db") #connects to databased

product_filter = input("Enter product name to filter (or press Enter for all): ")

if product_filter:
    query = """
    SELECT PRODUCT, SUM(amount) AS total_sales
    FROM sales
    WHERE product = ?
    GROUP BY product
    ORDER BY total_sales DESC
    """
    df = pd.read_sql_query(query, conn, params=(product_filter,))
else:
    query = """
    SELECT product, SUM(amount) AS total_sales
    FROM sales
    GROUP BY product
    ORDER BY total_sales DESC
    """
    df = pd.read_sql_query (query, conn)

print("\nQuery Results:")    
print(df)

print(f"\nRows returned: {len(df)}")

df.to_csv("sales_report.csv", index=False)

print("\nReport saved as sales_report.csv")

conn.close()