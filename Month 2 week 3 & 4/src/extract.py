import pandas as pd
from pathlib import Path
from utils.logger_config import logger_setup
from utils.metadata_logger import extract_metadata, metadata_writer, get_processed_files

logger = logger_setup()

# def extract_files(file):
#     file_path = Path("data/bronze")
#     full_path = file_path/file
#     df = pd.read_csv(full_path)

#     file_name = os.path.splitext(full_path)[0]

#     metadata = extract_metadata(df, file_name)
#     metadata_writer(metadata)

#     return df.copy()

def extract_csv_files(file_dir):
    file_dir = Path(file_dir)
    dataframes = {}

    processed_files = get_processed_files()
    
    for csv_file in file_dir.glob("*.csv"):
        file_name = csv_file.stem
        
        if file_name in processed_files:
            logger.info(f"Skipping already processed file: {file_name}")
            continue

        try:
            df = pd.read_csv(csv_file)
           
            metadata = extract_metadata(df, file_name)
            metadata_writer(metadata, process="extract")

            dataframes[file_name] = df
        
        except Exception as e:
            logger.error(f"Error reading file {file_name} due to: {e}")
            continue

    return dataframes

result = extract_csv_files(file_dir="data/bronze")
print(result)