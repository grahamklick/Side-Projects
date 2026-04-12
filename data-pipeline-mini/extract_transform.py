import pandas as pd

#sample raw data
df = pd.DataFrame({
    "customer": ["Alice", "Bob", "Bob", None, "Eve"],
    "product": ["Laptop", "Mouse", "Mouse", "Keyboard", "Monitor"],
    "amount": [1200, 25, 25, 75, None]
    })

print("Raw data:")
print(df)

#clean data
df = df.drop_duplicates()
df = df.dropna()

print("\nCleaned data:")
print(df)

#save cleansed output
df.to_csv("cleaned_sales.csv", index=False)  #index=False restricts column/row numbers from being in output
print("\nSaved cleaned_sales.csv")