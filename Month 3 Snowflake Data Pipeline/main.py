from src.connectors.snowflake_connector import snowflake_conn
from src.extractors.extract_files import read_unprocessed_files
from src.loaders.load_snowflake_bronze import load_to_snowflake
from src.logger.logger_config import setup_logger

logger = setup_logger()

def main():
    unprocessed_dir = "./data/unprocessed" # Make into a passed argument
    conn = snowflake_conn()
    dfs = read_unprocessed_files(unprocessed_dir)

    for file_name, df in dfs.items():
        try:
            load_to_snowflake(df, file_name, conn)
            logger.info(f"{file_name} data successfully loaded to Snowflake")
        except Exception as e:
            logger.error(f"Error in loading data: {e}")
    
    conn.close()
    logger.info("Connection closed")
    logger.info(f"Pipeline to snowflake has finished!")

if __name__ == "__main__":
    main()