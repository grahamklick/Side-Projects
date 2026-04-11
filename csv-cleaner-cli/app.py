import pandas as pd #imports pandas, alias of pd for function calls
import sys #gives python system access, extra variables
import os #allows scripts to interact directly with operating system

#Determine total number of command-line arguments, including the script name. 
#Exit if the script is the only argument passed.
if len(sys.argv) < 2:
    print("Usage: python app.py <input_file> [output_file]")
    sys.exit(1)

#Capture filename or path being passed
input_file = sys.argv[1]

# Optional output file
if len(sys.argv) >= 3:
   output_file = sys.argv[2]
else:
   output_file = "cleaned_" + os.path.basename(input_file) #updated to stop non-existent directory error

# Attempt to read the file, if none present error & exit application
try:
     df = pd.read_csv(input_file)
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

#Print first N (default 10) rows of original data
print("Original data:")
print(df.head())

#Drop duplicate rows, rows with missing column data
df = df.drop_duplicates()
df = df.dropna()

output_file = output_file = "cleaned_" + os.path.basename(input_file) #updated to stop non-existent directory error
df.to_csv(output_file, index=False)

print(f"\nCleaned file saved as {output_file}")