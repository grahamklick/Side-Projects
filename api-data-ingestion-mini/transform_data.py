import json
import logging
from pathlib import Path
import pandas as pd

RAW_INPUT_PATH = Path("data/raw_users.json")
CLEAN_OUTPUT_PATH = Path("output/clean_users.csv")
LOG_FILE = Path("pipeline.log") #Path builds a folder for the logs, otherwise will just save as a file in the root directory of the project

#Identical to what was added to fetch_data, covers exceptions in transform_data
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE), #output to file
        logging.StreamHandler() #output to terminal
        ]
    )

#Add logging details to data transformation process
def load_raw_data(input_path):
    logging.info(f"Loading raw data from {input_path}")
    
    with open(input_path, "r", encoding="utf-8") as file: #opens file for reading only
        return json.load(file)
    
def transform_users(users):
    logging.info("Transforming user data.")
    cleaned_rows = []
    
    for user in users:
        cleaned_rows.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "phone": user.get("phone"),
            "website": user.get("website"),
            "city": user.get("address", {}).get("city"), #address is multi-part, use {} and .get for specific address component bc not explicit
            "zipcode": user.get("address", {}).get("zipcode"),
            "company_name": user.get("company", {}).get("name"),
            "company_bs": user.get("company", {}).get("bs"),
            })
        
    logging.info("Transformation completed.")
    return pd.DataFrame(cleaned_rows)

def save_clean_data(df, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=-True)
    df.to_csv(output_path, index=False)
    logging.info(f"Saved cleaned data to {output_path}") #replaced static print message with log message
    
def main():
    try:
        users = load_raw_data(RAW_INPUT_PATH)
        df = transform_users(users)
        save_clean_data(df, CLEAN_OUTPUT_PATH)
        print(df.head())
    except FileNotFoundError:
        logging.erro(f"Raw input file not found: {RAW_INPUT_PATH}")
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in raw input file: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in transform_data.py: {e}")
    
if __name__ == "__main__":
    main()
    