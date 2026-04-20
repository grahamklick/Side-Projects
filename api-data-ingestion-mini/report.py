import argparse
import csv
import sqlite3
from pathlib import Path

DB_FILE = "analytics.db"

REPORT_QUERIES = {
        "all_users": """
        SELECT
            id,
            name,
            username,
            email,
            city,
            company_name
        FROM users
        ORDER BY id
    """,
    "users_by_city": """
        SELECT
            city,
            COUNT(*) AS user_count
        FROM users
        GROUP BY city
        ORDER BY user_count DESC, city
    """,
    "company_list": """
        SELECT
            id,
            name,
            company_name,
            company_bs
        FROM users
        ORDER BY company_name, name
    """
}

def run_query(query):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute(query)
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    
    conn.close()
    return headers, rows

def print_report(headers, rows):
    print(" | ".join(headers))
    print("-" * 80)

    for row in rows:
        print(" | ".join(str(value) for value in row))
        
def export_to_csv(headers, rows, output_file):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"Report exported to {output_path}")
    
def main():
    parser = argparse.ArgumentParser(description="Run SQL reports on API-ingested user data.")
    parser.add_argument(
        "--report",
        choices=REPORT_QUERIES.keys(),
        default="all_users",
        help="Select which report to run"
    )
    parser.add_argument(
        "--output",
        help="Optional path to export the report of CSV"
    )
    
    args = parser.parse_args()

    query = REPORT_QUERIES[args.report]
    headers, rows = run_query(query)

    print_report(headers, rows)

    if args.output:
        export_to_csv(headers, rows, args.output)
    
if __name__ == "__main__":
    main()