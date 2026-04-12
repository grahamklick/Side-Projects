import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db") #connects to databased

query = """
SELECT product, SUM(amount) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_sales DESC
"""

df = pd.read_sql_query (query, conn)
print(df)

df.to_csv("sales_report.csv", index=False)

conn.close()