# Data Pipeline Mini
A simple end-to-end data pipeline project built with Python, pandas, and SQLite.

## What It Does
 1. Reads raw sales data from a CSV file
 2. Cleans the data by removing duplicates and missing values
 3. Saves cleaned data to a new CSV
 4. Loads cleaned data into SQLite
 5. Runs a SQL query to generate a report
 6. Exports the report to CSV

## Files
 - raw_sales.csv - raw input data
 - extract_transform.py - reads and cleans the raw CSV
 - load_db.py - loads cleaned CSV data into SQLite
 - report.py - queries the SQLite database and exports a report
 - run_pipeline.py - runs the full pipeline end-to-end
 - cleaned_sales.csv or custom output - cleaned intermediate data
 - pipeline.db - SQLite database
 - pipeline_report.csv - final report output

## Tools Used
 - Python
 - pandas
 - SQLite

## How to Run
python run_pipeline.py raw_sales.csv
or, manually:
python extract_transform.py raw_sales.csv
python load_db.py cleaned_raw_sales.csv
python report.py pipeline.db