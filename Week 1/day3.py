"""
✅ Task
Update your existing script to do the following:

1. Add a --save-summary optional argument
This should let the user optionally write the column info to a file like summary.txt.
    - You can default it to None, and only write to it if the user provides the flag.

2. When the flag is used:
For each CSV file, write the column summary into the file like this:

FILE: customers.csv
Rows: 1234 | Columns: 12

Column: name
Type: object
Missing: 0.0%
Mode: John

Column: age
Type: int64
Missing: 1.2%
Mode: 34

-------------------------------------
3. Use logging to notify:
Let the logger output messages like:

INFO | Writing summary to output/summary.txt
"""

import os
import pandas as pd
import argparse
import logging

logging.basicConfig(
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO,
)

logger = logging.getLogger()

def iterate_files(dir_path, save):
    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)

        try:
            if not file.lower().endswith(".csv"):
                continue

            df = pd.read_csv(full_path)
            logger.info(f"File - {file} read successfully!")
            
            column_info(df, save)
        
        except Exception as e:
            logger.debug(f"Couldn't read file: {e}")
        

def column_info(df, save):
    for column in df.columns:
        column_name = df[column].name
        column_dtype = df[column].dtypes
        column_isna = round(100 * (df[column].isna().sum() / len(df)), 1)
        column_mode = df[column].mode()
        most_frequent = column_mode.iloc[0] if not column_mode.empty else "N/A"

        if save:
            dir_path = os.path.dirname(save)
            if not os.path.exists(dir_path):
                    os.makedirs(dir_path, exist_ok=True)

            # Write to file
            logger.info(f"Writing summary to {save}")
            with open(save, "a") as f:
                f.write(f"\n=== Summary for DataFrame ({len(df)} rows) ===\n")
                f.write(f"Column name: {column_name}\n")
                f.write(f"Column dtype: {column_dtype}\n")
                f.write(f"Percent missing: {column_isna}\n")
                f.write(f"Column mode: {most_frequent}\n")

                f.write("---------------------------------------------\n")
        else:
            # Print to console
            logger.info(f"Column name: {column_name}")
            logger.info(f"Column dtype: {column_dtype}")
            logger.info(f"Percent missing: {column_isna}")
            logger.info(f"Column mode: {most_frequent}\n")

    


if __name__ == "__main__":
    # Inititate arguments to call - dir_path
    parser = argparse.ArgumentParser(description="Loop over .csv files and provides information")
    parser.add_argument(
        "dir_path", 
        type=str,
        help="Directory folder to loop over csv's"
        )
    parser.add_argument(
        "-s",
        "--save-summary",
        action="store_true",
        help="Saves summary of columns to a txt file"
        )
    
    args = parser.parse_args()

    save_path = "./output/summary.txt" if args.save_summary else None

    # dir_path = ./helper_files/
    # save_summary = "./output/" or None
    iterate_files(args.dir_path, save_path) #args.save_summary)