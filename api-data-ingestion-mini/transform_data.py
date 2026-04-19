import json
from pathlib import Path
import pandas as pd

RAW_INPUT_PATH = Path("data/raw_users.json")
CLEAN_OUTPUT_PATH = Path("output/clean_users.csv")

def load_raw_data(input_path):
    with open(input_path, "r", encoding="utf-8") as file: #opens file for reading
        return json.load(file)
    
def transform_users(users):
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
        
    return pd.DataFrame(cleaned_rows)

def save_clean_data(df, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=-True)
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")
    
def main():
    users = load_raw_data(RAW_INPUT_PATH)
    df = transform_users(users)
    save_clean_data(df, CLEAN_OUTPUT_PATH)
    print(df.head())
    
if __name__ == "__main__":
    main()
    