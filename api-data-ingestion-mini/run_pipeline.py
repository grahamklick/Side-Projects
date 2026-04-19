from fetch_data import fetch_users, save_raw_data, RAW_OUTPUT_PATH
from transform_data import transform_users, save_clean_data, CLEAN_OUTPUT_PATH

def main():
    users = fetch_users()
    save_raw_data(users, RAW_OUTPUT_PATH)
    
    df = transform_users(users)
    save_clean_data(df, CLEAN_OUTPUT_PATH)
    
    print("Pipeline completed successfully.")
    
if __name__ == "__main__":
    main()