import pandas as pd #imports pandas, alias of pd for function calls
import sys #gives python system access, extra variables
import os #allows scripts to interact directly with operating system
from cleaner.processor import load_csv, clean_data, save_csv #import

#Define overall function to utilize processor.py, app.py
def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]


    if len(sys.argv) >= 3:
       output_file = sys.argv[2]
    else:
       output_file = "cleaned_" + os.path.basename(input_file) #updated to stop non-existent directory error

    try:
       df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    print("Original data:")
    print(df.head())

    cleaned_df, metrics = clean_data(df)
    print("\nCleaning summary:")
    print(f"Original rows: {metrics['original_rows']}")
    print(f"Duplicates removed: {metrics['duplicates_removed']}")
    print(f"Rows with missing values removed: {metrics['rows_with_missing_removed']}")
    print(f"Final rows: {metrics['final_rows']}")
    save_csv(cleaned_df, output_file)

    print(f"\nCleaned file saved as {output_file}")

#Only run main() if the file is being executed, not upon import
#__name__ is native python variable
if __name__ == "__main__":
    main()