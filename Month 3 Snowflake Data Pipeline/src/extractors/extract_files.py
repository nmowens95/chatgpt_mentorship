import pandas as pd
from pathlib import Path
import yaml
from src.loaders.schema_loader import load_schema

SCHEMA_REGISTRY = {
    "claims": "claims.yaml",
    "customers": "customers.yaml",
    "procedures": "procedures.yaml",
    "providers": "providers.yaml"
}

def read_unprocessed_files(unprocessed_dir: str) -> dict:
    unprocessed_dir = Path(unprocessed_dir)
    dfs = {}
    
    try:
        for file in unprocessed_dir.glob("*.csv"):
            file_name = file.stem
            full_path = Path(unprocessed_dir/file)

            if file_name in SCHEMA_REGISTRY:
                df = pd.read_csv(full_path)
                dfs[file_name] = df

        return dfs
    
    except Exception as e:
        print(f"Error processing files in {unprocessed_dir}, error: {e}")