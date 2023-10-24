```python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Establish a connection to the database
def connect_to_db():
    conn = psycopg2.connect(
        dbname="emailmaster_scheduler",
        user="admin",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn

# Function to create a new shard
def create_shard(shard_name):
    conn = connect_to_db()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {shard_name};")
    cursor.close()
    conn.close()

# Function to distribute data across shards
def distribute_data(shard_names, data):
    for shard_name, shard_data in zip(shard_names, data):
        conn = psycopg2.connect(
            dbname=shard_name,
            user="admin",
            password="password",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        for query in shard_data:
            cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

# Function to create indexes for faster query responses
def create_indexes(table_name, column_names):
    conn = connect_to_db()
    cursor = conn.cursor()
    for column_name in column_names:
        cursor.execute(f"CREATE INDEX idx_{table_name}_{column_name} ON {table_name}({column_name});")
    conn.commit()
    cursor.close()
    conn.close()

# Example usage
if __name__ == "__main__":
    shard_names = ["shard1", "shard2", "shard3"]
    for shard_name in shard_names:
        create_shard(shard_name)

    data = [
        ["INSERT INTO users VALUES(1, 'John Doe', 'john.doe@example.com');"],
        ["INSERT INTO users VALUES(2, 'Jane Doe', 'jane.doe@example.com');"],
        ["INSERT INTO users VALUES(3, 'Bob Smith', 'bob.smith@example.com');"]
    ]
    distribute_data(shard_names, data)

    create_indexes("users", ["email"])
```