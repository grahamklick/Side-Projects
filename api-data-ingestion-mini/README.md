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

# Reporting
 - run default report: python report.py
 - run grouped by city: python report.py --report users_by_city
 - export to a csv: python report.py --report company_list --output reports/company_list.csv