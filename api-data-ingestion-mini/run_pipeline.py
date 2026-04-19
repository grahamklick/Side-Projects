import logging
from pathlib import Path
from fetch_data import fetch_users, save_raw_data, RAW_OUTPUT_PATH
from transform_data import transform_users, save_clean_data, CLEAN_OUTPUT_PATH
from load_to_db import load_csv_to_sqlite, DB_FILE, TABLE_NAME

LOG_FILE = Path("pipeline.log")

#Identical to what was added to fetch_data, covers exceptions in run_pipeline
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE), #output to file
        logging.StreamHandler() #output to terminal
        ]
    )

def main():
    try:
        logging.info("Pipeline started.")
        
        users = fetch_users()
        save_raw_data(users, RAW_OUTPUT_PATH)
    
        df = transform_users(users)
        save_clean_data(df, CLEAN_OUTPUT_PATH)
        
        load_csv_to_sqlite(CLEAN_OUTPUT_PATH, DB_FILE, TABLE_NAME)

        logging.info("Pipeline completed succesffully.")
        print("Pipeline completed successfully.")
    
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
    
if __name__ == "__main__":
    main()