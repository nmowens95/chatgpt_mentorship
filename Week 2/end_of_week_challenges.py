import os
import pandas as pd
import logging
import argparse

# Initialize logging information
logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    level=logging.INFO
)

logger = logging.getLogger()


def iterate_files(file_dir: str) -> list:
    data_frames = []
    for file in os.listdir(file_dir):
        full_path = os.path.join(file_dir, file)

        
        if file.endswith(".csv"):
            logger.info(f"---------------------")
            logger.info(f"Reading file {file}")
            logger.info(f"---------------------\n")
            file_name = file
            df = pd.read_csv(full_path)
            data_frames.append((df, file_name))
        
        else:
            print("Other file type\n")

    return data_frames

def column_summary(data_frames, include_dtype=True, include_missing=True) -> None:
    for df, file_name in data_frames:
        column_names = []
        column_dtype = []
        column_missing = []

        num_rows = len(df)
        num_cols = len(df.columns)

        for col in df:
            column_names.append(df[col].name)
            column_dtype.append(df[col].dtype)
            column_missing.append((df[col].isna().sum() /len(df[col]) * 100))


        print(f"CSV file name: {file_name}")
        print(f"Number of rows: {num_rows}")
        print(f"length of columns {num_cols}")
        print(f"Name of columns: {column_names}")
        if include_dtype:
            print(f"Data types of columns {column_dtype}")
        if include_missing:
            print(f"% missing of columns {column_missing}")
        print("")
        logger.info("✅ Successfully summarized columns for CSV\n")
        print("--------- End of csv report ---------\n")

if __name__ == "__main__":
    # Define parser and arguments for dynamic input
    parser = argparse.ArgumentParser(description="Input for csv summarizer mini challenge")
    parser.add_argument(
        "file_dir",
        type=str,
        help="Path to iterate over files for summarize files"
    )
    parser.add_argument(
        "--include-dtype",
        action="store_true",
        help="Optional if we want to add dtype info to summary"
    )
    parser.add_argument(
        "--include-missing",
        action="store_true",
        help="Optional if we want to add missing percentage info to summary"
    )

    args = parser.parse_args()

    data_frames = iterate_files(args.file_dir)
    column_summary(data_frames, args.include_dtype, args.include_missing)