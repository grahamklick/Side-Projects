# Data Pipeline Project

A simple end-to-end data pipeline project built with Python, pandas and SQlite

## What It Does
 1. Creates raw sales data, cleans it of dupes and nulls
 2. Saves cleaned data to CSV
 3. Loads cleaned data into SQlite
 4. Runs a SQL query to generate a report
 5. Exports the report to CSV

## Files
 - extract_transform.py - creates and cleans sample sales data
 - load_db.py - loads cleaned CSV data into SQLite
 - report.py - queries the SQLite database and exports a report
 - cleaned_sales.csv - cleaned intermediate data
 - pipeline.db - SQLite database
 - pipeline_report.csv - final report output

## Tools Used
 - Python
 - pandas
 - SQLite

## How to Run
 - python extract_transform.py
 - python load_db.py
 - python report.py