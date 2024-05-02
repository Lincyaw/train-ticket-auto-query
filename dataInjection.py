import random
import mysql.connector

# Generate random data
data = []
for _ in range(5):
    id = random.randint(1, 100)
    beyond_price = random.uniform(10, 100)
    idx = random.randint(1, 10)
    initial_price = random.uniform(50, 200)
    initial_weight = random.uniform(1, 10)
    within_price = random.uniform(5, 50)
    data.append((id, beyond_price, idx, initial_price, initial_weight, within_price))

# Connect to the MySQL database
# Replace the placeholders with your actual database connection details
conn = mysql.connector.connect(
    host='10.10.10.201',
    port=32124,
    user='root',
    password='yourpassword',
    database='ts'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()


# # Construct the SQL query
# sql = "INSERT INTO consign_price (id, beyond_price, idx, initial_price, initial_weight, within_price) VALUES (%s, %s, %s, %s, %s, %s)"
# Construct the SQL query
sql = "INSERT INTO consign_price (id, beyond_price, idx, initial_price, initial_weight, within_price) VALUES "
values = ', '.join([f"({id}, {beyond_price}, {idx}, {initial_price}, {initial_weight}, {within_price})" for (id, beyond_price, idx, initial_price, initial_weight, within_price) in data])
sql += values + ";"


# Execute the SQL query for each data row
cursor.executemany(sql, data)


# Commit the changes to the database
conn.commit()


# Close the cursor and connection
cursor.close()
conn.close()