import json
from pathlib import Path
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
RAW_OUTPUT_PATH = Path("data/raw_users.json")

def fetch_users():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    return response.json()

def save_raw_data(data, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        
def main():
    users = fetch_users()
    save_raw_data(users, RAW_OUTPUT_PATH)
    print(f"Saved raw data to {RAW_OUTPUT_PATH}")
    
if __name__ == "__main__":
    main()