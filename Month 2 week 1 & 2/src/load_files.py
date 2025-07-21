import os
from .logger_config import logger_setup

logger = logger_setup()

def load_files(df, file, output_dir="data/staged"):
    try:
        os.makedirs("data/staged", exist_ok=True)
        full_path = os.path.join(output_dir, file)
        df.to_csv(full_path, index=False)
        logger.info(f"Successfully pushed {file} to: {full_path}")
        return full_path
    
    except Exception as e:
        logger.error(f"File {file} was not able to be loaded, due to {e}")
        return None