import pandas as pd #imports pandas DA tools, sets pd as alias for calling

df = pd.DataFrame ({
	"name": ["Alice", "Bob", "Bob", None],
	"age": [25, 30, 30, 22],
	"city": ["St. Louis", "Chicago", "Chicago", "Dallas"]
})

print("Original data:")
print(df)

df = df.drop_duplicates()
df = df.dropna()

print("\nCleaned data:")
print(df)

df.to_csv("cleaned_data.csv", index=False)
print("\nSaved cleaned_data.csv")