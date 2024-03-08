import sqlite3
import pandas as pd

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def get_data(query,conn):
    df1 = pd.read_sql_query(query,conn)
    return df1

def preparation(df):
    df=df.dropna()
    return df