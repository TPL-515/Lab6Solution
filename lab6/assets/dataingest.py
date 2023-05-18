from dagster import asset, get_dagster_logger, Config, Output
from datetime import datetime
from lab6.crud.sqlite import *
import random
import pandas as pd
# Get our Logger
logger = get_dagster_logger()

class IngestDataConfig(Config):
    nrows: int = 20

@asset(description="This checks if our table exists")
def create_demo_table():
    logger.info('Create table if it does not exist within our database')
    try:
        create_table()
    except Exception as e:
        logger.error('Had issues with creating the table in the database')
        logger.error(e)

@asset(description="Return metadata for the database before")
def display_table_before(create_demo_table):
    logger.info('Getting the meta data for our database before adding')
    try:
        nrows, ncols, cols = get_table_meta()
        logger.info(f'The table has {nrows} rows\nThe table has {ncols} columns')
    except Exception as e:
        logger.error('Failed to get the table metadata')
        logger.error(e)
    return Output(None, metadata={"num_rows": nrows, "num_cols": ncols, "columns": cols})

@asset(description="This allows the user to read the data from within the table")
def pull_data(display_table_before):

    logger.info('Pulling the data from the table.')
    df = read_data()
    logger.info(f'Pulled {df.shape[0]} rows from the data table')

    return df

@asset(description="This ingests an example bit of data into the database")
def ingest_data(pull_data, config: IngestDataConfig):
    
    # Set our default random data bounds
    f1lowerbound = 10
    f1upperbound = 20
    f2lowerbound = 20
    f2upperbound = 40

    drift = 0
    nrows = pull_data.shape[0]

    # Generate some data drift
    if nrows > 50 and nrows <= 100:
        logger.info('Drift is 2')
        drift = 2
    if nrows > 100 and nrows <= 150:
        logger.info('Drift is 4')
        drift = 4
    if nrows > 150 and nrows <= 200:
        logger.info('Drift is 8')
        drift = 8
    if nrows > 200:
        logger.info('Drift is 16')
        drift = 16

    # Create our data
    data = []
    for i in range(config.nrows):
        if i < config.nrows // 2:
            f1 = random.uniform(f1lowerbound+drift, f1upperbound+drift)
            f2 = random.uniform(f2lowerbound+drift, f2upperbound+drift)
            label = 0
        else:
            f1 = random.uniform(f1lowerbound-drift, f1upperbound-drift)
            f2 = random.uniform(f2lowerbound-drift, f2upperbound-drift)
            label = 1
        data.append((f1, f2, label))

    logger.info(f'Injesting {len(data)} rows into the database')
    try:
        add_data(data)
    except Exception as e:
        logger.error('Failed to ingest data into the database')
        logger.error(e)

@asset(description="Return metadata for the database after")
def display_table_after(ingest_data):
    logger.info('Getting the meta data for our database after adding')
    try:
        nrows, ncols, cols = get_table_meta()
        logger.info(f'The table has {nrows} rows\nThe table has {ncols} columns')
    except Exception as e:
        logger.error('Failed to get the table metadata')
        logger.error(e)
    return Output(None, metadata={"num_rows": nrows, "num_cols": ncols, "columns": cols})

@asset(description="This allows the user to delete all the data from the database")
def clear_table():
    logger.info('Deleting all data from the database.')
    try:
        remove_data('demods')
    except Exception as e:
        logger.error('Failed to clear the database')
        logger.error(e)
