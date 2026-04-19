import json
import logging
from pathlib import Path
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
RAW_OUTPUT_PATH = Path("data/raw_users.json")
LOG_FILE = Path("pipeline.log") #Path builds a folder for the logs, otherwise will just save as a file in the root directory of the project

#Initialize logging config, no debug logging, timestamp/log level/message, output to a file & the terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE), #output to file
        logging.StreamHandler() #output to terminal
        ]
    )

#Step by step logging added
def fetch_users():
    logging.info("Starting API request to fetch users.")
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    logging.info("API request completed successfully.")
    return response.json()

def save_raw_data(data, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as file: #opens file for reading and writing
        json.dump(data, file, indent=2)
        
    logging.info(f"Saved raw data to {output_path}")

#Exception logging added  - will output that API failed and why.      
def main():
    try:
        users = fetch_users()
        save_raw_data(users, RAW_OUTPUT_PATH)
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in fetch_data.py: {e}")
    
    print(f"Saved raw data to {RAW_OUTPUT_PATH}")
    
if __name__ == "__main__":
    main()