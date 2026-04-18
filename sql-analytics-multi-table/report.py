import sqlite3
import pandas as pd

conn = sqlite3.connect("analytics.db")

#Report #1 - customer & product detail
query_1 = """
SELECT
    c.customer_name,
    p.product_name,
    SUM(o.quantity) AS total_quantity,
    SUM(o.quantity * p.price) AS total_spent
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_name, p.product_name
ORDER BY total_spent DESC
"""

df_detail = pd.read_sql_query(query_1, conn)

print("Customer Purchase Detail Report:")
print(df_detail)

df_detail.to_csv("customer_purchase_report.csv", index=False)
print("\nSaved customer_purchase_report.csv")

#Report #2 - Total spend by Customer
query_2 = """
SELECT
    c.customer_name,
    SUM(o.quantity * p.price) AS total_spent
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
"""

df_summary = pd.read_sql_query(query_2, conn)

print("Customer Spending Summary:")
print(df_summary)

df_summary.to_csv("customer_spending_summary.csv", index=False)
print("\nSaved customer_spending_summary.csv")

conn.close()