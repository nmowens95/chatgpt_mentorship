import pandas as pd
import os
from .logger_config import logger_setup

logger = logger_setup()

def extract_file(dir_path: str) -> list:
    try:
        # Set up a path to read the directory files
        files = os.listdir(dir_path)

        if not files:
            logger.warning(f"No files found in directory {files}")

        # Loop over to grab each file
        dataframes = []
        for file in files:
            if file.lower().endswith(".csv"):
                file = os.path.join(dir_path, file)
                file_name = os.path.basename(file)
                df = pd.read_csv(file)
                dataframes.append((df, file_name))
                logger.info(f"{file} successfully read into a dataframe!")
        return dataframes
    
    except Exception as e:
        logger.error(f"Failed to read file: {e}")