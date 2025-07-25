import json
from pathlib import Path
from src.utils.logger_config import logger_setup
from datetime import datetime
import pandas as pd

logger = logger_setup()

# Metadata to be written to file
def extract_metadata(df, file_name):
    metadata = {
        "file": str(file_name),
        "rows": len(df),
        "columns": len(df.columns),
        "extracted_at": datetime.now().isoformat()
    }
    return metadata

def transform_metadata(df: pd.DataFrame, filename: str) -> dict:
    metadata = {
        "file": str(filename),
        "status": "transformed",
        "transformed_at": datetime.now().isoformat()
    }
    return metadata

# Writes to file
def metadata_writer(metadata: dict, process: str) -> Path:
    output_dir = Path(f"logs/{process}_logs")
    output_dir.mkdir(parents=True, exist_ok=True)

    log_file = output_dir/f"{process}_log.jsonl"
    
    try:
        with open(log_file, "a") as f:
            json.dump(metadata, f)
            f.write("\n")

        logger.info(f"Successfully wrote metadata to: {log_file}")

    except Exception as e:
        logger.error(f"Failed to write metadata to: {log_file}")

    return log_file

def get_processed_files(log_dir=f"logs/extract_logs", process=None) -> set:
    log_path = Path(f"{log_dir}/{process}_log.jsonl")
    
    if not log_path.exists():
        return set()
    
    processed_files = set()
    with open(log_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line)
                processed_files.add(entry["file"])
            except json.JSONDecodeError:
                continue
            
    return processed_files