import subprocess #allows usage of external programs, shell commands, and apps
import sys
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if len(sys.argv) < 2:
    print ("Usage: python rune_pipeline.py <input.csv>")
    sys.exit(1)
    
input_csv = sys.argv[1]
cleaned_csv = "cleaned_" + os.path.basename(input_csv)
database_name = "pipeline.db"
table_name = "sales"
report_csv = "pipeline_report.csv"

logging.info("Starting pipeline...")
logging.info("Step 1: Extract and Transform")
subprocess.run(["python", "extract_transform.py", input_csv, cleaned_csv], check=True)
logging.info("Step 2: Load to Database")
subprocess.run(["python", "load_db.py", cleaned_csv, database_name, table_name], check=True)
logging.info("Step 3: Generate Report")
subprocess.run(["python", "report.py", database_name, table_name, report_csv], check=True)
logging.info("Pipeline completed successfully")

print("\nPipeline completed successfully")