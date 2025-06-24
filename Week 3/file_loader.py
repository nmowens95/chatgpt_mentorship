import pandas as pd
import os
from logger_config import setup_logger

logger = setup_logger()

def load_csv_files(dir_path):
    file_tuples = []
    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)

        if file.endswith("csv"):
            file_name, file_type = os.path.splitext(file)
            df = pd.read_csv(full_path)

            file_tuples.append((df, file_name, file_type))
            logger.info(f"Successfully logged: {file}")
        
        else:
            logger.info(f"File: {file} is not a csv file")
            
    return file_tuples