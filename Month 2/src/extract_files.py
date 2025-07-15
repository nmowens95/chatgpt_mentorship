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
                file_name, file_ext = os.path.splitext(file)
                full_name = file_name + file_ext
                file = os.path.join(dir_path, file)
                df = pd.read_csv(file)
                dataframes.append((df, file_name, full_name))
                logger.info(f"{file_name} successfully read into a dataframe!")
        return dataframes
    
    except Exception as e:
        logger.error(f"Failed to read file: {e}")