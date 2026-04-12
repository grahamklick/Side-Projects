import pandas as pd

#replaced prior sample data with data from external csv
df = pd.read_csv("raw_sales.csv")

#display initial data
print("Raw data:")
print(df)

#clean data
df = df.drop_duplicates()
df = df.dropna()

#display cleaned data
print("\nCleaned data:")
print(df)

#save cleansed output
df.to_csv("cleaned_sales.csv", index=False)  #index=False restricts column/row numbers from being in output
print("\nSaved cleaned_sales.csv")