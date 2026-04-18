# sql-analytics-multi-table
A small SQL + Python portfolio project that loads sample data into a SQLite database and generates reports using multi-table joins.

# What it does
This project demonstrates how to:
 - create a relational database with SQLite
 - load CSV data into multiple related tables
 - write SQL queries with joins across tables
 - generate simple reports from Python

# Files
 - setup_db.py creates the SQLite database and tables
 - load_data.py loads CSV data into the database
 - report.py runs SQL queries and prints joined report results

# To Run
 - python setup_db.py
 - python load_data.py
 - python report.py

# Example reports
This project includes examples of joined SQL reports such as:
 - orders with customer names
 - orders with product details
 - summary-style reporting across multiple tables

# Skills demonstrated
 - Python
 - SQLite
 - SQL joins
 - CSV data loading
 - basic data pipeline structure
 - portfolio-friendly project organization

# Future improvements
 - add filtering through CLI arguments
 - export reports to CSV
 - add logging
 - add validation checks before loading
 - add unit tests