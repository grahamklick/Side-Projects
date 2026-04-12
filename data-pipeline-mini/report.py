import sqlite3
import pandas as pd

conn = sqlite3.connect("pipeline.db")

query = """
SELECT product, SUM(amount) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_sales DESC
"""

df = pd.read_sql_query(query, conn)

print ("Pipeline report:")
print(df)

df.to_csv("pipeline_report.csv", index=False)
print("\nSaved pipeline_report.csv")

conn.close()