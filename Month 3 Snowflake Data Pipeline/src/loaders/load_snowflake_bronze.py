import pandas as pd
from src.logger.logger_config import setup_logger
from src.connectors.snowflake_connector import snowflake_conn

logger = setup_logger()

TABLE_REGISTRY = {
    "claims": "healthcare.raw.claims", 
    "providers": "healthcare.raw.providers",
    "procedures": "healthcare.raw.procedures",
    "customers": "healthcare.raw.customers"
}

# def insert_df_to_snowflake_table(df, file_name):
#     if file_name in TABLE_REGISTRY:
#         TABLE_REGISTRY[file_name]

def load_to_snowflake(df: dict, file_name, conn):
    table = TABLE_REGISTRY[file_name]
    try:
        with conn.cursor() as cursor:
            rows = [tuple(None if pd.isna(x) else x for x in row) for _, row in df.iterrows()]
            columns = ", ".join(df.columns)
            placeholders = ", ".join(['%s'] * len(df.columns))

            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.executemany(sql, rows)
            conn.commit()

        print(f"Data inserted into {table}")
        logger.info(f"Successfully inserted {len(df)} rows into {table}")
        
    except Exception as e:
        logger.error(f"Unable to load data from: {file_name}, error: {e}")