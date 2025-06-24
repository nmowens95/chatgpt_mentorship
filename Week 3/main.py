from logger_config import setup_logger
from file_loader import load_csv_files
from summarizer import summarize_df
import argparse

logger = setup_logger()

parser = argparse.ArgumentParser(description="Arguments to summarize csv files")
parser.add_argument(
    "dir_path",
    type=str,
    help="Path for files to iterate over"
)
args = parser.parse_args()

if __name__ == "__main__":
    file_tuples = load_csv_files(args.dir_path)
    
    try:
        for df, file_name, file_type in file_tuples:
            summarize_df(df, file_name, file_type)
    
    except Exception as e:
        logger.info(f"Error with summarizing files: {e}")
    
    logger.info(f"All files have successfully been summarized!")