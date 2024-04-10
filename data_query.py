# Define SQL query to select data
select_query = """
SELECT * FROM campaign_performance;
"""

# Execute SQL query to select data
with conn.cursor() as cur:
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
