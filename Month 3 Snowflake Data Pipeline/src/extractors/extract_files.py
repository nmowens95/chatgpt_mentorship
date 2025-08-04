import pandas as pd
from pathlib import Path
import yaml
from src.loaders.schema_loader import load_schema
from src.logger.logger_config import setup_logger
import shutil

logger = setup_logger()

SCHEMA_REGISTRY = {
    "claims": "claims.yaml",
    "customers": "customers.yaml",
    "procedures": "procedures.yaml",
    "providers": "providers.yaml"
}

def read_unprocessed_files(unprocessed_dir: str) -> dict:
    '''
    Returns: A dictionary with nested dictionaries - {{file_name: df}}
    '''
    unprocessed_dir = Path(unprocessed_dir)
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)
    dfs = {}
    
    try:
        for file in unprocessed_dir.glob("*.csv"):
            file_name = file.stem

            if file_name in SCHEMA_REGISTRY:
                df = pd.read_csv(file)
                schema = load_schema(SCHEMA_REGISTRY[file_name])
                expected_cols = [col["name"] for col in schema["columns"]]

                if set(expected_cols).issubset(df.columns):
                    dfs[file_name] = df
                    logger.info(f"Successfully extracted {file_name} with {len(df)} rows")
                    shutil.move(str(file), processed_dir / file.name)
                    if (processed_dir / file.name).exists():
                        logger.info(f"Moved {file_name}.csv to processed folder.")
                    else:
                        logger.error(f"Failed to move {file_name}.csv")
                else:
                    logger.warning(f"{file_name} missing expected columns. Skipping.")
    
        return dfs
    
    except Exception as e:
        print(f"Error processing files in {unprocessed_dir}, error: {e}")