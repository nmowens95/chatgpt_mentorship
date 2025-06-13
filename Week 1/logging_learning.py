import os
import pandas as pd
import argparse
import logging

'''
Resource:
- https://realpython.com/python-logging/
'''


'''
.

🎯 Task:
Refactor your current file summary script to:
- Replace print() calls with logging
- Use the logging module
- Log file summaries at INFO level
- Log errors with ERROR level
- Extract functionality into reusable functions
- e.g., analyze_file(file_path) and summarize_column(df, column)
- (Stretch Goal): Allow --log-level to be passed via argparse
'''

logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO,
)

logger = logging.getLogger()

def iterate_files(dir_path):
    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)

        try:
            if not file.lower().endswith(".csv"):
                continue

            df = pd.read_csv(full_path)
            logger.info(f"File - {file} read successfully!")
            
            column_info(df)
        
        except Exception as e:
            logger.debug(f"Couldn't read file: {e}")
        

def column_info(df):
    for column in df.columns:
        column_name = df[column].name
        column_dtype = df[column].dtypes
        column_isna = round(100 * (df[column].isna().sum() / len(df)), 1)
        column_mode = df[column].mode()
        most_frequent = column_mode.iloc[0] if not column_mode.empty else "N/A"

        logger.info(f"Column name: {column_name}")
        logger.info(f"Column dtype: {column_dtype}")
        logger.info(f"Percent missing: {column_isna}")
        logger.info(f"Column mode: {most_frequent}\n")

    print(f"---------------------------------------------\n")


if __name__ == "__main__":
    # Inititate arguments to call - dir_path
    parser = argparse.ArgumentParser(description="Directory to loop over .csv files")
    parser.add_argument(
        "dir_path", 
        type=str,
        help="Directory folder to loop over csv's"
        )
    
    args = parser.parse_args()

    iterate_files(args.dir_path)

