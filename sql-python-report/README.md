\# SQL PYTHON REPORT



A small python project that connects to a SQLite db, runs aggregation query, exports results to CSV.



\## Tools Used

&#x20;- Python using pandas

&#x20;- SQLite



\## Functionality

&#x20;- Connects to SQLite database

&#x20;- Aggregates sales by product

&#x20;- Sorts products by total sales, descending

&#x20;- Exports results to sales\_report.csv



\## Files

&#x20;- setup\_db.py - creates sample db and loads sample data

&#x20;- app.py - runs the SQL query and exports results

&#x20;- sales.db - SQLite database

&#x20;- sales\_report.csv - generated report output



\## How to Run

Setup the sample database:

&#x20;python setup\_db.py

Run the report:

&#x20;python app.py

