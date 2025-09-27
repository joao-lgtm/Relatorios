import sqlite3
import pandas as pd

def sql(query, db_path="db.sqlite3"):
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(query, conn)