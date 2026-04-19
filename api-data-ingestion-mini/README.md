# api-data-ingestion-mini
A small Python data pipeline project

# What It Does
 - fetches data from public API
 - saves raw API out
 - transforms nested JSON into tabular data
 - exports cleaned results to CSV

# Requirements
Install dependies: pip install requests pandas

# Usage
 - fetch raw data: python fetch_data.py
 - transform raw data: python transform_data.py
 - run pipeline: python run_pipeline.py

# Output Columns:
 - id
 - name
 - username
 - email
 - phone
 - website
 - city
 - zip
 - company name