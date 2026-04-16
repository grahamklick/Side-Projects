import sqlite3
import pandas as pd
import sys

#Updating to stop assuming fixed file and database names
if len(sys.argv) < 2:
    print("Usage: python load_db.py <input_csv> [database_name] [table_name]")
    sys.exit(1)

input_csv = sys.argv[1]
database_name = sys.argv[2] if len(sys.argv) >= 3 else "pipeline.db" #opportunity to enter a different DB name, not required will default if not provided
table_name = sys.argv[3] if len(sys.argv) >= 4 else "sales" #opportunity to enter different table within db, assuming using non-static, will defaul if not provided

df = pd.read_csv(input_csv) #updated to read the input file name from CLI argument
conn = sqlite3.connect(database_name) #updated to read the database_name from CLI argument
df.to_sql(table_name, conn, if_exists="replace", index=False) #updated to replace static data with calls to input values
conn.close

print(f"Loaded {input_csv} into {database_name} as table '{table_name}'")
