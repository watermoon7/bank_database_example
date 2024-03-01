import sqlite3 as sql
from reset import reset_db

conn = sql.connect('database.db')
transaction = conn.cursor()


# Function to reset the database by deleting tables and recreating them
def reset_database():
    reset_db()


# Function to add a new customer to the database
def add_customer(name, address):
    transaction.execute(f"""
        INSERT INTO Customer (name, address)
        VALUES (
            '{name}', 
            '{address}'    
        )
    """)
    conn.commit()


# Function to remove a customer from the database
def remove_customer(customer_id):
    transaction.execute(f"""
        DELETE
        FROM Customer
        WHERE account_id = {customer_id}
    """)
    conn.commit()


# Function to update customer information in the database
def update_customer(customer_id, new_name, new_address):
    transaction.execute(f"""
        UPDATE Customer 
        SET name = {new_name}, address = {new_address}
        WHERE customer_id = {customer_id}
    """)
    conn.commit()


# Function to open a new bank account for a customer
def open_account(initial_balance, account_type, interest, customer_id):
    transaction.execute(f"""
        INSERT INTO Account (balance, account_type, interest, customer_id)
        VALUES (
            {initial_balance},
            '{account_type}',
            {interest},
            {customer_id}
        )
    """)
    conn.commit()


# Function to close an existing bank account
def close_account(account_number):
    transaction.execute(f"""
        DELETE
        FROM Account
        WHERE account_number = {account_number}
    """)
    conn.commit()


# Function to withdraw funds from a bank account
def withdraw(account_number, amount):
    transaction.execute(f"""SELECT * FROM Account WHERE account_number = {account_number}""")
    balance = transaction.fetchone()[0]
    if amount > balance:
        print(f"Cannot withdraw this amount. Current balance: £{balance}")
    else:
        new_balance = balance - amount
        transaction.execute(f"""UPDATE * FROM Account WHERE account_number = {account_number}""")
    conn.commit()


# Function to deposit funds into a bank account
def deposit(account_number, amount):
    pass


# Function to transfer funds between two bank accounts
def transfer(from_account_number, to_account_number, amount):
    pass
