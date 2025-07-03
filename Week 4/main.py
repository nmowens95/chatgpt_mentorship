from src.datatools.logger_config import setup_logger
from src.datatools.file_loader import load_files
from src.datatools.summarizer import summarize_df
from src.datatools.parser import parse_args

def main():
    logger = setup_logger()
    args = parse_args()

    try:
        # Input layer
        file_tuples = load_files(args.dir_path)

        # Processing layer
        for df, file_name, file_type in file_tuples:
            summarize_df(df, file_name, file_type, args.features, args.writer)
         
    except Exception as e:
        logger.error(f"Pipeline failed due to: {e}")
    
    else:
        logger.info(f"All files have successfully been summarized!")

if __name__ == "__main__":
    main()