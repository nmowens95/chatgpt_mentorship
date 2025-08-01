import snowflake.connector
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def snowflake_conn():
    try:
        conn = snowflake.connector.connect(
            user=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD"),
            account=os.getenv("ACCOUNT"),
            warehouse=os.getenv("WAREHOUSE"),
            database=os.getenv("DATABASE"),
            schema=os.getenv("SCHEMA"),
            role=os.getenv("ROLE")
        )
        print("Connection successful")
        return conn
    
    except Exception as e:
        print(f"Error connecting to Snowflake, error: {e}")
        sys.exit(1)