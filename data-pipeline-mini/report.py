import sqlite3
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: python load_db.py <input_csv> [database_name] [table_name]")
    sys.exit(1)
    
database_name = sys.argv[1]
table_name = sys.argv[2] if len(sys.argv) >= 3 else "sales"
output_csv = sys.argv[3] if len(sys.argv) >= 4 else "pipeline_report.csv"

conn = sqlite3.connect(database_name)

query = f"""
SELECT product, SUM(amount) AS total_sales
FROM {table_name}
GROUP BY product
ORDER BY total_sales DESC
"""

df = pd.read_sql_query(query, conn)

print ("Pipeline report:")
print(df)

df.to_csv(output_csv, index=False)
print(f"\nSaved {output_csv}")

conn.close()