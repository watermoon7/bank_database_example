import sqlite3 as sql
import random

with open("data/first-names.txt", 'r') as f:
    first_names = f.read().split('\n')
with open("data/first-names.txt", 'r') as f:
    middle_names = f.read().split('\n')
with open("data/first-names.txt", 'r') as f:
    last_names = f.read().split('\n')
with open("data/street-addresses.txt", 'r') as f:
    addresses = [i.strip().rstrip('Ê') for i in f.read().split('\n')]

account_types = ['Current', 'Savings', 'Checking']


def generate_name():
    return f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"


def generate_accounts(transaction):
    for _ in range(100):
        transaction.execute(f"""
            INSERT INTO Customer (name, address)
            VALUES (
                '{generate_name()}', 
                '{random.choice(addresses)}'    
            )
        """)
        id_ = transaction.execute("""SELECT MAX(customer_id) FROM Customer""")
        transaction.execute(f"""
            INSERT INTO Account (balance, account_type, interest, customer_id)
            VALUES (
                {random.randint(0, 1000000) / 100},
                '{random.choice(account_types)}',
                {random.randint(5, 60) / 1000},
                {id_.fetchone()[0]}
            )
        """)


def reset_db():
    conn = sql.connect('database.db')
    transaction = conn.cursor()

    query = transaction.execute
    query("""DROP TABLE Customer""")
    query("""DROP TABLE Account""")
    query("""
            CREATE TABLE Customer(
                customer_id INTEGER NOT NULL PRIMARY KEY,
                name TEXT,
                address TEXT
            )
        """)

    query("""
        CREATE TABLE Account(
            account_number INTEGER NOT NULL PRIMARY KEY,
            balance REAL DEFAULT 0.00,
            account_type TEXT DEFAULT 'Current',
            interest REAL DEFAULT 0.01,
            customer_id INTEGER,
            FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)
        )
    """)

    generate_accounts(transaction)

    conn.commit()


reset_db()
