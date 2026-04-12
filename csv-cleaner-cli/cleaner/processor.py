#Moving logic into a processor file vs. single script
import pandas as pd

#create file load function that accepts a file path
#read csv passed
def load_csv(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)