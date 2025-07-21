import pandas as pd
from datetime import datetime
from pathlib import Path
import json
import os

def extract_metadata(df, file_name):
    metadata = {
        "file": str(file_name),
        "rows": len(df),
        "timestamp": datetime.now().isoformat()
    }
    return metadata

def metadata_writer(metadata: dict) -> Path:
    output_dir = Path("logs/extract_logs")
    output_dir.mkdir(parents=True, exist_ok=True)

    log_file = output_dir/f"extract_log.jsonl"
    
    with open(log_file, "a") as f:
        json.dump(metadata, f)
        f.write("\n")

    return log_file

def extract_files(file):
    file_path = Path("data/bronze")
    full_path = file_path/file
    df = pd.read_csv(full_path)

    file_name = os.path.splitext(full_path)[0]

    metadata = extract_metadata(df, file_name)
    metadata_writer(metadata)

    return df.copy()

file = "claims.csv"
result = extract_files(file)
print(result.head())