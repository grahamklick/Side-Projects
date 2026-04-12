#Moving logic into a processor file vs. single script
import pandas as pd

#create file load function that accepts a file path
#read csv passed
def load_csv(file_path):
    return pd.read_csv(file_path)

#Count original rows, rows after de-dupe, rows after na removed
def clean_data(df):
    original_rows = len(df)

    df = df.drop_duplicates()
    after_duplicates = len(df)

    df = df.dropna()
    final_rows = len(df)

   #log above file metrics
    metrics = {
       "original_rows": original_rows,
       "duplicates_removed": original_rows - after_duplicates,
       "rows_with_missing_removed": after_duplicates - final_rows,
       "final_rows": final_rows,
    }

    return df, metrics

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)