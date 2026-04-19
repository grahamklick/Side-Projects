import logging
import sqlite3
import pandas as pd
from pathlib import Path

CLEAN_INPUT_PATH = Path("output/clean_users.csv")
DB_FILE = "analytics.db"
TABLE_NAME = "users"
LOG_FILE = Path("pipeline.log")


#Identical to what was added to fetch_data, covers exceptions in load_to_db
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE), #output to file
        logging.StreamHandler() #output to terminal
        ]
    )

def load_csv_to_sqlite(csv_path, db_file, table_name):
    logging.info(f"Loading cleaned CSV from {csv_path}")
    df = pd.read_csv(csv_path)
    
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    
    logging.info(f"Loaded {len(df)} rows into table '{table_name}' in {db_file}")
    
def main():
    try:
        load_csv_to_sqlite(CLEAN_INPUT_PATH, DB_FILE, TABLE_NAME)
    except FileNotFoundError:
        logging.error(f"Clean CSV file not found: {CLEAN_INPUT_PATH}")
    except Exception as e:
        logging.error(f"Unexpected error in load_to_db.py: {e}")

#Python has default variable __name__ - will be executed if .py is run directly from this file, vs. imported (as it will be in run_pipeline)      
if __name__ == "__main__":
    main()