from logger_config import setup_logger
from file_loader import load_csv_files
from summarizer import summarize_df
from parser import parse_args

def main():
    logger = setup_logger()
    args = parse_args()

    file_tuples = load_csv_files(args.dir_path)

    feature_list = args.features.split(",") if args.features else []

    try:
        for df, file_name, file_type in file_tuples:
            summarize_df(df, file_name, file_type, feature_list)
    
    except Exception as e:
        logger.info(f"Error with summarizing files: {e}")
    
    else:
        logger.info(f"All files have successfully been summarized!")

if __name__ == "__main__":
    main()