'''
What I worked on:
- using argparse and how to pass in command line arguments as a python object
to make variables more dynamic instead of hard coded
'''

'''
Task:

'''

import os
import pandas as pd
import argparse

# Practice using argparse:
parser = argparse.ArgumentParser(description="Directory to loop over .csv files")
parser.add_argument("dir_path", type=str, help="Directory folder to loop over csv's")
args = parser.parse_args()

# def main(dir_path):
for file in os.listdir(args.dir_path):
    full_path = os.path.join(args.dir_path, file)

    try:
        if not file.lower().endswith(".csv"):
            continue

        df = pd.read_csv(full_path)
        rows = len(df)
        columns = len(df.columns)

        print(f"File name: {file}")
        print(f"Number of Rows: {rows} & Columns: {columns}\n")

        for column in df.columns:
            column_name = df[column].name
            column_dtype = df[column].dtypes
            column_isna = round(100 * (df[column].isna().sum() / len(df)), 1)
            column_mode = df[column].mode()
            most_frequent = column_mode.iloc[0] if not column_mode.empty else "N/A"

            print(f"Column name: {column_name}")
            print(f"Column dtype: {column_dtype}")
            print(f"Percent missing: {column_isna}")
            print(f"Column mode: {most_frequent}\n")

        print(f"---------------------------------------------\n")

    except Exception as e:
        print(f"Error with file: {file}, exception: {e}")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Summarize .csv files in a directory.")
#     parser.add_argument("dir_path", help="Path to the directory containing CSV files")

#     args = parser.parse_args()
#     main(args.dir_path)

"""
1. Initialize parser
    - parser = argparse.ArgumentParser(description=)
2. Create an argument or variable to call
    - parser.add_argument({variable}, help="describe incase we forget")
3. Finally parse the argument to be able to call it
    - args = parser.parse_args()

    This turns the command line argument to a python object that we can use
    - args.{variable} can now be called
"""