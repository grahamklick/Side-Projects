import pandas as pd
import sys
import os

#validate >= 2 arguments or prompt reminder and exit
#run in terminal like: python extract_transform.py raw_sales.cv --- runs the .py file, using the raw_sales.csv file = 2 arguments
if len(sys.argv) < 2:
    print("Usage: python extract_transform.py <input_file> [output_file]")
    sys.exit(1)
    
input_file = sys.argv[1]

if len(sys.argv) >= 3:
    output_file = sys.argv[2]
else:
    output_file = "cleaned_" + os.path.basename(input_file) # using os.path to overcome file folder issues experienced in earlier projects

#Load Data
df = pd.read_csv(input_file) #replaced hard coded file name, now can find based on input file provided, test using the raw_sales csv

print("Raw data:")
print(df)

#clean data
df = df.drop_duplicates()
df = df.dropna()

#display cleaned data
print("\nCleaned data:")
print(df)

#save cleansed output
df.to_csv(output_file, index=False)  #index=False restricts column/row numbers from being in output
print("\nSaved cleaned_sales.csv")