import yaml
import psycopg2
from src.utils.logger_config import logger_setup
import sys
import pandas as pd
from pathlib import Path

logger = logger_setup()

def load_db_config(path="config/postgres.yml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
        logger.info(f"Successfully read config file: {config}")
    return config

def get_pg_connection():
    config = load_db_config()["Postgres"]

    try:
        conn = psycopg2.connect(
            host=config["host"],
            port=config["port"],
            database=config["database"],
            user=config["user"],
            password=config["password"]
        )
        logger.info(f"Connection success")
        return conn
    
    except Exception as e:
        logger.error(f"Unable to connect to postgres: {e}")
        sys.exit(1)

def run_sql_file(cursor, filepath: str):
    logger.info(f"Executing SQL script: {filepath}")
    with open(filepath, "r") as f:
        sql = f.read()
        cursor.execute(sql)

TABLE_REGISTRY = {
    "claims_silver": "claims_gold",
    "customers_silver": "customers_gold"
}

def insert_csv_to_table(conn, csv_path: str, table_name: str):
    df = pd.read_csv(csv_path)
    logger.info(f"Loaded DataFrame with shape {df.shape} from {csv_path}")

    if table_name == "claims_gold":
        if df["claim_id"].isna().any():
            raise ValueError("Primary key 'claim_id' has null values")
        if df["customer_id"].isna().any():
            raise ValueError("Foreign key 'customer_id' has null values")
        if df["claim_id"].duplicated().any():
            raise ValueError("Duplicate 'claim_id found")
        
    elif table_name == "customers_gold":
       if df["customer_id"].isna().any():
            raise ValueError("Foreign key 'customer_id' has null values")
       if df["customer_id"].duplicated().any():
            raise ValueError("Duplicate 'customer_id' values found.")

    else:
        logger.info(f"{table_name} not accounted for")

    logger.info(f"Inserting {len(df)} rows from {csv_path.name} into {table_name}")

    with conn.cursor() as cursor:
        # Step 1: Create tables
        try:
            run_sql_file(cursor, "sql/gold/create_claims_gold.sql")
            run_sql_file(cursor, "sql/gold/create_customers_gold.sql")
            logger.info("Tables already exist, or were created")
            conn.commit()
        except Exception as e:
            logger.error(f"Tables were not created: {e}")
        
        for _, row in df.iterrows():
            columns = ", ".join(df.columns)
            placeholders = ", ".join(['%s'] * len(row))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(None if pd.isna(x) else x for x in row))
        conn.commit()

def load_gold_to_postgres(file_dir: str, conn):
    file_dir = Path(file_dir)
    logger.info(f"CSV files found in {file_dir}: {[f.name for f in file_dir.glob('*.csv')]}")

    try:
        for file in file_dir.glob("*.csv"):
            if file.stem in TABLE_REGISTRY:
                table = TABLE_REGISTRY[file.stem]
                insert_csv_to_table(conn, file, table)
                logger.info(f"Successfully loaded: {file.stem} to {table}")
        
        logger.info(f"All data has been processed")

    except Exception as e:
        import traceback
        logger.error(f"Error when loading data from file {file}: {e}")
        logger.error(traceback.format_exc())

    finally:
        conn.close()
        logger.info("Postgres connection closed")

if __name__ == "__main__":
    file_dir = Path("data/silver")
    conn = get_pg_connection()

    try:
        load_gold_to_postgres(file_dir, conn)
        logger.info("Load success")
    
    except Exception as e:
        logger.error(f"Error in loading data: {e}")