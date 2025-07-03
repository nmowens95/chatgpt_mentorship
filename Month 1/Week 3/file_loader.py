import pandas as pd
import os
from logger_config import setup_logger

logger = setup_logger()

class CustomFileReadError(Exception):
    """Raised when reading a CSV file fails."""
    pass

def safe_read_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise CustomFileReadError(f"Error to read {file_path}: {e}")

def load_csv_files(dir_path):
    file_tuples = []

    if not os.path.exists(dir_path):
            raise CustomFileReadError(f"That directory doesn't exist: {dir_path}")
    
    files = os.listdir(dir_path)
    if not files:
        raise CustomFileReadError(f"No files exist in this directory:{dir_path}")

    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)

        if file.endswith("csv"):
            file_name, file_type = os.path.splitext(file)
            df = safe_read_csv(full_path)

            file_tuples.append((df, file_name, file_type))
            logger.info(f"Successfully logged: {file}")
        
        else:
            logger.info(f"File: {file} is not a csv file")
            
    return file_tuples