import pandas as pd
import logging
import os

logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO,
)

logger = logging.getLogger()

def iterate_files(dir_path):
    results = []

    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)           

        try:
            if file.lower().endswith(".csv"):
                logging.info(f"csv file")
                df = pd.read_csv(full_path)
                filetype = "csv"
                logger.info(f"File - {file} read successfully!")
    
        
            elif file.lower().endswith(".ndjson") or file.lower().endswith(".json"):
                logging.info(f"json file")
                df = pd.read_json(full_path, lines=True)
                filetype = "json"
                logger.info(f"File - {file} read successfully!")
            
            else:
                None
            
            results.append([df, filetype, file])
        
        except Exception as e:
            logger.debug(f"Couldn't read file: {e}")

    return results