import psycopg2

# Connect to Amazon Redshift cluster
conn = psycopg2.connect(
    dbname='your_database_name',
    user='your_username',
    password='your_password',
    host='your_redshift_host',
    port='your_redshift_port'
)

# Define SQL query to create table
create_table_query = """
CREATE TABLE campaign_performance (
    campaign_id INT,
    impressions INT,
    clicks INT,
    conversions INT,
    revenue FLOAT,
    date DATE
);
"""

# Execute SQL query to create table
with conn.cursor() as cur:
    cur.execute(create_table_query)
    conn.commit()

# Define SQL query to insert data
insert_query = """
INSERT INTO campaign_performance (campaign_id, impressions, clicks, conversions, revenue, date)
VALUES (%s, %s, %s, %s, %s, %s);
"""

# Example data
data = [(1, 1000, 50, 10, 500.00, '2024-04-10'),
        (2, 1500, 75, 15, 750.00, '2024-04-10')]

# Execute SQL query to insert data
with conn.cursor() as cur:
    cur.executemany(insert_query, data)
    conn.commit()
