import sqlite3
import pandas as pd

df = pd.read_csv("cleaned_sales.csv")

conn = sqlite3.connect("pipeline.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close

print("Loaded cleaned_sales.csv into pipeline.db as table 'sales'")
