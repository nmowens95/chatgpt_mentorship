import pandas as pd
from src.pipeline.transform_to_silver import bronze_to_silver
from src.pipeline.load_to_postgres import load_gold_to_postgres
from src.utils.logger_config import logger_setup

logger = logger_setup()

def main():
    try:
        logger.info("Pipeline starting...")
        bronze_to_silver("data/bronze")
        load_gold_to_postgres("data/silver")
    except Exception as e:
        logger.error(f"Error in pipeline {e}")
    finally:
        logger.info("Pipeline complete!")

if __name__ == "__main__":
    main()
