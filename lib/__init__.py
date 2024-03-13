# lib/config.py
import sqlite3

# CONN is a constant equal to a hash that contains a connection to the database.
CONN = sqlite3.connect('company.db')

# CURSOR is a constant that allows us to interact with the database and execute SQL statements.
CURSOR = CONN.cursor()
