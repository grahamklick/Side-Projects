import pandas as pd #imports pandas DA tools, sets pd as alias for calling

#Load CSV
df = pd.read_csv("data.csv")

print("Original data:")
print(df)

#Clean data
df = df.drop_duplicates()
df = df.dropna()

print("\nCleaned data:")
print(df)

#Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print ("\nSaved cleaned_data.csv")