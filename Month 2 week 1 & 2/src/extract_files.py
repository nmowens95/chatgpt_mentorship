import pandas as pd
import os
from .logger_config import logger_setup
from datetime import datetime
from pathlib import Path
import json

logger = logger_setup()

def extract_metadata(file_name: Path, df: pd.DataFrame) -> dict:
    metadata = {
        "file": str(file_name),
        "status": not df.empty,
        "rows": len(df),
        "timestamp": datetime.now().isoformat()
    }
    return metadata

def metadata_extract_writer(meta: object) -> Path:
    output_dir = Path("logs/extract_logs")
    output_dir.mkdir(parents=True, exist_ok=True)
    log_file = output_dir/"file_metadata.jsonl"

    with open(log_file, "a") as f:
        json.dump(meta, f)
        f.write("\n")
    
    logger.info(f"Successfully logged metadata to: {log_file}")
    
    return log_file


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

                # Grab metadata
                meta = extract_metadata(file_name, df)
                # Write metadata
                metadata_extract_writer(meta)

        return dataframes
    
    except Exception as e:
        logger.error(f"Failed to read file: {e}")
        raise