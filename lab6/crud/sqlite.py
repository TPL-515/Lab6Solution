from dagster import asset, get_dagster_logger, Output
import sqlite3
from pathlib import Path
from datetime import datetime
import random
import pandas as pd
# Get our Logger
logger = get_dagster_logger()

# Get our sql session
db = Path('database.db')
con = sqlite3.connect(db)
cursor = con.cursor()



import sqlite3
from pathlib import Path
import pandas as pd
# Get our sql session
db = Path('database.db')
con = sqlite3.connect(db)
cursor = con.cursor()

def create_table():
    create_table_text = """CREATE TABLE IF NOT EXISTS demods (
        feature1 real NOT NULL,
        feature2 real NOT NULL, 
        label integer NOT NULL
    )"""

    cursor.execute(create_table_text)

def get_table_meta():
    cursor.execute("SELECT * FROM demods")
    dat = cursor.fetchall()
    cols = ['feature1', 'feature2', 'label']
    df = pd.DataFrame(dat, columns=cols)
    nrows = df.shape[0]
    ncols = df.shape[1]
    return nrows, cols, cols

def add_data(data):
    cursor.executemany("INSERT INTO demods VALUES(?, ?, ?)", data)
    con.commit()
    con.close()

def remove_data(tablename):
    cursor.execute(f'DELETE FROM {tablename}')
    con.commit()
    con.close()

def read_data():

    cursor.execute("SELECT * FROM demods")
    dat = cursor.fetchall()
    df = pd.DataFrame(dat, columns=['feature1', 'feature2', 'label'])

    return df
