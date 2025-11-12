# OOP Lab 3 – Multi-Table Data Processing and Database Simulation

📦 Overview

This project demonstrates basic data manipulation using object-oriented programming (OOP) concepts.
It provides three main classes:

DataLoader — loads CSV files into Python lists of dictionaries

Table — represents a dataset and supports operations like filter, aggregate, and join

DB — a lightweight in-memory database for storing and retrieving tables by name

The main script loads Cities.csv and Countries.csv, then performs several queries.

🗂 Project Structure
.
├─ main.py                # Contains all classes and test script
├─ Cities.csv
└─ Countries.csv

🧠 How It Works
1. DataLoader

Loads a CSV file and returns its content as a list of dictionaries.

loader = DataLoader()
cities = loader.load_csv('Cities.csv')


If base_path is not specified, it defaults to the current file’s directory.

2. DB

Stores multiple Table objects in a dictionary.

my_DB = DB()
my_DB.insert(Table('cities', cities))
my_DB.insert(Table('countries', countries))

table = my_DB.search('cities')


insert(table) — adds a Table object to the database

search(name) — retrieves a table by name

3. Table

Encapsulates data operations for a single table.

Methods

filter(condition) — returns a new table containing rows that satisfy a lambda condition

aggregate(func, column) — applies an aggregation function (like sum, len, min, etc.) to a column

join(other_table, key) — performs an inner join on a common key column

__str__() — readable string representation of the table

⚙️ Key Features

No external dependencies — only Python standard library

Immutable-style filter() (does not modify the original table)

Nested-loop join between two tables

Simple aggregation on numeric columns

⚠️ Notes

aggregate() automatically tries to convert values to float. If conversion fails, it uses the raw string.

join() is a basic O(n×m) nested loop join — fine for small datasets but not optimized for large data.

Make sure your CSV column names match exactly (country, EU, coastline, temperature, etc.).

🧩 Possible Improvements

Add select(columns) and groupby() functions

Support for left/right/outer joins

Schema validation and data type checking

Integration with pandas or SQLite for larger datasets