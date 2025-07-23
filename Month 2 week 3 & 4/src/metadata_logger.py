import json
from pathlib import Path
from utils.logger_config import logger_setup
from datetime import datetime

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

# Writes to file
def metadata_writer(metadata: dict) -> Path:
    output_dir = Path("logs/extract_logs")
    output_dir.mkdir(parents=True, exist_ok=True)

    log_file = output_dir/f"extract_log.jsonl"
    
    try:
        with open(log_file, "a") as f:
            json.dump(metadata, f)
            f.write("\n")

        logger.info(f"Successfully wrote metadata to: {log_file}")

    except Exception as e:
        logger.error(f"Failed to write metadata to: {log_file}")

    return log_file

def get_processed_files(log_path=("logs/extract_logs/extract_log.jsonl")) -> set:
    log_path = Path(log_path)
    
    if not log_path.exists():
        return set()
    
    proecessed_files = set()
    with open(log_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line)
                proecessed_files.add(entry["file"])
            except json.JSONDecodeError:
                continue
            
    return proecessed_files