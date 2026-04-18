import argparse #enables creating CLIs
import csv #light-weight version of pandas for using csv files
import sqlite3
from pathlib import Path #allows for oop

DB_FILE = "analytics.db"

REPORT_QUERIES = {
    "orders_with_customers": """
       SELECT
           o.order_id,
           c.cusotmer_name,
           o.order_date,
           o.quantity
        FROM orders o
        JOIN customer c
            ON o.customer_id = c.customer_id
        ORDER BY o.order_id    
    """,
    "orders_with_products": """
        SELECT
            o.order_id,
            p.product_name,
            p.category,
            o.quantity,
            o.oder_date
        FROM orders o
        JOIN products p
            ON o.product_id = p.product_id
        ORDER BY o.order_id
    """,
        "full_order_details": """
        SELECT
            o.order_id,
            c.customer_name,
            p.product_name,
            o.quantity,
            o.order_date
        FROM orders o
        JOIN customer c
            ON o.customer_id = c.customer_id
        JOIN products p
            ON o.product_id = p.product_id
        ORDER BY o.order_id
    """
}

def run_query(query: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute(query)
    rows = cursor.fetchall() #retrieve all records from query result
    headers = [description[0] for description in cursor.description] #retrieve column names
    
    conn.close()
    return headers, rows

def print_report(headers, rows):
    print(" | ".join(headers)) #takes headers, created single formatted string pipe delimited - creates clean, column separated output
    print("-" * 60) #will print 60 hyphens to create a line
    
    for row in rows:
        print (" | ".join(str(value) for value in row))
        
def export_to_csv(headers, rows, output_file):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True) #create file folder to store report output
    
    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)
    
    print(f"Report exported to {output_path}")
    
def main():
    parser = argparse.ArgumentParser(description="Run SQL reports from the sales database.")
    parser.add_argument(
        "--report",
        choices=REPORT_QUERIES.keys(),
        default="full_order_details",
        help="Select which report to run"
        )
    parser.add_argument(
        "--output",
        help="Optional path to export the report as CSV"
        )
    
    args = parser.parse_args() #processes input provided by user in terminal

    query = REPORT_QUERIES[args.report]
    headers, rows = run_query(query)

    print_report(headers, rows)

    if args.output:
        export_to_csv(headers, rows, args.output)
        
if __name__ == "__main__":
    main()


